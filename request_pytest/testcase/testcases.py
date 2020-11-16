# -*- coding: utf-8 -*-
from request_pytest.api.tag import Tag


import pytest




class Testag:
    tag = Tag()
    test_data = tag.open_yml("./test_all_data.yml")

    @pytest.mark.parametrize("adddata,updata", test_data)
    def test_all(self, adddata: dict, updata: dict):
        try:
            assert self.tag.add(adddata)["errmsg"] == "created"
        except AssertionError as e:
            if "invalid tagid" in e.__str__():
                assert self.tag.delete({"tagid": adddata["tagid"]})["errmsg"] == "deleted"
            if "UserTag Name Already Exist" in e.__str__():
                for i in self.tag.query()["taglist"]:
                    if i["tagname"] == adddata["tagname"]:
                        assert self.tag.delete({"tagid": i["tagid"]})["errmsg"] == "deleted"
                        break
            assert self.tag.add(adddata)["errmsg"] == "created"
            assert self.tag.update(updata)["errmsg"] == "updated"