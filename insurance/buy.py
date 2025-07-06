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
    #InsuranceModule
    insurance=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Insurance']")))
    insurance.click()
    #buyInsuranceModule
    buy=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,"Buy OSHC Insurance")))
    buy.click()
    #startDate
    startDate=wait.until(EC.element_to_be_clickable((By.XPATH,"//label[text()='Start Date']/following-sibling::div//div[text()='Pick a date']")))
    startDate.click()
    sYear=driver.find_element(By.XPATH,"//span[@class='ms-1']")
    sYear.click()
    sYearOpt=wait.until(EC.visibility_of_element_located((By.XPATH,"//button[text()='2025']")))
    sYearOpt.click()
    sMonth=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Jun']")))
    sMonth.click()
    sDay=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='15']")))
    sDay.click()
    sDone=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Done']")))
    sDone.click()
    #endDate
    endDate=wait.until(EC.element_to_be_clickable((By.XPATH,"//label[text()='End Date']/following-sibling::div//div[contains(text(),'Pick a date')]")))
    endDate.click()
    eYear=driver.find_element(By.XPATH,"//span[@class='ms-1']")
    eYear.click()
    eYearOpt=wait.until(EC.visibility_of_element_located((By.XPATH,"//button[text()='2035']")))
    eYearOpt.click()
    eMonth=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Jan']")))
    eMonth.click()
    eDay=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='19']")))
    eDay.click()
    eDone=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Done']")))
    eDone.click()
    #no.ofAdult
    adultsNum=wait.until(EC.element_to_be_clickable((By.NAME,"numAdults")))
    adultsNum.send_keys("2")
    #no.ofChild
    child=wait.until(EC.element_to_be_clickable((By.ID,"yes")))
    child.click()
    childNum=wait.until(EC.visibility_of_element_located((By.NAME,"numChildren")))
    childNum.send_keys("2")
    #getPriceButton
    getPrice=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Get Price']")))
    getPrice.click()
    assert "buy-oshc" in driver.current_url,"URL does not contain 'buy-oshc'"
    print("Test executed successfully")
except AssertionError as ae:
    print(f"Assertion failed:{ae}")
except Exception as e:
    print(f"Test failed:{e}")
finally:
    time.sleep(3)