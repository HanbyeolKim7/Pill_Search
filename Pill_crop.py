import cv2
from ultralytics import YOLO
import os

def crop_pill(image_path, detected_boxes, output_dir):
    image = cv2.imread(image_path)

    cropped_images = []
    for idx, (x1, y1, x2, y2) in enumerate(detected_boxes):
        cropped_image = image[y1:y2, x1:x2]
        cropped_output_path = os.path.join(output_dir, f"cropped_object_{idx}.jpg")
        cv2.imwrite(cropped_output_path, cropped_image)
        cropped_images.append(cropped_image)

    return cropped_images
