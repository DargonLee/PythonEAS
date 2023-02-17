# -*- coding: utf-8 -*-

"""
@author: harlan
@software: PyCharm
@file: models.py
@time: 2023/2/16 14:19
"""
'''
用来存放类
'''
import datetime

from db import db_handler

class Base:
    def __init__(self, name):
        self.name = name
        self.reg_date = datetime.datetime.now()
        self.save()

    def save(self):
        db_handler.save_data(self)

    @classmethod
    def select(cls, name):
        obj = db_handler.select_data(cls, name)
        return obj


# 管理员、老师、学生、课程
class Admin(Base):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.reg_date = datetime.datetime.now()

        # 累计付费人次
        self.pay_num = 0
        # 今日营收
        self.today_money = {}
        # 累计营收
        self.all_money = 0

        # 流水
        self.flow = []
        '''
        [
            [time, course_name, money, '收入'],
            [time, teacher_name, money, '支出']
        ]
        '''
        super(Admin, self).__init__(name)




class Student(Base):
    def __init__(self, name, pwd):
        self.pwd = pwd
        self.locked = False

        self.course_list = []
        self.learn_course_list = []
        super(Student, self).__init__(name)


class Teacher(Base):
    pass

class Course(Base):
    pass