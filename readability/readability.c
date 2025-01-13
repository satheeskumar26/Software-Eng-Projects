#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = "";

    do
    {
        // Prompt the user for some text
        text = get_string("Text: ");
    }
    while (strlen(text) == 0);

    // Count the number of letters
    int letters = count_letters(text);
    //  Count words, and sentences in the text
    int words = count_words(text);
    printf("words %i\n", words);
    //  Count sentences in the text
    int sentences = count_sentences(text);

    float L = ((float) letters / words) * 100;
    float S = ((float) sentences / words) * 100;

    float index = (0.0588 * L - 0.296 * S - 15.8);

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 1 && index <= 16)
    {
        printf("Grade %i\n", (int) round(index));
    }
    else
    {
        printf("Grade 16+\n");
    }
}

int count_letters(string text) // Return the number of letters in input text
{
    int len = strlen(text);
    int num_of_let = 0;

    for (int i = 0; i < len; i++) // for i in len check if text[i] isalpha
    {
        if (isalpha(text[i]))
        {
            num_of_let++;
        }
    }
    return (num_of_let);
}

int count_words(string text) // Return the number of words in text.
{
    int len = strlen(text);
    int num_of_space = 0 + 1;

    for (int i = 0; i < len; i++)
    {
        if (i == 0 && text[i] == 32)
        {
        }
        else if (i == len - 1 && text[i] == 32)
        {
        }
        else if (text[i] == 32 && text[i + 1] == 32)
        {
        }
        else if (text[i] == 32)
        {
            num_of_space++;
        }
    }

    return (num_of_space);
}

int count_sentences(string text)
{
    // Return the number of sentences in text
    int len = strlen(text);
    int num_of_sent = 0;

    for (int i = 0; i < len; i++)
    {
        if (text[i] == 33 || text[i] == 46 || text[i] == 63) // 33 = ! 46 = . 63 = ?
        {
            num_of_sent++;
        }
    }

    return (num_of_sent);
}
