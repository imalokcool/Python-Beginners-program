n = int(input())
a,b,c = 0,1,0
for i in range(0,n-1):
    print(c,end=' ')
    c= a + b
    a = b
    b = c
