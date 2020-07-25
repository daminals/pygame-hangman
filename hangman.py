from random_word import RandomWords
import pygame

# initialize display
pygame.init()
screen_width = 700
screen_height = 400

white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode([screen_width, screen_height])

pygame.display.set_caption('hangman')
font = pygame.font.Font('squarefont/Square.ttf', 24)

icon = pygame.image.load('favicon.png')
pygame.display.set_icon(icon)

# TODO - loading screen

# pick a random word, NOT one with -
r = RandomWords()
solution = r.get_random_word()
while '-' in solution:
    solution = r.get_random_word()

print(solution)
list_sol = list(solution)
guess_list = [' __ '] * len(list_sol)

str_guess = ' '.join(guess_list)

# text rendering

text = font.render(str_guess, True, black)

textRect = text.get_rect()

textRect.center = (screen_width - 50, screen_height // 5)

# coords
x = 50
y = 25


# the game
while True:
    screen.fill(black)

    screen.blit(text, textRect)

    continue_game = True
    lose_mechanism = 0
    while continue_game:
        letter = input('letter: ')
        while letter == "________":
            print('how dare you try to crash my game whore \n pick a new letter you ignorant slut')
            letter = input('letter: ')

        if letter not in list_sol:
            lose_mechanism += 1
            print('nah dog, thats ' + str(lose_mechanism) + " wrong")

        while letter in list_sol:
            letter_index = list_sol.index(letter)

            guess_list[letter_index] = letter
            list_sol[letter_index] = "________"

            print(guess_list)

        # loss mechanism

        if lose_mechanism == 5:
            print('LMAO U LOST MASSIVE L')
            continue_game = False

        if list_sol and all(elem == '________' for elem in list_sol):
            print('u got it boo')
            continue_game = False

    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            # deactivates the pygame library
            pygame.quit()

            # quit the program.
            quit()

            # Draws the surface object to the screen.
        pygame.display.update()

    pygame.display.quit()
