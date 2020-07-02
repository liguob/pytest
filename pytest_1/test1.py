import pytest
import yaml


from pytest_1.calculator_method import Calculators


@pytest.mark.parametrize(["a", "b"], yaml.safe_load(open("data.yml")))
class TestCalculator(Calculators):

    def test_add(self, setup, a, b):
        try:
            assert a + b == self.add(a, b)
        except TypeError:
            print("值类型错误")

    def test_sub(self, setup, a, b):
        try:
            assert a - b == self.sub(a, b)
        except TypeError:
            print("值类型错误")

    def test_mul(self, setup, a, b):
        try:
            print(self.mul(a,b))
            assert a * b == self.mul(a, b)
        except TypeError:
            print("值类型错误")

    def test_div(self, setup, a, b):
        try:
            assert a / b == self.div(a, b)
        except TypeError:
            print("值类型错误")
        except ZeroDivisionError:
            print("被除数不能为0")
