list1 = list(map(int,input("Enter the array:").split()))
count = 0
search = int(input("Enter the element to be searched:"))
for i in range(0,len(list1)):
    if (search==list1[i]):
        count = count + 1
if (count>0):
    print("Yes,",search," is present, and it is repeated",count, "times")
else:
    print("Not present")