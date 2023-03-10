# -*- coding: utf-8 -*-

"""
@author: harlan
@software: PyCharm
@file: student_interface.py
@time: 2023/2/16 14:18
"""
'''
学生接口
'''
import os
import logging

from conf import settings
from db import models

stu_logger = logging.getLogger('student')

def student_register_interface(name, pwd):
    stu_path = os.path.join(
        settings.DB_DIR,
        'Student',
        name
    )

    if os.path.exists(stu_path):
        return False, f'用户名：{name} 已存在！'

    # 学生不存在, 开始注册
    stu_obj = models.Student(name, pwd)
    msg = f'用户{name}注册成功！'
    stu_logger.info(msg)
    return True, msg