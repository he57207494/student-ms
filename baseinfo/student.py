# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox

from service import service


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.setUp()

    #添加的初始化设置
    def setUp(self):
        self.getClassAndGrade()
        self.tableWidget.itemSelectionChanged.connect(self.getItem)
        self.pushButton_2.clicked.connect(self.add)
        self.pushButton.clicked.connect(self.query)
        self.pushButton_3.clicked.connect(self.edit)
        self.pushButton_4.clicked.connect(self.delete)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(763, 357)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./image/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 761, 191))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 61, 21))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(80, 10, 61, 21))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 10, 61, 21))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(210, 10, 61, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 10, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 10, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(520, 10, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 250, 61, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 250, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 250, 61, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(400, 250, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 250, 41, 21))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(570, 250, 51, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(530, 280, 31, 21))
        self.label_6.setObjectName("label_6")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(570, 280, 61, 21))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(340, 280, 61, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(160, 280, 61, 21))
        self.label_8.setObjectName("label_8")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(220, 280, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(400, 280, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 250, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 711, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "学生信息管理"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "学生编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "学生姓名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "班级"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "年龄"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "性别"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "家庭地址"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "联系电话"))
        self.label.setText(_translate("MainWindow", "所属年级："))
        self.label_2.setText(_translate("MainWindow", "所属班级："))
        self.pushButton.setText(_translate("MainWindow", "刷新"))
        self.pushButton_2.setText(_translate("MainWindow", "添加"))
        self.pushButton_3.setText(_translate("MainWindow", "修改"))
        self.pushButton_4.setText(_translate("MainWindow", "删除"))
        self.label_3.setText(_translate("MainWindow", "学生编号："))
        self.label_4.setText(_translate("MainWindow", "学生姓名："))
        self.label_5.setText(_translate("MainWindow", "年龄："))
        self.label_6.setText(_translate("MainWindow", "性别："))
        self.label_7.setText(_translate("MainWindow", "联系电话："))
        self.label_8.setText(_translate("MainWindow", "家庭住址："))
        self.label_9.setText(_translate("MainWindow", "信息设置"))

    #获取年级和班级信息，并显示在下拉框中
    def getClassAndGrade(self):
        class_result = service.query2("select * from tb_class")
        grade_result = service.query2("select * from tb_grade")

        self.comboBox_3.addItem("男")
        self.comboBox_3.addItem("女")

        for i in class_result:
            self.comboBox_2.addItem(i[2])
        for i in grade_result:
            self.comboBox.addItem(i[1])

    #添加学生信息
    def add(self):
        student_id = self.lineEdit.text()
        studentName = self.lineEdit_2.text()
        studentAge = self.lineEdit_3.text()
        studentPhone = self.lineEdit_5.text()
        studentAdress = self.lineEdit_4.text()

        if self.comboBox.currentText() != "" and self.comboBox_2.currentText() != "":
            gradeID = service.query("select gradeID from tb_grade where gradeName = %s",(self.comboBox.currentText(),))
            classID = service.query("select classID from tb_class where className = %s",(self.comboBox_2.currentText(),))
            if len(gradeID) > 0 and len(classID) > 0:
                result = service.exec("insert into tb_student(stuID,stuName,classID,gradeID,sex,age,address,phone) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                                      (student_id,studentName,classID[0][0],gradeID[0][0],self.comboBox_3.currentText(),studentAge,studentAdress,studentPhone))
                if result > 0:
                    QtWidgets.QMessageBox.information(None, '提示', '信息添加成功', QtWidgets.QMessageBox.Ok)
                else:
                    QtWidgets.QMessageBox.information(None, '提示', '信息添加失败', QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(None, '提示', '年级或班级不存在', QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.warning(None, '警告', '请输入数据', QtWidgets.QMessageBox.Ok)


    #查询学生信息，并显示在表格当中
    def query(self):
        gname = self.comboBox.currentText()
        cname = self.comboBox_2.currentText()
        if gname != "" and cname != "":
            gradeID = service.query("select gradeID from tb_grade where gradeName = %s",(gname,))
            classID = service.query("select classID from tb_class where className = %s",(cname,))
            result = service.query("select * from tb_student where gradeID = %s and classID = %s",(gradeID[0][0],classID[0][0]))
            if len(result) > 0:
                self.tableWidget.setRowCount(0)
                row = len(result)
                for i in range(row):
                    self.tableWidget.insertRow(i)
                    for j in range(len(result[0]) - 1):
                        if j == 2:
                            data = QTableWidgetItem(gname+cname)
                        else:
                            data = QTableWidgetItem(str(result[i][j]))
                        self.tableWidget.setItem(i,j,data)
            else:
                QtWidgets.QMessageBox.warning(None, '警告', '查询失败', QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.warning(None, '警告', '请输入数据', QtWidgets.QMessageBox.Ok)


    def getItem(self):
        row = self.tableWidget.currentRow()
        self.lineEdit.setText(self.tableWidget.item(row,0).text())
        self.lineEdit_2.setText(self.tableWidget.item(row,1).text())
        self.lineEdit_3.setText(self.tableWidget.item(row,3).text())
        self.lineEdit_4.setText(self.tableWidget.item(row,5).text())
        self.lineEdit_5.setText(self.tableWidget.item(row,6).text())
        self.select = self.lineEdit.text()
        if self.tableWidget.item(row,4).text() == "男":
            self.comboBox_3.setCurrentIndex(0)
        else:
            self.comboBox_3.setCurrentIndex(1)


    def edit(self):
        student_id = self.lineEdit.text()
        studentName = self.lineEdit_2.text()
        studentAge = self.lineEdit_3.text()
        studentPhone = self.lineEdit_5.text()
        studentAdress = self.lineEdit_4.text()

        if self.comboBox.currentText() != "" and self.comboBox_2.currentText() != "":
            gradeID = service.query("select gradeID from tb_grade where gradeName = %s",(self.comboBox.currentText(),))
            classID = service.query("select classID from tb_class where className = %s",(self.comboBox_2.currentText(),))
            if len(gradeID) > 0 and len(classID) > 0:
                result = service.exec("update tb_student  set stuID =%s,stuName = %s,gradeID = %s, age=%s,sex=%s,address=%s,phone=%s,classID=%s where stuID = %s",
                                      (student_id,studentName,gradeID[0][0],studentAge,self.comboBox_3.currentText(),
                                       studentAdress,studentPhone,classID[0][0],student_id))
                if result > 0:
                    QtWidgets.QMessageBox.information(None, '提示', '信息修改成功', QtWidgets.QMessageBox.Ok)
                else:
                    QtWidgets.QMessageBox.information(None, '提示', '信息修改失败', QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(None, '提示', '年级或班级不存在', QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.warning(None, '警告', '请输入数据', QtWidgets.QMessageBox.Ok)


    def delete(self):
        try:
            if self.select != "":
                result = service.exec("delete from tb_student where stuID = %s",(self.select,))
                if result > 0:
                    QtWidgets.QMessageBox.information(None, '提示', '信息删除成功', QMessageBox.Ok)
                    self.tableWidget.clearContents()
                    self.query()
            else:
                QtWidgets.QMessageBox.information(None, '提示', '请选择要删除的数据', QMessageBox.Ok)
        except Exception as e:
            QtWidgets.QMessageBox.information(None, '提示', str(e), QMessageBox.Ok)