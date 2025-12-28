# Level 3 Question 18

secret = 7 
print("Guess the secret number : ")
guess= int(input())
while(guess!=secret):
    if(guess > secret):
        print("Too high")
    else :
        print("Too low ")
    guess = int(input("Guess the number again : "))
print("You guessed the number correctly ! ")