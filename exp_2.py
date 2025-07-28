
user_input = input("Enter a list of numbers separated by spaces: ")

numbers = [int(num) for num in user_input.split()]

unique_numbers = list(set(numbers))

unique_numbers.sort()

print("List after removing duplicates:", unique_numbers)

