import requests
import urllib.parse
import sys
import json

query = sys.argv[1]

params = {
    "count": 20,
    "q": query
}

response = requests.get(
    'https://api.douban.com/v2/movie/search?'+urllib.parse.urlencode(params))


alfredList = []


def addMember(movie):
    score = movie["rating"]["average"]

    title = movie["title"]
    pubdate = movie["year"]
    subtitle = movie["original_title"]
    authorList = []
    for author in movie["directors"]:
        authorList.append(author["name"])

    # 电影 url
    alt = movie["alt"]

    realTitle = title

    if len(subtitle) > 0:
        realTitle = title + " / " + subtitle

    item = {
        "type": "file",
        "title": realTitle,
        "arg": alt,
        "subtitle": "导演: {}, 评分 {}, 日期: {}".format(",".join(authorList), score, pubdate),
        "icon": {
            "path": "img/movie.png"
        }
    }
    alfredList.append(item)


for movie in response.json()["subjects"]:
    addMember(movie)

data = {
    "items": alfredList
}

print(json.dumps(data))
