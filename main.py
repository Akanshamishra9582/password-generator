import random 
import string

def generate_password(length=12,uppercase=True,lowercase=True,digits=True,special_chars=True):
    characters = ' '
    if uppercase :
        characters += string.ascii_uppercase
    if lowercase :
        characters += string.ascii_lowercase
    if digits :
        characters += string.digits
    if special_chars:
        characters+= string.punctuation
    if not characters:
        print("error , Atleast one character type must be selected")
        return None

    
    password = ''.join(random.choice(characters)for _ in range(length))
    return password


print("Welcome to the password generator")
print("you can customize your passowrd by selecting the character types to include")


password_length = int (input("enter the length of password : "))
include_uppercase = input("include uppercase letters? (y/n)").lower() =='y'
include_lowercase = input ("include lowercase letter ? (y/n)").lower()=='y'
include_digits = input ("include digits ? (y/n) : ").lower() == 'y'
include_special_chars = input ("include special characters ? (y/n) : ").lower() == 'y'


generated_password = generate_password(
    length=password_length,
    uppercase=include_uppercase,
    lowercase=include_lowercase,
    digits = include_digits,
    special_chars=include_special_chars
)

if generated_password:
    print("generated password :", generated_password)
else :
    print("No password generated. please try again")