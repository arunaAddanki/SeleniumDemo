import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expectedList = ['Cucumber - 1 kg', 'Raspberry - 1/4 kg', 'Strawberry - 1/4 kg']
actualList = []

service_obj = Service("D:/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
# to return list of elements
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
assert count == 3
#chaining of web elements
for result in results:
    actualList.append(result.find_element(By.XPATH,"h4").text)
    #add items to cart
    result.find_element(By.XPATH,"div/button").click()
#assert expectedList == actualList
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
#handling or create xpath by using text
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(4)
#functional validation
#sum validation
prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum=0
for price in prices:
    sum = sum + int(price.text) # 48 + 160 + 180
print(sum)

totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == totalAmount

#apply coupon code rahulshettyacademy
driver.find_element(By.CSS_SELECTOR,".promocode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
#time.sleep(5)
#explicit wait
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

#grab the value
discountedAmount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert totalAmount > discountedAmount