import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


validateText = "Option3"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
try:
    assert driver.title == "abc"
except Exception as e:
    print(e)
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    driver.get_screenshot_as_file('//screenshots/'+'screenshot-%s.png' % now)
