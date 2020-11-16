import pytest
import yaml

from pytest_1.caculator_base.calculator_method import Calculators


@pytest.mark.parametrize("a, b", yaml.safe_load(open("data/data.yml")))
class TestCalculator(Calculators):

    @pytest.mark.run(order=-2)
    def test_mul(self, a, b):
        try:
            print(self.mul(a, b))
            assert a * b == self.mul(a, b)
        except TypeError:
            print("值类型错误")

    @pytest.mark.denpendency(depens=["test_mul"])
    @pytest.mark.run(order=-1)
    def check_div(self, a, b):
        try:
            assert a / b == self.div(a, b)
        except TypeError:
            print("值类型错误")
        except ZeroDivisionError:
            print("被除数不能为0")

    @pytest.mark.run(order=2)
    @pytest.mark.dependency(name="test_div")
    def check_sub(self, a, b):
        try:
            assert a - b == self.sub(a, b)
        except TypeError:
            print("值类型错误")

    @pytest.mark.run(order=1)
    def test_add(self, a, b):
        try:
            assert a + b == self.add(a, b)
        except TypeError:
            print("值类型错误")
