from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from config import BASE_URL
from login import test_login
from trash import test_trash
from users.users import test_users
from users.post import test_post
from users.edit import test_edit
from category import test_category
import time
import logging
from dotenv import load_dotenv

load_dotenv()

# Basic configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
if __name__ == '__main__':
    driver = webdriver.Firefox()  # Create instance
    driver.maximize_window()
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 20)
    try:
        test_login(wait)
        test_users(wait)
        test_trash(wait)
        test_edit(wait)
        test_category(wait)
        test_post(wait)

    except Exception as e:
        logger.exception(f"Unexpected error occured : {e}")
    finally:
        time.sleep(5)
        if 'driver' in locals():
            try:
                driver.quit()
            except Exception:
                logger.exception("Error quitting WebDriver")