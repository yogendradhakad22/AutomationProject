
def test_samplefixture(preSetupWork):
    print("this will run before test function from conftest.py")
    assert preSetupWork == "I set up resources before each test function"