# Plurality Voting System
This project implements a plurality voting system in C, allowing users to conduct a simple election. The program enables voters to cast votes for their preferred candidates and determines the winner(s) based on the highest number of votes.

## Features
- Prompts the user to input the number of candidates and their names.
- Accepts votes for candidates from voters.
- Tracks the vote count for each candidate.
- Declares the winner(s) with the highest number of votes.
- Handles ties by announcing all candidates with the highest vote count.

## Problem Addressed
Manually managing an election and counting votes can be error-prone and time-consuming. This program automates the voting process, ensuring accurate vote tallying and fair results.

## How to Use
1. **Compile the Program**: Use a C compiler to compile the source code, e.g., `clang plurality.c -o plurality`.
2. **Run the Program**: Execute the compiled program, passing the candidates' names as command-line arguments:
   ```bash
   ./plurality Alice Bob Charlie
   ```
3. **Vote**: Input the number of voters and cast votes for the candidates.
4. **View Results**: The program will display the winner(s) or indicate a tie if applicable.

## Why This Project?
This project was part of my Harvard CS50x coursework, designed to enhance my understanding of arrays, loops, and logical conditions in C programming.
