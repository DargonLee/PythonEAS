# -*- coding: utf-8 -*-

"""
@author: harlan
@software: PyCharm
@file: src.py
@time: 2023/2/16 14:14
"""

'''
用户视图层
'''
import logging
import sys
test_logger = logging.getLogger('视图层')

from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt6.QtCore import Qt
from ui.login import Ui_Form as LoginUIMixin

from conf import settings
from lib.common import pwd_to_sha256
from interface import admin_interface, common_interface, student_interface

class LoginWindow(LoginUIMixin, QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint) # 隐藏窗口边框

        self.admin_is_here = False

    # 获取用户类型
    def get_user_type(self):
        checkbox = self.checkBox.isChecked()
        checkbox2 = self.checkBox_2.isChecked()
        checkbox3 = self.checkBox_3.isChecked()
        user_type_dic = {
            'Student': checkbox,
            'Teacher': checkbox2,
            'Admin': checkbox3,
        }
        for user_type in user_type_dic:
            if user_type_dic.get(user_type):
                return user_type

    # 登录功能
    def login(self):
        test_logger.debug('登录')
        username = self.lineEdit.text().strip()
        pwd = self.lineEdit_2.text().strip()
        user_type = self.get_user_type()

        # 判断用户名或密码是否为空
        if not username or not pwd:
            QMessageBox.warning(self, '警告', '用户名或密码不能为空')
            return

        pwd = pwd_to_sha256(pwd)
        obj = common_interface.login_interface(
            username, pwd, user_type
        )



    # 注册功能
    def register(self):
        test_logger.debug('注册')
        username = self.lineEdit_3.text().strip()
        pwd = self.lineEdit_4.text().strip()
        re_pwd = self.lineEdit_5.text().strip()
        # 判断两次密码是否一致
        if pwd != re_pwd:
            QMessageBox.warning(self, '警告','两次密码输入不一致')
            return

        # import re
        # if not re.findall('^[a-zA-Z\w{2,9}]$',username):
        #     QMessageBox.warning(self, '警告', '用户名长度必须为3-10的字符\n只能由字母、数字、下划线组成')
        #     return

        # 密码加密
        pwd = pwd_to_sha256(pwd)

        # 调用注册接口
        if self.admin_is_here:
            flag, msg = student_interface.student_register_interface(username, pwd)
        else:
            flag, msg = admin_interface.admin_register_interface(username, pwd)

        QMessageBox.about(self, '提示', msg)

        # 注册失败
        if not flag:return

        # 跳转到登录页面
        self.open_login_page()

        # 清空输入框文字
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_5.setText('')

        self.lineEdit.setText(username)
        self.lineEdit_2.setFocus()

    # 打开登录页面
    def open_login_page(self):
        test_logger.debug('打开登录页面')
        self.stackedWidget.setCurrentIndex(0)

    # 打开注册页面
    def open_register_page(self):
        test_logger.debug('打开注册页面')
        self.stackedWidget.setCurrentIndex(1)

        # 判断是否有管理员存在
        flag, msg = common_interface.check_admin_is_here()
        if flag:
            self.label_2.setText('学生注册')
            self.admin_is_here = True



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

def run():
    # 展示界面
    app = QApplication(sys.argv)

    login_window = LoginWindow()
    login_window.show()


    sys.excepthook = except_hook # 重新定义异常挂钩
    sys.exit(app.exec())