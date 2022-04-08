import pytest

from pytestDemo.baseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class Testexample2(BaseClass):

    def test_editProfile(self, dataLoad):
        log=self.getlogger()
        log.info(dataLoad[0])
        log.info(dataLoad[1])
        log.info(dataLoad[2])
        log.info(dataLoad)

    def test_crossBrowser(self, crossBrowser):
        log=self.getlogger()
        log.info(crossBrowser[0])
