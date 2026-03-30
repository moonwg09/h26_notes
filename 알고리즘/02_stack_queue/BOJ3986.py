
N = int(input())

count = 0

for _ in range(N):

    line = input()
    stack = []
    for char in line:
        if char == 'A':
            if stack and stack[-1] == 'A':
                stack.pop()
            else:
                stack.append(char)
        
        if char == 'B':
            if stack and stack[-1] == 'B':
                stack.pop()
            else:
                stack.append(char)
    if not stack:
        count += 1

print(count)


# word로 해서 a, b 둘다 같을시에만 빼고 더하기 때문에 구지 2개로 나눌 필요 없이 word == char랑 같으면으로 쓰면된다

#word = input()  
#for char in word:
#if stack and stack[-1] == ch:
