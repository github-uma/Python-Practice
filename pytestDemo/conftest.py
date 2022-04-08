import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")


@pytest.fixture()
def dataLoad():
    print("Test data provider")
    return ["Uma", "Shaker", "umashanker.testing@gmail.com"]


@pytest.fixture(params=[("chrome", "Uma"), ("firefox", "Uma", "Shanker"), ("edge", "user")])
def crossBrowser(request):
    return request.param
