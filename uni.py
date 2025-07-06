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
    #UniversitiesModule
    uni=wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Universities")))
    uni.click()
    #search
    search=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Search']")))
    search.send_keys("a")
    #country
    country=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[.//span//span[text()='All Countries']]")))
    country.click()
    countryOpt=wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='United Kingdom']")))
    countryOpt.click()
    #detail
    details=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[.//a[@href='/admin/universities/14']]")))
    details.click()
    apply=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[.//span[text()='Apply Now']]")))
    apply.click()
    assert "universities" in driver.current_url,"URL does not contain 'universities'"
    print("Test executed successfully")
except AssertionError as ae:
    print(f"Assertion failed:{ae}")
except Exception as e:
    print(f"Test failed:{e}")
finally:
    time.sleep(3)