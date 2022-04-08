from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
mouseHover = driver.find_element(By.CSS_SELECTOR, "#mousehover")
action = ActionChains(driver)
action.move_to_element(mouseHover).perform()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "a[href='#top']")))
items=driver.find_elements(By.CSS_SELECTOR, "div.mouse-hover-content a")
for item in items:
    print(item.text)