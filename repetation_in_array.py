n = int(input("Enter size of array:"))
k = int(input("Enter element to be searched:"))
li = []
count= 0
for i in range(0,n):
    x = int(input("Enter element:"))
    li.append(x)
for i in range(0,n):
    if (k==li[i]):
        count = count + 1
print(k,"is repeated",count,"times")

