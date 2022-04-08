import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(3)
searchedProducts = driver.find_elements(By.XPATH, "//div[@class='products']/div")
assert len(searchedProducts) == 3
buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']")
for button in buttons:
    button.click()
driver.find_element(By.CSS_SELECTOR, "a.cart-icon>img").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, "input.promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, "button.promoBtn").click()
print(driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text)


