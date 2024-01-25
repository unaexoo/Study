#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main() {
	Mat img = imread("coins.jpg", 1);
	CV_Assert(img.data);

	// 1) 명암도 영상 변환
	Mat gray;
	cvtColor(img, gray, COLOR_BGR2GRAY); 

	// 2) 가우시안 블러링
	Mat blur;
	GaussianBlur(gray, blur, Size(3, 3), 0);

	// 3) 이진화
	Mat binary;
	threshold(blur, binary, 55, 255, THRESH_BINARY); //60을 해보니 원 안에 점 생김

	// 4) 모폴로지 열림 연산
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
