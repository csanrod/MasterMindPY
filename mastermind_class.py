from random import randint

# -- USEFUL FUNCTIONS -- #
def random_number(limit):
    # Generates a random number between [0-limit]
    return randint(0, limit)

def number_of_repetitions(number, list_of_numbers):
    # Counts how many times number apears in list_of_numbers
    # and returns that count.
    count = 0
    for i in list_of_numbers:
        if number == i:
            count += 1
    return count

# -- MASTERMIND GAME CLASS -- #
class MmGame():
    def __init__(self):

        # Constructor that sets:
        #  - lvl
        #  - repetition
        #  - parameters
        #      -- number of digits
        #      -- limit to generate random number
        #      -- number of attempts
        #  - secret number
        #      -- integer format
        #      -- list format
                
        self.__lvl = self.__set_lvl()
        self.__repetition = self.__repeat_digits()
        self.__config_parameters()
        self.__secret_number_generator()

    def __print_menu(self): 
        # Prints menu
        print("WELCOME TO MASTERMIND GAME")
        print("Please set difficulty:",
              "\n\t1.Basic \t(3 digits --> [0-4], 6 attempts)",
              "\n\t2.Normal \t(4 digits --> [0-5], 8 attempts)",
              "\n\t3.Hard  \t(5 digits --> [0-9], 10 attempts)")

    def __print_parameters(self):
        # Prints parameters
        print("Your selection...",
              "\n\t Level  \t-->", self.__lvl,
              "\n\t Digits \t-->", self.__number_of_digits,
              "\n\t Attempts \t-->", self.__attempts,
              "\n\t Repetition \t-->", self.__repetition)

    def __set_lvl(self):
        # Set the difficulty
        self.__print_menu()
        while True:
            try:
                lvl_value = int(input("Difficulty: "))
                while lvl_value > 3 or lvl_value < 1:
                    print ("Out of range, try it again...")
                    lvl_value = int(input("Difficulty: "))
                return lvl_value
            except ValueError:
                print ("Wrong format, try it again...")

    def __repeat_digits(self):
        # Set the repetition option
        repeat = True
        answer = input("Do you want repeated digits? (y/n): ")
        while answer != "y" and answer != "n":
            answer = input("FAIL, please insert 'y' or 'n': ")
        if answer == "n":
            repeat = False
        return repeat

    def __config_parameters(self):
        # Set the parameters
        if self.__lvl == 1:
            self.__number_of_digits = 3
            self.__limit = 4
            self.__attempts = 6
        elif self.__lvl == 2:
            self.__number_of_digits = 4
            self.__limit = 5
            self.__attempts = 8
        elif self.__lvl == 3:
            self.__number_of_digits = 5
            self.__limit = 9
            self.__attempts = 10
        else:
            print("Something unexpected happened...")
        self.__print_parameters()

    def __secret_number_generator(self):
        # Generates random number and list according to parameters
        self.__secret_number_list = []
        counter = self.__number_of_digits
        number = random_number(self.__limit)
        
        self.__secret_number_list.append(number)
        counter -= 1
        self.__secret_number = number*(10**(counter))
        while counter > 0:
            if self.__repetition:
                number = random_number(self.__limit)
            else:
                while number in self.__secret_number_list:
                    number = random_number(self.__limit)
            self.__secret_number_list.append(number)
            counter -= 1
            self.__secret_number = self.__secret_number + number*(10**(counter))

    def start_game(self):

        # Launch the game
        #
        # Algorithm:
        #   1) Is digit in secret number?
        #   2) Count how many times apear every digit in the list
        #   3) Count how many digits are in their right position (corrects)
        #   4) Substract '2)' and '3)' to obtain half corrects
        
        print("Starting...")
        self.__correct = self.__half_correct = 0
        index_i = index_j = number_rep = 0
        used = []
        while self.__attempts > 0:
            number_attempt = input("Please introduce your number (attemtp "+ str(self.__attempts)+"): ")
            for i in number_attempt:
                if int(i) in self.__secret_number_list: 
                    if i not in used:
                        number_rep = number_rep + number_of_repetitions(int(i), self.__secret_number_list)
                        used.append(i)
                    for j in self.__secret_number_list:
                        if i == str(j):
                            if index_i == index_j:
                                self.__correct += 1
                                break
                        index_j += 1
                    index_j = 0
                index_i += 1
            used[:] = []
            self.__half_correct = number_rep - self.__correct
            number_rep = 0
            
            print("\tCorrect -->", self.__correct)
            print("\tHalf correct -->", self.__half_correct)
            if int(number_attempt) == self.__secret_number:
                self.__attempts = -1
            else:
                self.__correct = 0
                self.__half_correct = 0
                self.__attempts -=1
                index_i = 0

        print("SECRET NUMBER:", self.__secret_number)   
        if self.__attempts == 0:
            print("You dont have more attempts...")
            print("... GAME OVER ...")
        else:
            print("... VICTORY! ...")
            
# -- PROGRAM -- #
myGame = MmGame()
myGame.start_game()