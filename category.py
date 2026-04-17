from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

logger = logging.getLogger(__name__)
# Basic configuration
logging.basicConfig(level=logging.INFO)

# Click on date filter input / button

def test_category(wait):
    try:
        Categories = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/aside/div/div[3]/div[2]/ul/a[2]/li/div")))
        Categories.click()
        time.sleep(3)
        create_category = wait.until(EC.presence_of_element_located((By.ID, "add-category")))
        create_category.click()
        title = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/main/div/div/div[2]/div[2]/div/input")))
        title.click()
        slug = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/main/div/div/div[2]/div[3]/div/input")))
        slug.click()
        select = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/main/div/div/div[2]/div[4]/div/div/div/div")))
        select.click()
        description = wait.until(EC.presence_of_element_located((By.XPATH, "  /html/body/div[1]/div/div/main/div/div/div[2]/div[5]/div/div[2]/div[2]/div")))
        description.click()
      
    
    except Exception as e:
         logger.exception("✅")









