#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        // check if there is input
        printf("Usage: ./substitution Key\n");
        return (1);
    }

    int num_of_char = strlen(argv[1]);
    string ciphertext = argv[1];

    if (num_of_char != 26)
    {
        // check if there is 26 char
        printf("Key must contain 26 characters.\n");
        return (1);
    }

    for (int i = 0; i < num_of_char; i++)
    {
        if (!isalpha(ciphertext[i]))
        {
            // check if all char are alpha
            printf("Key must contain alphadetic characters.\n");
            return (1);
        }
    }

    int seen[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // 65 to 90

    for (int i = 0; i < num_of_char; i++)
    {
        // convert all chr to upper, then - 65 to set it to 0 to 26 like A to Z
        int seen_position = toupper(ciphertext[i]) - 65;
        // add + 1 if alpha is passed
        seen[seen_position] = seen[seen_position] + 1;

        if (seen[seen_position] == 2)
        {
            printf("Key must not contain repeted characters.\n");
            return (1);
        }
    }

    // Ask for plain text
    string plaintext = get_string("plaintext: ");
    int plain_len = strlen(plaintext);
    int plaintext_position = 0;
    char decipher[plain_len];

    // for the len of plaintext, check if lower or upper or others
    for (int i = 0; i < plain_len; i++)
    {
        if (isupper(plaintext[i]))
        {
            // plaintext - 65 to set it to 0 to 26 range like A to Z.
            plaintext_position = plaintext[i] - 65;
            // use plaintext_position on ciphertext.
            decipher[i] = toupper(ciphertext[plaintext_position]);
        }
        else if (islower(plaintext[i]))
        {
            plaintext_position = plaintext[i] - 97;
            decipher[i] = tolower(ciphertext[plaintext_position]);
        }
        else
        {
            // if it not alph just pass it as it is.
            decipher[i] = plaintext[i];
        }
    }

    // add zerow to the end on the arry.
    decipher[plain_len] = '\0';

    printf("ciphertext: %s\n", decipher);
}
