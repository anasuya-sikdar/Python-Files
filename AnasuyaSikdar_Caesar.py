#Anasuya Sikdar
#Assignment 4.2

def Caesar(message, shift):
    # Creating the alphabet string
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Creating the cipher using string slicing
    cipher = alphabet[shift:] + alphabet[:shift]
    
    # Printing the alphabet and the cipher
    print(f"alphabet: {alphabet}")
    print(f"cipher  : {cipher}")
    
    # Encrypt the message string
    encryptedMsg = ""
    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            encryptedMsg += cipher[index]
        else:
            encryptedMsg += char
    
    return encryptedMsg

def main():
    message = input("Enter the message: ").upper()
    shift = int(input('Enter shift amount: '))
    encryptedMsg = Caesar(message, shift)
    print(f"{message}")
    print(f"{encryptedMsg}")


   
