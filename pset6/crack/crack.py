from crypt import crypt
import sys
import cs50

# TF       || 51.xJagtPnb6s ||
# UPenn    || 50GApilQSG3E2 ||
# puppy    || 502sDZxA/ybHs ||
# FTW      || 50C6B0oz0HWzo ||
# Yale     || 50WUNAFdX/yjA ||
# lloyd    || 50n0AAUD.pL8g ||
# maybe    || 50CcfIk1QrPr6 ||
# nope     || 50JIIyhDORqMU ||
# ROFL     || 51v3Nh6ZWGHOQ ||
# hola     || 61v1CDwwP95bY ||
# sean     || 508ny6Rw0aRio ||
# LOL      || 50cI2vYkF0YU2 ||


#  make sure there exist one command argument only
if len(sys.argv) == 2:

    # uncomment this tree lines to generate new hashes
    
    # new_hash = crypt(sys.argv[1], "50")
    # print(f"{new_hash}");
    # sys.exit(0)

    salt = sys.argv[1]

    # generated password to crack encrypted one
    generated_password = ""

    # store alphabetic ASCII characters in an array + 0
    arr = "0ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    print("Trying to hack entered hash, please wait an hour, a day or months,\nyou will stay here a long long (long)^(inf) time :D")

    # try all possible passwords of length 5 or less
    r = 4
    for i in arr:
        for j in arr:
            for k in arr:
                for l in arr:
                    for m in arr:

                        # concat and take 5-r characters
                        generated_password = i + j + k + l + m
                        generated_password = generated_password[r:5]

                        # try password
                        if crypt(generated_password, salt) == sys.argv[1]:
                            print(f"Password found!\n{generated_password}")
                            sys.exit(0)

                    if r > 3: r = 3
                if r > 2: r = 2
            if r > 1: r = 1
        if r > 0: r = 0
        print(f"{i} of A-Z-a-z")

    print("Nothing found :(")
else:
    print("Usage: python crack.py hash")
    sys.exit(1)