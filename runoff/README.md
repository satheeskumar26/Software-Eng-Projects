# Runoff Voting System
This project implements a runoff voting system in C, allowing voters to rank candidates in order of preference. The program eliminates the candidate with the fewest votes in successive rounds until one candidate receives a majority, ensuring a fair election result.

## Features
- Prompts voters to rank candidates in order of preference.
- Calculates the number of votes for each candidate in each round.
- Eliminates the candidate with the fewest votes in each round.
- Handles ties by eliminating all tied candidates with the fewest votes.
- Declares the winner when a candidate receives a majority of the votes.

## Problem Addressed
Runoff voting ensures that the elected candidate has majority support, addressing issues with simple plurality voting systems where a winner may lack widespread voter approval.

## How to Use
1. **Compile the Program**: Use a C compiler to compile the source code, e.g., `clang runoff.c -o runoff`.
2. **Run the Program**: Execute the compiled program, passing the names of the candidates as command-line arguments:
   ```bash
   ./runoff Alice Bob Charlie
   ```
3. **Input Voter Preferences**: Enter the number of voters and rank the candidates for each voter.
4. **View Results**: The program will simulate the runoff process and declare the winner.

## Why This Project?
This project was part of my Harvard CS50x coursework, designed to strengthen my understanding of arrays, loops, and ranked-choice voting systems in C programming.
