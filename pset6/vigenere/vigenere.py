import sys
import cs50

# encrypts letter using key letter
def shift(char, num_letter):
    shift = ord(sys.argv[1][num_letter].lower()) - 97
    return chr((ord(char) - 97 + shift) % 26 + 97)

# check if argument is correct
if len(sys.argv) == 2 and sys.argv[1].isalpha():
    
    # ask for text for encrypt
    plain_text = input("plaintext: ")
    
    # number of key's letter
    num_letter = 0
    
    result = ''

    # iterates through text's letters
    for char in plain_text:
        if char.isalpha():
            if char.isupper():
                char = char.lower()
                result += shift(char, num_letter).upper()
            else:
                result += shift(char, num_letter)

            if num_letter < len(sys.argv[1]) - 1:
                num_letter += 1
            else:
                num_letter = 0
        else:
            result += char

    print(f"ciphertext: {result}")
else:
    print("Usage: python vigenere.py key")
    sys.exit(1)
