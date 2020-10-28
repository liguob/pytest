# -*- coding: utf-8 -*-
import pytest

from api.tag import Tag


class Testag:
    tag = Tag()
    test_data = tag.open_yml("./test_all_data.yml")

    @pytest.mark.parametrize("adddata,updata", test_data)
    def test_all(self, adddata: dict, updata: dict):
        try:
            assert self.tag.add(**adddata)["errmsg"] == "created"
        except AssertionError as e:
            if "invalid tagid" in e.__str__():
                self.tag.delete(**{"tagid": adddata["tagid"]})
                assert self.tag.add(**adddata)["errmsg"] == "created"
            if "UserTag Name Already Exist" in e.__str__():
                for i in self.tag.query()["taglist"]:
                    if i["tagname"] == adddata["tagname"]:
                        self.tag.delete(**{"tagid": i["tagid"]})
                        break
                    else:
                        raise Exception("查询标签异常，没有对应的tagid")
        assert self.tag.add(**adddata)["errmsg"] == "created"
        assert self.tag.update(**updata)["errmsg"] == "updated"
