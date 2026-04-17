
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

logger = logging.getLogger(__name__)
# Basic configuration
logging.basicConfig(level=logging.INFO)

# Click on date filter input / button

def test_trash(wait):
    try:
        user = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div/aside/div/div[2]/div[2]")))
        user.click()
        trash = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[3]")))
        trash.click()
        trash_btn = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div[2]/button[2]")))
        trash_btn.click()
    except Exception as e:
        logger.exception("succesfully moved to trash")





