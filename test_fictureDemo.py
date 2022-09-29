import pytest
# we can defining the fixture either at top or end
@pytest.fixture()
def setup():
    print("i will be executing first")
    yield
    print("i will executed last")

def test_fictureDemo(setup):
    print("i will execute steps in fictureDemo method")
