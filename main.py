import random
print("number guessing game")
number = random.randint(1, 9)
chances = 0
print("guess a number between 1 and 9")

while chances < 3:
    guess = int(input())
    if guess == number:
        print("Wow. Congratz. You won!")
        break
    elif guess < number:
        print("Your answer is too low sorry. Try something higher than", guess)
    elif guess > number:
        print("Your answer is too high. Try something lower than", guess)
    chances += 1
if not chances < 5:
    print("YOU DIED the number was", number)
