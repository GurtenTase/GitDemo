import pytest
from TestsFrame.pageobjects.homepage import HomePage
from TestsFrame.testdata.HomepageData import HomepageData
from TestsFrame.utilities.baseclass import BaseClass



class TestHomepage(BaseClass):

    def test_formsubmision(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.getname(getData["FirstName"])
        homepage.getmail(getData["Mail"])
        homepage.getid(getData["password"])
        log.info("te dhenat u futen me sukses")
        homepage.getcheckbox()
        self.selectoptionbytext(homepage.getgender(), getData["gender"])
        homepage.getsubmit()
        successmsg = homepage.getsuccess().text
        assert "Success" in successmsg
        self.driver.refresh()


    @pytest.fixture(params=HomepageData.test_HomepageData)
    def getData(self, request):
        return request.param
