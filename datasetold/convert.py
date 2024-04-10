import cv2
from os import listdir
from os.path import isfile, join
b = r"D:\Yolo v8\datasetold\img_gray_test"
mypath = r"D:\Yolo v8\datasetold\valid\images"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for filename in onlyfiles:
    print(mypath + "\\" + filename)
    a = cv2.imread(mypath + "\\" + filename)
    c = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(filename, c)
cv2.waitKey(0)