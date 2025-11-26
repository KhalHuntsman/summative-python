# Overview

This project is a Summative Python Assessment focused on applying core Natural Language Processing (NLP) techniques using pure Python. The goal of the program is to analyze the content of a news article and extract meaningful insights such as word usage, sentence counts, and paragraph structure.

All analysis is performed inside a single file:
- pythonAssessment.py

The user pastes the article directly into the program (inside triple quotes), and the script outputs several key statistics based on the text.

### What the Program Does

pythonAssessment.py includes five text-analysis functions and a main execution block. Together, they perform the following operations:

1. Count Specific Word

- count_specific_word(text, search_word)
- Counts how many times a given word appears
- Removes punctuation
- Case-insensitive
- Returns 0 if search word is not found

2. Identify Most Common Word

- identify_most_common_word(text)
- Determines the most frequently used word in the article
- Strips punctuation and normalizes casing
- Returns None for empty text

3. Calculate Average Word Length

- calculate_average_word_length(text)
- Computes the average length of all words
- Excludes punctuation
- Returns 0 for empty text

4. Count Paragraphs

- count_paragraphs(text)
- Counts paragraphs based on blank lines
- Treats consecutive non-empty lines as a single paragraph
- Returns 1 if the text is empty (per assignment guidelines)

5. Count Sentences

- count_sentences(text)
- Counts sentences using ., !, and ?
- Guarantees a minimum return value of 1 for empty text

6. Main Program

At the bottom of pythonAssessment.py, a special block:

if __name__ == "__main__":


runs the entire analysis by:

- Accepting the article pasted directly in triple quotes
- Calling each analysis function
- Printing all results to the console

### Technologies Used

This project uses:
- Python 3.x
- Built-in Python libraries only
- string (for punctuation removal)
- Core NLP / text-processing logic implemented manually
- No external packages or modules are required.

### File Structure
summative/
│
├── pythonAssessment.py    # ALL logic, functions, and article analysis
└── README.md              # This documentation file

- No other files (such as .txt articles) are required — the article is pasted into the script directly.

### How to Run the Program

Navigate to the summative directory in your terminal:
- cd summative

Run the script using Python:

#### On Windows:
python pythonAssessment.py

#### On macOS/Linux:
python3 pythonAssessment.py

#### View the output in your terminal.

The program will print:
- Count of a specific word
- Most common word
- Average word length
- Number of paragraphs
- Number of sentences

📝 How to Use the Program

Inside pythonAssessment.py, locate this block:

 # Paste your article here
    article = """
    Copy/Paste the article you want to analyze here.
    
    It can include multiple paragraphs.

    Just make sure it stays inside of the triple quotes and replaces these instructions.

    Do not forget to revert the file before future uses so instructions reappear.
    """


Replace the placeholder text with the full article you want to analyze.
Save the file and re-run the script. Revert with ctrl + z or undo, save it, and close the file prior to closing the file.

### Purpose of This Project

This project demonstrates skills in:

- String processing
- Conditional logic
- Looping and dictionaries
- Parsing paragraphs and sentences
- Writing modular Python functions
- Organizing a standalone Python program

It also reflects best practices such as using:

if __name__ == "__main__":

to prevent accidental execution when importing the file.