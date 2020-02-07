email = input("Enter your email:")
atcount, ucount, dotcount = 0, 0, 0
if (email[0].isdigit()):
    print("Invalid mail")
elif (email[0] == '@'):
    print("Invalid mail")
else:
    for i in range(0, len(email)):
        if (email[i] == ' '):
            print("Invalid mail")
            break
        else:
            if (email[i]=='@'):
                atcount = atcount + 1
            if (email[i]=='.'):
                dotcount = dotcount + 1
    if (atcount>=1 and dotcount>=1):
        print("Valid mail")
    else:
        print("Invalid mail")
