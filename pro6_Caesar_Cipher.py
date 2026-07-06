'''write a python program to implement caesar cipher'''
def caesar_cipher(message,key):
    encrypted_message = ""
    for char in message:
        if char.isupper():
            encrypted_char = chr((ord(char)+key-65)%26+65)
        elif char.islower():
            encrypted_char = chr((ord(char)+key-97)%26+97)
        else:
            encrypted_char=char
        encrypted_message += encrypted_char
    return encrypted_message

message = input("Enter the message: ")
key = int(input("Enter the key: "))

encrypted_message=caesar_cipher(message,key)

print("Original message: ",message)
print("Shift: ",key)
print("Encrypted Message: ",encrypted_message)
