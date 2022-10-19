#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    float Change;
        do
        {
            Change = get_float("Change owed: ");
        }
        while (Change<=0);

        int Cents = round(Change*100);

        int Count=0, Quarter=25, Dime=10, Nickel=5, Penny=1;
        while (Cents>=Quarter)
        {
            Count++;
            Cents=Cents-Quarter;
        }
        while (Cents>=Dime)
        {
            Count++;
            Cents=Cents-Dime;
        }
        while (Cents>=Nickel)
        {
            Count++;
            Cents=Cents-Nickel;
        }
        while (Cents>=Penny)
        {
            Count++;
            Cents=Cents-Penny;
        }
        printf("%i\n", Count);
}