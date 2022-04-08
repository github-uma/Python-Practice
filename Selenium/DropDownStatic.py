from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(0.5)
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
continents = Select(driver.find_element(By.XPATH, "//select[@name='continents']"))
continents.select_by_index(2)
opt = continents.first_selected_option
print("Selected option is: " + opt.text)

continents.select_by_index(1)
opt = continents.first_selected_option
print("Selected option is: " + opt.text)
driver.close()
