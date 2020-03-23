# 用for循环实现1~100求和
# sum = 0
# for x in range(101):
#     sum += x
# print(sum)

"""
range(101)可以产生一个0到100的整数序列。
range(1, 100)可以产生一个1到99的整数序列。
range(1, 100, 2)可以产生一个1到99的奇数序列，其中2是步长，即数值序列的增量。
"""
# 用for循环实现1~100之间的偶数求和
# sum = 0
# for x in range(0, 101, 2):
#     sum += x
# print(sum)

# sum = 0
# for x in range(0, 101):
#     if x % 2 == 0:
#         sum += x
# print(sum)

"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""

import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input("请输入："))
    if number < counter:
        print("再大点")
    elif number > counter:
        print("再小点")
    else:
        print("猜对了")
        break
print("你总共猜了%d次" % counter)
