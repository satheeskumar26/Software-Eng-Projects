# Readability
This project implements a program in C that calculates the readability grade level of a given text using the Coleman-Liau index. By analyzing the number of letters, words, and sentences in the text, the program determines the U.S. grade level required to comprehend the text.

## Features
- Analyzes user-inputted text for:
  - **Letters**: Counts alphabetic characters.
  - **Words**: Counts sequences of characters separated by spaces.
  - **Sentences**: Counts text ending with `.`, `!`, or `?`.
- Calculates the readability grade level using the Coleman-Liau index formula:
  ```
  index = 0.0588 * L - 0.296 * S - 15.8
  ```
  - `L`: Average number of letters per 100 words.
  - `S`: Average number of sentences per 100 words.
- Outputs the grade level or special cases:
  - `Before Grade 1` for very simple texts.
  - `Grade 16+` for very complex texts.

## Problem Addressed
Determining the readability of text manually can be challenging and subjective. This program automates the process using a mathematical formula, providing quick and accurate results for assessing text complexity.

## How to Use
1. **Compile the Program**: Use a C compiler to compile the source code, e.g., `clang readability.c -o readability`.
2. **Run the Program**: Execute the compiled program:
   ```bash
   ./readability
   ```
3. **Input Text**: When prompted, enter the text you want to analyze.
4. **View Grade Level**: The program will output the readability grade level.

Example:
```
$ ./readability
Text: This is CS50. It's a great course.
Grade 5
```

## Why This Project?
This project was part of my Harvard CS50x coursework, designed to strengthen my skills in text processing, mathematical computations, and logical problem-solving using C programming.
