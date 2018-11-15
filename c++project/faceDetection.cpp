#include<opencv2/core/core.hpp>
#include<opencv2/highgui.hpp>
#include<opencv2/objdetect.hpp>
#include<opencv2/imgproc.hpp>
#include<iostream>

using namespace cv;
using namespace std;

CascadeClassifier face_cascade;

int  main(int argc, char** argv){
	if(argc != 2)
	{
		cout <<"Usage: display_img Image"<< endl;
		return -1;
	}
	String cascade_path="/usr/local/share/opencv4/haarcascades/haarcascade_frontalface.xml";
	face_cascade.load(cascade_path);
	Mat image;
	Mat image_gray;
	image=imread(argv[1], IMREAD_COLOR);
	if(! image.data)
	{
		cout << "could not open or find image"<<endl;
		return -1;
	}
	cvtColor(image,image_gray,COLOR_BGR2GRAY);
	vector<Rect> faces;
	face_cascade.detectMultiScale(image_gray, faces);
	for (size_t i =0;i<faces.size();i++)
	{
		rectangle(image_gray,faces[i], Scalar(255,0,0),2);

	}

	namedWindow("Display",WINDOW_AUTOSIZE);
	imshow("Display",image);
	waitKey(0);
	return 0;
}
