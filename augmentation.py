# GIVEWAY 수평
# 30_sign 수직

# Nopark 수직수평

# Nonstop no stand 수평 수직 수직수평

# priority_road 수직 수평 수직수평

# 오른쪽 수평 ->왼쪽

# 왼쪽 수평 -> 오른쪽
import cv2
import sys, os, time
import itertools
import math, random
import glob

# load the image with imread()
base_image_path = "/Users/hogeunryu/Downloads/part3/Image/Dataset/"

image_types = ["WARNING/GIVE_WAY/",
               "PROHIBITORY/30_SIGN/", 
               "PROHIBITORY/NO_PARKING/", 
               "PROHIBITORY/NO_STOPPING_NO_STANDING/", 
               "INFORMATION/PRIORITY_ROAD/",
               "MANDATORY/PASS_EITHER_SIDE/",
               "MANDATORY/PASS_LEFT_SIDE/",
               "MANDATORY/PASS_RIGHT_SIDE/"]

for im_type in image_types:              
    print(im_type)
    name = 0 
    for ex in glob.glob(os.path.join(base_image_path, im_type, "*")):
            im = cv2.imread(ex)
            name += 1 
            if not im is None:
                # copy image to display all 4 variations
                copy_im = im.copy()
                if im_type == "WARNING/GIVE_WAY/" or im_type == "MANDATORY/PASS_LEFT_SIDE/" or im_type == "MANDATORY/PASS_RIGHT_SIDE/":
                    horizontal_img = cv2.flip(copy_im, 0)
                    # print(str(base_image_path + im_type + str(name) + ".jpg"))
                    cv2.imwrite(str(base_image_path + im_type + str(name) + ".jpg"), horizontal_img)

                elif im_type == "PROHIBITORY/30_SIGN/":
                    vertical_img = cv2.flip(copy_im, 1)
                    # print(str(base_image_path + im_type + str(name) + ".jpg"))
                    cv2.imwrite(str(base_image_path + im_type + str(name) + ".jpg"), vertical_img)

                elif im_type == "PROHIBITORY/NO_PARKING/":
                    both_img = cv2.flip(copy_im, -1)
                    # print(str(base_image_path + im_type + str(name) + ".jpg"))
                    cv2.imwrite(str(base_image_path + im_type + str(name) + ".jpg"), both_img)

                else:
                    copy_im2 = copy_im.copy()
                    copy_im3 = copy_im.copy()

                    horizontal_img = cv2.flip(copy_im2, 0)
                    vertical_img = cv2.flip(copy_im3, 1)
                    both_img = cv2.flip(copy_im, -1) 
                    # print(str(base_image_path + im_type + str(name) + "both" + ".jpg"))
                    cv2.imwrite(str(base_image_path + im_type + str(name) + "hori" + ".jpg"), horizontal_img)
                    cv2.imwrite(str(base_image_path + im_type + str(name) + "vert" + ".jpg"), vertical_img)
                    cv2.imwrite(str(base_image_path + im_type + str(name) + "both" + ".jpg"), both_img)

