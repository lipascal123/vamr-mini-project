# Python script to undistort the images taken from a fisheye camera

import numpy as np
import cv2

#number of images
n_images = 971
start_img = 13

# plot images
show_images = False

K = np.array([  [284.54730224609375, 0,                   420.948486328125],
                [0,                  285.53131103515625,  393.4858093261719],
                [0,                  0,                   1] ]) 

D = np.array(   [-0.0015544580528512597, 0.03598850965499878, 
                 -0.03366529941558838,    0.0053024617955088615])

for i in range(start_img, n_images):
    # Read respective grayscale image
    img = cv2.imread("images/frame%04d.jpg" % (i),0)
    
    #cv2.imshow('image distorted', img)

    # check if file path is valid 
    if img is None:
        print("Check file path")

    h, w = img.shape[:2]
    # dim = (840, 800)
    # map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, dim, cv2.CV_16SC2)
    # img_undist = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)

    new_K, roi = cv2.getOptimalNewCameraMatrix(K,D,(w,h),0,(w,h))
                   

    # Checking to make sure the new camera materix was properly generated
    #print(new_K)


    # undistort image
    img_undist = cv2.fisheye.undistortImage(img, K, D, np.eye(3), K)

    # save rectified image
    cv2.imwrite('images_rect/img_%05d.png' % (i-start_img), img_undist)


    # show image
    if show_images == True:
        # stack images horizontally
        images_h = np.hstack((img, img_undist))
        # Plot images
        cv2.imshow('left distorted, right undistorted',images_h)
        cv2.waitKey(0)
        cv2.destroyAllWindows() 

