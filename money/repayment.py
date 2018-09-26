# -*- coding: utf-8 -*-
# 贷款还款
import json
import sys

import time

reload(sys)
sys.setdefaultencoding('UTF8')

input_data = '{query}'

KEY = "items"

UID_KEY = "uid"
TYPE_KEY = "type"
TITLE_KEY = "title"
SUBTITLE_KEY = "subtitle"
ARG_KEY = "arg"
AUTOCOMPLETE_KEY = "autocomplete"
ICON_KEY = "icon"
ICON_TYPE_KEY = "type"
ICON_PATH_KEY = "path"


def new_default_alfred_element(types="text", title="", subtitle="", arg="", autocomplete="", icon={}):
    millis = int(round(time.time() * 1000))
    default_element = {UID_KEY: str(millis), TYPE_KEY: types, TITLE_KEY: title, SUBTITLE_KEY: subtitle, ARG_KEY: arg, AUTOCOMPLETE_KEY: autocomplete, ICON_KEY: icon}
    return default_element


class AlfredResult:

    def __init__(self):
        self.result = {KEY: []}

    def add(self, element):
        self.result[KEY].append(element)

    def to_string(self):
        print(json.dumps(self.result))


alreds = AlfredResult()

fields = input_data.split()


# 等额本息
def average_capital_plus_interest(year_rate, years=0, total=0.0):
    # [贷款本金×月利率×（1+月利率）^还款月数]÷[（1+月利率）^还款月数－1]
    year_rate = year_rate / 100.0
    month_rate = year_rate / 12.0

    total_months = years * 12
    current_month = 1

    total_tmp = total
    total_interest = 0
    total_capital = 0
    total_pay = 0
    while current_month <= total_months:
        total_pay_per_month = (total * month_rate * pow((1 + month_rate), total_months)) / (pow(1 + month_rate, total_months) - 1)
        total_pay += total_pay_per_month

        current_month_interest = total_tmp * month_rate
        total_interest += current_month_interest

        current_month_capital = total_pay_per_month - current_month_interest
        total_capital += current_month_capital

        # print("第 {} 月, 还的本金为 {:.2f} 元, 利息为 {:.2f} 元, 一共 {:.2f} 元".format(current_month, current_month_capital, current_month_interest, total_pay_per_month))
        total_tmp -= current_month_capital
        current_month += 1

    # print("一共还利息 {:.2f}, 一共还了 {:.2f} {:.2f}%%".format(total_interest, total_pay, (total_pay - total) / float(total) * 100))
    prefix = "等额本息(每月还款额都是固定的)"
    ele = new_default_alfred_element(title="{}, 每月要还".format(prefix), subtitle="{:.2f} 元".format(total_pay / float(total_months)))
    alreds.add(ele)
    ele = new_default_alfred_element(title="{}, 一共还".format(prefix), subtitle="{:.2f} 元".format(total_pay))
    alreds.add(ele)
    ele = new_default_alfred_element(title="{}, 利息占比".format(prefix), subtitle="{:.2f}%".format((total_pay - total) / float(total) * 100))
    alreds.add(ele)


# 等额本金
def average_capital(year_rate, years=0, total=0.0, n_month=1):
    year_rate = year_rate / 100.0
    month_rate = year_rate / 12.0
    # 每月还款金额= （贷款本金/ 还款月数）+（本金 — 已归还本金累计额）×每月利率

    total_months = years * 12
    current_month = 1

    payed_capital_money = 0

    total_interest = 0
    total_pay = 0

    # alred
    prefix = "等额本金(每月还款额不是固定的)"

    while current_month <= total_months:
        total_pay_per_month = total / total_months + (total - payed_capital_money) * month_rate
        total_pay += total_pay_per_month
        payed_capital_money += total / total_months

        current_month_interest = total_pay_per_month - total / total_months
        total_interest += current_month_interest

        # print("第 {} 月, 还的本金为 {:.2f}, 利息为 {:.2f}, 一共要还 {:.2f}".format(current_month, float(total) / total_months, current_month_interest, total_pay_per_month))

        if current_month == n_month:
            ele = new_default_alfred_element(title="{}, 第{}个月要还".format(prefix, int(n_month)), subtitle="{:.2f} 元".format(total_pay_per_month))
            alreds.add(ele)

        current_month += 1

    # print("一共还利息 {:.2f}, 一共还了 {:.2f}, {:.2f} %".format(total_interest, total_pay, (total_pay - total) / float(total) * 100))
    ele = new_default_alfred_element(title="{}, 一共还".format(prefix), subtitle="{:.2f} 元".format(total_pay))
    alreds.add(ele)
    ele = new_default_alfred_element(title="{}, 利息占比".format(prefix), subtitle="{:.2f}%".format((total_pay - total) / float(total) * 100))
    alreds.add(ele)


if len(fields) >= 3:
    total_pay_money = float(fields[0])
    total_year = float(fields[1])
    year_rate = float(fields[2])
    n_month = 1
    if len(fields) >= 4:
        n_month = float(fields[3])

    average_capital_plus_interest(year_rate, total_year, total_pay_money)
    average_capital(year_rate, total_year, total_pay_money, n_month)
else:
    alreds.add(new_default_alfred_element(title="错误参数 {}".format(len(fields)), subtitle=",".join(fields)))
alreds.to_string()