
'''
import datetime
timestamp = 1577916881
value = datetime.datetime.fromtimestamp(timestamp)
print(value.strftime('%Y-%m-%d %H:%M:%S'))

a = value.strftime('%Y')
a = int(a)'''

a = {"from":"0x773f8361d112a99540118a8c10242b10","to":"0x383bcb1a7be9647494d87c60b075510d"}
import json

a=[]
f=open('22.txt')
for line in f:
    line=line.rstrip('\n')
    a.append(line)

print(
