from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

logger = logging.getLogger(__name__)
# Basic configuration
logging.basicConfig(level=logging.INFO)

# Click on date filter input / button

def test_post(wait):
  post = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div/aside/div/div[3]/div[2]/ul/a[1]/li/div")))
  post.click()
  add_post = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div/button[2]")))
  add_post.click()
  time.sleep(3)