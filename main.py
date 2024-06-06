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
# import Pill_shape
import shape
import Pill_text
import warnings
from Api import RestApi


def upload_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path


def run(image):
    model_path = "yolo_training.pt"
    key_path = "pill.json"
    output_dir = "output"
    cls_model_path = "shape_yolo.pt"

    # Warning 숨기기
    warnings.filterwarnings("ignore", message="The parameter 'pretrained' is deprecated", category=UserWarning)
    warnings.filterwarnings("ignore",
                            message="Arguments other than a weight enum or `None` for 'weights' are deprecated",

                            category=UserWarning)
    # cv2.imshow("", image)
    # cv2.waitKey()

    # Pill detection
    detected_boxes, result_image = Pill_detect.detect_pill(model_path, image)

    # Pill color
    cropped_images = Pill_crop.crop_pill(result_image, detected_boxes, output_dir)
    pass

    result_dict = {i: dict() for i in range(len(cropped_images))}

    for n in range(len(cropped_images)):
        pill_color = Pill_color.detect_pill_color(cropped_images[n])
        # for filename in os.listdir(output_dir):
        #     if filename.endswith(".jpg") or filename.endswith(".png"):
        #         color_path = os.path.join(output_dir, filename)
        #         color_path = color_path.replace("/", "\\")
        #         pill_color = Pill_color.detect_pill_color(color_path)
        result_dict[n]["pill_color"] = pill_color
        print("Detected color:", pill_color)

        # Pill shape
        pill_shape = shape.shape_detect(cls_model_path, cropped_images)
        result_dict[n]["pill_shape"] = pill_shape
        print("Detected shape:", pill_shape)

        # Pill text
        # for filename in os.listdir(output_dir):
        #     if (filename.endswith(".jpg") or filename.endswith(".png")):
        #         image_path = os.path.join(output_dir, filename).replace("/", "\\")
        image_path = output_dir + "\\" + "cropped_object_" + str(n) + ".jpg"
        pill_text = Pill_text.detect_text(image_path, key_path)
        result_dict[n]["pill_text"] = pill_text
        print("Detected text:", pill_text)
        os.remove(image_path)

        # 생성된 파일 삭제
        # file_paths = []
        # for filename in os.listdir(output_dir):
        #     if filename.endswith(".jpg") or filename.endswith(".png"):
        #         image_path = os.path.join(output_dir, filename)
        #         image_path = image_path.replace("/", "\\")
        #         file_paths.append(image_path)

        # for file_path in file_paths:
        #     if os.path.exists(file_path):
        #         os.remove(file_path)

    return result_dict


if __name__ == '__main__':
    run()
