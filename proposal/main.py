print("Will you be My GirlFriend?")
a = input("Yes Or No :-")
if a != "Yes" or a != "yes" and a != "No" or a != "no":
    print("Wrong answer. Please try again....")
print("")


def success():
    for row in range(6):
        for col in range(7):
            if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
                print("❤️", end=" ")
            else:
                print(" ", end="")
        print()


def success_feeling():
    print("\n I Love YOU")


if a == "Yes" or a == "yes":
    success(), success_feeling()


def failure():
    for row in range(6):
        for col in range(7):
            if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
                print("😥", end="")
            else:
                print(" ", end="")
        print()


def failure_feeling():
    print("\n All The Best for your Love Life :(")


if a == "No" or a == "no":
    failure(), failure_feeling()
