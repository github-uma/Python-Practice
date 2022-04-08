from timeit import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# webdriver.firefox(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/dropdownsPractise/")
# identify element with id locator and then send input
driver.find_element(By.ID, "autosuggest").send_keys("ind")
# to pause execution
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
#countries = driver.find_elements(By.CSS_SELECTOR, "a[class='ui-corner-all']")
# iterate over the list and scan the desired option
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
