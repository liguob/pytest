# -*- coding: utf-8 -*-
from string import Template

import requests
import yaml


class Baseapi:

    def send_api(self, req: dict):
        return requests.request(**req).json()

    def open_yml(self, path):
        with open(path) as f:
            data = yaml.safe_load(f)
        return data

    @classmethod
    def template(cls, filepath, data, sub=None):
        with open(filepath, encoding="utf-8") as f:
            if sub:
                return yaml.safe_load(
                    Template(
                        yaml.dump(
                            yaml.safe_load(f)[sub]
                        )
                    ).substitute(data)
                )
            else:
                return yaml.safe_load(Template(yaml.dump(f.read())).substitute(data))
