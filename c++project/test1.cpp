#include<opencv2/highgui.hpp>
#include<iostream>

int  main(int argc, char** argv){

	cv::Mat image;
	//image=cv::imread("example.jpg", CV_LOAD_IMAGE_COLOR);
	image=cv::imread("example.jpg", CV_HAL_DFT_STAGE_COLS);
	cv::namedWindow("Display",cv::WINDOW_AUTOSIZE);
	cv::imshow("Display",image);
	cv::waitKey(0);
	return 0;
}
