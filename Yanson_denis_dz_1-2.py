import os
import yaml


def mkdir_yaml(some_val):
    if type(some_val) == dict:
        for i in some_val:

            if not os.path.exists(i):
                os.mkdir(i)
            os.chdir(i)
            mkdir_yaml(some_val[i])
            os.chdir("..")
    else:
        for i in some_val:
            if type(i) == dict:
                mkdir_yaml(i)
            else:
                open(i, 'w')


with open(r'config.yaml') as file:
    folder_dict = yaml.load(file, Loader=yaml.FullLoader)
mkdir_yaml(folder_dict)
