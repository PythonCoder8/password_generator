import string, random, sys

special_chars = "!@#$%^&*()"

try:
    chars = int(input("How many characters do you want to have in your new password? (a strong password should have at least 12)?: "))

except ValueError:
    sys.exit("Input should be a number")

print("".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + special_chars, k=chars)))
