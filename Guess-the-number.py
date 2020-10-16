import random as ran
import function_module

# def welcome():
#     print(' ------------------------------------------------------------')
#     print('| \    /\    /   ;---   |       ___    ____   |\  /|  ;---    |')
#     print('|  \  /  \  /    |---   |      |      |    |  | \/ |  |---    |')
#     print('|   \/    \/     "---   |__    |___   |____|  |    |  "---    |')
#     print('|-------------------------------------------------------------|')
#     print('|                     -------   ____                          |')
#     print('|                        |     |    |                         |')
#     print('|                        |     |____|                         |')
#     print('|-------------------------------------------------------------|')
#     print('|                   -------  |   |  ;---                      |')
#     print('|                      |     |---|  |---                      |')
#     print('|                      |     |   |  "---                      |')
#     print('|-------------------------------------------------------------|')
#     print('|               -----     -----   |\  /|  ;---                |')
#     print('|              |  ----   |_____|  | \/ |  |---                |')
#     print('|              |___| |   |     |  |    |  "---                |')
#     print(' -------------------------------------------------------------')

#print( num )
function_module.welcome()
print("\n\n\nGUESS THE NUMBER!!!")
num = int( ran.random() * 100 )
guess = 0
max_g = 100
min_g = 0
chances = 10
while (guess != num and chances != 0):
    guess = int(input("what would be the number? :"))
    if (guess < num):
        if guess > min_g:
            min_g = guess
        print(guess, " is 'smaller'.")
        print("Search between: ", min_g, " and ", max_g)
    elif (guess > num):
        if guess < max_g:
            max_g = guess
        print(guess, " is 'greater'.")
        print( "Search between: ", min_g, " and ", max_g)
    else:
        print(guess , ' = ' , num)
        print("congratulation you have succesfully found the number!!!!")
    chances = chances-1
    print("chances left : ", chances, "\n")
