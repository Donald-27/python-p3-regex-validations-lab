import re

# Matches names like "John Cena", "Anya Taylor-Joy", and "D'Angelo"
# Starts with uppercase followed by lowercase letters,
# then zero or more groups starting with space, apostrophe, or hyphen,
# followed by uppercase letter and lowercase letters.
name = r"^[A-Z][a-z]*([ '-][A-Z][a-z]+)*$"

name_regex = re.compile(name)

# placeholders for phone and email regex
phone_number = r"^(\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$"
phone_regex = re.compile(phone_number)



email_address = r'^[a-zA-Z][a-zA-Z0-9_.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
email_regex = re.compile(email_address)
