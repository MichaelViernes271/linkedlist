from LinkedListDataStructure import LinkedList
from subprocess import call
import os
import time
import sys

class Main:
    """main program for the linkedlist app"""
    def __init__(self):
        self.linklist = LinkedList()

    def display_menu(self):
        """for printing a stylized menu"""

        # for the scribbles wrtten in the menu display
        menu_titles = ["LINKEDLIST APPLICATION", 
        "Programmed by: Viernes, Michael", "BSCOE 2-1", "<<< MAIN MENU >>>", 
        "(1) CREATE LIST", "(2) ADD HEAD", "(3) ADD AFTER [ELEMENT]", "(4) DELETE NODE", 
        "(5) DISPLAY", "(6) COUNT", "(7) REVERSE", "(8) SEARCH", "(9) EXIT"]

        for i in menu_titles:
            if i == menu_titles[0]:
                i = i.center(60, "=")
                print(i)
                continue
            elif i == menu_titles[3]:
                print("=", " "*56, "=")
            i = i.center(56, " ")
            print("=", i, "=")
        print("=" * 60)
        
    def create_list(self):
        try:
            length = int(input("Length of elements => "))
            if length <= 0 :
                raise Exception
            elif length >= 1:
                self.linklist.addToStart(input("Element => "))
            for x in range(length-1):
                self.linklist.addToEnd(input("Element => "))
        except Exception:
            print(">>> Cannot initiate list.")
    
    def add_head(self):
        self.linklist.addToStart(input("Head => "))
        self.linklist.display()
        
    def linklist_opt(self, usr_input):
        try:
            if usr_input == 1: # CREATE LIST
                self.create_list()
                
            elif usr_input == 2: # ADD HEAD
                self.add_head()
            elif usr_input == 3: # ADD AFTER [ELEMENT]
                self.linklist.display()
                value = input("Insert new node => ")
                position = int(input("...At position =>"))
                self.linklist = self.linklist.addAfter(value, position, self.linklist)
                self.linklist.display()
                
            elif usr_input == 4: # DELETE NODE
                usr_input = input("Which item would you like to remove? ")
                is_found = self.linklist.remove(usr_input)
                print("Is the item found? ", is_found)
            elif usr_input == 5: # DISPLAY
                self.linklist.display()
            elif usr_input == 6: # COUNT
                size = self.linklist.length()
                print("The size of the current linked list is",size)
            elif usr_input == 7: # REVERSE
                self.linklist.reverse()
                self.linklist.display()
            elif usr_input == 8: # SEARCH
                position = self.linklist.index(input("Search for element => "))
                print("Position is at ", position)
            elif usr_input == 9: # EXIT
                ask = input("Do you want to try again? [y/n] => If yes, the program redisplay the main menu. Otherwise, program exits.")
                self.clear_console()
                if ask == "n":
                    exit()
            elif usr_input == 11:# CLEAR
                print("LIST CLEARED".center(60,"#"))
                self.linklist.clear()
            else:
                return None
        except Exception:
            sys.stdout.write("\n\n\nPlease enter appropriate input.")
            time.sleep(2)
        input("PROCESS COMPLETE".center(50, "="))
        self.clear_console()
        
    def clear_console(self):
        call("cls" if os.name == "posix" else "clear")
        
        
if __name__ == "__main__":
    m = Main()
    while True:
        try:            
            m.display_menu()         
            m.linklist_opt(int(input(">>> Select an option: ")))
        except Exception:
            print("Use an appropriate option.")
            time.sleep(1)
            m.clear_console()


    