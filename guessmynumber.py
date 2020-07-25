import random


number = random.randint(1,100)
print('i bet youll never guess my number teehee')

true = True
number_of_guesses = 0
while true:
    guess = int(input('ok guess between 1 and 100 uwu: '))
    number_of_guesses += 1
    if not guess == number:
        if guess > number:
            print('owo... its so big.... ')
        else:
            print('uwu... too small.. teehee')
    else:
        true = False
        print('\nOWO u guessed my number teehee')
        print('and it only took ' + str(number_of_guesses) + " guesses uwu")

