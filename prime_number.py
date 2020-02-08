n = int(input())
count = 0
li = []
for i in range(2, int(n / 2)):
    if n % i == 0:
        print("Not Prime")
        count = count + 1
        break
    else:
        continue
if count == 0:
    print("Prime")


