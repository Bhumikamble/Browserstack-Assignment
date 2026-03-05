# 🚀 BrowserStack Assignment – El País Article Scraper

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green)
![BrowserStack](https://img.shields.io/badge/BrowserStack-Cross--Browser%20Testing-orange)
![PyTest](https://img.shields.io/badge/PyTest-Testing-yellow)

## 📖 Overview

This project automates a workflow that scrapes and analyzes articles from the **El País Opinion section** using **Selenium and BrowserStack**.

### The automation performs the following steps:

1. Opens the **El País Opinion page** using Selenium.
2. Scrapes the **first 5 article titles in Spanish**.
3. Translates the titles **from Spanish to English**.
4. Performs **text analysis to detect repeated words**.
5. Executes tests on **multiple browsers via BrowserStack**.

### 🎯 Key Concepts Demonstrated

* Selenium-based **browser automation**
* Web scraping using **BeautifulSoup**
* Language translation using **Deep Translator**
* **Parallel cross-browser testing** with BrowserStack
* Secure configuration using **dotenv**

---

# 📁 Project Structure

```
.
├── __pycache__/              # Python compiled cache files
├── .pytest_cache/            # Pytest cache directory
├── images/                   # Screenshots captured during tests
├── log/                      # Execution log files
├── venv/                     # Python virtual environment

├── .env                      # Environment variables (credentials)
├── analyzer.py               # Performs repeated word analysis
├── browserstack_config.py    # BrowserStack configuration
├── browserstack.yml          # BrowserStack execution configuration
├── driver_factory.py         # WebDriver creation and management
├── main.py                   # Main entry point of the project
├── scraper.py                # Web scraping logic
├── translator.py             # Handles Spanish → English translation
├── utils.py                  # Helper utility functions
├── test_browserstack.py      # Cross-browser Selenium tests

├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

---

# 📄 File Description

| File                     | Purpose                                     |
| ------------------------ | ------------------------------------------- |
| `main.py`                | Runs the complete automation workflow       |
| `scraper.py`             | Scrapes Spanish article titles from El País |
| `translator.py`          | Translates titles to English                |
| `analyzer.py`            | Detects repeated words in translated titles |
| `driver_factory.py`      | Initializes Selenium WebDriver              |
| `browserstack_config.py` | Stores BrowserStack capabilities            |
| `test_browserstack.py`   | Runs Selenium tests on BrowserStack         |
| `.env`                   | Stores BrowserStack credentials             |
| `requirements.txt`       | Lists Python dependencies                   |

---

# ⚙️ Prerequisites

Ensure the following are installed before running the project:

* Python **3.9+**
* BrowserStack account
* Internet connection

---

# 📥 Step 1: Clone the Repository

```bash
git clone <repository-url>
cd browserstack-assignment
```

---

# 🧪 Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac / Linux**

```bash
source venv/bin/activate
```

---

# 📦 Step 3: Install Dependencies

Install dependencies manually:

```bash
pip install selenium beautifulsoup4 requests deep-translator python-dotenv pytest
```

Or install from requirements file:

```bash
pip install -r requirements.txt
```

---

# 🔐 Step 4: Configure BrowserStack Credentials

Create a `.env` file in the root directory.

```
BROWSERSTACK_USERNAME=your_browserstack_username
BROWSERSTACK_ACCESS_KEY=your_browserstack_access_key
```

You can find these credentials in the **BrowserStack Dashboard**.

---

# 🌐 Step 5: Scraping Logic

The script accesses the following page:

```
https://elpais.com/opinion/
```

Using **BeautifulSoup**, it extracts the **first 5 article titles**.

### Example Spanish Titles

```
España enviará a Chipre la fragata ‘Cristóbal Colón’
El secretario general de la OTAN justifica la ofensiva contra Irán
Financial Times define a Sánchez como “la némesis de Trump en Europa”
```

---

# 🌍 Step 6: Translation

The project uses **Deep Translator** to translate Spanish titles into English.

### Example

Spanish

```
España enviará a Chipre la fragata ‘Cristóbal Colón’
```

English

```
Spain will send the frigate ‘Cristobal Colon’ to Cyprus
```

---

# 📊 Step 7: Word Analysis

The translated titles are analyzed to detect **frequently repeated words**.

### Example Output

```
Repeated Words

Europe : 2
Spain : 2
Iran : 2
```

---

# ▶️ Step 8: Running the Project

Run the main script:

```bash
python main.py
```

### Expected Output

```
Page Title: EL PAÍS: el periódico global

Article 1
Spanish: ....
Translated: ....

Article 2
Spanish: ....
Translated: ....
```

---

# 🧪 Step 9: Running BrowserStack Tests

Run tests directly:

```bash
python test_browserstack.py
```

Or execute using **PyTest**:

```bash
pytest -v

browserstack-sdk pytest  
```

---

# 📊 Step 10: Viewing Results on BrowserStack

After execution:

1. Login to **BrowserStack**
2. Navigate to **Automate Dashboard**
3. Open **Build Runs**

You will be able to view:

* Test status
* Video recordings
* Logs
* Screenshots

---

# 🌎 Browsers Used

Tests are executed across multiple browsers to ensure compatibility.

* Chrome
* Firefox
* Edge
* Safari
* Chrome (Mac)

---

# 🛠 Technologies Used

| Technology      | Purpose                         |
| --------------- | ------------------------------- |
| Selenium        | Browser automation              |
| BeautifulSoup   | HTML parsing                    |
| Requests        | Fetch webpage content           |
| Deep Translator | Language translation            |
| PyTest          | Test execution                  |
| BrowserStack    | Cross-browser cloud testing     |
| dotenv          | Environment variable management |

---

# 📌 Expected Output Example

```
Page Title: EL PAÍS: el periódico global

Articles

Article 1
Spanish: España enviará a Chipre la fragata ‘Cristóbal Colón’
Translated: Spain will send the frigate ‘Cristobal Colon’ to Cyprus

Article 2
Spanish: El secretario general de la OTAN justifica la ofensiva contra Irán
Translated: NATO Secretary General justifies offensive against Iran
```

---

# 🏁 Conclusion

This project demonstrates a **complete automation pipeline** combining:

* Web scraping
* Language translation
* Text analysis
* Cross-browser testing

It highlights how automation can **collect, process, and analyze real-time news data** while ensuring **cross-browser compatibility using BrowserStack**.
