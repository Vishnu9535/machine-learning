import requests 
import sys 
import json

# if len(sys.argv) !=2:
#     sys.exit()

responce = requests.get("https://api.github.com/events",stream=True)
print(json.dumps(responce.json(),indent=2))
# responce=responce.json()
# for i in responce["results"]:
#     print(i["trackName"])