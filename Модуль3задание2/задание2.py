import ast

import datetime
timestamp = 1577916881
value = datetime.datetime.fromtimestamp(timestamp)
#print(value.strftime('%Y-%m-%d %H:%M:%S'))
a = value.strftime('%m')
a = int(a)

adres = '6893471494264041902476759713387637260397696323592049455435171115739407560315033370567624081459643613290304703351527410005665278225022404900561112668260023'
 
with open('Task2-txlist.txt') as f:
    data = [ast.literal_eval(line) for line in f]
 

mm1 = 0
mm2 = 0
b1 = 0
b2 = 0

for i in data:
    dt = datetime.datetime.fromtimestamp(i["time"]).month
    if dt <= 6:
        if i["type"] in ["receive", "input"] and i["to"] == adres:
            b1 += int(i["value"])
            mm1 += 1
    else:
        if i["type"] in ["receive", "input"] and i["to"] == adres:
            b2 += int(i["value"])
            mm2 += 1

print(f"Кол-во транзакций в первое полугодие: {mm1} на сумму {b1}")
print(f"Кол-во транзакций во второе полугодие: {mm2} на сумму {b2}")
print(f"Во сколько раз доходы в первой и во второй половине отличаются: {round(b1/b2, 3)}")
        
        


