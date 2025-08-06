import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()
str3 = input().strip()

length = [[[0]*(len(str3)+1) for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
max_result = 0

for i in range(len(str1)):
    for j in range(len(str2)):
        for k in range(len(str3)):
            prev = length[i+1][j+1][k] if length[i+1][j][k+1] <= length[i+1][j+1][k] else length[i+1][j][k+1]
            prev = prev if length[i][j+1][k+1] <= prev else length[i][j+1][k+1]
            cur = length[i][j][k]
            if str1[i] == str2[j] and str2[j] == str3[k]:
                cur += 1
            length[i+1][j+1][k+1] = max(prev, cur)
            max_result = max(max_result, length[i+1][j+1][k+1])

print(max_result)