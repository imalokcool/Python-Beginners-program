count = 0
arr = list(map(int, input().split()))
print(arr)
sum1 = int(input("Sum of pair:"))
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if ((arr[i]+arr[j]) == sum1):
            print(arr[i],arr[j])
            count = count + 1
if(count==0):
    print("Pair doesn't exists")

