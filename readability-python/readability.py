# Coleman-Liau index
text = input("Text: ")

# Calcalate words
count_word = 1
count_alpha = 0
count_sentence = 0

for i in text:
    # Words
    if i == " ":
        count_word = count_word + 1
    # alpha
    if i.isalpha():
        count_alpha = count_alpha + 1
    # alpha
    if i in (".", "!", "?"):
        count_sentence = count_sentence + 1

# get the avarage of 100 words
word_avr = count_word / 100

leters = count_alpha / word_avr
sentence = count_sentence / word_avr

index = 0.0588 * leters - 0.296 * sentence - 15.8

if index < 1:
    print("Before Grade 1")
elif index >= 1 and index <= 16:
    print(f"Grade {round(index)}")
elif index > 16:
    print("Grade 16+")
