from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

logger = logging.getLogger(__name__)
# Basic configuration
logging.basicConfig(level=logging.INFO)

# Click on date filter input / button

def test_edit(wait):
    try:

        dot = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/main/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[6]/button")))
        dot.click()
        # view_profile = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]")))
        # view_profile .click()
        edit_btn =  wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[1]")))
        edit_btn.click()
        full_name  = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div/div/main/div/div/div[2]/div[1]/div/input")))
        full_name.send_keys("Ramesh singh lol")
        role = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div/div/main/div/div/div[2]/div[6]/div/div/div[2]")))
        role.click()
        time.sleep(3)
        option = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div/div/main/div/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]")))
        option.click()
       
        reddit  = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div/main/div/div/div[2]/div[7]/div/input")))
        reddit.send_keys("https")
        twitter  = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div/main/div/div/div[2]/div[7]/div/input")))
        twitter.send_keys("")
        Linkedin  = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div/main/div/div/div[2]/div[7]/div/input")))
        Linkedin.send_keys("")
        create_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div/main/div/div/div[1]/div/button")))
        create_btn .click()

        time.sleep(5)



    except Exception as e:
         logger.exception("user creation failed")
         raise e