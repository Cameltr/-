# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(615, 558)
        self.label = QtWidgets.QLabel(login)
        self.label.setGeometry(QtCore.QRect(-70, 0, 731, 561))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("familytreeapp/background.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(login)
        self.label_2.setGeometry(QtCore.QRect(130, 40, 141, 501))
        font = QtGui.QFont()
        font.setFamily("田氏颜体大字库")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(login)
        self.pushButton.setGeometry(QtCore.QRect(360, 430, 141, 51))
        font = QtGui.QFont()
        font.setFamily("田氏颜体大字库")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(165, 165, 165);\n"
"color:white;\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "家谱信息管理系统"))
        self.label_2.setText(_translate("login", "家\n"
"谱\n"
"信\n"
"息\n"
"管\n"
"理\n"
"系\n"
"统\n"
""))
        self.pushButton.setText(_translate("login", "开始使用"))
