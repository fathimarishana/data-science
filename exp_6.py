from datetime import datetime

# Get input from the user
date1_input = input("Enter the first date (YYYY-MM-DD): ")
date2_input = input("Enter the second date (YYYY-MM-DD): ")

# Convert input strings to datetime objects
try:
    date1 = datetime.strptime(date1_input, "%Y-%m-%d")
    date2 = datetime.strptime(date2_input, "%Y-%m-%d")

    # Compare the two dates
    if date1 < date2:
        print(f"The earlier date is: {date1_input}")
    elif date2 < date1:
        print(f"The earlier date is: {date2_input}")
    else:
        print("Both dates are the same.")
except ValueError:
    print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

