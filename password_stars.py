minimum_pass_length = 8

user_password = input("Your password: ")

while len(user_password) < minimum_pass_length:
    print(f"Password must be {minimum_pass_length} characters or longer.")
    user_password = input("Your password: ")

print("*" * len(user_password))