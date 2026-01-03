# Practiced today with some while loops and made this game
# The game gives u 3 attempts to guess

attempts = 3

while attempts > 0:
    guess = int(input("Guess The Number: "))

    if guess == 67:
        print("Good job you guessed it right! ")
        break
    else:
        attempts -= 1
        print(f"Nope you have {attempts} Attempts left! ")


if attempts == 0:
    print("Out of Attempts!")
