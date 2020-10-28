# -*- coding: utf-8 -*-
from collections import defaultdict
from string import Template

from typing import List

import yaml

from api.base_api import Baseapi

with open("./test_all_data.yml", "r") as f:
    data = yaml.safe_load(f)
print(data[0])
data[0].update({"token": "test"})
# for key, value in data.items():
#     test_data.update()
# print(test_data)
data[0]={'tagname': 'liguo1', 'tagid': 1, 'access_token': 'zTW0mlfSJOUq5ebl3tpbMjfeIpMHKtcK_hc6eb60IaAB8MxMP-RR66LlxbPUoKwdUybfFFyGuitHJElTM-8bi-MZpYoWSrc84m-k5gHCcblTyNq40TBCdFIMi4JLn4Q0D9HNTqmMy4MWcbLbTNyqUIn0T4uPSi9HXrGm02L02sJ6nYAvgSbb76tDEMrmC4x44W09zee5SX5Rqr9A_5hE9Q'}
test = Baseapi()
data = test.template("../data/tag.yml", data[0], "add")
# def abc(**data):
#     data.update()
print(data)
print(type(data))
