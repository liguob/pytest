# -*- coding: utf-8 -*-
import json

import pytest
import yaml

from request_test.api.base_api import Baseapi


class Wework(Baseapi):

    @pytest.fixture()
    def get_token(self):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": "ww2e7cc010c046e221",
                "corpsecret": "2hsqoRb2oW77jsNjQYpcIDoJfZrTikXCG-Iqdgbr-Xo"
            }
        }
        try:
            token = self.send_api(data)["access_token"]
        except KeyError:
            raise Exception("获取token失败")
        else:
            with open("./token.json", "w") as f:
                json.dump(token, f)