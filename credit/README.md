# Credit Card Validator

This project implements a credit card validation program in C using **Luhn's Algorithm**. The program identifies whether a given credit card number belongs to American Express, MasterCard, or Visa, or if it is invalid. It achieves this by analyzing the structure, starting digits, and checksum of the input.

## Features
- Prompts the user to input a credit card number.
- Validates the number using **Luhn's Algorithm**:
  1. Multiplies every second digit (from right to left) by 2 and adds the digits of the resulting products.
  2. Sums the above result with the digits that weren’t multiplied by 2.
  3. Checks if the total is divisible by 10 (i.e., its last digit is 0).
- Identifies the credit card provider based on starting digits:
  - **American Express**: Starts with 34 or 37, and has 15 digits.
  - **MasterCard**: Starts with 51, 52, 53, 54, or 55, and has 16 digits.
  - **Visa**: Starts with 4, and has 13 or 16 digits.
- Outputs one of the following:
  - `AMEX\n`
  - `MASTERCARD\n`
  - `VISA\n`
  - `INVALID\n`

## Example Use Case
When executed, the program interacts with the user as follows:
```bash
$ ./credit
Number: 4003600000000014
VISA
```

## Problem Addressed
Validating credit card numbers manually can be tedious and error-prone. This program automates the process, ensuring the correctness of the input while checking its compliance with specific industry standards. It provides immediate feedback on whether the card is valid and identifies the provider.

## Why This Project?
This project was part of my Harvard CS50x coursework, designed to strengthen my problem-solving skills, deepen my understanding of algorithms, and enhance my proficiency in C programming.

This repository includes:
- `credit.c`: The main program file containing the implementation of the credit card validation logic.
- Sample input/output examples for testing.

Feel free to explore the code and reach out with any suggestions or feedback!
