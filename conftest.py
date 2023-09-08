import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.chrome.service import Service
import time
@pytest.fixture(scope="class")
def setup(request):
 #   Service_obj=Service("C:\\Users\\Primotech\\Downloads\\chromedriver_win32\\chromedriver.exe")
  #  driver=webdriver.Chrome(service=Service_obj)
    driver=webdriver.Chrome()
    request.cls.driver=driver
    driver.maximize_window
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    driver.find_element(By.NAME,"username").send_keys("Admin")
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    time.sleep(3)
    #driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-chevron-right']").click()
    yield
    driver.close