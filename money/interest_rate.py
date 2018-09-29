#-- 利率 --

import requests
import json
from bs4 import BeautifulSoup

import requests

cookies = {
    'Hm_lvt_f65ab30a4196388f1696a9a62fbdc763': '1503068767',
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
list_3month=[]
list_6month=[]
list_1year=[]
list_2year=[]
list_3year=[]
list_5year=[]

i = 0
for tr in trs :
    index = 0
    tds = tr.find_all("td")
    bank_name = ""

    # 活期
    demand_deposit_interest_rate = 0.0

    # 整存整取
    whole_deposit_and_whole_withdrawal_3month = 0.0
    whole_deposit_and_whole_withdrawal_6month = 0.0
    whole_deposit_and_whole_withdrawal_1year = 0.0
    whole_deposit_and_whole_withdrawal_2year = 0.0
    whole_deposit_and_whole_withdrawal_3year = 0.0
    whole_deposit_and_whole_withdrawal_5year = 0.0

    # 零存整取
    lump_sum_withdrawal_1year = 0.0
    lump_sum_withdrawal_3year = 0.0
    lump_sum_withdrawal_5year = 0.0


    bank_name = tds[index].get_text()
    index += 1
    if i == 0 :
        # 人民银行基准
        bank_name = "人民银行基准"
        index += 1

    demand_deposit_interest_rate = tds[index].get_text()
    index += 1

    whole_deposit_and_whole_withdrawal_3month = tds[index].get_text()
    index += 1
    if i != 0 :
        list_3month.append({
            "name":bank_name,
            "rate":whole_deposit_and_whole_withdrawal_3month
        })
    
    whole_deposit_and_whole_withdrawal_6month = tds[index].get_text()
    index += 1
    list_6month.append({
        "name":bank_name,
        "rate":whole_deposit_and_whole_withdrawal_6month
    })

    whole_deposit_and_whole_withdrawal_1year = tds[index].get_text()
    index += 1
    if i != 0 :
        list_1year.append({
            "name":bank_name,
            "rate":whole_deposit_and_whole_withdrawal_1year
        })

    whole_deposit_and_whole_withdrawal_2year = tds[index].get_text()
    index += 1
    list_2year.append({
        "name":bank_name,
        "rate":whole_deposit_and_whole_withdrawal_2year
    })    

    whole_deposit_and_whole_withdrawal_3year = tds[index].get_text()
    index += 1
    if i != 0 :
        list_3year.append({
            "name":bank_name,
            "rate":whole_deposit_and_whole_withdrawal_3year
        })    

    whole_deposit_and_whole_withdrawal_5year = tds[index].get_text()
    index += 1
    if i != 0 :
        list_5year.append({
            "name":bank_name,
            "rate":whole_deposit_and_whole_withdrawal_5year
        })

    lump_sum_withdrawal_1year = tds[index].get_text()
    index += 1

    lump_sum_withdrawal_3year = tds[index].get_text()
    index += 1

    lump_sum_withdrawal_5year = tds[index].get_text()
    index += 1

    i += 1

    item = {
        "title": "{} 整存整取利率".format(bank_name),
        "subtitle": "活期:{}%|3月:{}%|6月:{}%|1年:{}%|2年:{}%|3年:{}%|5年:{}%".format(
            demand_deposit_interest_rate,
            whole_deposit_and_whole_withdrawal_3month,
            whole_deposit_and_whole_withdrawal_6month,
            whole_deposit_and_whole_withdrawal_1year,
            whole_deposit_and_whole_withdrawal_2year,
            whole_deposit_and_whole_withdrawal_3year,
            whole_deposit_and_whole_withdrawal_5year
        ), 
        "icon": {
            "path": "img/money.png"
        }
    }
    alfredResponse.append(item)

list_3month.sort(key=lambda e: e["rate"], reverse=True)
list_6month.sort(key=lambda e: e["rate"], reverse=True)
list_1year.sort(key=lambda e: e["rate"], reverse=True)
list_2year.sort(key=lambda e: e["rate"], reverse=True)
list_3year.sort(key=lambda e: e["rate"], reverse=True)
list_5year.sort(key=lambda e: e["rate"], reverse=True)

list_3month_item = {
    "title":"三个月max {}, min {}".format(list_3month[0]["name"], list_3month[-1]["name"]),
    "subtitle": "最大利率为 {}%, 最小利率为 {}%".format(list_3month[0]["rate"], list_3month[-1]["rate"]),
    "icon":{
        "path": "img/money.png"
    }
}

list_6month_item = {
    "title":"六个月max {}, min {}".format(list_6month[0]["name"], list_6month[-1]["name"]),
    "subtitle": "最大利率为 {}%, 最小利率为 {}%".format(list_6month[0]["rate"], list_6month[-1]["rate"]),
    "icon":{
        "path": "img/money.png"
    }
}

list_1year_item = {
    "title":"一年max {}, min {}".format(list_1year[0]["name"], list_1year[-1]["name"]),
    "subtitle": "最大利率为 {}%, 最小利率为 {}%".format(list_1year[0]["rate"], list_1year[-1]["rate"]),
    "icon":{
        "path": "img/money.png"
    }
}

list_2year_item = {
    "title":"二年max {}, min {}".format(list_2year[0]["name"], list_2year[-1]["name"]),
    "subtitle": "最大利率为 {}%, 最小利率为 {}%".format(list_2year[0]["rate"], list_2year[-1]["rate"]),
    "icon":{
        "path": "img/money.png"
    }
}

list_3year_item = {
    "title":"三年max {}, min {}".format(list_3year[0]["name"], list_3year[-1]["name"]),
    "subtitle": "最大利率为 {}%, 最小利率为 {}%".format(list_3year[0]["rate"], list_3year[-1]["rate"]),
    "icon":{
        "path": "img/money.png"
    }
}


list_5year_item = {
    "title":"五年max {}, min {}".format(list_5year[0]["name"], list_5year[-1]["name"]),
    "subtitle": "最大利率为 {}%, 最小利率为 {}%".format(list_5year[0]["rate"], list_5year[-1]["rate"]),
    "icon":{
        "path": "img/money.png"
    }
}

data = {
    "items" : [list_3month_item, list_6month_item, list_1year_item, list_2year_item, list_3year_item, list_5year_item] + alfredResponse
}    

print(json.dumps(data))