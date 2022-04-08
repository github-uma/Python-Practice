from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# get method to hit URL on browser
driver.get("https://rahulshettyacademy.com/angularpractice/")
# identify element with css locator and then send input
driver.find_element(By.CSS_SELECTOR, "[name='name']").send_keys("Rahul")
# identify element with name locator and then send input
driver.find_element(By.NAME, "email").send_keys("Shetty")
# identify checkbox with id attribute and then select
driver.find_element(By.ID, "exampleCheck1").click()
# select class provide the methods to handle the options in dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
# identify element with xpath and then click
driver.find_element(By.XPATH, "//input[@type='submit']").click()
# identify element with class name and then get its text
print(driver.find_element(By.CLASS_NAME, "alert-success").text)
