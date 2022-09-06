from selenium.webdriver.common.by import By


class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver

    findcountry = (By.ID, "country")
    selcountry = (By.LINK_TEXT,"term & Conditions" )
    # self.driver.find_element(By.CSS_SELECTOR, "button[class*='btn-info']").click()


    def getfindcountry(self):
        return self.driver.find_element(*ConfirmationPage.findcountry)

    def getselcoutry(self):
        return self.driver.find_element(*ConfirmationPage.selcountry)
