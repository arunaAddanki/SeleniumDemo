from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#chrome driver
service_obj = Service("C:/Users/User/Documents/Python Scripts/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.msystechnologies.com")
print(driver.title)
print(driver.current_url)