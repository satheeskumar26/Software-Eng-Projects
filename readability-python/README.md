# Readability
This project implements a program in Python to evaluate the readability level of a given text using the Coleman-Liau index. By analyzing the number of letters, words, and sentences in the text, the program determines the U.S. grade level required to understand the text.

## Features
- Analyzes input text to count:
  - Letters: Alphabetic characters.
  - Words: Sequences separated by spaces.
  - Sentences: Ended by `.`, `!`, or `?`.
- Calculates the Coleman-Liau index using the formula:
  ```
  index = 0.0588 * L - 0.296 * S - 15.8
  ```
  Where:
  - `L` is the average number of letters per 100 words.
  - `S` is the average number of sentences per 100 words.
- Outputs the text's readability grade level:
  - `Grade X`: Indicates the U.S. school grade level.
  - `Before Grade 1`: For very simple texts.
  - `Grade 16+`: For complex texts beyond grade 16.

## Problem Addressed
Manually assessing the readability of text can be subjective and time-consuming. This program automates the process, providing an objective and accurate measure of readability.

## How to Use
1. **Run the Program**: Execute the Python script and input a block of text when prompted:
   ```bash
   python readability.py
   Text: Congratulations! Today is your day. You're off to Great Places!
   Grade 3
   ```
2. **View Results**: The program will calculate and display the readability grade level.

## Why This Project?
This project was part of my Harvard CS50x coursework, designed to transition from C to Python while reinforcing skills in text analysis, algorithms, and problem-solving.
