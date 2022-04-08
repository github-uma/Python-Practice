import pytest


def test_FirstProgram():
    assert "abc" == "xyz"


@pytest.mark.smoke
def test_SecondProgram():
    assert "abc" != "xyz"
