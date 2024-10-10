import ast
import json
import pytest
import requests
from common.setting import get_log_path
from utils.get_excel import get_excel
from utils.logger.logger import Logger
from utils.mysql_utils.mysql_utils import MysqlHelper
from utils.random_utils.random_utils import DataGenerator

case_datas = get_excel()

logger = Logger()

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

def test_random():
    from utils.random_utils.customProvider import CustomProvider
    from faker import Faker
    faker = Faker()
    faker.add_provider(CustomProvider)
    name = faker.mouse()
    print(f'{name},++++++++++++++++++')

def test_sql():
    mysqlHelper = MysqlHelper()
    sql = 'select count(*) from cic_customer_info where delete_flag = %s'
    params = {0}
    logger.info('结果')
    result = mysqlHelper.get_one(sql,params)
    print(result)
