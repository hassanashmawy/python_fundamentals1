walk_or_run = ""
km = 0

# print("Tired".casefold())
# print("tired".casefold)
# print("Tired".casefold)
# print("tired".casefold())

apples_eated = int(input("How many apples did you eat?\n"))
energy = apples_eated*2
print("a whole {}.. great! your energy is: {}".format(apples_eated, energy))


while True:
    if energy == 1:
        print(">>> Watch your energy! you can walk to increase by 1")
    walk_or_run = input("Would you like to walk or run?")
    if energy > 0:
        
        
        if walk_or_run.casefold() == "walk" :
            km += 1
            energy = energy+1
        elif walk_or_run.casefold() == "run" :
            km += 5
            energy = energy-1
        elif walk_or_run.casefold() == "tired":
            print("That fast! you practiced a {} km today!".format(km))
            exit(0)
        else:
            print("stay lazy and do: {} or whatever!".format(walk_or_run))
    else:
        print("you have {} energy! you can't run without energy! you may walk to increase your energy by 1".format(energy))

    # print("you want to: " + walk_or_run)
    print("ahaa, you practiced a {} km today so far!".format(km))


    