from cs50 import get_string
from sys import argv, exit


def main():

    if len(argv) == 2:
        with open(argv[1], "r") as banned:
            banned_data = banned.readlines()
            banned_list = [element.replace('\n', '') for element in banned_data]

            if len(banned_list) == 0:
                print("Usage: banned list is empty")
                exit(1)

            print('What message would you like to censor?')
            text_list = input().split(' ')

            result = []
            for word in text_list:
                if word.lower() in banned_list:
                    result.append('*' * len(word))
                else:
                    result.append(word)
            print(' '.join(result))

    else:
        print("Usage: python bleep.py dictionary")
        exit(1)

if __name__ == "__main__":
    main()
