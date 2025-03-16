def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift  # Reverse the shift for decryption

    for char in text:
        if char.isalpha():  # Only shift letters
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char  # Keep non-alphabetic characters unchanged

    return result

# User input
mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

# Perform encryption or decryption
output = caesar_cipher(message, shift, mode)
print(f"Result: {output}")
