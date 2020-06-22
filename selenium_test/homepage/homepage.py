# -*- coding: utf-8 -*-
"""
@Time    : 2020/6/22 16:01
@Author  : liguobin
@File    : indexpage.py
"""
import json
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.wait import WebDriverWait

from selenium_test.basemeshod.basemethod import BaseMethod


class HomePage(BaseMethod):

