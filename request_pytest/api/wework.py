# -*- coding: utf-8 -*-
from request_pytest.api.base_api import Baseapi


class Wework(Baseapi):
    data = {"corpid": "ww2e7cc010c046e221"}

    def get_token(self, corpsecret):
        self.data.update({"corpsecret": corpsecret})
        data = self.template("../data/tag.yml", self.data, "token")
        return self.send_api(data)["access_token"]