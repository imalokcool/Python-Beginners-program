li = []
n = int(input("Enter number of commands:"))
for i in range(0,n):
    p,q = int(input()),int(input())
    li.insert(p,q)
print(li)
remove = int(input("Remove:"))
li.remove(remove)
append = int(input("Append:"))
li.append(append)
li.sort()
li.pop(len(li)-1)
li.reverse()
print(li)