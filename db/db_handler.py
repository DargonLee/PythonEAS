# -*- coding: utf-8 -*-

"""
@author: harlan
@software: PyCharm
@file: db_handler.py
@time: 2023/2/16 14:18
"""

import os
import pickle

from conf import settings

def save_data(obj):
    # 获取对象的保存路径
    # obj.__class__:拿到对象的类
    # obj.__class__.__name__:拿到类名 str
    class_name = obj.__class__.__name__
    obj_dir = os.path.join(
        settings.DB_DIR,
        class_name
    )

    # 判断文件夹是否存在，如果不存在，就创建文件夹
    if not os.path.isdir(obj_dir):
        os.mkdir(obj_dir)

    obj_path = os.path.join(
        obj_dir,
        obj.name
    )

    # 保存文件
    with open(obj_path, 'wb')as f:
        pickle.dump(obj, f)

def select_data(cls, name):
    obj_path = os.path.join(
        settings.DB_DIR,
        cls.__name__,
        name
    )

    # 判断文件是否存在
    if os.path.exists(obj_path):
        return

    # 读取文件
    with open(obj_path, 'rb')as f:
        obj = pickle.load(f)
        return obj

