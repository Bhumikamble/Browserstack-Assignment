# Step 1: Import required libraries
import os
from selenium import webdriver
from dotenv import load_dotenv

# Step 2: Load environment variables from .env file
load_dotenv()

# Step 3: Retrieve BrowserStack username from environment variables
USERNAME = os.getenv("BROWSERSTACK_USERNAME")
# Step 4: Retrieve BrowserStack access key from environment variables
ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")

# Step 5: Define factory function to create BrowserStack WebDriver
def create_browserstack_driver(capabilities):
    # Step 6: Initialize remote WebDriver with BrowserStack hub and credentials
    driver = webdriver.Remote(
        command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub.browserstack.com/wd/hub",
        desired_capabilities=capabilities
    )

    # Step 7: Return initialized WebDriver instance
    return driver