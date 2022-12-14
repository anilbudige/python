M = int(input())
N = int(input())
for number in range(M,N+1):
    count = 0
    for divider in range(2,number//2+1):
        if number%divider == 0:
            count+=1
    if count >= 1:
        print(number)
