# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\storage.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(637, 338)
        Form.setStyleSheet("background-color: #A0B9D0;\n"
"color: #3d5673;")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(25, 25, 25, 15)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_93 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        self.label_93.setFont(font)
        self.label_93.setObjectName("label_93")
        self.verticalLayout.addWidget(self.label_93)
        self.tableWidget_2 = QtWidgets.QTableWidget(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(-1)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setStyleSheet("QTableWidget {\n"
"    border-radius: 15px;\n"
"    border: 1px solid #3d5673;\n"
"    background-color: #A0B9D0;\n"
"    padding:10px;\n"
"    padding-left:20px;\n"
"    gridline-color: #3d5673;\n"
"    color:#3B3561;\n"
"    font-family: \'Times New Roman\', serif;\n"
"    font-size: 15px;\n"
"}\n"
"QHeaderView {\n"
"    background-color: #A0B9D0;\n"
"    border-radius: 10px;\n"
"    color:#3B3561;\n"
"    font-family: \'Times New Roman\', serif;\n"
"    font-size: 1s5px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #A0B9D0;\n"
"    border: none;\n"
"    border-radius: 25px;\n"
"    font-family: \'Times New Roman\', serif;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #A0B9D0;\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"}\n"
"QScrollArea{\n"
"    border:none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border:none;\n"
"    background: #A0B9D0;\n"
"    width: 8px;\n"
"    border-radius:5px;\n"
"    padding-top:5px;\n"
"    padding-left:2px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #3E8989;\n"
"    min-height: 20px;\n"
"    border-radius:3px;\n"
"    padding-left: 15px\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border:none;\n"
"    background: #A0B9D0;\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border:none;\n"
"    background: #A0B9D0;\n"
"    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical {\n"
"    background: #A0B9D0;\n"
"}\n"
"\n"
"QScrollBar::sub-page:vertical {\n"
"    background: #A0B9D0;\n"
"}\n"
"\n"
"/*Horizontal scrollbar*/\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #A0B9D0;\n"
"    height: 8px;\n"
"    border-radius: 5px;\n"
"    padding-top: 2px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #3E8989;\n"
"    min-width: 20px;\n"
"    border-radius: 3px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: #A0B9D0;\n"
"    width: 0px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: #A0B9D0;\n"
"    width: 0px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal {\n"
"    background: #A0B9D0;\n"
"}\n"
"\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: #A0B9D0;\n"
"}\n"
"\n"
"QTableView::item{\n"
"    padding-left: 20px;\n"
"    textAlignment: center\n"
"}\n"
"QTableView::item:selected{\n"
"    selection-background-color: #3B3561;\n"
"    selection-color: white;\n"
"}\n"
"")
        self.tableWidget_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_2.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_2.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_2.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(50)
        self.verticalLayout.addWidget(self.tableWidget_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_93.setText(_translate("Form", "Disk Partition"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Device"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Total Storage"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Used Storage"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Free Storage"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Percent"))
