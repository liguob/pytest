# -*- coding: utf-8 -*-
import pytest
import yaml

from appnium_test.pages.App import App


class Testapp():

    def setup(self):
        self.run = App().start()
        self.start = self.run.main()

    def teardown(self):
        self.run.quit()

    @pytest.mark.parametrize(['name', 'gender', 'phone'],
                             yaml.safe_load(open("data.yml", encoding='utf-8'))["addmember"])
    def test_add(self, name, gender, phone):
        assert 1 == 1
        assert True == self.start.goto_membermanage().goto_addcontact().edit_name(name).edit_gender(gender). \
            edit_phone(phone).save_member().toast_text("添加成功")

    @pytest.mark.parametrize(['name'],
                             yaml.safe_load(open("data.yml", encoding='utf-8'))["delmember"])
    def test_del(self, name):
        assert name not in self.start.goto_membermanage().goto_memberinvite(name).goto_delcontact(name). \
            del_confirm().get_member()