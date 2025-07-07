# 🛒 Ecommerce Automation

This project automates the **Signup** and **Login** workflows of an ecommerce website using **Python**, **Selenium**, and **PyTest**. It simulates real-user behavior, generates unique credentials during signup, saves them to a JSON file, and uses the same credentials to perform login — ensuring a complete end-to-end test.

---

## 🚀 Features

- ✅ Automates user **Signup** flow
- ✅ Saves user credentials to a **JSON file**
- ✅ Uses saved credentials in **Login** flow
- ✅ Uses `webdriver_manager` for easy ChromeDriver management
- ✅ Clean structure using **Page Object Model (POM)** (optional)
- ✅ Configurable via `pytest.ini`

---

## 🛠 Tech Stack

- Python 3.x
- Selenium
- PyTest
- WebDriver Manager
- JSON (for data sharing)
- [pytest-order](https://pypi.org/project/pytest-order/) (optional)

---

## 📁 Project Structure
 ```
ecommerce-automation/
├── tests/
│ ├── test_signup.py # Signup automation (with data save)
│ ├── test_login.py # Login automation (reads data)
│ └── init.py
├── utils/
│ ├── driver_setup.py # get_driver() using Chrome + manager
│ └── init.py
├── conftest.py # Pytest fixture for browser
├── temp_login_data.json # Auto-generated user credentials
├── pytest.ini # Pytest config
├── requirements.txt # Dependencies
├── .gitignore # Ignore venv/.idea/pycache
└── README.md # You're reading it :)



---

## 🧾 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ecommerce-automation.git
cd ecommerce-automation

