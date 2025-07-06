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
    #staffModule
    staff=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Staff']")))
    staff.click()
    #manageStaff
    manageStaff=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,"Manage Staff")))
    manageStaff.click()
    #search
    search=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search']")))
    search.send_keys("a")
    #clearFilter
    clear=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Clear Filters']")))
    clear.click()
    #activeStatus
    active=wait.until(EC.element_to_be_clickable((By.XPATH, "//tr[td[li[text()='1']]]//button[@role='switch']")))
    active.click()
    #editStaff
    editBtn=wait.until(EC.element_to_be_clickable((By.XPATH, "//tr[td[li[text()='1']]]//button[.//span[text()='Open menu']]")))
    editBtn.click()
    edit=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,"Edit")))
    edit.click()
    editName=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Enter Full Name']")))
    editName.clear()
    driver.execute_script("arguments[0].value='test';",editName)
    """add=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[.//span[text()='Add new Staff']]")))
    add.click()"""
    assert "staff" in driver.current_url,"URL does not contain 'staff'"
    print("Test executed successfully")
except AssertionError as ae:
    print(f"Assertion failed:{ae}")
except Exception as e:
    print(f"Test failed:{e}")
finally:
    time.sleep(3)