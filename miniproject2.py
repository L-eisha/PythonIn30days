#CWH
#PASSWORD GENERATOR
#level1
import random
chars =" abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()ASBCDEFGHIJKLMNOPQRSTUVWXYZ"
length=int(input("Enter length:"))
password =""
for a in range (length):
    password+=random.choice(chars)
    print (password)

#level2
import random
import string
import argparse

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    chars = list(string.ascii_lowercase)
    if use_upper:


