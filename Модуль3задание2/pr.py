adres = '6893471494264041902476759713387637260397696323592049455435171115739407560315033370567624081459643613290304703351527410005665278225022404900561112668260023'

import hashlib
import datetime
import json
import ast


time = 1577916881
a = datetime.datetime.fromtimestamp(time)
a = a.strftime('%m')

with open('Task2-txlist.txt') as file:
    data = [ast.literal_eval(line) for line in file]
mm1 = 0
mm2 = 0
b1 = 0
b2 = 0

for i in data:
    dt = datetime.datetime.fromtimestamp(i['time']).month
    if dt <= 6:
        if (i['type'] == 'receive' or i['type'] == 'input') and i['to'] == adres:
            b1 += int(i['value'])
            mm1 += 1
    else:
        if i["type"] in ["receive", "input"] and i["to"] == adres:
            b2 += int(i["value"])
            mm2 += 1
            
