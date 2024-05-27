import cv2
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def train_knn_classifier():
    color_ranges = {
        '갈색': [(100, 100, 100), (50, 30, 30)],
        '연두': [(50, 100, 100), (255, 255, 0)],
        '노랑': [(30, 100, 100), (255, 255, 255)],
        '하양': [(180, 100, 100), (255, 255, 255)],
        '분홍': [(170, 100, 100), (255, 192, 203)],
        '주황': [(10, 100, 100), (255, 165, 255)],
        '초록': [(50, 100, 100), (0, 128, 0)],
        '투명': [(0, 0, 0), (255, 255, 255)],
        '검정': [(0, 0, 0), (0, 0, 0)],
        '자주': [(150, 100, 100), (255, 0, 255)],
        '빨강': [(0, 100, 100), (255, 0, 0)],
        '파랑': [(110, 100, 100), (0, 0, 255)],
        '회색': [(0, 0, 0), (128, 128, 128)],
        '청록': [(170, 100, 100), (0, 128, 128)],
        '남색': [(170, 100, 100), (0, 0, 128)],
        '보라': [(150, 100, 100), (128, 0, 128)]
    }

    X_train = []
    y_train = []

    for color, (lower, upper) in color_ranges.items():
        lower = np.array(lower)
        upper = np.array(upper)
        X_train.append((lower + upper)/2)
        y_train.append(color)

    X_train = np.array(X_train)
    y_train = np.array(y_train)

    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(X_train, y_train)

    return knn

def detect_pill_color(image_path):
    knn = train_knn_classifier()
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    mean_hsv = np.mean(hsv_image.reshape(-1,3), axis=0)
    predicted_color = knn.predict([mean_hsv])[0]

    return predicted_color

if __name__ == "__main__":
    image_path = "C:/Image_Recognition/pill_detection/cro/0e6du5cvjrl4102_object_0.jpg"

    print(detect_pill_color(image_path))