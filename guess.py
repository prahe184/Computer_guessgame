import random
#Guess the number (user)
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x} : '))
        if guess < random_number:
            print("Sorry guess again. It's too low")
        if guess > random_number:
            print("Sorry guess again. It's too high")
    
    print(f"Congratulations!. You've guessed the number correctly {random_number}")

def computer_guess(x):
        low = 1
        high = x
        feedback = ''
        while feedback != 'c':
            if low != high:
                 guess = random.randint(low,high)
            else:
                 guess = low #low = high
            feedback= input(f"Is {guess} too high (h), low (l) or correct (c)? ")
            if feedback == 'h':
                 high = guess - 1
            elif feedback == 'l':
                 low = guess + 1

        print(f"Congrats, The computer guessed your number {guess} correctly")
        
computer_guess(10)
