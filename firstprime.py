n = int(input())
numbers = []
for i in range(n):
    number = int(input())
    isPrime=True
    if number > 1:
        for j in range(2, number):
            if (number % j) == 0:
                isPrime=False
                break
        if isPrime==True:
            numbers.append(number)
print(numbers[0])
