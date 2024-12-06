import re

#text
text = """Here are some phone numbers:
123-456-7890, (123) 456-7890, 987-654-3210.
Feel free to call me!"""

# Regular expression to match phone numbers
phone_regex = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'

#extract all phone numbers
phone_numbers = re.findall(phone_regex, text)

print("Extracted Phone Numbers:")
for number in phone_numbers:
    print(number)

