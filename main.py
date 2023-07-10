import random

word_list = ["pelota", "arco", "libro", "medicos"]
chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
    display.append("_")

lives = len(display)
print(f'Tenes {lives} vidas')

end_of_the_game = False

while not end_of_the_game:
    guess = input("Adivina una letra: ").lower()

    for s in range(len(chosen_word)):
        if chosen_word[s] == guess:
            display[s] = guess
            print(lives)
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(lives)
        if lives == 0:
            print(f"Perdiste :( La palabra era {chosen_word}.")
            end_of_the_game = True


if "_" not in display:
    end_of_the_game = True
    print(f"Ganaste! :) La palabra era {chosen_word}.")