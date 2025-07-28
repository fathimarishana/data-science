def search_and_replace():
    filename = input("Enter the filename: ")
    word_to_search = input("Enter the word to search: ")
    word_to_replace = input("Enter the replacement word: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()

        updated_content = content.replace(word_to_search, word_to_replace)

        with open(filename, 'w') as file:
            file.write(updated_content)

        print(f"All occurrences of '{word_to_search}' have been replaced with '{word_to_replace}' in {filename}.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

search_and_replace()

