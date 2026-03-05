# Step 1: Import required libraries and modules
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

# Step 2: Load environment variables from .env file
load_dotenv()

# Step 3: Retrieve BrowserStack credentials from environment variables
USERNAME = os.getenv("BROWSERSTACK_USERNAME")
ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")

# Step 4: Construct BrowserStack hub URL with credentials
URL = f"https://{USERNAME}:{ACCESS_KEY}@hub.browserstack.com/wd/hub"

# Step 5: Define list of browser configurations to test
browsers = [
    ("Chrome", "Windows", "10"),
    ("Firefox", "Windows", "10"),
    ("Edge", "Windows", "10"),
    ("Safari", "OS X", "Ventura"),
    ("Chrome", "OS X", "Ventura")
]

# Step 6: Loop through each browser configuration
for browser, os_name, os_version in browsers:

    # Display current browser being tested
    print("\nRunning on:", browser)

    # Step 7: Create Chrome options object
    options = Options()

    # Step 8: Configure BrowserStack specific options
    bstack_options = {
        "os": os_name,
        "osVersion": os_version,
        "projectName": "ElPais Assignment",
        "buildName": "ElPais Build",
        "sessionName": f"ElPais Test {browser}"
    }

    # Step 9: Set browser capabilities
    options.set_capability("browserName", browser)
    options.set_capability("browserVersion", "latest")
    options.set_capability("bstack:options", bstack_options)

    # Step 10: Initialize remote WebDriver with BrowserStack
    driver = webdriver.Remote(
        command_executor=URL,
        options=options
    )

    # Step 11: Navigate to target URL
    driver.get("https://elpais.com/opinion")

    # Step 12: Extract and display page title
    print("Page Title:", driver.title)

    # Step 13: Close browser session and clean up resources
    driver.quit()