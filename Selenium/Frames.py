import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.CSS_SELECTOR, "#tinymce").clear()
driver.find_element(By.CSS_SELECTOR, "#tinymce").send_keys("adding text into iframe")
time.sleep(5)
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h3").text)