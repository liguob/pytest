# -*- coding: utf-8 -*-
import pytest
import yaml

from appnium_test.pages.App import App


class Testapp(App):

    def setup(self):
        self.run = self.start().main()

    def teardown(self):
        self.quit()

    @pytest.mark.parametrize(['name', 'gender', 'phone'], yaml.safe_load(open("./data/data.yml")).get())
    def test_add(self, name, gender, phone):
        assert '添加成功' == self.run.goto_membermanage().goto_addcontact().edit_name(name).edit_gender(gender).edit_phone(
            phone). \
            save_member().find_toast().text

    def test_del(self, name):
        assert name not in self.run.goto_membermanage().goto_memberinvite().goto_delcontact().del_confirm().get_member()
