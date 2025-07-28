def copy_file_contents():
    # Get file names from the user
    source_file = input("Enter the source file name (with extension): ")
    destination_file = input("Enter the destination file name (with extension): ")

    try:
        # Open the source file in read mode
        with open(source_file, 'r') as src:
            contents = src.read()

        # Open the destination file in write mode and write contents
        with open(destination_file, 'w') as dest:
            dest.write(contents)

        print(f"Contents copied successfully from '{source_file}' to '{destination_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{source_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
copy_file_contents()

