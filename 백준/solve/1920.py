import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
x = list(map(int, input().split()))

def find(num, start, end): # 숫자 num을 a에서 찾는다
    if start == end:
        return 1 if a[start] == num else 0

    mid = int((start+end)/2)
    if num <= a[mid]:
        return find(num, start, mid)
    else:
        return find(num, mid+1, end)
    
for num in x:
    print(find(num, 0, len(a)-1))