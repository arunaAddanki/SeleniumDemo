from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:/Users/User/Documents/Python Scripts/geckodriver")
driver = webdriver.Firefox(service=service_obj)
driver.get("https://www.hackerrank.com")
driver.maximize_window()
print(driver.current_url)
print(driver.title)
driver.get("https://www.codechef.com")
driver.minimize_window()
driver.forward()
driver.back()
driver.refresh()
driver.close()