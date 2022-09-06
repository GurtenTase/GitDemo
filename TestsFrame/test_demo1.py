from selenium.webdriver.common.by import By
from TestsFrame.pageobjects.homepage import HomePage
from TestsFrame.utilities.baseclass import BaseClass


class Test1(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopitems()
        celularet = checkoutpage.getcelularet()
        log.info("Kap celularet")
        i = -1
        for celulari in celularet:
            i = i+1
            tipi = celulari.text
            log.info(tipi)
            if tipi == "Samsung Note 8":
                checkoutpage.getblerje()[i].click()
                break
        checkoutpage.getcheckout().click()
        confirmationpage = checkoutpage.getconfcheckout()
        log.info("Entering Country name al")
        confirmationpage.getfindcountry().send_keys("al")
        self.verifylinkpresence("Albania")
        confirmationpage.getselcoutry().click()
        self.driver.find_element(By.CSS_SELECTOR, "button[class*='btn-info']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()
        msg = self.driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
        log.info(msg)
        assert "Success" in msg
