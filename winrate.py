from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

phantom_extension_dir = r"C:\Users\Danny\AppData\Local\Google\Chrome\User Data\Default\Extensions\bfnaelmomeimhlpmgjnjophhpkkoljpa\24.22.1_0"  # Adjust this path as needed

driver = Driver(uc=True, extension_dir=phantom_extension_dir)

driver.get("chrome-extension://bfnaelmomeimhlpmgjnjophhpkkoljpa/onboarding.html")

#click create wallet button
create_wallet_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/main/div[2]/div/div[2]/button[1]"))
)
driver.execute_script("arguments[0].scrollIntoView(true);", create_wallet_button)
create_wallet_button.click()

time.sleep(0.5)

#inputs password
password_input = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@data-testid='onboarding-form-password-input']"))
)
password = "11111111" 
password_input.send_keys(password)

time.sleep(0.5)

confirm_password_input = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@data-testid='onboarding-form-confirm-password-input']"))
)
confirm_password_input.send_keys(password)

time.sleep(0.5)

button = driver.find_element(
        "xpath", "//*[@id='root']/main/div[2]/form/div[2]/span/input"
)

driver.execute_script("arguments[0].scrollIntoView(true);", button)

button.click()

time.sleep(0.5)

button = driver.find_element(
        "xpath", "//*[@id='root']/main/div[2]/form/button"
)

driver.execute_script("arguments[0].scrollIntoView(true);", button)

button.click()

time.sleep(0.5)

button = driver.find_element(
        "xpath", "//*[@id='root']/main/div[2]/form/div[2]/span/input"
)

driver.execute_script("arguments[0].scrollIntoView(true);", button)

button.click()

time.sleep(0.5)

button = driver.find_element(
        "xpath", "//*[@id='root']/main/div[2]/form/button"
)

driver.execute_script("arguments[0].scrollIntoView(true);", button)

button.click()


time.sleep(1)

url = "https://app.cielo.finance/profile/AjUdVos5oc7NpK7ubYm7KvxpyNMp7Ts19SMAn51aXg6f"
driver.uc_open_with_reconnect(url, reconnect_time=30)

try:
    connect_button = driver.find_element("xpath", "/html/body/main/div/div/button")
    driver.execute_script("arguments[0].scrollIntoView(true);", connect_button)
    connect_button.click()
    print("Clicked 'Connect' button.")
except Exception as e:
    print(f"Error while clicking 'Connect' button: {e}")

try:
    get_started_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[p[text()='Get Started']]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", get_started_button)
    get_started_button.click()
    print("Clicked 'Get Started' button.")
except Exception as e:
    print(f"Error: {e}")


#manually connect to phantom wallet
time.sleep(3)

windows = driver.window_handles
driver.switch_to.window(windows[-1])  #switch to the last opened window

time.sleep(3)



driver.execute_script("arguments[0].scrollIntoView(true);", button)

button.click()

try:
    button = driver.find_element(
        "xpath", "//*[@id='root']/div/div[1]/div/div[2]/div/button[2]"
    )
    password_input_popup = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@type='password']"))
    )
    password_input_popup.send_keys(password)
    print("Entered password into Phantom Wallet.")
    
    submit_button = driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/div[2]/div/button")
    submit_button.click()
except Exception as e:
    print(f"Error while entering password in the Phantom Wallet popup: {e}")
time.sleep(15)

driver.quit()
