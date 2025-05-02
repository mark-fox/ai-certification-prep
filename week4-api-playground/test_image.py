import requests

with open(".\week3-pretrained-models\sample-images\Penguin.jpg", "rb") as img:
    response = requests.post("http://127.0.0.1:5000/classify-image", files={"image": img})
    print(response.json())
