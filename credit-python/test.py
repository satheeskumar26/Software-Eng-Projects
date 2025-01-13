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
    rev_num = number[::-1] # Revers num
    odd_num = rev_num[1::2] # sec_to_last
    evn_num = rev_num[::2]

    print(rev_num)
    print(odd_num)
    print(evn_num)

    # First half
    sum = 0
    for num in odd_num:
        mlt = int(num) * 2
        print("mlt less: ", mlt)
        if mlt >= 10:
            print("mlt more: ", mlt)
            split_mlt = str(mlt)
            print("mlt split: ", split_mlt[0] , split_mlt[1])
            mlt = int(split_mlt[0]) + int(split_mlt[1])
        sum = sum + mlt

    print("first sum: ",sum)
    # Sec half
    for num in evn_num:
        sum = sum + int(num)

    print("full sum: ",sum)

    if sum % 10 == 0:
        print(result)
        break
    else:
        print("INVALID")
        break
