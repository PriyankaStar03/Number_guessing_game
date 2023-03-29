
# no of gauesses 9
# print no of guesses left
# no of guesses h took to finish
# after 9 guess GAME OVER...

n=315
print("This is game to guess my favourite no.")
print("In this game, you have total 10 chances to guess my favourite no")
i=0
while(i<=9):
    a = int(input())
    if a<315:
        print("Your no is smaller than my favourite no and you have", 9-i, "guesses")
        i=i+1
    elif a>315:
        print("Your no is larger than my favourite no and you have", 9-i, "guesses")
        i=i+1
    else:
        print("Amazing!, you got the right no and you also have", 9-i, "guesses left. The no is 315 ")

print("Sorry, the game is over, try the game next time...")