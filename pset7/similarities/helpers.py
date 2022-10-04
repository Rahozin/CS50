# import nltk
# nltk.download('punkt')
from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # create lists of unique lines
    a_list = list(dict.fromkeys(a.split('\n')))
    b_list = list(dict.fromkeys(b.split('\n')))

    # create a list of common elements from two lists
    result = []
    for element in a_list:
        if element in b_list:
            result.append(element)
    return result


def sentences(a, b):
    """Return sentences in both a and b"""

    # create lists of unique sentences
    a_list = list(dict.fromkeys(sent_tokenize(a)))
    b_list = list(dict.fromkeys(sent_tokenize(b)))
    
    # create a list of common elements from two lists
    result = []
    for element in a_list:
        if element in b_list:
            result.append(element)
    return result


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # create lists of unique substrings of length "n"
    a_list = []
    b_list = []
    for char_num in range(0, len(a) - n + 1):
        a_list.append(a[char_num:char_num + n])
        a_list = list(dict.fromkeys(a_list))
    for char_num in range(0, len(b) - n + 1):
        b_list.append(b[char_num:char_num + n])
        b_list = list(dict.fromkeys(b_list))
    
    # create a list of common elements from two lists
    result = []
    for element in a_list:
        if element in b_list:
            result.append(element)
    return result


# arg1 = 'qwerty\nqwert.\nqwer.\nasdfg\nq\nq123'
# arg2 = 'qwerty\nqwert.\nqwer\nqwe\nqw\nq\n123'
# argn = 3


# if __name__ == '__main__':
#     # print(lines(arg1, arg2))
#     # print(sentences(arg1, arg2))
#     print(substrings(arg1, arg2, argn))