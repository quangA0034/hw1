import random
numbers = []
print("Enter 10 numbers:")
for i in range(10):
    num = input(f"Enter number {i+1}: ")
    numbers.append(num)
ordered_num = sorted(numbers)
print(f"The number list:{ordered_num}")

strings = []
print("Enter 10 strings:")
for i in range(10):
    string = input(f"Enter string {i+1}: ")
    strings.append(string)
strings.sort()

print(f"Strings List:{strings}")

random_numbers = [random.randint(1, 1000) for _ in range(10)]
print(f"Randomly Generated Numbers List: {random_numbers}")