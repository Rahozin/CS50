#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int number;
        do
        {
            number = get_int("Height: ");
        }
        while (1>number||number>8);
        for (int i=1;i<=number;i++)
        {
            for (int k = number;k-i>0;k--)
            {printf(" ");}
            for (int j = 1;j<=i;j++)
            {printf("#");}
            printf("  ");
            for (int j = 1;j<=i;j++)
            {printf("#");}
            printf("\n");
        }
}