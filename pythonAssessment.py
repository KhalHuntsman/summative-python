#!/usr/bin/env python3

# Author: <Hunter Steele>
# Date: <11/26/25>
# version: 1.1

import string  # Used for punctuation removal in text-processing functions

# Count Specific Word
def count_specific_word(text, search_word):
    """Counts occurrences of a specific word in a text."""
    # Handle edge cases: empty text or empty search term
    if not text or not search_word:
        return 0
    
    # Build a translation table to remove punctuation
    translator = str.maketrans('', '', string.punctuation)

    # Normalize text: remove punctuation and convert to lowercase for consistent matching
    clean_text = text.translate(translator).lower()
    clean_word = search_word.lower()

    # Split into words and count matches
    words = clean_text.split()
    return words.count(clean_word)


# Identify Most Common Word
def identify_most_common_word(text):
    """Returns the most common word in the text."""
    # If text is empty or contains only whitespace, there is no word to analyze
    if not text.strip():
        return None

    # Remove punctuation and normalize casing
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator).lower()

    # Split into individual words
    words = clean_text.split()

    # If no valid words exist after cleaning, return None
    if not words:
        return None

    # Count occurrences of each word using a dictionary
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    # Determine the word with the highest count
    # (This line must be outside the loop to avoid returning early)
    most_common = max(word_counts, key=word_counts.get)
    return most_common


# Calculate Average Word Length
def calculate_average_word_length(text):
    """Calculates the average length of words in the text."""
    # If text is empty or only whitespace, average length is 0
    if not text.strip():
        return 0
    
    # Remove punctuation to measure only actual word characters
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator)

    # Split into words
    words = clean_text.split()

    if not words:
        return 0

    # Sum the lengths of all words and divide to find the average
    total_length = sum(len(word) for word in words)
    return total_length / len(words)


# Count Paragraphs
def count_paragraphs(text):
    """Counts paragraphs based on empty lines."""
    # By assignment rules: empty text counts as 1 paragraph
    if not text.strip():
        return 1
    
    # Split text into lines for paragraph evaluation
    lines = text.split("\n")

    paragraphs = 0
    in_paragraph = False  # Tracks whether we are currently inside a paragraph block

    for line in lines:
        # A line with content starts or continues a paragraph
        if line.strip():
            if not in_paragraph:  # Only count a new paragraph when entering one
                paragraphs += 1
                in_paragraph = True
        else:
            # Blank line ends the current paragraph block
            in_paragraph = False
        
    return paragraphs


# Count Sentences
def count_sentences(text):
    """Counts sentences based on punctuation."""
    # Empty text must count as 1 sentence per project requirements
    if not text.strip():
        return 1
    
    sentence_endings = ".!?"
    count = 0

    # Count any character that ends a sentence
    for char in text:
        if char in sentence_endings:
            count += 1

    # Guarantee at least 1 sentence is returned
    return max(1, count)


# MAIN PROGRAM — RUN THE ANALYSIS
if __name__ == "__main__":
    
    # Triple-quoted string where the article is pasted directly.
    # The user replaces this placeholder with the full news article text.
    article = """
    Copy/Paste the article you want to analyze here.
    
    It can include multiple paragraphs.

    Just make sure it stays inside of the triple quotes and replaces these instructions.

    Do not forget to revert the file before future uses so instructions reappear.
    """

    # Function calls to analyze the article and print results to the console
    print("Count of 'the':", count_specific_word(article, "the"))
    print("Most common word:", identify_most_common_word(article))
    print("Average word length:", calculate_average_word_length(article))
    print("Paragraph count:", count_paragraphs(article))
    print("Sentence count:", count_sentences(article))
