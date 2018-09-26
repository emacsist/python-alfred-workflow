import sys
import json

BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

rawString=sys.argv[1]
# GBa3ZaMWV => 4288568232571445
#rawString="4288568232571445"

def int10to62(midString):
    mid = int(midString)
    result = ""
    while mid > 0 :
        a = mid % 62
        result = "{}{}".format(BASE62[a], result)
        mid = int((mid - a) / 62)
    return result

def encode(midString):
    result = ""

    i = len(midString) - 7
    while i > -7:
        offset1 =  0 if i < 0 else i
        offset2 = i + 7
        base62String = int10to62(midString[offset1:offset2])

        if i > 0 and len(base62String) < 4 :
            zeroLen = 4 - len(base62String)
            for _ in range(zeroLen):
                base62String = "0" + base62String

        result = base62String + result
        i-= 7
    return result

base62String = encode(rawString)

item = {
    "title" : rawString,
    "subtitle": base62String,
    "arg": base62String,
    "icon": {
        "path":"img/hash.png"
    }
}

alfredResponse = []
alfredResponse.append(item)

alfredData = {
    "items":alfredResponse
}

print(json.dumps(alfredData))