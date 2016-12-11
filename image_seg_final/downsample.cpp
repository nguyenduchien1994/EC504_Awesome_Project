/**
 * @file Pyramids.cpp
 * @brief Sample code of image pyramids (pyrDown and pyrUp)
 * @author OpenCV team
 */

#include "opencv2/imgproc.hpp"
#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"

using namespace cv;

/// Global variables
Mat src, dst, tmp,img;

const char* window_name = "Pyramids Demo";


/**
 * @function main
 */
int main( void )
{
  /// General instructions
  printf( "\n Zoom In-Out demo  \n " );
  printf( "------------------ \n" );
  printf( " * [u] -> Zoom in  \n" );
  printf( " * [d] -> Zoom out \n" );
  printf( " * [ESC] -> Close program \n \n" );

  //![load]
  img = imread( "/home/aditya/image_seg_final/cat.jpg" ); // Loads the test image
  src = imread( "/home/aditya/image_seg_final/trees.jpg" );
  cv::resize(src,src,img.size());
  if( src.empty() )
    { printf(" No data! -- Exiting the program \n");
      return -1; }
  //![load]

  tmp = src;
  dst = tmp;

  //![create_window]
  imshow( window_name, dst );
  //![create_window]
  
  //![infinite_loop]
  
   return 0;
}
