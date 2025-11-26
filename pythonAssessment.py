#!/usr/bin/env python3

# Author: Hunter Steele
# Date: 11/26/25
# Version: 1.1

import string  # Provides access to punctuation characters

# Count Specific Word
def count_specific_word(text, search_word):
    """Counts occurrences of a specific word in a text."""
    if not text or not search_word:
        return 0
    
    # Remove punctuation and normalize casing
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator).lower()
    clean_word = search_word.lower()

    words = clean_text.split()
    return words.count(clean_word)


# Identify Most Common Word
def identify_most_common_word(text):
    """Returns the most common word in the text."""
    if not text.strip():
        return None

    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator).lower()
    words = clean_text.split()

    if not words:
        return None

    # Count each word's frequency
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    # Return the word with the highest frequency
    return max(word_counts, key=word_counts.get)


# Calculate Average Word Length
def calculate_average_word_length(text):
    """Calculates the average length of words in the text."""
    if not text.strip():
        return 0
    
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator)
    words = clean_text.split()

    if not words:
        return 0
    
    total_length = sum(len(word) for word in words)
    return total_length / len(words)


# Count Paragraphs
def count_paragraphs(text):
    """Counts paragraphs based on empty lines."""
    if not text.strip():
        return 1
    
    lines = text.split("\n")

    paragraphs = 0
    in_paragraph = False

    # Paragraph is counted when entering non-empty text after a blank line
    for line in lines:
        if line.strip():
            if not in_paragraph:
                paragraphs += 1
                in_paragraph = True
        else:
            in_paragraph = False
        
    return paragraphs


# Count Sentences
def count_sentences(text):
    """Counts sentences based on punctuation."""
    if not text.strip():
        return 1
    
    sentence_endings = ".!?"
    count = sum(1 for char in text if char in sentence_endings)

    return max(1, count)


# MAIN PROGRAM — RUN THE ANALYSIS
# Includes required while loop, for loop, and if/else
if __name__ == "__main__":

    # Simple menu loop (satisfies while-loop requirement)
    while True:
        print("\n--- Text Analysis Menu ---")
        print("1. Run analysis")
        print("2. Exit")
        choice = input("Choose an option (1 or 2): ")

        # Conditional required in rubric
        if choice == "2":
            print("Exiting program...")
            break
        elif choice != "1":
            print("Invalid choice. Please select 1 or 2.")
            continue

        # User pastes their article here
        article = """
        Copy/Paste the article you want to analyze here.
        
        It can include multiple paragraphs.

        Make sure it stays within the triple quotes and replaces these instructions.
        """

        # Tuple list used to loop through results (satisfies for-loop requirement)
        results = [
            ("Count of 'the'", count_specific_word(article, "the")),
            ("Most common word", identify_most_common_word(article)),
            ("Average word length", calculate_average_word_length(article)),
            ("Paragraph count", count_paragraphs(article)),
            ("Sentence count", count_sentences(article)),
        ]

        for label, value in results:
            print(f"{label}: {value}")
