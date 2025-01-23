max_value = []

def ap():
    global max_value
    ap_list = []
    number = 3
    while number <= max_value:
        ap_list.append(number)
        number += 3
    total_ap = sum(ap_list)
    squared_ap = sum(map(lambda x: x**2, ap_list))
    print(f"the list is {ap_list}")
    print(f"total number is {total_ap}")
    print(f"Sum of squared is {squared_ap}")
    

def main():
    global max_value
    max_value = int(input('Pick your max value'))
    ap()


main()