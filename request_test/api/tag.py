# -*- coding: utf-8 -*-
from api.base_api import Baseapi
from api.wework import Wework


class Tag(Baseapi):
    corpsecret = "2hsqoRb2oW77jsNjQYpcIDoJfZrTikXCG-Iqdgbr-Xo"

    def __init__(self):
        self.token = Wework().get_token(self.corpsecret)

    def add(self, **req):
        req.update({"access_token": self.token})
        req = self.template("../data/tag.yml", req, "add")
        return self.send_api(req)

    def delete(self, **req):
        req.update({"access_token": self.token})
        req = self.template("../data/tag.yml", req, "delete")
        return self.send_api(req)

    def update(self, **req):
        req.update({"access_token": self.token})
        req = self.template("../data/tag.yml", req, "update")
        return self.send_api(req)

    def query(self):
        req = self.template("../data/tag.yml", {"access_token": self.token}, "query")
        return self.send_api(req)