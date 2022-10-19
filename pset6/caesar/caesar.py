import sys
import cs50

def shiftChar(char, k):
    char = chr(((ord(char) - 97 + k)%26)+97)
    return char

if len(sys.argv) == 2:
    k = int(sys.argv[1])
    print('plaintext: ', end='')
    plaintext = input()
    print("ciphertext: ", end='')
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                char = char.lower()
                char = shiftChar(char, k)
                print(char.upper(), end='')
            else:
                char = shiftChar(char, k)
                print(char, end='')
        else:
            print(char, end='')
    print()
else:
    print("Just one positive integer argument is needed")
    sys.exit(1)
