found = 0
s = input("Enter a string:")
ch = input("Character to be searched:")
for i in range(0,len(s)):
    if (ch == s[i]):
        print("true")
        found = found + 1
if(found==0):
    print("false")


