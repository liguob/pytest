from selenium import webdriver

from selenium_test.pages.loginpage import LoginPage


class TestContact:

    def setup(self):
        self.main = LoginPage().login()

    # def test_add_contact(self):
    #     _member_data = ('测试人员1', 'id1000', 13199991000)
    #     assert '测试人员1' in self.main.goto_add_contact().add_member(*_member_data).get_members()

    def test_uplpad_contact(self):
        file_path = 'D:/用户目录/下载/通讯录导入文件.xlsx'
        import_name = '小王'
        assert '小王' in self.main.goto_upload().upload_file(file_path).get_members()

    def test_delete_contact(self):
        delete_name = '小王'
        assert '小王' not in self.main.goto_members().delete_member(delete_name).get_members()

    def teardown(self):
        self.main.driver.quit()