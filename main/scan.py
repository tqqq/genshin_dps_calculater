# coding=utf-8

import json

from main.const import ARTIFACTS_DATA


def scan_artifacts():
    artifacts_data = json.loads(open(ARTIFACTS_DATA, 'r', encoding='utf-8').read())
    return artifacts_data
