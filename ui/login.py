# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 601)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(24)
        Form.setFont(font)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=Form)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.page)
        font = QtGui.QFont()
        font.setFamily("PingFang SC")
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(255, 38, 0);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.page)
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(100)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(79, 143, 0);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.page)
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius:10;\n"
"padding:10px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.page)
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(18)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius:10;\n"
"padding:10px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(parent=self.page)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(14)
        self.checkBox.setFont(font)
        self.checkBox.setAutoExclusive(True)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(parent=self.page)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(14)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setAutoExclusive(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(parent=self.page)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(14)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setAutoExclusive(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_2.addWidget(self.checkBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.page)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(79, 143, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 143, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:  rgb(169, 169, 169);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.page)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(79, 143, 0);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 143, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:  rgb(169, 169, 169);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.page_2)
        font = QtGui.QFont()
        font.setFamily("PingFang SC")
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"rgb(255, 38, 0)\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_7.addWidget(self.pushButton_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(30)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(parent=self.page_2)
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(100)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(79, 143, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_6.addItem(spacerItem8)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.page_2)
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(18)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border-radius:10;\n"
"padding:10px;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_6.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.page_2)
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(18)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border-radius:10;\n"
"padding:10px;")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_6.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.page_2)
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(18)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border-radius:10;\n"
"padding:10px;")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_6.addWidget(self.lineEdit_5)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(100)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.page_2)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(20)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(79, 143, 0);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 143, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:  rgb(169, 169, 169);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_10.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.page_2)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(20)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"background-color: rgb(79, 143, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 143, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:  rgb(169, 169, 169);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_10.addWidget(self.pushButton_6)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_8.addLayout(self.verticalLayout_6)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_5.addItem(spacerItem10)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.horizontalLayout_9.addLayout(self.verticalLayout_4)
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout_5.addWidget(self.stackedWidget)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(Form.login) # type: ignore
        self.pushButton_2.clicked.connect(Form.open_register_page) # type: ignore
        self.pushButton_5.clicked.connect(Form.open_login_page) # type: ignore
        self.pushButton_6.clicked.connect(Form.register) # type: ignore
        self.pushButton_4.clicked.connect(Form.close) # type: ignore
        self.pushButton_3.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "教务管理系统"))
        self.pushButton_3.setText(_translate("Form", "X"))
        self.label.setText(_translate("Form", "教务管理系统"))
        self.lineEdit.setPlaceholderText(_translate("Form", "账号"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "密码"))
        self.checkBox.setText(_translate("Form", "学生"))
        self.checkBox_2.setText(_translate("Form", "老师"))
        self.checkBox_3.setText(_translate("Form", "管理员"))
        self.pushButton.setText(_translate("Form", "登录"))
        self.pushButton_2.setText(_translate("Form", "注册"))
        self.pushButton_4.setText(_translate("Form", "X"))
        self.label_2.setText(_translate("Form", "管理员注册"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "账号"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "密码"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "确认密码"))
        self.pushButton_5.setText(_translate("Form", "登录"))
        self.pushButton_6.setText(_translate("Form", "注册"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
