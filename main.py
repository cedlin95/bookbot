import os

# Initialize the letter_count dictionary to store frequencies
letter_count = {}

def main():
    total_words = 0
    with open("bookbot/books/Frankenstein.txt") as f:
        file_contents = f.read()

    # Split the text into words
    words = file_contents.split()

    # Iterate over each word
    for current_word in words:
        total_words += 1
        # Iterate over each letter in the word
        for letter in current_word:
            # Check if letter is already in the dictionary
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    # Print the letter count
    print('--- Begin report of books/frankenstein.txt ---/n/n')
    for letter in letter_count:
        num_of_occurences = letter_count[letter]
        print(f'the character {letter} was found {num_of_occurences} times')

main()