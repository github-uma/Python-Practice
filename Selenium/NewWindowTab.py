import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div.example")))
parentWindow = driver.window_handles[0]
childWindow: str = driver.window_handles[1]
driver.switch_to.window(childWindow)
actualText = driver.find_element(By.CSS_SELECTOR, "div.example").text
print(actualText)
assert actualText == "New Window"
print("child window title "+driver.title)
driver.switch_to.window(parentWindow)
print("parent window title "+driver.title)

