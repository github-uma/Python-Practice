import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

validateText = "Option3"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# identify edit box and send input
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(validateText)
# identify Alert button and then click
driver.find_element(By.ID, "alertbtn").click()
# create alert object and switch to it
alert = driver.switch_to.alert
time.sleep(3)
# get the alert text and validate with assertion
alertText = alert.text
assert validateText in alertText
#to accept alert
alert.accept()