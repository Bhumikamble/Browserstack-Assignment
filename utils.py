# Step 1: Import required libraries
from deep_translator import GoogleTranslator
import re
from collections import Counter


# Step 2: Define function to translate a single title
def translate_titles(title):
    # Step 3: Attempt translation with error handling
    try:
        # Step 4: Translate text from auto-detected language to English
        translated = GoogleTranslator(source="auto", target="en").translate(title)
        # Step 5: Return translated text
        return translated
    # Step 6: Catch and handle translation errors
    except Exception as e:
        print("Translation error:", e)
        # Step 7: Return original title if translation fails
        return title


# Step 8: Define function to analyze repeated words in multiple titles
def analyze_words(titles):
    # Step 9: Initialize empty list to store all words
    words = []

    # Step 10: Loop through each title
    for title in titles:
        # Step 11: Remove punctuation from title
        clean = re.sub(r"[^\w\s]", "", title)

        # Step 12: Convert to lowercase and split into individual words
        split_words = clean.lower().split()

        # Step 13: Add words to main list
        words.extend(split_words)

    # Step 14: Count frequency of each word
    word_count = Counter(words)

    # Step 15: Filter to keep only words that appear more than once
    repeated = {word: count for word, count in word_count.items() if count > 1}

    # Step 16: Return dictionary of repeated words and their counts
    return repeated