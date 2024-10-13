import requests

responce = requests.post(
    "http://localhost:8000/essay/invoke",
    json= {'input':{"topic":"my best friend"}})
print(responce.json()['output']['content'])