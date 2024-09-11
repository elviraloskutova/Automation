from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/inputs")
    input_field = driver.find_element(By.TAG_NAME, "input")
    input_field.send_keys("1000")
    input_field.clear()
    input_field.send_keys("999")

except Exception as ex:
    print(ex)
finally:
    driver.quit()
