# -*- coding: utf-8 -*-
from string import Template

import requests
import yaml


class Baseapi:

    def send_api(self, req):
        return requests.request(**req).json()

    def open_yml(self, path):
        with open(path) as f:
            data = yaml.safe_load(f)
        return data

    def template(self, file_path, data, sub):
        with open(file_path, encoding="utf-8") as f:
            return yaml.safe_load(
                Template(
                    yaml.dump(
                        yaml.safe_load(f)[sub]
                    )
                ).substitute(**data)
            )