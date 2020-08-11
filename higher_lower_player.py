print("Think of a number between 1 and 100 and I'll guess it.")
times = int(input("How many guesses do i get? ")) - 1
large_number = 100
small_number = 1
answer = input("Is the number higher, lower, or the same as " + str(int((large_number + small_number) / 2)) + "? ")
for i in range(times):
    times -= 1
    if answer == "lower":
        if int((large_number + small_number) / 2) - small_number != 1:
            large_number = int((large_number + small_number) / 2)
            answer = input(
                "Is the number higher, lower, or the same as " + str(int((large_number + small_number) / 2)) + "? ")
        else:
            print("Wait; how can it be both higher than", small_number, "and lower than",
                  str(int((large_number + small_number) / 2)) + "?")
            exit()
    elif answer == "higher":
        if large_number - int((large_number + small_number) / 2) != 1:
            small_number = int((large_number + small_number) / 2)
            answer = input(
                "Is the number higher, lower, or the same as " + str(int((large_number + small_number) / 2)) + "? ")
        else:
            print("Wait; how can it be both higher than", str(int((large_number + small_number) / 2)), "and lower than",
                  str(large_number) + "?")
            exit()
    elif answer == "same":
        print("I won!")
        exit()
if times == 0 and int((large_number + small_number) / 2) == 50:
    result = int(input("I lost; what was the answer? "))
    if answer == "higher" and result > 50:
        print("Well played!")
    elif answer == "higher" and result < 50:
        print("That can't be; you said it was higher than 50!")
    elif answer == "lower" and result < 50:
        print("well played!")
    elif answer == "lower" and result > 50:
        print("That can't be; you said it was lower than 50!")
elif times == 0:
    result = int(input("I lost; what was the answer? "))
    if answer == "higher":
        if int((large_number + small_number) / 2) < result < large_number:
            print("Well played")
        elif result < int((large_number + small_number) / 2):
            print("That can't be; you said it was higher than", str(int((large_number + small_number) / 2)) + "!")
        elif result > large_number:
            print("That can't be; you said it was lower than", str(large_number) + "!")
    elif answer == "lower":
        if small_number < result < int((large_number + small_number) / 2):
            print("well played")
        elif result > int((large_number + small_number) / 2):
            print("That can't be; you said it was lower than", str(int((large_number + small_number) / 2)) + "!")
        elif result < small_number:
            print("That can't be; you said it was higher than", str(small_number) + "!")
