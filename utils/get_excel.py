import pandas as pd
from common.setting import get_case_path

def get_excel():
    path = get_case_path()
    df = pd.read_excel(path, sheet_name='pytest_custom')

    data_dicts = []

    # 遍历每一行
    for index, row in df.iterrows():
        # 使用 zip 函数将表头和对应的值组合成字典
        data_dict = dict(zip(df.columns, row))
        data_dicts.append(data_dict)
    print(type(data_dicts))
    print(len(data_dicts))
    return data_dicts