from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import main_ui
from login import loginWindow
from service import service
from settings import grade
from baseinfo import student
from baseinfo import result
from settings import Class
from settings import subject
from settings import examkinds
from query import studentinfo
from query import resultinfo


import datetime
class MainWindow(QtWidgets.QMainWindow,loginWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.setFixedSize(431, 287)
        self.label.setPixmap(QtGui.QPixmap("./image/login_image.png"))
        self.pushButton.clicked.connect(self.openMain)
        self.pushButton_2.clicked.connect(self.close)
        self.lineEdit_2.editingFinished.connect(self.openMain)  #输入密码后按下回车键也可以登录
    def openMain(self):
        userName = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if userName != "" and password != "":
            print("hello")
            result = service.query('select * from tb_user where userName = %s and userPwd = %s',(userName,password))
            if len(result) > 0:
                self.mainWindows = main_ui.Ui_mainWindow()
                self.mainWindows.label.setPixmap(QtGui.QPixmap("./image/login_image.png"))
                self.mainWindows.statusbar.showMessage("当前用户：{} | 登录时间：{} | {}".format(userName,datetime.datetime.now(),"四曲实验室"))
                self.mainWindows.setFixedSize(431, 450)
                self.mainWindows.menu.triggered[QtWidgets.QAction].connect(self.openSet)    #为基础设置菜单中的QAaction绑定triggered信号
                self.mainWindows.menu_2.triggered.connect(self.openSet)  #为学生管理菜单中的QAaction绑定triggered信号
                self.mainWindows.menu_3.triggered.connect(self.openSet)

                self.mainWindows.show()
                self.hide()
            else:
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                QMessageBox.warning(None, "警告", "账号或密码错误", QMessageBox.Ok)

        else:
            QMessageBox.warning(None, "警告", "用户名或密码不能为空！", QMessageBox.Ok)

    def openSet(self,m):
        if m.text() == "年级设置":
            self.gradeWindow = grade.Ui_MainWindow()
            self.gradeWindow.show()
        if m.text() == "班级设置":
            self.classWindow = Class.Ui_MainWindow()
            self.classWindow.show()
        if m.text() == "信息管理":
            self.studentWindow = student.Ui_MainWindow()
            self.studentWindow.show()
        if m.text() == "考试科目设置":
            self.subjectWindow = subject.Ui_MainWindow()
            self.subjectWindow.show()
        if m.text() == "考试类别":
            self.examkindsWindow = examkinds.Ui_MainWindow()
            self.examkindsWindow.show()
        if m.text() == "成绩管理":
            self.resultWindow = result.Ui_MainWindow()
            self.resultWindow.show()
        if m.text() == "学生信息查询":
            self.studentinfoWindow = studentinfo.Ui_MainWindow()
            self.studentinfoWindow.show()
        if m.text() == "成绩信息查询":
            self.resultinfoWindow = resultinfo.Ui_MainWindow()
            self.resultinfoWindow.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())