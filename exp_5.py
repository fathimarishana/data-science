def have_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

# Get input from the user
list1_input = input("Enter the first list (comma-separated): ")
list2_input = input("Enter the second list (comma-separated): ")

# Convert input strings to lists
list1 = list1_input.split(',')
list2 = list2_input.split(',')

# Optional: Strip whitespace from each element
list1 = [item.strip() for item in list1]
list2 = [item.strip() for item in list2]

# Check for common members
result = have_common_member(list1, list2)

print("Do the lists have a common member?", result)

