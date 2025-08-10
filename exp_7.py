from datetime import datetime, timedelta
current_date = datetime.now()
new_date = current_date - timedelta(days=5)
print("current date:",current_date.strftime("%y-%m-%d"))
print("date after subtracting 5 days:",new_date.strftime("%y-%m-%d"))

