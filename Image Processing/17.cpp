#include<iostream>
#include<opencv2/opencv.hpp>

using namespace std;
using namespace cv;

Mat img, gray, edge;
int th1 = 50, th2 = 50;

void onTrackbar1(int , void*) {
    Canny(gray, edge, th1,th1*2 ,3);
    imshow("canny edge", edge);
}
void onTrackbar2(int, void*) {
    Canny(gray, edge, th2,th2*2, 3);
    imshow("canny edge", edge);
}
int main() {
    img = imread("color_space.jpg", 1);
    CV_Assert(img.data);
    cvtColor(img, gray, COLOR_BGR2GRAY);

    namedWindow("canny edge", WINDOW_NORMAL);
    createTrackbar("th1", "canny edge", &th1, 255, onTrackbar1);
    createTrackbar("th2", "canny edge", &th2, 255, onTrackbar2);

    waitKey(0);
    return 0;
}