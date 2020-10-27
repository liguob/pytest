# -*- coding: utf-8 -*-
from request_test.api.base_api import Baseapi


class Tag(Baseapi):

    def tag_add(self, tagname: str, tagid: int, get_token):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/create",
            "params": {
                "access_token": get_token,
                "tagid": tagid
            },
            "json": {
                "tagname": tagname
            }
        }
        return self.send_api(data)

    def tag_delete(self, tagid: int, get_token):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/delete",
            "params": {
                "access_token": get_token,
                "tagid": tagid
            }
        }
        return self.send_api(data)

    def tag_update(self, tagid: int, tagname: str, get_token):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/update",
            "params": {
                "access_token": get_token
            },
            "json": {
                "tagid": tagid,
                "tagname": tagname
            }
        }
        return self.send_api(data)

    def tag_querl(self, get_token):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/list",
            "params": {
                "access_token": get_token
            }
        }
        return self.send_api(data)
