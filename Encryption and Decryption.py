import random 

# Selecting an random Number as encryption key
random_number = random.randint(1,10)

data = input("Enter the original Data :")

#encryption -----------------------------------------------------
encrypted_Data = [ord(char) for char in data]
for i in range(0,len(encrypted_Data)):
    encrypted_Data[i] = encrypted_Data[i] + random_number

# Encrypted data
NewEncryptedData = [chr(char) for char in encrypted_Data]
print(f"ENCRYPTED DATA : {''.join(NewEncryptedData)}")

#-----------------------------------------------------
# Decryption Process
Decrypted_Data = [ord(char) for char in NewEncryptedData]
for i in range(0,len(Decrypted_Data)):
    Decrypted_Data[i] = Decrypted_Data[i] - random_number

NewDecryptedData = [chr(char) for char in Decrypted_Data]
print(f"DECRYPTED DATA : {''.join(NewDecryptedData)}")

