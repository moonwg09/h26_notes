n = int(input())

for i in range(1, n + 1):

    digit_sum = sum(map(int, str(i)))
    

    total = i + digit_sum
    
    if total == n:
        print(i) 
        break
else:
    print(0)