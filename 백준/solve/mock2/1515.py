import sys
input = sys.stdin.readline
data = input().strip()

num = 0
while(data):
    num += 1
    str_num = str(num)

    while len(str_num) and len(data):
        if str_num[0] == data[0]:
            data = data[1:]
        str_num = str_num[1:]

print(num)