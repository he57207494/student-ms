# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(436, 412)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 100, 431, 121))
        self.label.setObjectName("label")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 436, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(mainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(mainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(mainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(mainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(mainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(mainWindow)
        self.action_6.setObjectName("action_6")

        self.action_7 = QtWidgets.QAction(mainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtWidgets.QAction(mainWindow)
        self.action_8.setObjectName("action_8")

        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menu_2.addAction(self.action_5)
        self.menu_2.addAction(self.action_6)

        self.menu_3.addAction(self.action_7)
        self.menu_3.addAction(self.action_8)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "学生成绩管理系统"))
        self.label.setText(_translate("mainWindow", "TextLabel"))
        self.menu.setTitle(_translate("mainWindow", "基础设置"))
        self.menu_2.setTitle(_translate("mainWindow", "基本信息管理"))
        self.menu_3.setTitle(_translate("mainWindow", "系统查询"))
        self.menu_4.setTitle(_translate("mainWindow", "系统管理"))
        self.action.setText(_translate("mainWindow", "年级设置"))
        self.action_2.setText(_translate("mainWindow", "班级设置"))
        self.action_3.setText(_translate("mainWindow", "考试科目设置"))
        self.action_4.setText(_translate("mainWindow", "考试类别"))
        self.action_5.setText(_translate("mainWindow", "信息管理"))
        self.action_6.setText(_translate("mainWindow", "成绩管理"))
        self.action_7.setText(_translate("mainWindow", "学生信息查询"))
        self.action_8.setText(_translate("mainWindow","成绩信息查询"))
