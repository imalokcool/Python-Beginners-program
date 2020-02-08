balance = int(input("Enter your Balance:"))
char = 'y'
ask = []
while(char == 'y'):
    ask = input("Query:").split()
    if(ask[0] == "deposit"):
        balance = balance + int(ask[1])
        print("Amount deposited, current balance:", balance)
    elif(ask[0] == "withdraw"):
        balance = balance - int(ask[1])
        print("Withdrawl Successful, current balance:", balance)
    char = input("Do you want to continue: (y/n):")


