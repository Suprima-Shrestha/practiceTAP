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
    #noticesModule
    notices=wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Notices")))
    notices.click()
    next=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Next ']")))
    next.click()
    assert "notices" in driver.current_url,"URL does not contain 'notices'"
    print("Test executed successfully")
except AssertionError as ae:
    print(f"Assertion failed:{ae}")
except Exception as e:
    print(f"Test failed:{e}")
finally:
    time.sleep(3)
