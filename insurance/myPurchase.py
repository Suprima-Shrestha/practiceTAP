import time
from password import mail,pw
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Edge()
driver.get("https://authorized-partner.netlify.app/")
driver.maximize_window()
wait=WebDriverWait(driver,10)
try:
    #login
    driver.find_element(By.XPATH,"//p[text()='Login']").click()
    email=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='email']")))
    email.send_keys(mail)
    password=driver.find_element(By.ID,"password")
    password.send_keys(pw)
    button=driver.find_element(By.XPATH,"//button[@type='submit']")
    button.click()
    #insuranceModule
    insurance=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Insurance']")))
    insurance.click()
    #myPurchase
    myPurchase=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,"My Purchase")))
    myPurchase.click()
    #search
    search=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search']")))
    search.send_keys("a")
    #statusSelection
    status=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[.//span//span[text()='Select Status']]")))
    status.click()
    statusOpt=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[.//span//span[text()='All']]")))
    statusOpt.click()
    #clearFilter
    clear=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Clear Filters']")))
    clear.click()
    #buuInsuranceButton
    add=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[.//h4[text()='Buy Insurance']]")))
    add.click()
    assert "my-purchase" in driver.current_url, "URL does not contain 'my-purchase'"
    print("Test executed successfully")
except AssertionError as ae:
    print(f"Assertion failed:{ae}")
except Exception as e:
    print(f"Test failed:{e}")
finally:
    time.sleep(3)