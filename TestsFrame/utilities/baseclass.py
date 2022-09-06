import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler('logs.log')
        formater = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formater)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def verifylinkpresence(self, text):

        shteti = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Albania")))
        self.driver.find_element(By.LINK_TEXT, text).click()

    def selectoptionbytext(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)


