# Credit
while True:
    number = input("Number: ")

    # Check if is number
    if not number.isnumeric():
        print("INVALID")
        break

    # Check if == (15, 16, 13)
    if not len(number) in (15, 16, 13):
        print("INVALID")
        break

    # ////////// Check Card Type //////////

    # Check American Express
    if int(number[:2]) in (34, 37):
        result = "AMEX"

    # Check MasterCard
    elif int(number[:2]) in (51, 52, 53, 54, 55):
        result = "MASTERCARD"

    # Check VISA
    elif int(number[0]) == 4:
        result = "VISA"

    else:
        print("INVALID")
        break

    # ////////// Luhn's Algorithm //////////

    # Check if card is real 4234567890123
    rev_num = number[::-1]  # Revers num
    odd_num = rev_num[1::2]  # sec_to_last
    evn_num = rev_num[::2]

    # First half
    sum = 0
    for num in odd_num:
        mlt = int(num) * 2

        if mlt >= 10:
            split_mlt = str(mlt)
            mlt = int(split_mlt[0]) + int(split_mlt[1])

        sum = sum + mlt

    # Sec half
    for num in evn_num:
        sum = sum + int(num)

    if sum % 10 == 0:
        print(result)
        break
    else:
        print("INVALID")
        break


# American Express 15
# MasterCard 16
# Visa 13, 16

# American Express 34 or 37
# MasterCard 51, 52, 53, 54, or 55
# Visa  4.

# Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
# Add the sum to the sum of the digits that weren’t multiplied by 2.
# If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!
