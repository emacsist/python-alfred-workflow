# 分期付款计算器

import time
import json

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

# print(fields)

if len(fields) != 3:
    alreds.add(new_default_alfred_element(title="错误参数", subtitle=",".join(fields)))
else:
    total_money = float(fields[0])
    total_months = float(fields[1])
    month_rate = float(fields[2])

    # 年利率=12*每期手续费*分期期数/[（1+分期期数)/2]
    # 名义利率

    year_rate_logic = month_rate * 12
    # 实际利率 = (期数 * 2) / (期数 + 1) * 名义年利率
    # 12 * month_rate * total_months / ((1 + total_months) / 2)
    year_rate_real = (total_months * 2) / (total_months + 1) * year_rate_logic

    alreds.add(new_default_alfred_element(title="名义年利率", subtitle=("%.2f%%" % year_rate_logic)))
    alreds.add(new_default_alfred_element(title="实际年利率", subtitle=("%.2f%%" % year_rate_real)))

    # 每月的本金
    month_money_original = (total_money / total_months)
    # 每月利息
    month_interest = (total_money * month_rate / 100)
    # 每月应还
    month_real_money = month_interest + month_money_original

    alreds.add(new_default_alfred_element(title="每月还本金", subtitle=("%.2f 元" % month_money_original)))
    alreds.add(new_default_alfred_element(title="每月还利息", subtitle=("%.2f 元" % month_interest)))
    alreds.add(new_default_alfred_element(title="每月还款额", subtitle=("%.2f 元" % month_real_money)))
    alreds.add(new_default_alfred_element(title="总还款利息", subtitle=("%.2f 元" % (month_interest * total_months))))
    alreds.add(new_default_alfred_element(title="总还款金额", subtitle=("%.2f 元" % (month_real_money * total_months))))

alreds.to_string()
