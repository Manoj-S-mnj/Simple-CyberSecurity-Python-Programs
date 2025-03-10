import itertools

pin_code = input("Set a 4-digit PIN: ")
count = 0 
# Brute force attack
for attempt in itertools.product("0123456789", repeat=4):
    guess = ''.join(attempt)
    print("Trying:", guess)
    count += 1
    if guess == pin_code:
        print("PIN found:", guess)
        break
print("Count : ", count)
