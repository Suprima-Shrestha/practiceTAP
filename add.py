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
    #addNewApllicationModule
    addNew=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,"Add New Application")))
    addNew.click()
    name=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Enter Your Full Name']")))
    name.send_keys("xyz")
    date=driver.find_element(By.XPATH,"//div[text()='Pick a date']")
    date.click()
    year=driver.find_element(By.XPATH,"//span[@class='ms-1']")
    year.click()
    driver.find_element(By.XPATH,"//button[text()='2003']").click()
    month=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Jan']")))
    month.click()
    day=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='11']")))
    day.click()
    done=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Done']")))
    done.click()
    email=driver.find_element(By.XPATH,"//input[@placeholder='Enter Your Email Address']")
    email.send_keys("xyc@gmail.com")
    phone=driver.find_element(By.XPATH,"//input[@placeholder='00-00000000']")
    phone.send_keys("9812345678")
    nextBtn1=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Next']")))
    nextBtn1.click()
    country=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[.//span//span[text()='Select a country']]")))
    country.click()
    countryOpt=wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='United Kingdom']")))
    countryOpt.click()
    degree=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[.//span//span[text()='Select degree type']]")))
    degree.click()
    degreeOpt=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Bachelors']")))
    degreeOpt.click()
    uni=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[.//span//span[text()='Select a University']]")))
    uni.click()
    """uniSearch=wait.until(EC.visibility_of_element_located((By.XPATH,"//div//input[@placeholder='Search...']")))
    uniSearch.send_keys("b")"""
    uniOpt=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Abertay University - Scotland']")))
    uniOpt.click()
    course=wait.until(EC.visibility_of_element_located((By.XPATH,"//button[.//span//span[text()='Select a Course']]")))
    course.click()
    """courseSearch=wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search...']")))
    courseSearch.send_keys("p")"""
    courseOpt=wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='Sports Development and Coaching BSc (Hons)']")))
    courseOpt.click()
    intake=wait.until(EC.visibility_of_element_located((By.XPATH,"//button[.//span//span[text()='Select intake']]")))
    intake.click()
    intakeOpt=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='September']")))
    intakeOpt.click()
    location=wait.until(EC.element_to_be_clickable((By.XPATH,"//label[text()='Onshore']")))
    #location=wait.until(EC.element_to_be_clickable((By.XPATH,"//label[text()='Offshore']")))
    location.click()
    nextBtn2=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Next']")))
    nextBtn2.click()
    """nextBtn2=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Previous']")))
    nextBtn2.click()"""
    file=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@type='file']")))
    file.send_keys(r"C:\Users\asus\OneDrive\Pictures\b4.jpg")
    submit=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
    submit.click()
    """pre=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Previous']")))
    pre.click()"""
    assert "application-form" in driver.current_url,"URL does not contain 'application-form'"
    print("Test executed successfully")
except AssertionError as ae:
    print(f"Assertion failed:{ae}")
except Exception as e:
    print(f"Test failed:{e}")
finally:
    time.sleep(10)