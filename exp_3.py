user_input = input("Enter elements of a tuple (e.g., a 1 b 2): ")

items = user_input.split()

if len(items) % 2 != 0:
    print("Error: Please enter an even number of elements (key-value pairs).")
else:

    input_tuple = tuple(items)

    result_dict = {}
    for i in range(0, len(input_tuple), 2):
        key = input_tuple[i]
        value = input_tuple[i + 1]
        result_dict[key] = value

    print("Dictionary:", result_dict)

