# Step 1: Import required modules
from scraper import scrape_articles
from translator import translate_text
from analyzer import analyze_titles

# Step 2: Scrape Spanish articles from the web
spanish_titles = scrape_articles()

# Step 3: Initialize list to store translated titles
translated_titles = []

# Step 4: Print header for articles section
print("\nARTICLES:\n")

# Step 5: Loop through each Spanish title and translate it
for i, title in enumerate(spanish_titles, 1):

    # Translate the current title
    translated = translate_text(title)
    translated_titles.append(translated)

    # Display the article with both Spanish and translated versions
    print(f"\nArticle {i}")
    print("Spanish Title:", title)
    print("Translated Title:", translated)


# Step 6: Print header for analysis section
print("\nRepeated words more than twice:")

# Step 7: Analyze translated titles to find repeated words
repeated = analyze_titles(translated_titles)

# Step 8: Display the analysis results
for word, count in repeated.items():
    print(word, ":", count)