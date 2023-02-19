# -*- coding: utf-8 -*-

"""
@author: harlan
@software: PyCharm
@file: common_interface.py
@time: 2023/2/17 11:09
"""

'''
公共接口
'''

import os
import logging

from conf import settings
from db import models

common_logger = logging.getLogger('common')


# 判断类型下面是否有对象
def check_obj_is_here(user_type):
    admin_dir = os.path.join(
        settings.DB_DIR,
        user_type
    )

    if os.path.isdir(admin_dir) and os.listdir(admin_dir):
        return True, f'{user_type}已存在！'

    return False, f'{user_type}不存在！'


def login_interface(name, pwd, user_type):
    # if user_type == 'Admin':
    #     obj = models.Admin.select(name)
    # elif user_type == 'Student':
    #     obj = models.Student.select(name)
    # elif  user_type == 'Teacher':
    #     obj = models.Teacher.select(name)

    cls = getattr(models, user_type)
    obj = cls.select(name)

    # 判断用户是否存在
    if not obj:
        return False, '用户名不存在'

    # 校验密码
    if pwd != obj.pwd:
        return False, '密码错误'

    # 判断用户是否被冻结
    if obj.locked:
        return False, '用户已被冻结'

    # 返回登录成功
    msg = f'用户：{name} 登录成功'
    common_logger.info(msg)
    return True, msg
