from random import randint

def set_lvl():
    print("WELCOME TO MASTERMIND GAME")
    print("Please set difficulty:",
        "\n\t1.Basic \t(3 digits --> [0-4], 6 attempts)",
        "\n\t2.Normal \t(4 digits --> [0-5], 8 attempts)",
        "\n\t3.Hard  \t(5 digits --> [0-9], 10 attempts)")
    
    while True:
        try:
            lvl_value = int(input("Difficulty: "))
            while lvl_value > 3 or lvl_value < 1:
                print ("Out of range, try it again...")
                lvl_value = int(input("Difficulty: "))
            return lvl_value
        except ValueError:
            print ("Wrong format, try it again...")

def repeat_digits():
    repeat = True
    answer = input("Do you want repeated digits? (y/n): ")
    while answer != "y" and answer != "n":
        answer = input("FAIL, please insert y --> yes or n --> no: ")
    if answer == "n":
        repeat = False
    return repeat

def start_game(lvl, repeat):
    print("Loading...")

    secret_number_list = []
    correct = 0
    half_correct = 0

    if lvl == 1:
        print("\tDifficulty => BASIC")
        n_digits = 3
        limit = 4
        attempts = 6
    elif lvl == 2:
        print("\tDifficulty => NORMAL")
        n_digits = 4
        limit = 5
        attempts = 8
    else:
        print("\tDifficulty => HARD")
        n_digits = 5
        limit = 9
        attempts = 10   
    print("\tAttempts =>", attempts)
    print("\tN_digits =>", n_digits)
    if repeat:
        print("\tRepetition => Yes")
    else:
        print("\tRepetition => No")
    # -- Algorithm that generates the secret number -- #
    number = random_number(limit)
    secret_number_list.append(number)
    n_digits -= 1
    secret_number = number*(10**(n_digits))
    while n_digits > 0:
        if repeat:
            number = random_number(limit)
        else:
            while number in secret_number_list:
                number = random_number(limit)
        secret_number_list.append(number)
        n_digits -= 1
        secret_number = secret_number + number*(10**(n_digits))
    
    print(secret_number_list[:])
    print(secret_number)
    print("Starting...")

    index = 0
    while attempts > 0:
        number_attempt = input("Please introduce your number (attemtp "+ str(attempts)+"): ")
        for i in number_attempt:
            if int(i) in secret_number_list:
                if index == secret_number_list.index(int(i)):
                    correct +=1
                else:
                    half_correct +=1
            index += 1
        print("Correct -->", correct)
        print("Half correct -->", half_correct)
        if correct != len(secret_number_list):
            correct = 0
            half_correct = 0
            index = 0
            attempts -=1
        else:
            attempts = -1
    if attempts == 0:
        print("... GAME OVER ...")
    else:
        print("... VICTORY! ...")

def random_number(limit):
    return randint(0, limit)

start_game(set_lvl(), repeat_digits())