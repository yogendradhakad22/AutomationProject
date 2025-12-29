# conftest.py is a special global file in pytest that is used to define fixtures and hooks that can be shared across multiple test files in a directory.

import pytest

@pytest.fixture(scope="function")
def preSetupWork():
    return "I set up resources before each test function"
