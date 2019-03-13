import cv2
import sys, os, time
import itertools
import math, random
import glob

# img = cv2.imread("/Users/hogeunryu/Downloads/part3/1277104195Image000013.jpg")
# # xywh = [421.951760, 466.808005, 393.983863, 437.145083]
# xywh = [437, 466, 393, 421]

# crop_img = img[xywh[0]:xywh[1], xywh[2]:xywh[3]] 
# cv2.imshow("cropped", crop_img)
# cv2.waitKey(0)

base_image_path = "Image/"
image_types = ["Set1Part0", "Set2Part0"]

# for im_type in image_types:
#     for ex in glob.glob(os.path.join(base_image_path, im_type, "*")):
#         print(ex)
#         im = cv2.imread(ex)
#         print(im)
#         if not im is None:
#             crop_img = im[xywh[0]:xywh[1], xywh[2]:xywh[3]] 
#             cv2.imshow("cropped", crop_img)
#             cv2.waitKey(0)

in_file = open("/Users/hogeunryu/Downloads/part3/Image/Set2Part0/annotations.txt")
# print(in_file)
paths = ""
for line in in_file:
	if not line.find(";") == -1:
		# print("find ;")
		print(line)
		print("line")
		# print(line.count(";"))
		split = line.split(';')
		print(split)
		print("split")
		# print(type(line[:25]))
		for splt in split:
			print(splt)
			print("splt")
			if len(splt) > 1:
				list_slt = splt.split(",")
				# print(type(list_slt))
				# print(list_slt[-1])
				# print(list_slt[-2])
				# print(list_slt[-3])
				# print(list_slt[-4])
				# print(list_slt[-5])
				# print(type(list_slt[-6]))
				index = split[0].find(":")
				img_name = split[0][:index]
				im = cv2.imread("/Users/hogeunryu/Downloads/part3/Image/Set2Part0/" + img_name)
				if not im is None:
					if len(list_slt) <= 2:
						print(list_slt)
						print(len(list_slt))
						print("list_slt")
					else:
						file_path = str("/Users/hogeunryu/Downloads/part3/Image/Dataset/"+list_slt[-2][1:]+"/"+list_slt[-1][1:]+"/")
						directory = os.path.dirname(file_path)
						print(directory)
						if not os.path.exists(directory):
							os.makedirs(directory)
						print("ok")
						crop_img = im[int(float(list_slt[-3])):int(float(list_slt[-5])), int(float(list_slt[-4])):int(float(list_slt[-6]))] 
						print(str(directory+line[:25]))
						cv2.imwrite(str(directory+line[:25]), crop_img)
	# print(type(splt))
	# linelist = linestring.split()
	# first = linelist[0]
	# last = linelist[-1]
	# F = first[:20]
	# L = last[:20]
	# FP = first[:20].find(",")
	# LP = last[:20].find(",")
	# First = F[FP+1:]+","+F[:FP]
	# Last = L[LP+1:]+","+L[:LP]
	# print(congestion)
	# if congestion == '1':
	#     color = 'blue'
	#     print(color)
	# else:
	# 	print("wh")
