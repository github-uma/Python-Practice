import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
#driver = webdriver.Ie(service=Service(IEDriverManager().install()))
wait = WebDriverWait(driver, 30)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/shop")
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for product in products:
    if product.find_element(By.XPATH, "div/h4/a").text == "Blackberry":
        product.find_element(By.XPATH, "div[2] / button").click()
        break
driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "input.form-control").clear()
driver.find_element(By.CSS_SELECTOR, "input.form-control").send_keys("2")
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success").click()
driver.find_element(By.ID, "country").send_keys("Ind")
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
agreed = driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']")
if agreed.get_attribute("checked") != "true":
    agreed.click()
# assert agreed.is_selected()
# driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()
successMsg = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print(successMsg)
assert "Success! Thank you!" in successMsg
driver.get_screenshot_as_file("screen.png")
