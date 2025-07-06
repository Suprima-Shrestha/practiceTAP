import time
import traceback
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
    #profileInfo
    profile=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='abc']")))
    profile.click()
    changePassword=wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='Change Password']")))
    changePassword.click()
    oldPassword=wait.until(EC.visibility_of_element_located((By.NAME,"old_password")))
    oldPassword.send_keys(pw)
    newPassword=wait.until(EC.visibility_of_element_located((By.NAME,"password")))
    newPassword.send_keys("Jm0101010$")
    confirmPassword=wait.until(EC.element_to_be_clickable((By.NAME,"confirmPassword")))
    confirmPassword.send_keys("Jm0101010$")
    submitBtn=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
    submitBtn.click()
    assert "change-password" in driver.current_url,"URL does not contain 'change-password'"
    print("Test executed successfully")
except Exception as e:
    print(f"Test failed:{e}")
    traceback.print_exc()
finally:
    time.sleep(3)