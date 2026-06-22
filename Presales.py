import chromedriver_autoinstaller
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import os
import time
import pyautogui
import keyboard


# Setup ChromeDriver
custom_path = os.path.join(os.getcwd(), "chromedriver")
os.makedirs(custom_path, exist_ok=True)
chromedriver_autoinstaller.install(path=custom_path)

# Load data
data = pd.read_excel("data.xlsx", dtype={'incoming_date': str, 'delivery_last_date': str})
total_rows = len(data)

# Start WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)
driver.get("https://login.microsoftonline.com/0d2c1116-d7c2-4380-b446-78e71d8f2465/oauth2/v2.0/authorize?response_type=code&client_id=9fb6f30e-8ae3-42e5-9e85-491fe68ab9b6&redirect_uri=https%3A%2F%2Ferp.betopiagroup.com%2Fauth_oauth%2Fsignin&scope=openid+profile+email+offline_access+User.Read&state=%7B%22d%22%3A+%22betopia_live%22%2C+%22p%22%3A+7%2C+%22r%22%3A+%22https%253A%252F%252Ferp.betopiagroup.com%252Fweb%22%7D&nonce=5TS_ReKXohjTW2iVIzinzL5ivTzQTR_8eY_4xhyHcQE&code_challenge=-e9vNrXw4IFxvr1B3WJBthGS3aSviv6smTcS-3kjZvc&code_challenge_method=S256&sso_reload=true")
time.sleep(3)
# Login
driver.find_element(By.NAME, "loginfmt").send_keys("rakibul@smtech24.com")
driver.find_element(By.ID, "idSIButton9").click()
time.sleep(3)
driver.find_element(By.NAME, "passwd").send_keys("Rakib863580@")
driver.find_element(By.ID, "idSIButton9").click()
time.sleep(3)
next_btn_0 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "idSubmit_ProofUp_Redirect"))
)

next_btn_0.click()

skip_btn = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Skip setup']")
    )
)

skip_btn.click()

no_btn = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "idBtn_Back"))
)
no_btn.click()
time.sleep(3)
# Log file setup
with open("log_results.txt", "a") as log_file:
    remaining_rows = total_rows

    for index, row in data.iterrows():
        print(f"Remaining: {remaining_rows}")

        driver.get("https://erp.betopiagroup.com/odoo/action-4341")
        time.sleep(2)

        # Click New Button
        driver.find_element(By.NAME, "action_open_new_incoming_query_popup").click()
        time.sleep(1)

        # Source
        source_field = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, "incoming_query_method_id_0"))
        )

        source_field.click()
        source_field.clear()
        source_field.send_keys(str(row["Source"]))
        source_field.send_keys(Keys.ENTER)

        # Platform Source
        driver.find_element(By.ID, "platform_source_id_0").send_keys(str(row["Platform Source"]))
        driver.find_element(By.ID, "platform_source_id_0").send_keys(Keys.ENTER)
        time.sleep(1)

        # Profile
        driver.find_element(By.ID, "profile_id_0").send_keys(str(row["Profile"]))
        driver.find_element(By.ID, "profile_id_0").send_keys(Keys.ENTER)
        #time.sleep(1)

        # Client 
        driver.find_element(By.ID, "partner_id_0").send_keys(str(row["Client"]))
        driver.find_element(By.ID, "partner_id_0").send_keys(Keys.ENTER)
        time.sleep(1)

        # Project Category
        driver.find_element(By.ID, "project_category_id_0").send_keys(str(row["Project Category"]))
        driver.find_element(By.ID, "project_category_id_0").send_keys(Keys.ENTER)
        #time.sleep(1)

        # Current Status
        driver.find_element(By.ID, "lead_status_id_0").send_keys(str(row["Current Status"]))
        driver.find_element(By.ID, "lead_status_id_0").send_keys(Keys.ENTER)
        #time.sleep(1)

        # Quoted Amount
        driver.find_element(By.ID, "amount_0").clear()
        driver.find_element(By.ID, "amount_0").send_keys(str(row["Quoted Amount"]))
        driver.find_element(By.ID, "amount_0").send_keys(Keys.ENTER)
        # time.sleep(1)

        # Current Condition
        driver.find_element(By.ID, "current_condition_id_0").send_keys(str(row["Current Condition"]))
        driver.find_element(By.ID, "current_condition_id_0").send_keys(Keys.ENTER)

        # Quotation URL
        driver.find_element(By.ID, "job_link_0").send_keys(str(row["Quotation URL"]))
        driver.find_element(By.ID, "job_link_0").send_keys(Keys.ENTER)
        #time.sleep(1)
        
        # Inbox URL
        driver.find_element(By.ID, "inbox_url_0").send_keys(str(row["Inbox URL"]))
        driver.find_element(By.ID, "inbox_url_0").send_keys(Keys.ENTER)
       # time.sleep(1)

        # Sent Offer
        driver.find_element(By.ID, "sent_offer_note_0").send_keys(str(row["Sent Offer"]))
        driver.find_element(By.ID, "sent_offer_note_0").send_keys(Keys.ENTER)
        #time.sleep(1)

        save_btn = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[contains(@class,'o_form_button_save')]"
            ))
        )
        #time.sleep(15)
        save_btn.click()
        
        remaining_rows -= 1
        time.sleep(1)
