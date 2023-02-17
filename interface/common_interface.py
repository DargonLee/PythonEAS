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

from conf import settings
from db import models

# 判断管理员是否存在
def check_admin_is_here():
    admin_dir = os.path.join(
        settings.DB_DIR,
        'Admin'
    )

    if os.path.isdir(admin_dir) and os.listdir(admin_dir):
        return True, '管理员已存在！'

    return False, '管理员不存在！'

def login_interface(name, pwd, user_type):
    # if user_type == 'Admin':
    #     obj = models.Admin.select(name)
    # elif user_type == 'Student':
    #     obj = models.Student.select(name)
    # elif  user_type == 'Teacher':
    #     obj = models.Teacher.select(name)

    cls = getattr(models, user_type)
    obj = cls.select(name)