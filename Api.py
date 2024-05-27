import requests

class RestApi:
    def __init__(self):
        self.basic_url = "http://15.165.129.252:8080/"

    def getFromText(self, pill_text: str):
        url = self.basic_url + "/api/pill/print/" + pill_text
        data = None

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

        return data

    def getFromColor(self, pill_color: str):
        url = self.basic_url + "/api/pill/color/" + pill_color
        data = None

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

        return data

    def getFromShape(self, pill_shape: str):
        url = self.basic_url + "/api/pill/shape/" + pill_shape
        data = None

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

        return data

    def find_pills(self,detected_color: str, detected_shape: str, detected_text: str):
        restapi = RestApi()
        found_pills = []
        pill_search_text = restapi.getFromText(detected_text)
        pill_search_shape = restapi.getFromShape(detected_shape)
        pill_search_color = restapi.getFromColor(detected_color)

        if pill_search_text:
            found_pills = pill_search_text
        if pill_search_color:
            if found_pills:
                found_pills = [pill for pill in found_pills if pill_search_color]
            else:
                found_pills = pill_search_color
        if pill_search_shape:
            if found_pills:
                found_pills = [pill for pill in found_pills if pill_search_shape]
            else:
                found_pills = pill_search_shape

        if not found_pills:
            print('알약을 찾을 수 없습니다')

        return found_pills
if __name__ == "__main__":
    restapi = RestApi()
    result = restapi.find_pills("갈색", "장방형", "FT-CRE")
    #result = restapi.getFromText("FT-CRE")
    print(result)


