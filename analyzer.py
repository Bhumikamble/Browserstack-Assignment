# Step 1: Import required libraries
import re
from collections import Counter

# Step 2: Define function to analyze titles for repeated words
def analyze_titles(titles):

    # Step 3: Initialize empty list to store all words from titles
    words = []

    # Step 4: Loop through each title in the list
    for title in titles:
        # Step 5: Remove punctuation from the title
        cleaned = re.sub(r'[^\w\s]', '', title)
        # Step 6: Convert to lowercase and split into individual words, then add to words list
        words.extend(cleaned.lower().split())

    # Step 7: Count the frequency of each word
    counter = Counter(words)

    # Step 8: Filter to keep only words that appear more than twice
    repeated = {word: count for word, count in counter.items() if count > 2}

    # Step 9: Return the dictionary of repeated words and their counts
    return repeated