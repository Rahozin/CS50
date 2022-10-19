#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int shift(char c);

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        string alphabetic = argv[1];
        int key = 0;
        for (int j = 0; j < strlen(alphabetic); j++)
        {
            char letter = alphabetic[j];
            if (!isalpha(letter))
            {
                printf("Usage: ./vigenere keyword\n");
                return 1;
            }
        }
        string plain_text = get_string("plaintext: ");
        printf("ciphertext: ");
        for (int i = 0, k = 0; i < strlen(plain_text); i++)
        {
            if (k == strlen(alphabetic))
            {
                k = 0;
            }
            key = shift(alphabetic[k]);
            if (plain_text[i] >= 65 && plain_text[i] <= 90)
            {
                printf("%c", (65 + ((plain_text[i] % 65) + key) % 26));
                k++;
            }
            if (plain_text[i] >= 97 && plain_text[i] <= 122)
            {
                printf("%c", (97 + ((plain_text[i] % 97) + key) % 26));
                k++;
            }
            if (plain_text[i] < 65 || (plain_text[i] > 90 && plain_text[i] < 97) || plain_text[i] > 122)
            {
                printf("%c", plain_text[i]);
            }
        }
        printf("\n");
    }
    else
    {
        return 1;
    }
}

int shift(char c)
{
    int shift;
    if islower(c)
    {
        shift = (int) c - 97;
    }
    else
    {
        shift = (int) c - 65;
    }
    return shift;
}