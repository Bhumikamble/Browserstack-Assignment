# Step 1: Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_articles():
    # Step 2: Set up Chrome options for headless mode
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    # Step 3: Initialize Chrome WebDriver with configured options
    driver = webdriver.Chrome(options=options)

    # Step 4: Navigate to the target website
    driver.get("https://elpais.com/")
    
    # Step 5: Wait for page to fully load
    time.sleep(5)

    # Step 6: Find all article header elements using CSS selector
    articles = driver.find_elements(By.CSS_SELECTOR, "h2 a")

    # Step 7: Initialize list to store Spanish article titles
    spanish_titles = []

    # Step 8: Loop through first 5 articles and extract titles
    for article in articles[:5]:
        # Extract and clean the article title text
        title = article.text.strip()

        # Step 9: Add non-empty titles to the list
        if title:
            spanish_titles.append(title)

    # Step 10: Close the WebDriver and clean up resources
    driver.quit()

    # Step 11: Return the list of Spanish titles
    return spanish_titles