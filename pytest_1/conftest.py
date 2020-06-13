import pytest


@pytest.fixture(scope="function")
def setup():
    print("\n开始计算\n")


@pytest.fixture(scope="function")
def teardown():
    print("\n计算结束\n")
