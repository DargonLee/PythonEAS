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
login_window = None
login_name = None
login_user_type = None

from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt6.QtCore import Qt, QCoreApplication
from ui.login import Ui_Form as LoginUIMixin
from ui.home import Ui_Form as HomeUIMixin
_translate = QCoreApplication.translate

from qt_material import apply_stylesheet

from conf import settings
from lib.common import pwd_to_sha256
from interface import admin_interface, common_interface, student_interface

class LoginWindow(LoginUIMixin, QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint) # 隐藏窗口边框

        self.admin_is_here = False
        self.login_window_init()
        self.open_login_page()

    #创建学校
    def add_school(self):
        name = self.lineEdit_6.text().strip()
        addr = self.lineEdit_7.text().strip()
        if not name or not addr:
            QMessageBox.warning(self, '警告', '学校名或地址不能为空')
            return
        # 调用添加学校的接口
        global login_name
        flag, msg = admin_interface.add_school_interface(
            name,
            addr,
            login_name
        )
        QMessageBox.about(self, '提示', msg)
        if not flag:
            return
        # 学校添加成功，进入主页
        self.lineEdit_6.setText('')
        self.lineEdit_7.setText('')
        self.go_home()

    def go_home(self):
        self.close()
        # 进入主页
        self.home_window = HomeWindow()
        self.home_window.show()

    # 初始化登录窗口
    def login_window_init(self):
        self.lineEdit.setText(settings.LOGIN_USER)
        user_type_dic = {
            'Student': self.checkBox,
            'Teacher': self.checkBox_2,
            'Admin': self.checkBox_3,
        }
        user_type_dic.get(settings.LOGIN_TYPE).setChecked(True)

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
        flag, msg = common_interface.login_interface(
            username, pwd, user_type
        )
        if not flag:
            QMessageBox.warning(self, '登录失败',msg)
            return

        # 登录成功
        settings.config.set('USER', 'LOGIN_USER', username)
        settings.config.set('USER', 'LOGIN_TYPE', user_type)
        with open(settings.CONFIG_PATH, 'w', encoding='utf-8-sig')as f:
            settings.config.write(f)

        # 记录下用户名和类型
        global login_name, login_user_type
        login_name = username
        login_user_type = user_type

        # 判断是否有学校
        flag, msg = common_interface.check_obj_is_here('School')
        if not flag:
            # 如果没有学校的时候，是管理员登录，跳转到创建学校的界面
            if user_type == 'Admin':
                self.stackedWidget.setCurrentIndex(2)
            else:
                QMessageBox.warning(self, '警告', '当前不存在学校，请联系管理员添加学校')
            return

        # 进入主页
        self.go_home()

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
        self.lineEdit.setFocus()
        self.show()

    # 打开注册页面
    def open_register_page(self):
        test_logger.debug('打开注册页面')
        self.stackedWidget.setCurrentIndex(1)

        # 判断是否有管理员存在
        flag, msg = common_interface.check_obj_is_here('Admin')
        if flag:
            self.label_2.setText('学生注册')
            self.admin_is_here = True

    # 打开创建学校页面
    def open_add_school_page(self):
        self.stackedWidget.setCurrentIndex(2)
        self.show()

class HomeWindow(HomeUIMixin,QWidget):
    def __init__(self):
        super(HomeWindow, self).__init__()
        self.setupUi(self)

        self.open_home_page()
        self.home_window_init()

    # 主页数据初始化
    def home_window_init(self):
        self.load_school_name()

        if login_user_type == 'Admin':
            self.admin_init()
        elif login_user_type == 'Teacher':
            self.teacher_init()
        elif login_user_type == 'Student':
            self.student_init()

    # 管理员数据初始化
    def admin_init(self):
        # self.stackedWidget.setCurrentIndex(0)
        pass

    # 学生数据初始化
    def student_init(self):
        self.teacher_init()
        self.pushButton_6.close()

    # 老师数据初始化
    def teacher_init(self):
        self.pushButton_2.close()
        self.pushButton_4.close()
        self.pushButton_5.close()
        self.pushButton_3.setText('查看课程')
        # self.stackedWidget.setCurrentIndex(1)

    # 学校名字加载功能
    def load_school_name(self, combobox=None):
        school_name_list = common_interface.get_all_school_name()
        if login_user_type == 'Admin' and not combobox:
            school_name_list.append('添加学校')
            combobox = self.comboBox
        if not combobox:
            combobox = self.comboBox

        combobox.close()

        for index, school_name in enumerate(school_name_list):
            self.combobox.addItem("")
            self.comboBox.setItemText(index, _translate("self", school_name))


    # 切换学校
    def change_school(self):
        test_logger.debug('切换学校')
        current_text = self.comboBox.currentText()
        if current_text == '添加学校':
            login_window.show()
            login_window.open_add_school_page()

    # 打开主页
    def open_home_page(self):
        test_logger.debug('打开主页')
        self.stackedWidget.setCurrentIndex(0)

    # 打开学员管理
    def open_stu_list_page(self):
        self.stackedWidget.setCurrentIndex(2)

    # 打开课程管理
    def open_course_list_page(self):
        self.stackedWidget.setCurrentIndex(3)
        print('打开课程管理')

    # 打开老师管理
    def open_teacher_list_page(self):
        self.stackedWidget.setCurrentIndex(4)
        print('打开老师管理')

    # 打开财务
    def open_money_page(self):
        self.stackedWidget.setCurrentIndex(5)

    # 打开设置页面
    def open_settings_page(self):
        self.stackedWidget.setCurrentIndex(6)

    # 退出登录
    def login_out(self):
        self.close()
        # login_window:LoginWindow
        login_window.show()
        login_window.open_login_page()

        global login_name, user_type
        login_name = None
        login_user_type = None

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

def run():
    # 展示界面
    app = QApplication(sys.argv)

    global login_window
    login_window = LoginWindow()

    # setup stylesheet
    # apply_stylesheet(app, theme='dark_teal.xml')
    # apply_stylesheet(app, theme='light_blue.xml')

    login_window.show()
    sys.excepthook = except_hook # 重新定义异常挂钩
    sys.exit(app.exec())