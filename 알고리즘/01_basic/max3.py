a, b, c = map(int, input().split())  #split()은 띄어쓰기 해준다, int(정수형)으로 바꿔준다. , map은 앞에있는 명령어를 뒤에 있는 명령어에 적용
max = a
if max < b : max = b
if max < c : max = c
print(max)
