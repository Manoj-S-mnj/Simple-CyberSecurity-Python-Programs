# This program checks if the entered password is correct based on the username
# Dictionary storing usernames and passwords

UserData = {
    "example@gmail.com": "Example@1",
    "example2@gmail.com": "Example@2",
    "example3@gmail.com": "Example@3",
    "example4@gmail.com": "Example@4"
}

UserName = input("Enter Your User Name: ")

if UserName in UserData:
    Password = input("Enter Your Password: ")
    if UserData[UserName] == Password:
        print("Login Successful! ✅")
    else:
        print("Incorrect Password! ❌")

else:
    print("Check Your user name you may be new to this platform! ❌")
