from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

def shape_detect(model_path, image_path):
    model = YOLO(model_path)
    results = model.predict(image_path)

    result = results[0]
    probs = result.probs
    predicted_class_index = probs.top1

    predicted_class_name = model.names[predicted_class_index]
    if predicted_class_name == "circle":
        pill_shape = "원형"
    elif predicted_class_name == "crescent":
        pill_shape = "반원형"
    elif predicted_class_name == "diamond":
        pill_shape = "마름모형"
    elif predicted_class_name == "etc":
        pill_shape = "기타"
    elif predicted_class_name == "hexagon":
        pill_shape = "육각형"
    elif predicted_class_name == "oblong":
        pill_shape = "장방형"
    elif predicted_class_name == "octagon":
        pill_shape = "팔각형"
    elif predicted_class_name == "pentagon":
        pill_shape = "오각형"
    elif predicted_class_name == "rectangle":
        pill_shape = "사각형"
    elif predicted_class_name == "triangle":
        pill_shape = "삼각형"
    elif predicted_class_name == "oval":
        pill_shape = "타원형"
    return pill_shape


if __name__ == '__main__':
    model_path = "C:/Image_Recognition/pill_detection/best (2).pt"
    image_path = "C:/Image_Recognition/pill_detection/test_image/K-031142_0_2_0_2_70_340_200.png"
    predicted_class_name = shape_detect(model_path, image_path)
    print("Predicted class:", predicted_class_name)