import pytest


@pytest.mark.skip
def test_CreditProgram():
    assert "abc" != "xyz"


@pytest.mark.smoke
def test_CreditProgram2():
    var = 5
    assert var == 4


@pytest.fixture()
def test_fixtureDemo(setup):
    print("I will be test_fixtureDemo method")
