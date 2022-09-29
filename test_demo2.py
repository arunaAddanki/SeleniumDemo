import pytest
@pytest.mark.skip
@pytest.mark.smoke
def test_Greet():
    msg = "aru"
    assert msg == "hi" , "Test Failed because Strings do not match"