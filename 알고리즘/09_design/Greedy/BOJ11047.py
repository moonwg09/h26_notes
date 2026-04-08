

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# 1. 동전의 가치들을 리스트에 담습니다.
coins = []
for _ in range(n):
    coins.append(int(input()))

# 2. 비싼 동전부터 확인하기 위해 리스트를 뒤집습니다.
coins.reverse()

count = 0
for coin in coins:
    # 3. 목표 금액이 0원이면 더 이상 계산할 필요가 없으므로 종료
    if k == 0:
        break
    
    # 4. 현재 동전으로 낼 수 있는 최대 개수를 더합니다. (몫)
    count += k // coin
    
    # 5. 남은 잔돈을 계산합니다. (나머지)
    k %= coin

print(count)