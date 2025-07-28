from datetime import datetime, timedelta

# Ask the user how many days to subtract
try:
    days_to_subtract = int(input("Enter the number of days to subtract from today's date: "))

    # Get today's date
    current_date = datetime.today()

    # Subtract the days
    new_date = current_date - timedelta(days=days_to_subtract)

    # Print the result
    print("Current date:", current_date.strftime("%Y-%m-%d"))
    print(f"Date after subtracting {days_to_subtract} days:", new_date.strftime("%Y-%m-%d"))

except ValueError:
    print("Please enter a valid number.")

