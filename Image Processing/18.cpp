#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main() {
	Mat img = imread("coins.jpg", 1);
	CV_Assert(img.data);

	// 1) ��ϵ� ���� ��ȯ
	Mat gray;
	cvtColor(img, gray, COLOR_BGR2GRAY); 

	// 2) ����þ� ����
	Mat blur;
	GaussianBlur(gray, blur, Size(3, 3), 0);

	// 3) ����ȭ
	Mat binary;
	threshold(blur, binary, 55, 255, THRESH_BINARY); //60�� �غ��� �� �ȿ� �� ����

	// 4) �������� ���� ����
	Mat morp;
	Matx <uchar, 3, 3> mask;
	mask << 0, 1, 0,
			1, 1, 1,
			0, 1, 0;
	morphologyEx(binary, morp, MORPH_OPEN, mask);

	imshow("img", img);
	imshow("gray", gray);
	imshow("blur", blur);
	imshow("binary", binary);
	imshow("mophology", morp);

	waitKey(0);
	return 0;
}
