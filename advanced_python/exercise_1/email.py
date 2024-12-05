import re

# Regular expression for email validation
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Function to validate email
def validate_email(email):
    if re.match(email_regex, email):
        return f"'{email}' is a valid email."
    else:
        return f"'{email}' is NOT a valid email."

# Test cases
emails = ["csilla.toth@example.com", "invalid-email", "hello@world.", "test@domain.org"]
for email in emails:
    print(validate_email(email))
