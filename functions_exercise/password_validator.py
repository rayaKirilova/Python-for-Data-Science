def validate_password(password: str) -> str:
    if not (6 <= len(password) <= 10):
        print("Password must be between 6 and 10 characters")

    if not password.isalnum():
        print("Password must consist only of letters and digits")

    digit_count = sum(1 for char in password if char.isdigit())
    if digit_count < 2:
        print("Password must have at least 2 digits")

    if 6 <= len(password) <= 10 and password.isalnum() and digit_count >= 2:
        print("Password is valid")


input_text = input()
validate_password(input_text)