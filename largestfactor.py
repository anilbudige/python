number = int(input())
k = int(input())
count = 0
for item in range(number,0,-1):
    if number % item == 0:
        count += 1
    if count == k:
        print(item)
        break
if count<k:
    print("1")
