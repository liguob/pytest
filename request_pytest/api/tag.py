# -*- coding: utf-8 -*-
from request_pytest.api.base_api import Baseapi
from request_pytest.api.wework import Wework


class Tag(Baseapi):
    corpsecret = "2hsqoRb2oW77jsNjQYpcIDoJfZrTikXCG-Iqdgbr-Xo"
    tag_file = "../data/tag.yml"
    req = {}

    def __init__(self):
        self.token = Wework().get_token(self.corpsecret)
        self.req.update({"access_token": self.token})

    def add(self, req: dict):
        # req.update({"access_token": self.token})
        self.req.update(req)
        req = self.template(self.tag_file, self.req, "add")
        print(req)
        return self.send_api(req)

    def delete(self, req: dict):
        self.req.update(req)
        # req.update({"access_token": self.token})
        req = self.template(self.tag_file, self.req, "delete")
        return self.send_api(req)

    def update(self, req: dict):
        # req.update({"access_token": self.token})
        self.req.update(req)
        req = self.template(self.tag_file, self.req, "update")
        return self.send_api(req)

    def query(self):
        req = self.template(self.tag_file, self.req, "query")
        return self.send_api(req)
