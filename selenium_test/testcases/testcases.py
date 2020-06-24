from selenium_test.pages.loginpage import LoginPage


class TestContact:

    def setup_class(self):
        self.main = LoginPage()

    def add_contact_test(self):
        _member_data = ('测试人员1', 'id1000', 13199991000)
        assert '测试人员1' in self.main.login().goto_add_contact().add_member(*_member_data).get_members()

    def delete_member_test(self):
        