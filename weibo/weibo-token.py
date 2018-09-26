import requests
import sys
import json
import time

token=sys.argv[1]

data = {
    "access_token":token
}

response = requests.post("https://api.weibo.com/oauth2/get_token_info", data=data).json()

alredResponse = []

for k, v in response.items():
    item = {
        "title": k,
        "subtitle":v,
        "arg":v,
        "icon": {
            "path":"img/weibo.png"
        }
    }

    if k == "uid" :
        item["arg"] = "http://weibo.com/u/{}".format(v) 

    if k == "create_at":
        old_subtitle = item["subtitle"]
        full_createat = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(v))
        item["subtitle"] = "{} / {}".format(old_subtitle, full_createat)
    elif k == "expire_in":
        old_subtitle = item["subtitle"]
        expireIn = response["create_at"] + v
        full_expire = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(expireIn))
        item["subtitle"] = "{} / {}".format(old_subtitle, full_expire)
        

    alredResponse.append(item)    

alfredData = {
    "items": alredResponse
}    

print(json.dumps(alfredData))