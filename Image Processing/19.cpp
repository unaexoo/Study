#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

bool check_match(Mat img, Point start, Mat mask, int mode = 0) {
	for (int u = 0; u < mask.rows; u++) {
		for (int v = 0; v < mask.cols; v++) {
			Point pt(v, u);
			int m = mask.at<uchar>(pt);
			int p = img.at<uchar>(start + pt);

			bool ch = (p == 255);
			if (m == 1 && ch == mode) return false;
		}
	}
	return true;
}
void erosion(Mat img, Mat& dst, Mat mask) {
	dst = Mat(img.size(), CV_8U, Scalar(0));
	if (mask.empty()) mask = Mat(3, 3, CV_8UC1, Scalar(1));

	Point h_m = mask.size() / 2;
	for (int i = h_m.y; i < img.rows-h_m.y; i++) {
		for (int j = h_m.x; j < img.cols-h_m.x; j++) {
			Point start = Point(j, i) - h_m;
			bool check = check_match(img, start, mask, 0);
			dst.at<uchar>(i, j) = (check) ? 255 : 0;
		}
	}
}
void dilation(Mat img, Mat& dst, Mat mask) {
	dst = Mat(img.size(), CV_8U, Scalar(0));
	if (mask.empty()) mask = Mat(3, 3, CV_8UC1, Scalar(1));

	Point h_m = mask.size() / 2;
	for (int i = h_m.y; i < img.rows - h_m.y; i++) {
		for (int j = h_m.x; j < img.cols - h_m.x; j++) {
			Point start = Point(j, i) - h_m;
			bool check = check_match(img, start, mask, 1);
			dst.at<uchar>(i, j) = (check) ? 0 : 255;
		}
	}

}
void morpholy(Mat img, Mat& dst, Mat mask, bool isErosion) {
	dst = Mat(img.size(), CV_8U, Scalar(0));
	if (mask.empty()) mask = Mat(3, 3, CV_8UC1, Scalar(1));

	Point h_m = mask.size() / 2;
	for (int i = h_m.y; i < img.rows - h_m.y; i++) {
		for (int j = h_m.x; j < img.cols - h_m.x; j++) {
			Point start = Point(j, i) - h_m;
			bool check = check_match(img, start, mask, isErosion ?0:1);
			dst.at<uchar>(i, j) = (check) ? (isErosion ? 255 : 0) : (isErosion ? 0:255);
		}
	}
}
int main() {
	Mat img = imread("morph_test.jpg", 0);
	CV_Assert(img.data);
	Mat th_img, dst1, dst2,dst3,dst4;
	threshold(img, th_img, 128, 255, THRESH_BINARY);

	uchar data[] = { 0,1,0,
					1,1,1,
					0,1,0 };
	Mat mask(3, 3, CV_8UC1, data);
	erosion(th_img, dst1, (Mat)mask);
	dilation(th_img, dst2, (Mat)mask);

	morpholy(th_img, dst3, (Mat)mask, true);//Erosion
	morpholy(th_img, dst4, (Mat)mask, false);//Dilation

	imshow("img", img);
	imshow("erosion", dst1);
	imshow("dilation", dst2);

	imshow("m_erosion", dst3);
	imshow("m_dilation", dst4);
	waitKey(0);
	return 0;
}