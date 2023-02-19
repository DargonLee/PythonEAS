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
import logging

from db import models

admin_logger = logging.getLogger('admin')


def admin_register_interface(name, pwd):
    # 调用管理员类，实例化一个管理员对象，在保存
    admin_obj = models.Admin(name, pwd)
    msg = f'{name}注册成功'
    admin_logger.info(msg)
    return True, msg


def add_school_interface(name, addr, admin_name):
    # 判断学校是否存在
    school_obj = models.School.select(name)
    if school_obj:
        return False, f'学校：{name} 已存在'

    # 由管理员创建学校
    admin_obj = models.Admin.select(admin_name)
    admin_obj.add_school(name, addr)
    msg = f'管理员：{admin_name} 创建:学校：{name} 成功'
    admin_logger.info(msg)
    return True, msg
