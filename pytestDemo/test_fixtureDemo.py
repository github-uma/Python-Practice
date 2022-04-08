import pytest

from pytestDemo.baseClass import BaseClass


@pytest.mark.usefixtures("setup")
class TestFixtureDemo(BaseClass):

    def test_validateFifture1(self):
        log=self.getlogger()
        log.info("First Test Method")

    def test_validateFifture2(self):
        log=self.getlogger()
        log.info("Second Test Method")

    def test_validateFifture3(self):
        print("Third Test Method")

    def test_validateFifture4(self):
        print("Fourth Test Method")
