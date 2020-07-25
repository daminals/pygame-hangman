# import pygame module in this program
import pygame
from random_word import RandomWords
from pygame.locals import *

# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# define the RGB value for white,
# green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)

# assigning values to X and Y variable
X = 700
Y = 400

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y), 0, 32)

icon = pygame.image.load('favicon.png')
pygame.display.set_icon(icon)

# set the pygame window name
pygame.display.set_caption('hangman')

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('squarefont/Square.ttf', 32)

# game start

r = RandomWords()
solution = r.get_random_word(minLength=4, maxLength=10, hasDictionaryDef="true")


print(solution)
list_sol = list(solution)
guess_list = [' __ '] * len(list_sol)


def list2str(list_var):
    list_var = ' '.join(list_var)
    return list_var


str_guess = list2str(guess_list)

# create a text surface object,
# on which text is drawn on it.
text = font.render(str_guess, True, white)

# create a rectangular object for the
# text surface object
textRect = text.get_rect()

# set the center of the rectangular object.
textRect.center = (X // 2, Y - (Y // 5))


def update(new_info):
    text = font.render(new_info, True, white)
    pygame.draw.rect(display_surface, white, textRect)
    display_surface.blit(text, textRect)
    pygame.display.update()


# completely fill the surface object
# with white color
display_surface.fill(black)

# copying the text surface object
# to the display surface object
# at the center coordinate.
display_surface.blit(text, textRect)

pygame.display.update()

continue_game = True
lose_mechanism = 0
letters_guessed = []


# infinite loop
while True:

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.

    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.

        if event.type == pygame.QUIT:
            # deactivates the pygame library
            pygame.quit()

            # quit the program.
            quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:  # Pressing ESC quits.
                pygame.quit()
                quit()



    while continue_game:
        letter = input('letter: ')
        while letter == "________" or letter in letters_guessed:
            print('how dare you try to break my game whore \nyou already KNOW you picked that damn letter')
            letter = input('letter: ')
        letters_guessed.append(letter)

        if letter not in list_sol:
            lose_mechanism += 1
            print('nah dog, thats ' + str(lose_mechanism) + " wrong")

        while letter in list_sol:
            letter_index = list_sol.index(letter)

            guess_list[letter_index] = letter
            list_sol[letter_index] = "________"

            print(guess_list)

        str_guess = list2str(guess_list)
        update(str_guess)

        # loss mechanism

        if lose_mechanism == 5:
            print('LMAO U LOST MASSIVE L')
            continue_game = False
            break

        if list_sol and all(elem == '________' for elem in list_sol):
            print('u got it boo')
            continue_game = False
            break

        # Draws the surface object to the screen.
