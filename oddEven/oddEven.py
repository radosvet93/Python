def oddEven():
    userN = int(input('Write a number\n'))
    check = int(input('divide by\n'))

    if userN % 4 == 0:
        print('Your number can be divided by 4')
    elif userN % 2:
        print('Your number is even')
    else:
        print('Your number is odd')

    if userN % check == 0:
        print(userN, "Divides evenly with", check)
    else:
        print(userN, "Divides not evenly with", check)

    input()
oddEven()

