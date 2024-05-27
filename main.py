import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from io import BytesIO
import numpy as np
import cv2
import Pill_detect
import Pill_crop
import Pill_color
#import Pill_shape
import shape
import Pill_text
import warnings
from Api import RestApi

def upload_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def run():
    model_path = "C:/Image_Recognition/pill_detection/yolo_training.pt"
    key_path = "C:/Users/hanby/Downloads/pill-423416-edf9cc43013f.json"
    output_dir = "C:/Image_Recognition/pill_detection/"
    cls_model_path = "C:/Image_Recognition/pill_detection/shape_yolo.pt"

    # Warning 숨기기
    warnings.filterwarnings("ignore", message="The parameter 'pretrained' is deprecated", category=UserWarning)
    warnings.filterwarnings("ignore",
                            message="Arguments other than a weight enum or `None` for 'weights' are deprecated",
                            category=UserWarning)

    # 사용자로부터 이미지 받기
    image_path = upload_file()

    # Pill detection
    detected_boxes, result_image = Pill_detect.detect_pill(model_path, image_path)

    # Pill color
    cropped_images = Pill_crop.crop_pill(image_path, detected_boxes, output_dir)
    for filename in os.listdir(output_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            color_path = os.path.join(output_dir, filename)
            color_path = color_path.replace("/", "\\")
            pill_color = Pill_color.detect_pill_color(color_path)
    print("Detected color:", pill_color)

    # Pill shape
    pill_shape = shape.shape_detect(cls_model_path,cropped_images)
    print("Detected shape:", pill_shape)

    # Pill text
    for filename in os.listdir(output_dir):
        if (filename.endswith(".jpg") or filename.endswith(".png")):
            image_path = os.path.join(output_dir, filename).replace("/", "\\")
    pill_text = Pill_text.detect_text(image_path, key_path)
    print("Detected text:", pill_text)
    os.remove(image_path)

    # 생성된 파일 삭제
    file_paths = []
    for filename in os.listdir(output_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(output_dir, filename)
            image_path = image_path.replace("/", "\\")
            file_paths.append(image_path)

    for file_path in file_paths:
        if os.path.exists(file_path):
            os.remove(file_path)

    return pill_color, pill_shape, pill_text

if __name__ == '__main__':
    run()