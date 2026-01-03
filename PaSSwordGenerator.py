
import random
import string   
import secrets
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'  
symbols = '!#$%&()*+'
# 
print("Welcome to the python Generator")
nletters=int(input("How many letters would you like in your password?\n"))
nnumbers=int(input("How many numbers would you like in your password?\n"))
nsymbols=int(input("How many symbols would you like in your password?\n") )
password=""
password_list = []
for i in range(1,nletters+1):
    char=random.choice(letters)
    password_list+=char
# 
for i in range(1,nnumbers+1):
   char=random.choice(numbers)
   password_list+=char  
# 
for i in range(1,nsymbols+1):
    char=random.choice(symbols)
    password_list+=char
# 
random.shuffle(password_list)
for char in password_list:
    password+=char
print(f"Your password is: {password}")
