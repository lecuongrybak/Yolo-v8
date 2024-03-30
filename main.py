from ultralytics import YOLO
import torch.multiprocessing as mp
import torch
from multiprocessing import Process, freeze_support

def func():
    model = YOLO("yolov8n.yaml")
    results = model.train(data="datasetold\dataold.yaml", imgsz=640, epochs=50)

if __name__ == '__main__':
    freeze_support()  # Cần thiết nếu chương trình sẽ được đóng băng để tạo thành một file thực thi
    Process(target=func).start()