import pytest
@pytest.fixture
def sample_fixture():
    print("This will run before test function")
    yield
    print("This will run after test function")

def test_example(preSetupWork, sample_fixture):
    print("this will run before test function from conftest.py")
    assert preSetupWork == "I set up resources before each test function"


    