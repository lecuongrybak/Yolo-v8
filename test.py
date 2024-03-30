from ultralytics import YOLO
import cvzone
import cv2
import math

model = YOLO('D:\\Yolo v8\\runs\\detect\\train35\\weights\\last.pt')
model.predict(source=0, conf=0.6, show=True)