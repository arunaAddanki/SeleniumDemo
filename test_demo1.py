# Any pytest file should start with test_
import pytest

#Any code should be wrapped in method only


# According to pytest framework standards you have to write everything as a function


#pytest method names should start with test

# -k stands for method name execution

# -s stands for logs in output

# -v stands for more info metadata

# you can run specific file by py.test <filename>

# you can mark (tag) tests @pytest.mark.smoke and then run it with -m

# you can skip tests with @pytest.mark.skip

@pytest.mark.smoke
def test_firstProgram():
    print("Hello aruna")

# running but not reporting either pass or fail
@pytest.mark.xfail
def test_Greet():
    print("Hello Naga")



