#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :usage of pyyaml
@Date     :2021/04/29 19:31:24
@Author      :xbMa
'''

import yaml
from pathlib import Path

'''
    <pyyaml_test_data_1.yaml>

    raincoat: 1
    coins: 5
    books: 23
    spectacles: 2
    chairs: 12
    pens: 6
'''
with open("pyyaml_test_data_1.yaml") as f:

    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)

'''
    <pyyaml_test_data_2.yaml>

    cities:
     - Nanjing
     - Beijing
     - Shanghai
     - tianjin
     - shenzhen
    ---
    companies:
     - HuaWei
     - Zte
     - Alibaba
     - Tencent
     - Baidu
'''
with open("pyyaml_test_data_2.yaml") as f:

    docs = yaml.load_all(f, Loader=yaml.FullLoader)
    for y in docs:
        print(y)

# Dump to yaml
users = [{'name': 'xbMa', 'occupation': 'engineer'},
         {'name': 'Tom', 'occupation': 'Teacher'}]

print(yaml.dump(users))

# Write data to yaml
with open("user.yaml", "w") as f:
    yaml.dump(users, f)
# Delete the file
Path("user.yaml").unlink()

# Sort by key
with open("pyyaml_test_data_1.yaml") as f:

    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)

    sorted_by_key = yaml.dump(data, sort_keys=True)
    print(sorted_by_key)