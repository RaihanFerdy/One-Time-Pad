import string, random, os
        
def encrypt(message):
    key_upper = ''
    key_lower = ''
    result = ''
    for i in range(len(message)):
        key_upper += random.choice(string.ascii_uppercase)
        key_lower += random.choice(string.ascii_lowercase)
        char = message[i]
        if char.isupper():
            result_index = (string.ascii_uppercase.index(char) + string.ascii_uppercase.index(key_upper[i])) % 26
            result += string.ascii_uppercase[result_index]
        elif char.islower():
            result_index = (string.ascii_lowercase.index(char) + string.ascii_lowercase.index(key_lower[i])) % 26
            result += string.ascii_lowercase[result_index]
        else:
            result += char
            
    save_file =  input("Save file to txt? [y/n]: ")
    if save_file == 'y':
        
        os.system("cls")
        with open(f"encrypt.txt", 'w') as f:
            f.write(f"Message: {message}\n")
            if message.isupper():
                f.write(f"Key: {key_upper}\n")
            if message.islower():
                f.write(f"Key: {key_lower}\n")
            f.write(f"Result: {result}")
            
    elif save_file == 'n':
        os.system("cls")
        print(f"\nMessage: {message}")
        if message.isupper():
            print(f"Key: {key_upper}")
        if message.islower():
            print(f"Key: {key_lower}")
        print(f"Result: {result}\n")

def decrypt(message, key):
    key_upper = key.upper()
    key_lower = key.lower()
    result = ''
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            result_index = (string.ascii_uppercase.index(char) - string.ascii_uppercase.index(key_upper[i])) % 26
            result += string.ascii_uppercase[result_index]
        elif char.islower():
            result_index = (string.ascii_lowercase.index(char) - string.ascii_lowercase.index(key_lower[i])) % 26
            result += string.ascii_lowercase[result_index]
        else:
            result += char
            
    save_file =  input("Save file to txt? [y/n]: ")
    if save_file == 'y':
        os.system("cls")
        with open(f"decrypt.txt", 'w') as f:
            f.write(f"Message: {message}\n")
            if message.isupper():
                f.write(f"Key: {key_upper}\n")
            if message.islower():
                f.write(f"Key: {key_lower}\n")
            f.write(f"Result: {result}")
            
    elif save_file == 'n':
        os.system("cls")
        print(f"\nMessage: {message}")
        if message.isupper():
            print(f"Key: {key_upper}")
        if message.islower():
            print(f"Key: {key_lower}")
        print(f"Result: {result}\n")
    
message = input("Input message: ")
method = input("Select method: [e/d]: ").lower()
if method == "e":
    encrypt(message)
elif method == "d":
    key = input("Input key: ")
    decrypt(message, key)