# -*- coding: utf-8 -*-

import requests
import yaml


class Baseapi:


    def send_api(self, data):
        return requests.request(**data).json()

    def open_yml(self, path):
        with open(path) as f:
            data = yaml.safe_load(f)
        return data