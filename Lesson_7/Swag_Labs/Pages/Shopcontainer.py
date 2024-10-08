from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ShopContainer:
    def __init__(self, browser):
        self.browser = browser

    # Кликаем на кнопку checkout
    def checkout(self):
        self.check = (By.ID, "checkout")
        self.browser.find_element(*self.check).click()
    
    # Вводим данные получателя
    def info(self):
        self.first_name = (By.ID, "first-name")
        self.browser.find_element(*self.first_name).send_keys("Elvira")
        self.last_name = (By.ID, "last-name")
        self.browser.find_element(*self.last_name).send_keys("Loskutova")
        self.postcode = (By.ID, "postal-code")
        self.browser.find_element(*self.postcode).send_keys("601500")
        self.continue_button = (By.ID, "continue")
        self.browser.find_element(*self.continue_button).click()
    
    # Получаем итоговую сумму заказа и выводим ее в нужном формате
    def price(self):
        return self.browser.find_element(By.CSS_SELECTOR, '[data-test="total-label"]').text