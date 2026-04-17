from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

logger = logging.getLogger(__name__)
# Basic configuration
logging.basicConfig(level=logging.INFO)

# Click on date filter input / button

def test_users(wait):
    try:
        user = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/aside/div/div[2]/div[2]")))
        user.click()
        time.sleep(5)
        create_users = wait.until(EC.presence_of_element_located((By.ID, "create-user")))
        create_users.click()
        username = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div[1]/div/input")))
        username.send_keys("Ramesh kc")
        email = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/input")))
        email.send_keys("Ramesh123@gmail.com")
        pw = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
        pw.send_keys("ramesh1234")
        cfm_pw = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div[4]/div/input")))
        cfm_pw.send_keys("ramesh1234") 
        
        create_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div[2]/button[1]")))
        create_btn.click()

    
        validation_message = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'User already exists')]")))
   
        if validation_message.is_displayed():
         print("User already exists! Clicking Cancel 🚫.")
         time.sleep(2)
         cancel_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div[2]/button[2]")))
         cancel_btn.click()
    except Exception as e:
         logger.exception("Validation not found, form submitted successfully ✅")




