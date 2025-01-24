numbers = []

def negative_int():
    negatives_list = list(filter(lambda num: num < 0, numbers))
    print(f"The negative numbers are {negatives_list}")

def even_int():
    even_numbers = list(filter(lambda num: num % 2 == 0, numbers))
    print(f"Total even numbers are {len(even_numbers)}")

def sum_positive():
    positive_number = list(filter(lambda num: num > 0 and num % 3 == 0, numbers))
    total_sum = sum(positive_number)
    print(f"The sum of numbers are divisible by 3 is {total_sum}")

def main():
    while True:
        user_input = int(input("Enter a number (0 to quit): "))
        if user_input == 0:
            break
        numbers.append(user_input)

    negative_int()
    even_int()
    sum_positive()

main()






        



   
