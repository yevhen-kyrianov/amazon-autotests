import pytest

@pytest.fixture(scope="session")
def setup_environment():
    # Setup code for the test environment
    print("Setting up the test environment")
    yield
    # Teardown code for the test environment
    print("Tearing down the test environment")

@pytest.fixture
def sample_data():
    # Example fixture providing sample data
    return {"key": "value"}

