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
    #appHistoryModule
    appHis=wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Application History")))
    appHis.click()
    search=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search']")))
    search.send_keys("a")
    show=driver.find_element(By.XPATH,"//button[.//span//span[text()='5']]")
    show.click()
    showOpt=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='50']")))
    showOpt.click()
    #country
    country=driver.find_element(By.XPATH,"//button[.//span//span[text()='All Countries']]")
    country.click()
    countryOpt=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='United Kingdom']")))
    countryOpt.click()
    #range
    range=driver.find_element(By.XPATH,"//button[.//span//span[text()='Select Range']]")
    range.click()
    rangeOpt=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Last 14 Days']")))
    rangeOpt.click()
    #statusd
    status=driver.find_element(By.XPATH,"//button/span[text()='All Status']")
    status.click()
    statusOpt=driver.find_element(By.XPATH,"//div[text()='Visa']")
    statusOpt.click()
    statusSelect=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[text()='Granted']")))
    #statusSelect=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[text()='Pending']")))
    statusSelect.click()
    clear=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Clear Filters']")))
    assert "application-history" in driver.current_url,"URL does not contain 'application-history'"
    print("Test executed successfully")
except AssertionError as ae:
    print(f"Assertion failed:{ae}")
except Exception as e:
    print(f"Test failed:{e}")
    traceback.print_exc()
finally:
    time.sleep(3)
