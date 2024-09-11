from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/login")
    input_name = driver.find_element(By.ID, "username").send_keys("tomsmith")
    input_pass = driver.find_element(
        By.ID, "password").send_keys("SuperSecretPassword!")
    button = driver.find_element(By.TAG_NAME, "button").click()

except Exception as ex:
    print(ex)
finally:
    driver.quit()
