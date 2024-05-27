import cv2
import logging
from ultralytics import YOLO

logging.getLogger("ultralytics").setLevel(logging.WARNING)
def detect_pill(model_path, image_path):
    model = YOLO(model_path, verbose=False)
    image = cv2.imread(image_path)
    results = model(image)

    detected_boxes =[]

    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy()
        scores = result.boxes.conf.cpu().numpy()
        classes = result.boxes.cls.cpu().numpy()

        for box, score, cls in zip(boxes, scores, classes):
            x1, y1, x2, y2 = map(int, box)
            label = f"{model.names[int(cls)]}: {score: .2f}"
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            detected_boxes.append((x1, y1, x2, y2))

    if not detected_boxes:
        return None

    return detected_boxes, image