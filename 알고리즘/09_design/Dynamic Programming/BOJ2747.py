# 재귀함수로 푸는 경우 에러가 발생한다 (시간초과)
# def fibo(num):

#     if num == 0:
#         return 0
#     if num == 1:
#         return 1
#     return fibo(num-1) + fibo(num-2)

# n = int(input())
# print(fibo(n))

# memorization

def fibo(num):
    if mem[num] == -1:
        mem[num] = fibo(num-1) + fibo(num-2)
    return mem[num]

n = int(input())
mem = [0,1] + [-1] * (n-1)
print(fibo(n))