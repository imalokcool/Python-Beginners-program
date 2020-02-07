
list = []
n = int(input(("Enter number of students:")))
for i in range(0,n):
    name = [input(("name:")),int(input(("cgpa:")))]
    list.append(name)

print(list)
for i in range(0,n):
    print("My name is", name[i])