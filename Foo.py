# Foo

from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

# Declare main game class
class Game:
    
    # declare init function
    def __init__(self):
        self.__isWellRunning__ = False
    
    def __del__(self):
        self.__isWellRunning__ = False

    # function for just run game
    def runGame(self):
        self.__isWellRunning__ = True

    # main menu
    def menu(self) -> str:
        
        # check is game ran well
        if self.__isWellRunning__ == True:
            # main menu
            print ("=================================")
            print ("1. Print all Eq")
            print ("2. Print item")
            print ("3. Change any item")
            print ("4. Change Items positions")
            print ("5. Exit")

            # set char (str) to int for error in while
            char = 1

            # check is char different type from str
            while type(char) != str:
                # if True, get from user selected option
                char = input(">")

            # return selected option to main loop
            return char

        # error if someone will want to run menu without running game
        else:
            input("You cant run menu without running game...")

# Declare Equipment class
class Equipment:
    
    def __init__(self):
        
        # set specified firstly player's Equipment
        self.EQ_ITEMS_OBJECTS = ["Smoczy ogon","Wilczy kiel","Mikstura Zdrowia","Mikstura Many","","","","","","",
                                 "","","","","","","","","",""]
        self.EQ_NUMBER_OF_ITEMS = [1,3,5,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        # If game Starts, Equipment is decrypted for game
        self.__decryptData__("equipment.eq")
    
    def __del__(self):
        # after exit from game or just deleting equipment, encrypt and save eq to file
        self.__encryptData__("equipment.eq")

    # print selected item from Equipment
    # get int and return int
    def printEQ(self, whichItem:int) -> int:
        return self.EQ_ITEMS_OBJECTS[whichItem-1], self.EQ_NUMBER_OF_ITEMS[whichItem-1]

    # print all eq for user
    def printAllEQ(self):
        for i in range(self.EQ_ITEMS_OBJECTS.__len__()):
            print("{}{} {}".format(i+1, ".", self.printEQ(i+1)))        

    # function for changing any item from eq to your own
    # need int, str and int for well working
    def changeItem(self, whichItem:int, itemName:str, numberOfItems:int):
        self.EQ_ITEMS_OBJECTS[whichItem-1] = itemName
        self.EQ_NUMBER_OF_ITEMS[whichItem-1] = numberOfItems

    # encrypt and save eq to file
    def __encryptData__(self, fileNameToEncrypt:str):
        pass

    # decrypt eq for program
    def __decryptData__(self, encryptedFileName:str):
        pass
