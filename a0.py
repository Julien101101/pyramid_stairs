# JULIEN SAVARY
# 22982687
# Assignment #0

def get_input() -> int:
    '''
    gets a number input
    '''
    number_of_stairs = int(input())
    return number_of_stairs


def white_space(i: int):
    '''
    creates a white space for stairs far away
    '''
    j = 0
    for j in range(i):
        print("  ", end="")


def add_one(stairs: int):
    return stairs + 1


def main():
    number_of_stairs = get_input()
    number_f = 0
    print("+-+")
    while number_f != number_of_stairs:
        white_space(number_f)
        print("| |")
        white_space(number_f)
        print("+-", end="")
        number_f = add_one(number_f)
        if number_f != number_of_stairs:
            print("+-+")

    print("+")


if __name__ == "__main__":
    main()

