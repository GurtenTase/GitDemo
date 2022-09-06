from selenium.webdriver.common.by import By

from TestsFrame.pageobjects.confirmationpage import ConfirmationPage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    celularet = (By.CSS_SELECTOR, "h4[class=card-title]")
    blerje = (By.CSS_SELECTOR, "button[class='btn btn-info']")
    checkout = (By.CSS_SELECTOR, "a[class*='btn']")
    confcheckout = (By.CLASS_NAME, "btn-success")

    def getcelularet(self):
        return self.driver.find_elements(*CheckOutPage.celularet)

    def getblerje(self):
        return self.driver.find_elements(*CheckOutPage.blerje)

    def getcheckout(self):
        return self.driver.find_element(*CheckOutPage.checkout)
    def getconfcheckout(self):
        self.driver.find_element(*CheckOutPage.confcheckout).click()
        return ConfirmationPage(self.driver)