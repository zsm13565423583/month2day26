import os
import yaml

from config import BASE_PATH


def get_yaml(filename):
    #文件流
    file_path = BASE_PATH + os.sep +"data"+os.sep +filename
    arr = []
    with open(file_path,"r") as f:
        for data in yaml.safe_load(f).values():
            arr.append(tuple(data.values()))

    return arr


# if __name__ == '__main__':
#     r =get_yaml("./login.ymal")