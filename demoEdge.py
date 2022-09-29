from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:/Users/User/Documents/Python Scripts/msedgedriver")
driver = webdriver.Edge(service=service_obj)
driver.get("https://www.geeksforgeeks.org/python-programming-language")
print(driver.title)
print(driver.current_url)
driver.maximize_window()
driver.get("https://www.kaggle.com")
driver.minimize_window()
driver.forward()
driver.back()
driver.refresh()
driver.close()