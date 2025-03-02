# This is an python code to check the password strength.....
password = input("Enter your password: ")
length = len(password)

capital = 0
small = 0
integer = 0
specialChar = 0

for i in range(0, length):
    if password[i].isupper():
        capital += 1
    elif password[i].islower():
        small += 1
    elif password[i].isdigit():
        integer += 1
    else:
        specialChar += 1


if length >= 8 and capital >= 1 and small >= 2 and integer >= 2 and specialChar >= 1:
    print("Your password is strong")
else:
    print("Give some strong password")
    
if not length >= 8 :
    print("Your password size should atleast 8")
if not capital >= 1 :
    print("Your password should contain atleast 1 capital letter")
if not small >= 2 :
    print("Your password should contain atleast 2 small letter")
if not integer >= 2 :
    print("Your password should contain atleast 2 digits")
if not specialChar >= 1 :
    print("Your password should contain atleast 1 special character")
    
    
    
    
    
    
    
    
    
    