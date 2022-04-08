import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
if driver.find_element(By.CSS_SELECTOR, "#displayed-text").is_displayed():
    driver.find_element(By.CSS_SELECTOR, "#displayed-text").send_keys("Hello")
    print(driver.find_element(By.CSS_SELECTOR, "#displayed-text").is_displayed())
driver.find_element(By.CSS_SELECTOR, "#hide-textbox").click()
print(driver.find_element(By.CSS_SELECTOR, "#displayed-text").is_displayed())