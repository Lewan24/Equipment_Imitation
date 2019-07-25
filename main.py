# Prosta Imitacja Ekwipunku do gry RPG
# Python 3.7 Linux-Windows

#TODO: Zmienic zapisywanie eq z compilatora do notatnika
#TODO: Stworzyc szyfr na liczby i nazwy itemow
#TODO: Deszyfracja pliku na poczatku programu
#TODO: Szyfrowanie na koncu oraz przy zamknieciu

# import all classes and functions from my file
from Foo import *

# set variable to check is Equipment have not any bugs
IS_EQ_GOOD = False

# set variable to check is Game ran okay
IS_GAME_GOOD = False

# set simple variable for input prompt
PROMPT = ">"

# set variable for All Game
GAME = Game()

# run game
GAME.runGame()

# check is game ran okay
if GAME.__isWellRunning__ == True:
    IS_GAME_GOOD = True
else:
    IS_GAME_GOOD = False

# main game loop
while IS_GAME_GOOD == True:
    
    # set variable for player's equipment
    EQ = Equipment()
    
    # check is Equipment okay and without bugs
    if EQ.EQ_ITEMS_OBJECTS.__len__() == EQ.EQ_NUMBER_OF_ITEMS.__len__():
        IS_EQ_GOOD = True
    else:
        IS_EQ_GOOD = False

    # second main loop
    while IS_EQ_GOOD == True:

        try:
            # function for clear screen (it is working for Windows, Linux and MacOS)
            clear()

            # try to get option from menu
            option = GAME.menu()
            
        except:
            # default option for exit
            option = "5"

        # print all eq
        if option == "1":
            clear()
            EQ.printAllEQ()

        # print declared item
        elif option == "2":
            clear()
            try:
                whichItem = int(input("Which Item you want to see?\n>"))
            except:
                whichItem = 1

            print(EQ.printEQ(whichItem))

        # change any item to own
        elif option == "3":
            clear()
            try:
                whichItem = int(input("Which item you wanna change?\n>"))
                newItemName = str(input("What name you wanna set?\n>"))
                howManyItems = int(input("How many items you wanna set?\n>"))

                EQ.changeItem(whichItem, newItemName, howManyItems)
            except:
                print("I will not change any item, just try again :)")

        # swap 2 items
        elif option == "4":
            clear()
            try:
                # get from user which items he want to swap
                firstItem = int(input("Which Items you want to change positions?\n>"))
                secondItem = int(input(">"))

                # set temporary names and numbers of selected items
                tmpNames = [EQ.EQ_ITEMS_OBJECTS[firstItem-1], EQ.EQ_ITEMS_OBJECTS[secondItem-1]]
                tmpNumbers = [EQ.EQ_NUMBER_OF_ITEMS[firstItem-1], EQ.EQ_NUMBER_OF_ITEMS[secondItem-1]]

                # swap 2 items
                EQ.changeItem(firstItem, tmpNames[1], tmpNumbers[1])
                EQ.changeItem(secondItem, tmpNames[0], tmpNumbers[0])

            # error with setting or swaping items
            except:
                print("Error, but I dont care why :)")
                
        else:
            # if you click anything other from menu
            exit()

        # after any action you have to click to continue
        input("Click anything to continue...")
        
    # if there are any bugs or errors with equipment
    else:
        # check how many items we have in first and second list
        # error checks firstly equipment declared in compiler
        print("Number of ItemObjects: {}, number of numbersOfItems: {}".format(EQ.EQ_ITEMS_OBJECTS.__len__(), EQ.EQ_NUMBER_OF_ITEMS.__len__()))

# when game is ran badly
else:
    print("You cant play game without running it...")
