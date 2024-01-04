# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\os_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(674, 441)
        Form.setStyleSheet("#Form{\n"
"    background-color: #A0B9D0;\n"
"    color: #3d5673;\n"
"}\n"
"QLabel{\n"
"    color: #3d5673;\n"
"}\n"
"#topic{\n"
"    padding-left:10px;\n"
"    padding-top:20px;\n"
"    padding-bottom:20px;    \n"
"}\n"
"#frame_7{\n"
"    background-color: #A0B9D0;\n"
"    border-radius:15px;\n"
"    padding: 5px;\n"
"    color: #3d5673;\n"
"    border: 1px solid #3d5673;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(25, -1, 25, 15)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topic = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(13)
        font.setBold(True)
        self.topic.setFont(font)
        self.topic.setObjectName("topic")
        self.verticalLayout.addWidget(self.topic, 0, QtCore.Qt.AlignTop)
        self.frame_7 = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_16.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_16.setSpacing(15)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.label_99 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        font.setBold(True)
        self.label_99.setFont(font)
        self.label_99.setObjectName("label_99")
        self.gridLayout_16.addWidget(self.label_99, 4, 2, 1, 1)
        self.txt_system = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(True)
        self.txt_system.setFont(font)
        self.txt_system.setObjectName("txt_system")
        self.gridLayout_16.addWidget(self.txt_system, 3, 0, 1, 2)
        self.txt_sysdate = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.txt_sysdate.setFont(font)
        self.txt_sysdate.setObjectName("txt_sysdate")
        self.gridLayout_16.addWidget(self.txt_sysdate, 6, 1, 1, 1)
        self.txt_systime = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.txt_systime.setFont(font)
        self.txt_systime.setObjectName("txt_systime")
        self.gridLayout_16.addWidget(self.txt_systime, 6, 3, 1, 1)
        self.label_101 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        font.setBold(True)
        self.label_101.setFont(font)
        self.label_101.setObjectName("label_101")
        self.gridLayout_16.addWidget(self.label_101, 6, 2, 1, 1)
        self.txt_machine = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.txt_machine.setFont(font)
        self.txt_machine.setObjectName("txt_machine")
        self.gridLayout_16.addWidget(self.txt_machine, 5, 3, 1, 1)
        self.label_91 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        font.setBold(True)
        self.label_91.setFont(font)
        self.label_91.setObjectName("label_91")
        self.gridLayout_16.addWidget(self.label_91, 6, 0, 1, 1)
        self.label_90 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        font.setBold(True)
        self.label_90.setFont(font)
        self.label_90.setObjectName("label_90")
        self.gridLayout_16.addWidget(self.label_90, 5, 0, 1, 1)
        self.label_89 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        font.setBold(True)
        self.label_89.setFont(font)
        self.label_89.setObjectName("label_89")
        self.gridLayout_16.addWidget(self.label_89, 4, 0, 1, 1)
        self.txt_release = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.txt_release.setFont(font)
        self.txt_release.setObjectName("txt_release")
        self.gridLayout_16.addWidget(self.txt_release, 4, 3, 1, 1)
        self.txt_version = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.txt_version.setFont(font)
        self.txt_version.setObjectName("txt_version")
        self.gridLayout_16.addWidget(self.txt_version, 5, 1, 1, 1)
        self.txt_node_name = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.txt_node_name.setFont(font)
        self.txt_node_name.setObjectName("txt_node_name")
        self.gridLayout_16.addWidget(self.txt_node_name, 4, 1, 1, 1)
        self.label_100 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        font.setBold(True)
        self.label_100.setFont(font)
        self.label_100.setObjectName("label_100")
        self.gridLayout_16.addWidget(self.label_100, 5, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_7)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.topic.setText(_translate("Form", "OS Information"))
        self.label_99.setText(_translate("Form", "Release"))
        self.txt_system.setText(_translate("Form", "N/A (Để tên system luôn)"))
        self.txt_sysdate.setText(_translate("Form", "N/A"))
        self.txt_systime.setText(_translate("Form", "N/A"))
        self.label_101.setText(_translate("Form", "System Time"))
        self.txt_machine.setText(_translate("Form", "N/A"))
        self.label_91.setText(_translate("Form", "System Date"))
        self.label_90.setText(_translate("Form", "Version"))
        self.label_89.setText(_translate("Form", "Node Name"))
        self.txt_release.setText(_translate("Form", "N/A"))
        self.txt_version.setText(_translate("Form", "N/A"))
        self.txt_node_name.setText(_translate("Form", "N/A"))
        self.label_100.setText(_translate("Form", "Machine"))
