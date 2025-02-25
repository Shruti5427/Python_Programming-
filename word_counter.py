import re

# Function to count words
def count_words(text):
    words = text.split()
    return len(words)

# Function to count characters (excluding spaces)
def count_characters(text):
    return len(text.replace(" ", ""))

# Function to count sentences
def count_sentences(text):
    sentences = re.split(r'[.!?]', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)

# Taking user input
text = input("Enter your text: ").strip()

# Checking if input is empty
if text == "":
    print("Please enter some text!")
else:
    # Counting words, characters, and sentences
    words = count_words(text)
    characters = count_characters(text)
    sentences = count_sentences(text)

    # Displaying results
    print("Word Count:", words)
    print("Character Count (excluding spaces):", characters)
    print("Sentence Count:", sentences)
