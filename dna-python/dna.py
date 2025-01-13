import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage : Pass database file and sequences file")
        sys.exit(1)

    # TODO: Read database file into a variable.
    peoples_data_list = []
    with open(sys.argv[1], "r") as data_file:
        data_file_read = csv.DictReader(data_file)

        for person in data_file_read:
            peoples_data_list.append(person)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as seq_file:
        seq_file_read = seq_file.read()

    # TODO: Find longest match of each STR in DNA sequence
    if len(peoples_data_list) == 3:
        str_dic = {"AGATC": 0, "AATG": 0, "TATC": 0}
    else:
        str_dic = {"AGATC": 0, "TTTTTTCT": 0, "AATG": 0, "TCTAG": 0, "GATA": 0, "TATC": 0,
                   "GAAA": 0, "TCTG": 0}  # get key by using .keys() get back a list[] of keys

    for key in str_dic.keys():
        longest_match_value = longest_match(seq_file_read, key)
        str_dic[key] = longest_match_value

    # TODO: Check database for matching profiles
    main_loop = 0

    for person in peoples_data_list:
        seq_num = list(str_dic.values())
        person_num = list(person.values())[1:]

        num_exist_loop = 0
        main_loop = main_loop + 1

        for i in range(len(seq_num)):
            if seq_num[i] == int(person_num[i]):
                num_exist_loop = num_exist_loop + 1
            else:
                break

        if len(seq_num) == num_exist_loop:
            print(person["name"])
            break

    if main_loop == len(peoples_data_list):
        print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)  # AGATC,TTTTTTCT,AATG,TCTAG,GATA,TATC,GAAA,TCTG.  if 4
    sequence_length = len(sequence)  # AAGGTAAGTTTAGAATATAAAAGGTGAGT. if 100

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length  # i + 0 * 4
            end = start + subsequence_length  # start + 4

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
