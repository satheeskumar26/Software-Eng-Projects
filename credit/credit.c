#include <cs50.h>
#include <stdio.h>

long long card_num;
int cal_checksun(long long c);
void card_lenght(long long cc);

int main(void)
{
    do
    {
        card_num = get_long_long("Type in a your card number: ");
    }
    while (!card_num); // check for card staring digits

    if (cal_checksun(card_num) == 1)
    {
        card_lenght(card_num);
    }
    else
    {
        printf("INVALID\n");
    }
}

int cal_checksun(long long c)
{
    card_num = c;

    long long get_card_num = card_num;
    long long counter = 0;
    int last_dig;
    int mult;
    int mult_first_dig;
    int mult_last_dig;
    int sum_even;
    int sum_ord_num;
    int result;

    while (get_card_num > 0)
    {
        last_dig = get_card_num % 10;     // get last dig
        get_card_num = get_card_num / 10; // remove last dig
        counter++;

        if ((counter % 2) == 0) // get even number
        {
            mult = last_dig * 2; // mult by 2

            if (mult >= 10)
            {
                mult_first_dig = mult / 10; // remove last dig
                mult_last_dig = mult % 10;  // get last dig
                mult = mult_first_dig + mult_last_dig;
            }

            sum_even = sum_even + mult;
        }
        else // get even number
        {
            sum_ord_num = sum_ord_num + last_dig;
        }

        result = sum_ord_num + sum_even;
    }

    if ((result % 10) == 0)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

void card_lenght(long long cc)
{

    card_num = cc;

    long long first_two_num = card_num;
    long long first_num = card_num;
    string card_name = "";
    long long card_num_02 = card_num;
    long long total_digits = 0;

    while (card_num_02 > 0) // check for card lenth
    {
        card_num_02 /= 10;
        total_digits++;
    }

    while (first_two_num >= 100) // get first_two_num
    {
        first_two_num /= 10;
    }

    while (first_num >= 10) // get first_num
    {
        first_num /= 10;
    }
    // check first two digits are compatible

    if (total_digits == 15 && (first_two_num == 34 || first_two_num == 37))
    {
        printf("AMEX\n");
    }

    else if (total_digits == 16 && (first_two_num == 51 || first_two_num == 52 || first_two_num == 53 ||first_two_num == 54 || first_two_num == 55))
    {
        printf("MASTERCARD\n");
    }

    else if ((total_digits == 13 || total_digits == 16) && first_num == 4)
    {
        printf("VISA\n");
    }

    else
    {
        printf("INVALID\n");
    }
}
