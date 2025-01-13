# Scrabble Scoring Game

## Overview
This project is a simplified implementation of a Scrabble-like game where two players compete by entering words. The program calculates the scores for each word based on Scrabble's point system and determines the winner. It is written in C as part of the Harvard CS50x course.

## Problem Statement
In Scrabble, players form words to score points, with each letter assigned a specific point value:

| Letter | Points | Letter | Points | Letter | Points |
|--------|--------|--------|--------|--------|--------|
| A      | 1      | J      | 8      | S      | 1      |
| B      | 3      | K      | 5      | T      | 1      |
| C      | 3      | L      | 1      | U      | 1      |
| D      | 2      | M      | 3      | V      | 4      |
| E      | 1      | N      | 1      | W      | 4      |
| F      | 4      | O      | 1      | X      | 8      |
| G      | 2      | P      | 3      | Y      | 4      |
| H      | 4      | Q      | 10     | Z      | 10     |
| I      | 1      | R      | 1      |        |        |

For example, the word "CODE" scores as follows:
- C = 3 points
- O = 1 point
- D = 2 points
- E = 1 point

Total: **7 points**

## How It Works
1. The program prompts Player 1 to enter a word.
2. The program prompts Player 2 to enter a word.
3. Each word is scored based on Scrabble's letter point values.
4. The program compares the scores and announces the winner:
   - If Player 1 has the higher score, the output is: `Player 1 wins!`
   - If Player 2 has the higher score, the output is: `Player 2 wins!`
   - If both scores are equal, the output is: `Tie!`

## Implementation Details
The project is implemented in a file called `scrabble.c` located in the `scrabble` folder. It follows these steps:

1. **Input**:
   - Prompt Player 1 for a word.
   - Prompt Player 2 for a word.

2. **Scoring**:
   - Use a pre-defined point table to calculate the score of each word by summing the points for all letters in the word.
   - Case-insensitive scoring ensures both uppercase and lowercase letters are handled correctly.

3. **Output**:
   - Print the winner based on the scores or declare a tie if the scores are equal.

## Example
Here’s a sample run of the program:
```
Player 1: CODE
Player 2: JAVA
Player 1 wins!
```
Explanation:
- "CODE" scores 7 points.
- "JAVA" scores 15 points.

The program correctly determines that Player 2 is the winner.

## File Structure
- `scrabble/`
  - `scrabble.c`: The main program file that implements the scoring logic and user interaction.

## Key Features
- Implements Scrabble scoring logic using a pre-defined point table.
- Handles case-insensitive input.
- Compares scores and announces the winner.
- Provides meaningful output for ties.

## How to Use
1. Clone the repository.
2. Navigate to the `scrabble` directory.
3. Compile the code using a C compiler, e.g., `clang scrabble.c -o scrabble`.
4. Run the program using `./scrabble` and follow the prompts to input words.

## Future Enhancements
- Add support for validating words against a dictionary.
- Implement a graphical interface for a more interactive experience.
- Extend functionality to allow for multiple rounds of play.

---
This project demonstrates basic C programming skills and logical thinking, making it an excellent learning experience for aspiring software engineers.
