
# try exception  마지막에 ctrl z 엔터하면 끝남
import sys

def getCantor(size):
    # base condition
    if size == 1: return '-'

    # divide
    new_size = size // 3
    center = ' ' * new_size
    side = getCantor(new_size)
    return side + center + side

while True:
    try:
        N = int(input())
        size = 3 ** N
        result_str = getCantor(size)
        print(result_str)
    except EOFError:
        break