n = int(input())
li = []
for i in range(0,n):
    p = input().split()
    if (p[0] == 'insert'):
        li.insert(int(p[1]),int(p[2]))
    elif (p[0] == 'print'):
        print(li)
    elif (p[0] == 'remove'):
        li.remove(int(p[1]))
    elif (p[0] == 'append'):
        li.append(int(p[1]))
    elif (p[0] == 'sort'):
        li.sort()
    elif (p[0] == 'pop'):
        li.pop(len(li)-1)
    elif (p[0] == 'reverse'):
        li.reverse()

