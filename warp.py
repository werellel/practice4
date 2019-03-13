import cv2
from imgaug import augmenters as iaa
import cv2
import sys, os, time
import itertools
import math, random
import glob

seq = iaa.Sequential([
	iaa.GaussianBlur(sigma=(0, 1.0))
])
seq1 = iaa.Sequential([
	iaa.ContrastNormalization((0.5, 1.0)),
	iaa.Add(value=10)
])
seq2 = iaa.Sequential([
	iaa.ContrastNormalization((0.5, 1.5)),
	iaa.Affine(rotate=-3, scale=1.1)
])
seq3 = iaa.Sequential([
	iaa.ContrastNormalization((0.5, 1.5)),
	iaa.PerspectiveTransform(scale=0.1)
])
seq4 = iaa.Sequential([
	iaa.ContrastNormalization((1.5, 1.5)),
])

# load the image with imread()
base_image_path = "/Users/hogeunryu/Downloads/part3/Image/Dataset/"
image_test = "/Users/hogeunryu/Downloads/part3/Image/Dataset/INFORMATION/PEDESTRIAN_CROSSING/PEDESTRIAN_CROSSING1277105776Image000033.jpg"
image_types = [ "MANDATORY/PASS_EITHER_SIDE/", 
				"OTHER/OTHER/", 
				"PROHIBITORY/60_SIGN/",
				"PROHIBITORY/90_SIGN/",
				"PROHIBITORY/110_SIGN/",
				"PROHIBITORY/120_SIGN/", 
				"PROHIBITORY/STOP/"]


for im_type in image_types:              
	print(im_type)
	name = 1000 
	for ex in glob.glob(os.path.join(base_image_path, im_type, "*")):
		im = cv2.imread(ex)
		name += 1 
		if not im is None:
		# copy image to display all 4 variations
			copy_im = im.copy()
			copy_im1 = im.copy()
			copy_im2 = im.copy()
			copy_im3 = im.copy()
			copy_im4 = im.copy()
			images_aug = seq.augment_image(copy_im)
			images_aug1 = seq1.augment_image(copy_im1)
			images_aug2 = seq2.augment_image(copy_im2)
			images_aug3 = seq3.augment_image(copy_im3)
			images_aug4 = seq4.augment_image(copy_im4)
			cv2.imwrite(str(base_image_path + im_type + str(name) + "1" + ".jpg"), images_aug)
			cv2.imwrite(str(base_image_path + im_type + str(name) + "2" + ".jpg"), images_aug1)
			cv2.imwrite(str(base_image_path + im_type + str(name) + "3" + ".jpg"), images_aug2)
			cv2.imwrite(str(base_image_path + im_type + str(name) + "4" + ".jpg"), images_aug3)
			cv2.imwrite(str(base_image_path + im_type + str(name) + "5" + ".jpg"), images_aug4)
			print(name)