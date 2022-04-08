import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
radiobuttons = driver.find_elements(By.NAME, "radioButton")
radiobuttons[2].click()
time.sleep(4)
assert radiobuttons[2].is_selected()