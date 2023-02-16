import random

digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

bulls = 0
cows = 0

random.shuffle(digits)
secret_num = digits[0:4]

print("guess a 4 digit number 0 through 9")

def pos(string1, string2):

    times = 0
    for ind, lett in enumerate(string2):
        if lett == string1[ind]:
            times += 1

    return times

tries = 0
while bulls < 4:
    
    cows = 0
    bulls = 0
    tries += 1
    guess = input('guess the number: ')
    for number in guess:
        cows += secret_num.count(number)
    bulls = pos(secret_num, guess)
    cows = cows -  bulls
    print("bulls:", bulls, "cows", cows)
    
print('you won in ', tries, " tries")
#kinda bad but good enough
#ezekiel