import sys
import json

BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

inputBase62String=sys.argv[1]
# GBa3ZaMWV => 4288568232571445
#inputBase62String = "GBa3ZaMWV"



def base62ToInt10String(base62String):
    base10String = ""
    c = 0
    for i in range(len(base62String)):
        n = len(base62String) - i - 1
        s = base62String[i:i+1]

        for k in range(len(BASE62)):
            if s == BASE62[k]:
                c += int(k * pow(62, n))
                break
        base10String = str(c)
    return base10String


def decode(base62String):
    base10Sring = ""

    i = len(base62String) - 4
    while i > -4:
        offset1 = 0 if i < 0 else i
        offset2 = i + 4
        base62TmpString = base62String[offset1:offset2]
        base10TmpString = base62ToInt10String(base62TmpString)

        if offset1 > 0:
            base10TmpString = base10TmpString.zfill(7)

        base10Sring = base10TmpString + base10Sring
        i -= 4

    return int(base10Sring)


decodedBase62String = decode(inputBase62String)

item = {
    "title": inputBase62String,
    "subtitle": decodedBase62String,
    "arg": decodedBase62String,
    "icon": {
        "path": "img/hash.png"
    }
}

alfredResponse = []
alfredResponse.append(item)

alfredData = {
    "items": alfredResponse
}

print(json.dumps(alfredData))
