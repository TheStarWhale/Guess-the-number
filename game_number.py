import random

def number():
    number_guess = random.randint(1, 100)
    attempts = 0
    print("Hello, digres a bit here 'Guess the number'") #Why in English? Because i'm too lazy ti switch the layout alas yes
    print('I made a number from 1 to 100. Guess!')

    while True:
        try:
            guess = int(input('enter what you think: '))
            attempts += 1

            if guess < number_guess:
                print('Number is greater')
            elif guess > number_guess:
                print('Number is less')
            else:
                print(f'Well done, you guessed the number {number_guess} in {attempts} attempts, keep going, and maybe youll make something worthwhile, haha')
        except ValueError:
            print('Dont be smart, enter a real number')
if __name__ == "__main__":
    number()