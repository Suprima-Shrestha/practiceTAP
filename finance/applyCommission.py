import time
from password import mail,pw
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback
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
    #financeModule
    finance=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Finance']")))
    finance.click()
    #commissionReportApply
    comReport=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,"Commission Report")))
    comReport.click()
    apply=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[.//h4[text()='Apply Commission']]")))
    apply.click()
    appId=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Enter Applicant ID']")))
    appId.send_keys("101")
    name=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Enter Student Name']")))
    name.send_keys("asd")
    """uni=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='']")))
    program=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='']")))"""
    assert "apply-commission" in driver.current_url,"URL does not contain 'apply-commission' "
    print("Test executed successfully")
except AssertionError as ae:
    print(f"Assertion failed:{ae}")
except Exception as e:
    print(f"Test failed due to:{e}")
    traceback.print_exc()
finally:
  time.sleep(3)