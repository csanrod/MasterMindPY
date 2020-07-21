
def set_lvl():
    print("Please set difficulty:",
        "\n\t1.Basic \t(3 digits --> [0-4], 6 attempts)",
        "\n\t2.Normal \t(4 digits --> [0-5], 8 attempts)",
        "\n\t3.Hard  \t(5 digits --> [0-9], 6 attempts)")
    
    while True:
        try:
            lvl_value = int(input("Difficulty: "))
            while lvl_value > 3 or lvl_value < 1:
                print ("Out of range, try it again...")
                lvl_value = int(input("Difficulty: "))
            return lvl_value
        except ValueError:
            print ("Wrong format, try it again...")

print(set_lvl())