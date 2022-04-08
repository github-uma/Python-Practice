import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(2)
searchedProducts = driver.find_elements(By.XPATH, "//div[@class='products']/div")
assert len(searchedProducts) == 3
buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
addedList = []
productList = []
for button in buttons:
    addedList.append(button.find_element(By.XPATH, "parent::div/parent::div//h4").text)
    button.click()
print(addedList)
originalamount = driver.find_element(By.XPATH, "//tbody/tr[2]/td[3]/strong").text
print(originalamount)
driver.find_element(By.CSS_SELECTOR, "a.cart-icon>img").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
listedproducts = driver.find_elements(By.CSS_SELECTOR, "p.product-name")
for product in listedproducts:
    productList.append(product.text)
print(productList)
assert addedList == productList
driver.find_element(By.CSS_SELECTOR, "input.promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, "button.promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
afterAmount = driver.find_element(By.CSS_SELECTOR, "span.discountAmt").text
print(afterAmount)
print(driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text)
assert float(originalamount)*0.9 == float(afterAmount)
