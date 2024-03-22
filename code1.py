from datetime import datetime, timedelta

def print_date_after_days(days):
    today = datetime.today()
    future_date = today + timedelta(days=days)
    print(future_date.strftime("%A, %B %d, %Y"))

# Example usage
days = int(input("Enter the number of days: "))
print_date_after_days(days)
