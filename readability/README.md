# Readability

## Overview

This program calculates the reading level of a given text using the Coleman-Liau index. By analyzing the number of letters, words, and sentences in the text, the program determines the U.S. grade level required to comprehend the text.

## Problem to Solve

In academia, publishing, and education, it’s essential to evaluate how challenging a piece of text might be for readers. The Coleman-Liau index provides a quantitative method to achieve this by assigning a grade level to the text. For example:

- A score of `3` implies the text is understandable by a third-grader.
- A score of `12` suggests the text is suitable for a twelfth-grader.

The program calculates this score to help users identify the readability level of their content.

## Implementation Details

The program reads a block of text from the user and evaluates it based on:

1. **Letters**: Any alphabetical character.
2. **Words**: A sequence of characters separated by spaces.
3. **Sentences**: Any sequence of text ending with `.`, `!`, or `?`.

The program uses the Coleman-Liau formula:

\[
\text{Index} = 0.0588 \times L - 0.296 \times S - 15.8
\]

Where:
- \( L \): Average number of letters per 100 words.
- \( S \): Average number of sentences per 100 words.

### Example

Input:
```
Congratulations! Today is your day. You're off to Great Places! You're off and away!
```

Output:
```
Grade 3
```

### Special Cases
- Texts with no sentences will result in `Before Grade 1`.
- Extremely complex texts may result in `Grade 16+`.

## Usage

This project was implemented as part of Harvard's CS50x course and demonstrates proficiency in C programming, text processing, and algorithm implementation.
