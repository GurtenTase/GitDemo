from selenium.webdriver.common.by import By
from TestsFrame.pageobjects.checkoutpage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, 'name')
    mail = (By.NAME, 'email')
    ID = (By.ID, 'exampleInputPassword1')
    checkbox = (By.XPATH, "//input[@id='exampleCheck1']")
    submit = (By.CSS_SELECTOR, "input[type='submit']")
    success = (By.CSS_SELECTOR, "div[class*='alert-success']")
    gender = (By.ID, "exampleFormControlSelect1")

    def shopitems(self):
        self.driver.find_element(*HomePage.shop).click()
        return CheckOutPage(self.driver)

    def getname(self, text):
        return self.driver.find_element(*HomePage.name).send_keys(text)

    def getmail(self,text):
        return self.driver.find_element(*HomePage.mail).send_keys(text)

    def getid(self,text):
        return self.driver.find_element(*HomePage.ID).send_keys(text)

    def getcheckbox(self):
        return self.driver.find_element(*HomePage.checkbox).click()

    def getsubmit(self):
        return self.driver.find_element(*HomePage.submit).click()

    def getsuccess(self):
        return self.driver.find_element(*HomePage.success)

    def getgender(self):
        return self.driver.find_element(*HomePage.gender)
