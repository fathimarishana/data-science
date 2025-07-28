user_input = input("Enter a list of numbers separated by spaces: ")

numbers = [float(num) for num in user_input.split()]

if numbers:
    largest = max(numbers)
    print("The largest number is:", largest)
else:
    print("No numbers were entered.")

