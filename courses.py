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
    #coursesModule
    courses=wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Courses")))
    courses.click()
    #search
    search=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search']")))
    search.send_keys("a")
    #country
    country=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[.//span//span[text()='All Countries']]")))
    country.click()
    countryOpt=wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='United Kingdom']")))
    countryOpt.click()
    #discipline
    discipline=wait.until(EC.visibility_of_element_located((By.XPATH,"//button[.//span//span[text()='All Disciplines']]")))
    discipline.click()
    disciplineOpt=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Creative Arts']")))
    disciplineOpt.click()
    #intake
    intake=wait.until(EC.visibility_of_element_located((By.XPATH,"//button[.//span//span[text()='All Intakes']]")))
    intake.click()
    """intakeOpt1=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[.//span[text()='February']]")))
    intakeOpt1.click()
    intake.click()"""
    intakeOpt2=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[.//span[text()='September']]")))
    intakeOpt2.click()
    #programType
    programType=wait.until(EC.visibility_of_element_located((By.XPATH,"//button[.//span//span[text()='All Program Type']]")))
    programType.click()
    programTypeOpt=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[.//span[text()='Advanced Diploma']]")))
    #programTypeOpt=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[.//span[text()='Bachelors']]")))
    programTypeOpt.click()
    #fee
    fee=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[.//span//span[text()='Fee Range']]")))
    fee.click()
    feeMin=wait.until(EC.element_to_be_clickable((By.ID,"min-fee")))
    feeMin.send_keys("arguments[0].value=200;")
    feeMax=wait.until(EC.element_to_be_clickable((By.ID,"max-fee")))
    feeMax.send_keys("arguments[0].value=20000;")
    feeReset=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Reset Fee Range']")))
    feeReset.click()
    #duration
    duration=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[.//span//span[text()='Duration Range']]")))
    duration.click()
    durationMin=wait.until(EC.element_to_be_clickable((By.ID,"min-fee")))
    durationMin.send_keys("arguments[0].value= 3;")
    durationMax=wait.until(EC.element_to_be_clickable((By.ID,"max-fee")))
    durationMax.send_keys("arguments[0].value=10;")
    durationReset=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Reset Duration Range']")))
    durationReset.click()
    #assertion
    assert "courses" in driver.current_url,"URL does not contain 'courses'"
    print("Test executed successfully")
except AssertionError as ae:
    print(f"Assertion failed:{ae}")
except Exception as e:
    print(f"Test failed:{e}")
    traceback.print_exc()
finally:
    time.sleep(3)
