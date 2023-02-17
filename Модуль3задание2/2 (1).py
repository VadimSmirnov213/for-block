import datetime, json

adr = "6893471494264041902476759713387637260397696323592049455435171115739407560315033" \
      "370567624081459643613290304703351527410005665278225022404900561112668260023"

with open("Task2-txlist.txt", "r") as file:
    data = file.read().split("\n")
lst = []

for i in data:
    n = json.loads(i)
    lst.append(n)

data = lst
mm1 = 0
mm2 = 0
b1 = 0
b2 = 0

for i in data:
    dt = datetime.datetime.fromtimestamp(i["time"]).month
    if dt <= 6:
        if i["type"] in ["receive", "input"] and i["to"] == adr:
            b1 += int(i["value"])
            mm1 += 1
    else:
        if i["type"] in ["receive", "input"] and i["to"] == adr:
            b2 += int(i["value"])
            mm2 += 1

print(f"Кол-во транзакций в первое полугодие: {mm1} на сумму {b1}")
print(f"Кол-во транзакций во второе полугодие: {mm2} на сумму {b2}")
print(f"Во сколько раз доходы в первой и во второй половине отличаются: {round(b1/b2, 3)}")

'''
summ1 = 0
col1 = 0

summ2 = 0
col2 = 0

for i in range(0,300):
    if int(datetime.datetime.fromtimestamp(int(data[i]['time'])).strftime('%m')) <= 6:
        if (data[i]['type'] == 'input' or data[i]['type'] == 'receive') and data[i]['from'] == adres:
            summ1 = summ1 + data[i]['value']
            col1 = col1 + 1
        elif data[i]['type'] == 'send' or data[i]['type'] == 'cash' and data[i]['to'] == adres:
            summ1 = summ1 + data[i]['value']
            col1 = col1 + 1
    if int(datetime.datetime.fromtimestamp(int(data[i]['time'])).strftime('%m')) > 6:
        if (data[i]['type'] == 'input' or data[i]['type'] == 'receive') and data[i]['from'] == adres:
            summ2 = summ2 + data[i]['value']
            col2 = col2 + 1
        elif data[i]['type'] == 'send' or data[i]['type'] == 'cash' and data[i]['to'] == adres:
            summ1 = summ1 + data[i]['value']
            col2 = col2 + 1
        
print(col1, '- количество транзакций с доходами за первое полугодие')
print(col2, '- количество транзакций с доходами за второе полугодие')
print(summ1, '- сумма транзакций с доходами за первое полугодие')
print(summ2, '- сумма транзакций с доходами за второе полугодие')
r = summ1 / summ2
print(round(r, 3), '- во сколько раз доходы за 1 полугодие отличаются от доходов за 2 полугодие')
            
'''
