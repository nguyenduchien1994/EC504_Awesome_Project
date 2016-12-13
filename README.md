# K-Image segmenation using network flow
# Both the C++11 and python dependencies are freely available. Installation is quite simple.
Code Dependency:
C++ 11
C++ opencv 2.4.13

Python dependency:
  python version 2.7
  scikit-learn
  numpy
  opencv

# Compilation instructions:
If you have pkg-config for opencv, the following command should compile the file

# 2 Segmentation:

#Compilation:
g++ -std=c++11 imagesegmentation.cpp -o imagesegmenation `pkg-config --cflags --libs opencv`

PS: If you don't have pkg-config you can expand the command `pkg-config --cflags --libs opencv`
In MAC OSX the command expands as following. Might have to change your path depending on your installation!

-I/usr/local/Cellar/opencv/2.4.13/include/opencv -I/usr/local/Cellar/opencv/2.4.13/include -L/usr/local/Cellar/opencv/2.4.13/lib -lopencv_calib3d -lopencv_contrib -lopencv_core -lopencv_features2d -lopencv_flann -lopencv_gpu -lopencv_highgui -lopencv_imgproc -lopencv_legacy -lopencv_ml -lopencv_nonfree -lopencv_objdetect -lopencv_ocl -lopencv_photo -lopencv_stitching -lopencv_superres -lopencv_ts -lopencv_video -lopencv_videostab

# RUN:
Please provide the <imagename> directly. Please don't provide the path. The images should be added into the image folder. The program automatically looks for images in the image folder.

./imagesegmentation <imagename> <clustering>
 <imagename> - name of the imagefile
 <clustering> - an integer value 0 or 1, if you want to use gmm or k-means. It uses gmm by default.
 
# K Segmenation :
 
 g++ -std=c++11 kimagesegmentation.cpp -o imagesegmenation `pkg-config --cflags --libs opencv`
 
 Please look into the pkg-config expansion above.
 
# RUN K-Segmentation
 
 ./imagesegmentation <imagename> <clustering> <numberOfSegments>
 <imagename> - name of the imagefile
 <clustering> - an integer value 0 or 1, if you want to use gmm or k-means
 <numberOfSegments> - The total number of segments you want the image to be divided into.
 
 
 
  
