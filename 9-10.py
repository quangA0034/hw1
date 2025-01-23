""""
ex9:
import random
def random_number():
    return random.randint(1,6)
number = random_number()
print(f"Random Number is {number}")
"""
def phone_book():
    name = []
    number = []

    while True:

        choice = int(input(f"Command (1 search, 2 add, 3 quit): "))
        if choice == 2:
            add_name = input('Name:')
            add_num = int(input('Number:'))
            name.append(add_name)
            number.append(add_num)
            print('ok!')
        elif choice == 1:
            search_name = input('Name:')
            if search_name in name:
                print(search_name)
                index = name.index(search_name)
                print(f"{number[index]}")
            else:
                print('Name not found')
        elif choice == 3:
            print('Quitting...')
            break

phone_book()