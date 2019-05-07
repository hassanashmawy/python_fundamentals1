def give_me_the_price(item):
    price = 0
    if item == "veggi":
            price = 2
    elif item == "bacon":
            price = 3
    elif item == "orange":
            price = 1
    else:
        pass
    
    return price


def calc(order):
    total=0
    for item  in order:
        total += give_me_the_price(item)
    return total

def print_bill(order):
    print('Bi is for bacon')
    print('----------------')
    
    for item in order:
        print("${:.2f}".format(give_me_the_price(item)), item)
    print('----------------')
    
    print("${:.2f} Total".format(calc(order)))
    print()
    print('Please come again')
    print()
    

# print_bill("sSSs")
print_bill(["veggi","veggi","bacon","orange"])
# print(calc())