import sys
import os
import json
import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.setup import get_driver

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.mark.order(2)
def test_user_login():
    print("🔐 Login Test Running")
    driver = None

    try:
        # ✅ Step 1: Load credentials
        with open("temp_login_data.json", "r") as f:
            data = json.load(f)
            email = data["email"]
            password = data["password"]

        # ✅ Step 2: Setup driver
        driver = get_driver()
        wait = WebDriverWait(driver, 20)

        print("Opening automationexercise.com")
        driver.get("https://automationexercise.com")

        print("Clicking Signup/Login")
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login"))).click()

        print("Filling login form")
        wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(email)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()

        print("Waiting for success message")
        success_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "//li/a[contains(text(),'Logged in as')]"))
        )
        success_text = success_element.text

        assert "Logged in as" in success_text, f"❌ Login failed, got: {success_text}"
        print("✅ Login successful:", success_text)

    except Exception as e:
        print(f"❌ Login test failed: {e}")
        raise

    finally:
        if driver:
            time.sleep(2)
            driver.quit()
            # ✅ Delete the temp login file after test
        if os.path.exists("temp_login_data.json"):
            os.remove("temp_login_data.json")
            print("🗑️ temp_login_data.json deleted")