import pytest

#Fixture is reused code that runs before each test function if referenced
#Copy fixture name and add as parameter to test function
#sample_fixture(scope="module") it will run once per module
#sample_fixture(scope="session") it will run once per test session
#sample_fixture(scope="function") it will run before each test function (default)
#sample_fixture(scope="class") it will run once per class
#sample_fixture(autouse=True) it will run before each test function without needing to reference it
#we need to @pytest.fixture before defining a fixture

@pytest.fixture
def sample_fixture():
    print("This will run before test function")

def test_example(sample_fixture):
    print("this is the test function")
    assert 1 + 1 == 2

def test_another_example():
    assert "hello".upper() == "HELLO"
    
@pytest.mark.skip
def test_skipped_example():
    assert 2 * 2 == 5

@pytest.mark.smoke
def test_smoke_example():
    assert 3 - 1 == 2