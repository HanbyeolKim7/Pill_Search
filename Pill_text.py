import io
from google.cloud import vision
from google.oauth2 import service_account

def detect_text(image_path, key_path):
    credentials = service_account.Credentials.from_service_account_file(key_path)
    client = vision.ImageAnnotatorClient(credentials=credentials)

    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if texts:
        detected_text = texts[0].description
        return detected_text

if __name__ == "__main__":
    image_path = "C:/Image_Recognition/pill_detection/cro/0e6du5cvjrl4102_object_0.jpg"
    key_path = "C:/Users/hanby/Downloads/pill-423416-edf9cc43013f.json"
    print(detect_text(image_path, key_path))  # 두 개의 인수 전달

