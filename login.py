from selenium.webdriver.common.by import By
import os 
from selenium.webdriver.support import expected_conditions as EC
import time
from config import BASE_URL
import logging
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def slow_type(element, text, delay=0.12):
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

def test_login(wait):
    try:
        username_val = os.getenv("User_name")
        password_val = os.getenv("Password")

        if not username_val or not password_val:
            raise ValueError("Username or Password env variable is not set!")

        # Add this debug line before slow_type
        logger.info("Username value: %r", username_val)
        logger.info("Password value: %r", password_val)

        # Enter username
        username = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div/div[1]/div/div/form/div/div[2]/div/input")
            )
        )
        username.clear()
        slow_type(username, username_val)

        # Enter password
        password_input = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div/div[1]/div/div/form/div/div[3]/div/input")
            )
        )
        password_input.clear()
        slow_type(password_input, password_val)

        # Click Login button
        login_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div/div[1]/div/div/form/div/button")
            )
        )
        login_btn.click()

        logger.info("✅ Login test passed")

    except Exception as e:
        logger.exception("❌ Login test failed: %s", e)
        raise