import yaml, os
from get_dir import BASE_DIR


class GetFileData:

    def __init__(self):
        pass

    def get_yaml_data(self, dataname):
        """
        返回yaml数据内容
        :param yamlName: 读取yaml文件名字
        :return:
        """
        with open(BASE_DIR + os.sep + "Data" + os.sep + dataname, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f).get("test_search_data")
        return data