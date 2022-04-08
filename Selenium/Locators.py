import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.google.com/")
searchTextBox = driver.find_element(By.NAME, "q")
searchTextBox.send_keys("selenium")
time.sleep(3)
print(driver.title)
searchTextBox.submit()
print(driver.title)
driver.close()