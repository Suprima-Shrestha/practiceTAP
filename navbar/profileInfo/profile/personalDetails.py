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
    #profileInfo
    profileInfo=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='abc']")))
    profileInfo.click()
    profile=wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Profile")))
    profile.click()
    #personalDetails
    editPersonalDetails=wait.until(EC.element_to_be_clickable((By.XPATH,"//h3[text()='Personal Information']/following-sibling::button[text()='Edit']")))
    editPersonalDetails.click()
    firstName=wait.until(EC.element_to_be_clickable((By.NAME,"firstName")))
    firstName.clear()
    driver.execute_script("arguments[0].value='pqrs';",firstName)
    lastName=wait.until(EC.element_to_be_clickable((By.NAME,"lastName")))
    lastName.clear()
    driver.execute_script("arguments[0].value='pqrs';",lastName)
    phone=wait.until(EC.element_to_be_clickable((By.NAME,"phoneNumber")))
    phone.clear()
    driver.execute_script("arguments[0].value=9801312345;",phone)
    save=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Save']")))
    save.click()
    #editAgencyDetails
    editAgency=wait.until(EC.element_to_be_clickable((By.XPATH,"//h3[text()='Agency Details']/following-sibling::button[text()='Edit']")))
    editAgency.click()
    agencyName=wait.until(EC.element_to_be_clickable((By.NAME,"agency_name")))
    agencyName.clear()
    driver.execute_script("arguments[0].value='PQR';",agencyName)
    role=wait.until(EC.element_to_be_clickable((By.NAME,"role_in_agency")))
    role.clear()
    driver.execute_script("arguments[0].value='QA';",role)
    assert ""
except AssertionError as ae:
    print(f"Assertion failed:{ae}")
except Exception as e:
    print(f"Test failed:{e}")
finally:
    time.sleep(3)