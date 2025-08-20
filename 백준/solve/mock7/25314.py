import sys

input = sys.stdin.readline
n = int(input())
result = ''

while (n>0):
    result += 'long '
    n -= 4
result += 'int'

print(result)