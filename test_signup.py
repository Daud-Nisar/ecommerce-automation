import sys
import os
import json
import time
import pytest
from selenium.webdriver.common.by import By
from utils.setup import get_driver

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.mark.order(1)
def test_user_registration():
    print("🔥 Signup Test Running")
    driver = None
    try:
        driver = get_driver()
        driver.get("https://automationexercise.com")
        driver.find_element(By.LINK_TEXT, "Signup / Login").click()

        email = "Adam" + str(int(time.time())) + "@mail.com"
        password = "SecurePass123"

        # Save email & password BEFORE registration
        with open("temp_login_data.json", "w") as f:
            json.dump({"email": email, "password": password}, f)

        driver.find_element(By.NAME, "name").send_keys("Adam Tester")
        driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(email)
        driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

        driver.find_element(By.ID, "id_gender1").click()
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "days").send_keys("10")
        driver.find_element(By.ID, "months").send_keys("October")
        driver.find_element(By.ID, "years").send_keys("1999")
        driver.find_element(By.ID, "first_name").send_keys("Adam")
        driver.find_element(By.ID, "last_name").send_keys("Scott")
        driver.find_element(By.ID, "address1").send_keys("123 Automation Street")
        driver.find_element(By.ID, "state").send_keys("Texas")
        driver.find_element(By.ID, "city").send_keys("Dallas")
        driver.find_element(By.ID, "zipcode").send_keys("48000")
        driver.find_element(By.ID, "mobile_number").send_keys("(409) 643-5902")
        driver.find_element(By.XPATH, "//button[@data-qa='create-account']").click()

        success_text = driver.find_element(By.XPATH, "//h2[@data-qa='account-created']").text
        assert "ACCOUNT CREATED!" in success_text, f"Expected 'ACCOUNT CREATED!' but got: {success_text}"
        print("✅ Signup successful")

    except Exception as e:
        print(f"❌ Signup test failed: {e}")
        raise

    finally:
        if driver:
            time.sleep(3)
            driver.quit()
