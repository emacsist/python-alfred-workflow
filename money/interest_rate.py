#-- 利率 --

import requests
import json
from bs4 import BeautifulSoup
import sys
import time
import numpy as np

import requests

cookies = {
    'Hm_lvt_f65ab30a4196388f1696a9a62fbdc763': str(int(time.time())),
    'vjuids': '-208f65f5a.15d44652056.0.1a123f655672d',
    'CNZZDATA1262910149': '1747259592-1503067974-http%253A%252F%252Fjingzhi.funds.hexun.com%252F%7C1503067974',
    '__utma': '194262068.1789259452.1503068837.1503068837.1503068837.1',
    '__utmz': '194262068.1503068837.1.1.utmcsr=jingzhi.funds.hexun.com|utmccn=(referral)|utmcmd=referral|utmcct=/000248.shtml',
    'cn_1263247791_dplus': '%7B%22distinct_id%22%3A%20%2215d4b0d34ba81d-0931eed5af693b-1b3f6d54-1aeaa0-15d4b0d34bba58%22%2C%22sp%22%3A%20%7B%22userID%22%3A%20%22%22%2C%22userName%22%3A%20%22%22%2C%22userType%22%3A%20%22nologinuser%22%2C%22userLoginDate%22%3A%20%2220170911%22%2C%22%24recent_outside_referrer%22%3A%20%22%24direct%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201505098587%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201505098587%7D%2C%22initial_view_time%22%3A%20%221505097262%22%2C%22initial_referrer%22%3A%20%22%24direct%22%2C%22initial_referrer_domain%22%3A%20%22%24direct%22%7D',
    'UM_distinctid': '15d4b0d34ba81d-0931eed5af693b-1b3f6d54-1aeaa0-15d4b0d34bba58',
    'ADVC': '356654af22a99b',
    'ADVS': '357ab2966b2846',
    'ASL': '17422,000xv,7416a2ea7143084f',
    'vjlast': '1500091064.1507722395.11',
    'hxck_webdev1_general': 'fundlist=150200_0|501050_0|510880_0|340005_0|000248_0&stocklist=002505_2',
    '__jsluid': 'db9a9e65d6497e8b0f30b5811d078b97',
    'HexunTrack': 'SID=201707151157400742b86fd5557e2416fb5a7b39dbd78311d&CITY=4403&TOWN=440300',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.22 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'https://www.google.com/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}

response = requests.get('http://data.bank.hexun.com/ll/ckll.aspx', headers=headers, cookies=cookies)


parsedHTML = BeautifulSoup(response.content, "lxml")
table = parsedHTML.find("table", attrs={"class":"bankTable"})

trs = table.tbody.find_all("tr")


alfredResponse=[]

list_data_item=[[], [], [], [], [], []]

i = 0
input_bank = "工"

if len(sys.argv) >= 2:
    input_bank = sys.argv[1]

#print("输入的ban为 {}".format(input_bank))

def subtitleFormat(item):
    subtitleFormat="max:{}%, min:{}%, diff: {:.2f}%, 存1W元每期相差:{:.2f}元"
    maxRate = "0.0" if item[0]["rate"] == "--" else item[0]["rate"]
    minRate = "0.0" if item[-1]["rate"] == "--" else item[-1]["rate"]
    diff_rate = float(maxRate)-float(minRate)
    return subtitleFormat.format(item[0]["rate"], item[-1]["rate"], diff_rate, diff_rate * 100)

for tr in trs :
    index = 0
    tds = tr.find_all("td")
    bank_name = ""
    list_data_item_index = 0

    # 整存整取
    #活期, 3个月, 6个月, 1年, 2年, 3年, 5年, 0存整取1年, 0存整取3年, 0存整取5年
    # 共10个元素
    data_wdww_index = 0
    data_wdww = [0.0 for x in range(10)]

    bank_name = tds[index].get_text()
    index += 1
    if i == 0 :
        # 人民银行基准
        bank_name = "人民银行基准"
        index += 1
        

    if bank_name != "人民银行基准" and (input_bank.strip() != "" and input_bank not in bank_name):
        continue

    # 活期 -> 0存整取5年
    # http://data.bank.hexun.com/ll/ckll.aspx
    for tdindex in range(0, 10):      
        data_wdww[data_wdww_index] = tds[tdindex + index].get_text()
        # 只处理 整存整取 范围的
        if i != 0 and tdindex > 0 and tdindex < 7:
            list_data_item[list_data_item_index].append({
                "name":bank_name,
                "rate":data_wdww[data_wdww_index]
            })
            list_data_item_index += 1
        data_wdww_index += 1
        
    i += 1
    item = {
        "title": "{} 整存整取利率".format(bank_name),
        "subtitle": "活期:{}%|3月:{}%|6月:{}%|1年:{}%|2年:{}%|3年:{}%|5年:{}%".format(
            data_wdww[0],
            data_wdww[1],
            data_wdww[2],
            data_wdww[3],
            data_wdww[4],
            data_wdww[5],
            data_wdww[6]
        ), 
        "icon": {
            "path": "img/money.png"
        }
    }

    item2 = {
        "title": "{} 零存整取利率".format(bank_name),
        "subtitle": "1年:{}%|3年:{}%|5年:{}%".format(
            data_wdww[7],
            data_wdww[8],
            data_wdww[9]
        ), 
        "icon": {
            "path": "img/money.png"
        }
    }
    alfredResponse.append(item)
    alfredResponse.append(item2)

name_map = {
    "0":"三个月",
    "1":"六个月",
    "2":"一年",
    "3":"二年",
    "4":"三年",
    "5":"五年"
}

for i, ele in enumerate(list_data_item):
    #print("{} => {}".format(i, ele))
    ele.sort(key=lambda e: e["rate"], reverse=True)    
    item = {
        "title":"{}max {}, min {}".format(name_map[str(i)], ele[0]["name"], ele[-1]["name"]),
        "subtitle": subtitleFormat(ele),
        "icon":{
            "path": "img/money.png"
        }
    }
    alfredResponse = [item] + alfredResponse

data = {
    "items" : alfredResponse
}    

print(json.dumps(data))