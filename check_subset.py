t = int(input())
a,b= [],[]
ch = 0
while(ch<t):
    a = int(input())
    for i in range(0,a):
        li = int(input())
        a.append(li)
    b = int(input())
    for i in range(0,b):
            li = int(input())
            b.append(li)
    ch= ch+1
if(a.issunset(b)):
    print("True")
else:
    print("False")