def capitalize_file_words():
    input_filename = input("Enter the name of the input file: ")

    try:
        
        with open(input_filename, 'r') as file:
            content = file.read()

    
        words = content.split()
        capitalized_words = [word.upper() for word in words]

        capitalized_content = ' '.join(capitalized_words)

        output_filename = input("Enter the name of the output file: ")

    
        with open(output_filename, 'w') as file:
            file.write(capitalized_content)

        print(f"Capitalized content has been written to '{output_filename}'.")

    except FileNotFoundError:
        print("Error: The input file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


capitalize_file_words()

