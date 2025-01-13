# Substitution Cipher
This project implements a substitution cipher program in C, allowing users to encrypt plaintext using a substitution key provided as input. The program replaces each letter in the plaintext with a corresponding letter from the key, preserving case and leaving non-alphabetic characters unchanged.

## Features
- Prompts the user for a substitution key (26 unique alphabetic characters).
- Validates the key for correctness and uniqueness.
- Accepts plaintext input from the user.
- Encrypts the plaintext using the provided substitution key.
- Outputs the resulting ciphertext.

## Problem Addressed
Manually encrypting messages with a substitution cipher can be error-prone and time-consuming. This program automates the process, ensuring accuracy and compliance with encryption rules.

## How to Use
1. **Compile the Program**: Use a C compiler to compile the source code, e.g., `clang substitution.c -o substitution`.
2. **Run the Program**: Execute the compiled program, passing a 26-character substitution key as a command-line argument:
   ```bash
   ./substitution YTNSHKVEFXRBAUQZCLWDMIPGJO
   ```
3. **Input Plaintext**: When prompted, enter the plaintext to encrypt.
4. **View Ciphertext**: The program will output the encrypted ciphertext based on the provided key.

## Why This Project?
This project was part of my Harvard CS50x coursework, designed to enhance my understanding of string manipulation, validation logic, and basic cryptographic techniques in C programming.

