import requests as rq

api_link = "http://127.0.0.1:5000/generate-image"
req = rq.post(api_link, json={"text": "pegions"})
print(req.json())