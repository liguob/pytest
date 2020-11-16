import os, sys
import pytest
import yaml

sys.path.append("G:\\pytest")


def pytest_addoption(parser):
    mygroup = parser.getgroup("params_liguobin")  # 创建自己的命令组
    mygroup.addoption("--env",
                      default='test',
                      dest="env",
                      help="set your run env"
                      )


@pytest.fixture(scope="session", autouse=True)
def new_option(request):
    data = request.config.getoption("--env")
    params = yaml.safe_load(open("data/env.yml", encoding='utf-8'))[data]
    print(f"当前环境：{params}")
    return data