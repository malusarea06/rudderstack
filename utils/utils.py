import json
from pathlib import Path

CONF = Path(".").absolute().joinpath("conf")

class Utils:
    def __init__(self):
        pass

    def read_conf(self, filename, relative_path):
        """
        Method to read conf/json file.
        :param filename: File Name
        :param relative_path: Relative path to file
        :return: (dict) Return file data
        """
        try:
            conf_file = CONF.joinpath(relative_path).joinpath(filename)
            print(conf_file)
            with open(conf_file) as fopen:
                config_data = json.load(fopen)
                return config_data
        except FileNotFoundError as exception:
            print("Error occured while reading conf file : ", exception)