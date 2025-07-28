def find_lines_with_consecutive_ones():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        print("Lines containing two consecutive '1's:")
        found = False
        for line_number, line in enumerate(lines, start=1):
            if "11" in line:
                print(f"Line {line_number}: {line.strip()}")
                found = True
        
        if not found:
            print("No lines with two consecutive '1's found.")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

find_lines_with_consecutive_ones()

