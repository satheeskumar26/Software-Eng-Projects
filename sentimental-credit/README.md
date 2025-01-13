# Sentimental Credit Validator
This project implements a credit card validation program in Python, using Luhn's Algorithm to determine whether a credit card number is valid. The program identifies the card type (American Express, MasterCard, Visa) or indicates if the number is invalid.

## Features
- Prompts the user to input a credit card number.
- Validates the number using Luhn's Algorithm:
  - Multiplies every second digit (from right to left) by 2 and adds the digits of the resulting products.
  - Sums the above result with the digits that weren’t multiplied by 2.
  - Checks if the total is divisible by 10 (i.e., its last digit is 0).
- Identifies the credit card provider based on starting digits:
  - **American Express**: Starts with 34 or 37, and has 15 digits.
  - **MasterCard**: Starts with 51, 52, 53, 54, or 55, and has 16 digits.
  - **Visa**: Starts with 4, and has 13 or 16 digits.
- Outputs one of the following:
  - `AMEX`
  - `MASTERCARD`
  - `VISA`
  - `INVALID`

## Problem Addressed
Manually validating credit card numbers can be tedious and prone to error. This program automates the process, ensuring correctness and providing immediate feedback on the card’s validity and type.

## How to Use
1. **Run the Program**: Execute the Python script and input the credit card number when prompted:
   ```bash
   python credit.py
   Number: 4003600000000014
   VISA
   ```
2. **View Results**: The program will display the card type or indicate if the number is invalid.

## Why This Project?
This project was part of my Harvard CS50x coursework, designed to transition from C to Python while reinforcing problem-solving skills and understanding of algorithms.
