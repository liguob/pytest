import pytest

@pytest.fixture(scope="function", autouse=True)
def setup():

    print("\n开始计算\n")
    yield
    print("\n结束计算\n")
