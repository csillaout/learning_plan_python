
import datetime

def current_datetime():
    """Display the current date and time."""
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

# Test the function
print("Current Date and Time:", current_datetime())