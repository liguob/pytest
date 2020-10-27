# -*- coding: utf-8 -*-
import Tap as Tap

from request_test.api.tag import Tag


class Testtap:

    def setup(self):
        self.tag = Tag()

    def test_all(self, tagname, tagid, get_token):
        self.tag.tag_add(tagname, tagid, get_token)
