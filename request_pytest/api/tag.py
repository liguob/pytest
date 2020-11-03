# -*- coding: utf-8 -*-
from request_pytest.api.base_api import Baseapi
from request_pytest.api.wework import Wework


class Tag(Baseapi):
    corpsecret = "2hsqoRb2oW77jsNjQYpcIDoJfZrTikXCG-Iqdgbr-Xo"
    tag_file = "../data/tag.yml"

    def __init__(self):
        self.token = Wework().get_token(self.corpsecret)

    def add(self, **req):
        req.update({"access_token": self.token})
        req = self.template(self.tag_file, req, "add")
        print(req)
        return self.send_api(req)

    def delete(self, **req):
        req.update({"access_token": self.token})
        req = self.template(self.tag_file, req, "delete")
        return self.send_api(req)

    def update(self, **req):
        req.update({"access_token": self.token})
        req = self.template(self.tag_file, req, "update")
        return self.send_api(req)

    def query(self):
        req = self.template(self.tag_file, {"access_token": self.token}, "query")
        return self.send_api(req)