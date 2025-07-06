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
    #staffModule
    staff=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Staff']")))
    staff.click()
    #additionStaff
    addStaff=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,"Add Staff")))
    addStaff.click()
    #nameField
    name=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Enter Full Name']")))
    name.send_keys("pqrs")
    #emailField
    email=driver.find_element(By.XPATH,"//input[@placeholder='Enter Your Email Address']")
    email.send_keys("pqrs@gmail.com")
    #phoneField
    phone=driver.find_element(By.XPATH,"//input[@placeholder='00-00000000']")
    phone.send_keys("9812345677")
    #passwordField
    password=wait.until(EC.visibility_of_element_located((By.NAME,"password")))
    password.send_keys("Abc12345!")
    confirmPass=wait.until(EC.element_to_be_clickable((By.NAME,"confirmPassword")))
    confirmPass.send_keys("Abc12345!")
    #addStaff
    add=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Add Staff']")))
    add.click()
    assert "add" in driver.current_url,"URL does not contain 'add'"
    print("Test executed successfully")
except AssertionError as ae:
    print(f"Assertion failed:{ae}")
except Exception as e:
    print(f"Test failed:{e}")
finally:
    time.sleep(3)