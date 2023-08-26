#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

col_alpha = ""
for i in range(1, nr_letters + 1):
    col_alpha += random.choice(letters)

col_sym = ""
for i in range(1, nr_symbols + 1):
    col_sym += random.choice(symbols)

col_num = ""
for i in range(1, nr_numbers + 1):
    col_num += random.choice(numbers)

easy_password = col_alpha + col_sym + col_num

password_list = []
for i in easy_password:
    password_list.append(i)

random.shuffle(password_list)
strong_password = ""
for i in password_list:
    strong_password += i

print(f"Here is your password: {strong_password}")