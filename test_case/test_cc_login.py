import ast
import json
import logging

import pytest
import requests

from common.setting import get_log_path
from utils.get_excel import get_excel
from utils.logger.logger import Logger

case_datas = get_excel()

logger = logging.getLogger()


@pytest.mark.parametrize("case_data", case_datas[0:1])
def test_login(case_data):
    url = case_data['host'] + case_data['url']
    method = case_data['method']
    headers = case_data['header']
    print(type(headers))
    headers = ast.literal_eval(headers)
    data = case_data['data']
    data = json.loads(data)
    print(headers)
    print(data)
    path_log = get_log_path()
    logger = Logger(log_file=path_log,name="test_login")
    logger.info("日志输出")
    response = requests.request(url=url, method=method,headers=headers ,json=data)
    print(response.json())