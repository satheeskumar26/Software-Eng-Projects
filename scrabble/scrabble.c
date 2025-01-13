#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int com_score(string player_input);

int main(void)
{
    string player_01 = get_string("player_01 type in a word: "); // Prompt the user for words
    string player_02 = get_string("player_02 type in a word: ");

    int player_01_score = com_score(player_01); // get score
    int player_02_score = com_score(player_02);

    if (player_01_score == player_02_score) // Print the winner or Tie
    {
        printf("Tie!\n");
    }
    else if (player_01_score > player_02_score)
    {
        printf("Player 1 wins!\n");
    }
    else if (player_01_score < player_02_score)
    {
        printf("Player 2 wins!\n");
    }
}

int com_score(string player_input) // Compute the score of each word
{
    int total_score = 0;
    int len = strlen(player_input); // get len of player_input
    int points[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    for (int i = 0; i < len; i++) // compare each input char with words
    {
        if (isalpha(player_input[i])) // pass thru only if alpha
        {
            if (!isupper(player_input[i])) // if not upper convert covert to upepr
            {
                player_input[i] = toupper(player_input[i]);
            }

            int get_point_postion = player_input[i] - 65; // upper 65 - 90
            total_score = total_score + points[get_point_postion];
        }

        total_score = total_score + 0; // this can be removed
    }
    return (total_score);
}
