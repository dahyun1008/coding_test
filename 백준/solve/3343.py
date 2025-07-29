import sys
from math import ceil

input = sys.stdin.readline
n, amount_g, price_g, amount_b, price_b = map(int, input().split())

if price_b/amount_b <= price_g/amount_g:
    price_g, amount_g, price_b, amount_b = price_b, amount_b, price_g, amount_g

best_price = pow(10, 18)

for chunk_b in range(amount_g):
    chunk_g = ceil((n-chunk_b*amount_b)/amount_g)
    chunk_g = 0 if chunk_g < 0 else chunk_g
    best_price = min(best_price, chunk_g * price_g +chunk_b * price_b)

print(best_price)