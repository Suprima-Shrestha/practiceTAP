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
    #notification
    notify=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[.//div[@class='relative']]")))
    notify.click()
    #viewAll
    viewAll=wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"View All")))
    viewAll.click()
    notificationList=wait.until(EC.visibility_of_element_located((By.XPATH,"//h2[text()='All Notifications']")))
    #assert Code
    assert notificationList.is_displayed(),"Notifications are not displayed"
    assert "notifications" in driver.current_url, "URL does not contain 'notifications'"
    print("Test passed successfully")
except AssertionError as ae:
    print(f"assertion failed: {ae}")
except Exception as e:
    print(f"test failed due to:{e}")
finally:
    time.sleep(3)