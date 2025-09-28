# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 17:46:32 2025
"""

'----------Password Checker------------'
print('Password Requirements:')
print('Minimum Length of 12 characters')
print('At least 1 symbol')
print('At least 1 number')
print('At least 1 Capital letter')

from getpass import getpass

# character sets
uletters = "QWERTYUIOPASDFGHJKLZXCVBNM"
lletters = "qwertyuiopasdfghjklzxcvbnm"
symbols  = "./<>?;`~\\|-=!@$%^&*()_+"
numbers  = "1234567890"

# user input
P1 = getpass('Insert Password Here: ')
P2 = getpass('ReType Password Here: ')

i = 0   # score counter

# Upper Case Letter Checker
if any(s in P1 for s in uletters):
    i += 1
else:
    print("No Uppercase Letter")

# Lower Case Letter Checker
if any(s in P1 for s in lletters):
    i += 1
else:
    print("No Lowercase Letter")

# Number Checker
if any(s in P1 for s in numbers):
    i += 1
else:
    print("No Numbers")

# Symbol Checker
if any(s in P1 for s in symbols):
    i += 1
else:
    print("No Symbol in Password")

# Length Checker
if len(P1) >= 12:
    i += 1
else:
    print("Password is too short")

# Check if passwords match
if P1 != P2:
    print("Passwords do not match")
    print("Score 0/5 → Retry")
else:
    # Grade Passwords
    if i == 0:
        print("Invalid Password")
    elif i == 1:
        print("Very Weak Password")
    elif i == 2:
        print("Weak Password")
    elif i == 3:
        print("Slightly Weak Password")
    elif i == 4:
        print("Medium Password")
    else:
        print("Strong Password")

    print("Score", i, "/5")

