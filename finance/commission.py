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
    #Login
    driver.find_element(By.XPATH,"//p[text()='Login']").click()
    email=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='email']")))
    email.send_keys(mail)
    password=driver.find_element(By.ID,"password")
    password.send_keys(pw)
    button=driver.find_element(By.XPATH,"//button[@type='submit']")
    button.click()
    #financeModule
    finance=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Finance']")))
    finance.click()
    #commission
    commission=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,"Commission")))
    commission.click()
    #contrySelection
    country=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[.//span//span[text()='All Countries']]")))
    country.click()
    countryOpt=wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='United Kingdom']")))
    countryOpt.click()
    #uniSelection
    uni=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[.//span[text()='Search universities']]")))
    uni.click()
    uniOpt=wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='Abertay University - Scotland']")))
    uniOpt.click()
    #intakeSelection
    intake=wait.until(EC.visibility_of_element_located((By.XPATH,"//button[.//span//span[text()='All Intakes']]")))
    intake.click()
    intakeOpt=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[.//span[text()='September']]")))
    intakeOpt.click()
    #listApperanace
    uniList=wait.until(EC.visibility_of_element_located((By.XPATH,"//td[.//p[text()='Test']]")))
    #downloadCommission
    download=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[.//span[text()='Download Commission']]")))
    download.click()
    assert "commission" in driver.current_url,"URL does not contain 'commission'"
    print("Test executed successfully")
except AssertionError as ae:
    print(f"Assertion failed:{ae}")
except Exception as e:
    print(f"Test failed: {e}")
finally:
    time.sleep(3)