#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    long Number;
    do
    {
        Number = get_long("Number: ");
    }
    while (Number<0);

    long d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16;
    d1 = round(Number/1000000000000000);
    d2 = round((Number%1000000000000000)/100000000000000);
    d3 = round((Number%100000000000000)/10000000000000);
    d4 = round((Number%10000000000000)/1000000000000);
    d5 = round((Number%1000000000000)/100000000000);
    d6 = round((Number%100000000000)/10000000000);
    d7 = round((Number%10000000000)/1000000000);
    d8 = round((Number%1000000000)/100000000);
    d9 = round((Number%100000000)/10000000);
    d10 = round((Number%10000000)/1000000);
    d11 = round((Number%1000000)/100000);
    d12 = round((Number%100000)/10000);
    d13 = round((Number%10000)/1000);
    d14 = round((Number%1000)/100);
    d15 = round((Number%100)/10);
    d16 = round((Number%10)/1);

    int ds1,ds3,ds5,ds7,ds9,ds11,ds13,ds15;
    ds1 = round(d1*2/10)+round(d1*2%10);
    ds3 = round(d3*2/10)+round(d3*2%10);
    ds5 = round(d5*2/10)+round(d5*2%10);
    ds7 = round(d7*2/10)+round(d7*2%10);
    ds9 = round(d9*2/10)+round(d9*2%10);
    ds11 = round(d11*2/10)+round(d11*2%10);
    ds13 = round(d13*2/10)+round(d13*2%10);
    ds15 = round(d15*2/10)+round(d15*2%10);

    int final_d;
    final_d = d2+d4+d6+d8+d10+d12+d14+d16+ds1+ds3+ds5+ds7+ds9+ds11+ds13+ds15;

    if (final_d%10 == 0 && Number > 1000000000000)
    {
        if (d1 == 5 && d2 <= 5)
        {printf("MASTERCARD\n");}
        else if (d1 == 4 || (d1 == 0 && d2 == 0 && d3 == 0))
        {printf("VISA\n");}
        else if (d1 == 0 && d2 == 3 && (d3 == 4 || d3 == 7))
        {printf("AMEX\n");}
        else
        {printf("INVALID\n");}
    }
    else
    {printf("INVALID\n");}
}