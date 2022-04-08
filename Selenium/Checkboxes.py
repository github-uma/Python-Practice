import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# identify generalized xpath for checkboxes
chkbxs = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
# iterate over the list and select them
for c in chkbxs:
    c.click()
    print(c.get_attribute("value"))
    # validate if checkbox is selected
    assert c.is_selected()
time.sleep(3)