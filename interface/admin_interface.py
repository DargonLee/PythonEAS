# -*- coding: utf-8 -*-

"""
@author: harlan
@software: PyCharm
@file: admin_interface.py
@time: 2023/2/16 14:14
"""

'''
管理员接口
'''

from db import models

def admin_register_interface(name, pwd):
    # 调用管理员类，实例化一个管理员对象，在保存
    admin_obj = models.Admin(name, pwd)
    return True, f'{name}注册成功'