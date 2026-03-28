umber = 7  # загадане число
attempts = 3

guesses = [5, 8, 7]  # приклад спроб

for guess in guesses:
    if guess == number:
        print("Вітаю! Ви вгадали!")
        break
    elif guess > number:
        print("Менше")
    else:
        print("Більше")
else:
    print(f"Ви програли! Число було {number}")
