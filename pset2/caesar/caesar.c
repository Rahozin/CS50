#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        string digits = argv[1];
        int argv_to_int = 0;
        int j = strlen(digits);
        for (int i = 0; i < j; i++)
        {
            int digit = (int) digits[i] - 48;
            if (digit < 0 || digit > 9)
            {
                printf("Usage: ./caesar key\n");
                return 0;
            }
            else
            {
                argv_to_int = argv_to_int + digit * pow(10, (j-i-1));
            }
        }
        string plain_text = get_string("plaintext: ");
        printf("ciphertext: ");
        for (int i = 0; i < strlen(plain_text); i++)
        {
            if (plain_text[i] >= 65 && plain_text[i] <= 90)
            {
                printf("%c", (65 + ((plain_text[i] % 65) + argv_to_int) % 26));
            }
            if (plain_text[i] >= 97 && plain_text[i] <= 122)
            {
                printf("%c", (97 + ((plain_text[i] % 97) + argv_to_int) % 26));
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
