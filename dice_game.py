import random
game = input("Do you want to play the game:")
while (game== "yes" or game== 'y' or game== "Yes" or game== 'Y'):
    print(random.randrange(1,6,1))
    game = input("Do you want to play the game again:")
print("end")