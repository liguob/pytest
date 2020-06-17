import pytest
import yaml

print (os.getcwd())

@pytest.mark.parametrize(["a", "b", "c"], yaml.safe_load(open("data.yml")))
class TestCalculator:

    def test_add(self, setup, teardown, a, b, c):
        assert a + b == c

    def test_sub(self, setup, teardown, a, b, c):
        assert a - b == c

    def test_mul(self, setup, teardown, a, b, c):
        assert a * b == c

    def test_div(self, setup, teardown, a, b, c):
        assert a / b == c


if __name__ == '__main__':
    pytest.main(["-s", "./"])
