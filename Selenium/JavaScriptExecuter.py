import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--start-maximize")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "name").send_keys("Hello")
print(driver.find_element(By.NAME, "name").text)
print(driver.find_element(By.NAME, "name").get_attribute("value"))
print(driver.execute_script("return document.getElementsByName('name')[0].value"))
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(5)

shopButton = driver.find_element(By.CSS_SELECTOR, "a[href='/angularpractice/shop']")
driver.execute_script("arguments[0].click()", shopButton)
