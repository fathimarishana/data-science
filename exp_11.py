def count_lines():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            print(f"Number of lines in '{filename}': {len(lines)}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

count_lines()

