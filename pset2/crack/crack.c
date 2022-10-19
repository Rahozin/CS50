// Password cracker assuming DES based encryption, in this case, the crypt() function of C.

#define _XOPEN_SOURCE
#include <unistd.h>
#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <crypt.h>

// Compile with || clang -o crack crack.c -lcrypt || or || make crack
// make crack
// Run with || ./crack [hash]

// Tested on
/*
1        || 50Xu9TV42tQOg || 0.002s      || 3,420 possible passwords
al       || 507IH4BV0kgzc || 0.789s      || 324,900 possible passwords
RoR      || 50b5ILzBEDplw || 45.780s     || 30,865,500 possible passwords
Ruby     || 50VfakyL0ptK. || 4170.874s   || 2,932,222,500 possible passwords
Linux    || 50u8HReKZleek || 355826.965s || 278,561,137,500 possible passwords

TF       || 51.xJagtPnb6s ||
UPenn    || 50GApilQSG3E2 ||
puppy    || 502sDZxA/ybHs ||
FTW      || 50C6B0oz0HWzo ||
Yale     || 50WUNAFdX/yjA ||
lloyd    || 50n0AAUD.pL8g ||
maybe    || 50CcfIk1QrPr6 ||
nope     || 50JIIyhDORqMU ||
ROFL     || 51v3Nh6ZWGHOQ ||
hola     || 61v1CDwwP95bY ||
sean     || 508ny6Rw0aRio ||
LOL      || 50cI2vYkF0YU2 ||
*/

int main(int argc, char* argv[]) {
    // make sure there exist one command argument only
    if (argc != 2) {
        printf("Usage: ./crack hash\n");
        return 1;
    }

    // uncomment this two lines to generate new hashes

    // printf("%s\n", crypt(argv[1], "50"));
    // return 0;


    // generated password to crack encrypted one
    char generated_password[6] = {};

    // test array to store passwords of all lengths
    char test[6] = {};

    // extract salt from encrypted password
    char salt[3];
    salt[0] = argv[1][0];
    salt[1] = argv[1][1];

    // store all ASCII characters in an array || <95 should change
    // char arr[95];
    // for(int i = 0; i < 95; i++) arr[i] = (char) (i + 32);

    // store alphabetic ASCII characters in an array || <53 should change
    char arr[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

    printf("Trying to hack entered hash, please wait an hour, a day or months,\nyou will stay here a long long (long)^(inf) time :D\n");

    // try all possible passwords of length 5 or less
    int r = 0;
    for(int i = 0; i < 53; i++)
    {
        generated_password[4] = arr[i];
        for(int j = 0; j < 53; j++)
        {
            generated_password[3] = arr[j];
            for(int k = 0; k < 53; k++)
            {
                generated_password[2] = arr[k];
                for(int l = 0; l < 53; l++)
                {
                    generated_password[1] = arr[l];
                    for(int m = 0; m < 53; m++)
                    {
                        if(r < 1) r = 1;

                        // generate first password
                        generated_password[0] = arr[m];

                        // take r characters
                        strncpy(test, generated_password, r);
                        test[r] = '\0';

                        // try password of length r
                        if(strcmp(crypt(test, salt), argv[1]) == 0)
                        {
                            printf("Password found!\n%s\n", test);
                            return 0;
                        }
                    }
                    if(r < 2) r = 2;
                }
                if(r < 3) r = 3;
            }
            if(r < 4) r = 4;
        }
        if(r < 5) r = 5;
        printf("%i of 52\n", i);
    }

    // if nothing found print nothing found xD
    printf("Nothing found :(\n");

    return 0;
}