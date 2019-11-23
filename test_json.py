import codecs
import csv
import json
from itertools import islice

# 读取各种类型的文件 .json  .txt  .csv
# 注意：谨防重名导致导入失败，不要将文件命名为 json.py
# as 可用于起别名
# json.loads(data) 将字符串转化为json格式
# read() 读取整个文件  readline()读取一行数据   readlines()读取所有行的数据
# a[::-1]  字符串反转
# a[:-1]   从位置0到位置-1之前的数,最后一个位置为-1.
# b = a[i:j]   表示复制a[i]到a[j-1]，以生成新的list对象  当i,j都缺省时，a[:]就相当于完整复制一份a
# 读取csv文件 谨防 中文乱码 + 表头
# csv.reader(codecs.open("./file/user_info.csv", "r", "gbk"))  codecs 是python编解码器，此处指定gbk
# islice(data, 0, None)   Python 提供的 itertools 工具，可在读取数据时从指定行开始，提高了一定的循环效率

print("--json--")
with open("./file/user_info.json", "r") as f:
    data = f.read()

users = json.loads(data)
print(users)

print("--txt--")
with open("./file/user_info.txt", "r") as f:
    data = f.readlines()
users = []
for u in data:
    user = u[:-1].split(":")  # 因为获取到的数据最后存在换行符，故需要先截取后分割
    users.append(user)
print(users)

a = 'python'
b = a[::-1]  # 字符串反转
print(b)  # nohtyp
c = a[::-2]  # 字符串反转，且隔1位获取
print(c)  # nhy
# 从后往前数的话，最后一个位置为-1
d = a[:-1]  # 从位置0到位置-1之前的数
print(d)  # pytho

users.clear()
print("--csv--")
data = csv.reader(codecs.open("./file/user_info.csv", "r", "gbk"))
for u in islice(data, 0, None):
    users.append(u)
print(users)
