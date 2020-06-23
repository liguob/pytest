from selenium_test.contactmember.contactmemberpage import ContactMemberPage
from selenium_test.indexpage.Loginpage import LoginPage
from selenium_test.homepage.homepage import HomePage
import pytest

from selenium_test.testcases.conftest import setup


class TestContactMember(setup):
    def setup_class(self,setup):
        self.stat = HomePage()

    def test_add_member(self):
        assert '测试人员1' in self.stat.goto_add_contact().add_member('测试人员1','id1111',1319991001)
