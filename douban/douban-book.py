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
    'https://api.douban.com/v2/book/search?'+urllib.parse.urlencode(params))


alfredList = []


def addMember(book):
    score = book["rating"]["average"]
    numRaters = book["rating"]["numRaters"]

    title = book["title"]
    pubdate = book["pubdate"]
    subtitle = book["subtitle"]
    author = book["author"]
    # 书的 url
    alt = book["alt"]
    price = book["price"]

    realTitle = title

    if len(subtitle) > 0:
        realTitle = title + "/" + subtitle

    item = {
        "type": "file",
        "title": realTitle,
        "arg": alt,
        "subtitle": "作者: {}, 评分 {}/{}, 价格: {}, 出版日期: {}".format(author, score, numRaters, price, pubdate),
        "icon": {
            "path": "img/book.png"
        }
    }
    alfredList.append(item)


for book in response.json()["books"]:
    addMember(book)

data = {
    "items": alfredList
}

print(json.dumps(data))
