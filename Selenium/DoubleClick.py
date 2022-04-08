import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)
driver.get("https://chercher.tech/practice/popups")
actions = ActionChains(driver)
actions.context_click(driver.find_element(By.CSS_SELECTOR, "#double-click")).perform()# for right click
actions.double_click(driver.find_element(By.CSS_SELECTOR, "#double-click")).perform()
wait.until(expected_conditions.alert_is_present())
alert = driver.switch_to.alert
assert alert.text == "You double clicked me!!!, You got to be kidding me"
alert.accept()
