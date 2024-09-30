import os


def root_path():
    """ 获取 根路径 """
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return path


def get_case_path():
    return root_path() + '\data\\vip_api_case.xlsx'


def get_log_path():
    return root_path() + '\data\\app.log'

