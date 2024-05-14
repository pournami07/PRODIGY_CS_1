def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is alphabetic
            if char.islower():  # Check if the character is lowercase
                encrypted_text += chr(((ord(char) - 97 + shift) % 26) + 97)
            else:  # The character is uppercase
                encrypted_text += chr(((ord(char) - 65 + shift) % 26) + 65)
        else:  # If the character is not alphabetic, simply append it
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    return caesar_cipher_encrypt(encrypted_text, -shift)

def main():
    choice = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").lower()
    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice.")
        return

    text = input("Enter the text: ")
    shift = int(input("Enter the shift value (an integer): "))

    if choice == 'encrypt':
        result = caesar_cipher_encrypt(text, shift)
        print("Encrypted text:", result)
    elif choice == 'decrypt':
        result = caesar_cipher_decrypt(text, shift)
        print("Decrypted text:", result)

if __name__ == "__main__":
    main()
