from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("/Users/User/Documents/Python Scripts/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.msystechnologies.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://www.w3schools.com")
driver.minimize_window()
driver.forward()
driver.back()
driver.refresh()
driver.close()