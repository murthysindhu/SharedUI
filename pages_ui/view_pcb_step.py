# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_pcb_step.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1097, 705)
        self.lineEdit_26 = QtWidgets.QLineEdit(Form)
        self.lineEdit_26.setGeometry(QtCore.QRect(10, 640, 61, 20))
        self.lineEdit_26.setReadOnly(True)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.listIssues = QtWidgets.QListWidget(Form)
        self.listIssues.setGeometry(QtCore.QRect(10, 470, 721, 171))
        self.listIssues.setObjectName("listIssues")
        self.leStatus = QtWidgets.QLineEdit(Form)
        self.leStatus.setGeometry(QtCore.QRect(70, 640, 171, 20))
        self.leStatus.setText("")
        self.leStatus.setReadOnly(True)
        self.leStatus.setObjectName("leStatus")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(370, 20, 331, 41))
        self.label.setObjectName("label")
        self.ckCheckFeet = QtWidgets.QCheckBox(Form)
        self.ckCheckFeet.setGeometry(QtCore.QRect(10, 390, 341, 31))
        self.ckCheckFeet.setObjectName("ckCheckFeet")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(380, 300, 101, 17))
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 201, 111))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.sbID = QtWidgets.QSpinBox(self.frame)
        self.sbID.setGeometry(QtCore.QRect(110, 0, 91, 21))
        self.sbID.setObjectName("sbID")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 111, 21))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_28.setGeometry(QtCore.QRect(0, 20, 111, 20))
        self.lineEdit_28.setReadOnly(True)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.pbSave = QtWidgets.QPushButton(self.frame)
        self.pbSave.setGeometry(QtCore.QRect(20, 80, 71, 21))
        self.pbSave.setObjectName("pbSave")
        self.pbCancel = QtWidgets.QPushButton(self.frame)
        self.pbCancel.setGeometry(QtCore.QRect(100, 80, 71, 21))
        self.pbCancel.setObjectName("pbCancel")
        self.pbNew = QtWidgets.QPushButton(self.frame)
        self.pbNew.setEnabled(True)
        self.pbNew.setGeometry(QtCore.QRect(20, 50, 71, 21))
        self.pbNew.setObjectName("pbNew")
        self.pbEdit = QtWidgets.QPushButton(self.frame)
        self.pbEdit.setGeometry(QtCore.QRect(100, 50, 71, 21))
        self.pbEdit.setObjectName("pbEdit")
        self.cbInstitution = QtWidgets.QComboBox(self.frame)
        self.cbInstitution.setGeometry(QtCore.QRect(110, 20, 91, 21))
        self.cbInstitution.setObjectName("cbInstitution")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(750, 120, 191, 16))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 300, 121, 17))
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 140, 691, 141))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pbClear1 = QtWidgets.QPushButton(self.frame_2)
        self.pbClear1.setGeometry(QtCore.QRect(640, 20, 51, 21))
        self.pbClear1.setObjectName("pbClear1")
        self.pbGoModule4 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoModule4.setGeometry(QtCore.QRect(580, 120, 51, 21))
        self.pbGoModule4.setObjectName("pbGoModule4")
        self.leModule5 = QtWidgets.QLineEdit(self.frame_2)
        self.leModule5.setGeometry(QtCore.QRect(490, 100, 91, 20))
        self.leModule5.setObjectName("leModule5")
        self.sbTool2 = QtWidgets.QSpinBox(self.frame_2)
        self.sbTool2.setGeometry(QtCore.QRect(80, 40, 51, 22))
        self.sbTool2.setMinimum(-1)
        self.sbTool2.setMaximum(2147483647)
        self.sbTool2.setObjectName("sbTool2")
        self.leModule3 = QtWidgets.QLineEdit(self.frame_2)
        self.leModule3.setGeometry(QtCore.QRect(490, 60, 91, 20))
        self.leModule3.setObjectName("leModule3")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_23.setGeometry(QtCore.QRect(190, 0, 141, 20))
        self.lineEdit_23.setReadOnly(True)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.pbGoTool1 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoTool1.setGeometry(QtCore.QRect(130, 20, 51, 21))
        self.pbGoTool1.setObjectName("pbGoTool1")
        self.sbTool5 = QtWidgets.QSpinBox(self.frame_2)
        self.sbTool5.setGeometry(QtCore.QRect(80, 100, 51, 22))
        self.sbTool5.setMinimum(-1)
        self.sbTool5.setMaximum(2147483647)
        self.sbTool5.setObjectName("sbTool5")
        self.pbGoModule3 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoModule3.setGeometry(QtCore.QRect(580, 60, 51, 21))
        self.pbGoModule3.setObjectName("pbGoModule3")
        self.lePcb6 = QtWidgets.QLineEdit(self.frame_2)
        self.lePcb6.setGeometry(QtCore.QRect(190, 120, 91, 20))
        self.lePcb6.setObjectName("lePcb6")
        self.pbGoModule2 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoModule2.setGeometry(QtCore.QRect(580, 40, 51, 21))
        self.pbGoModule2.setObjectName("pbGoModule2")
        self.leProtomodule5 = QtWidgets.QLineEdit(self.frame_2)
        self.leProtomodule5.setGeometry(QtCore.QRect(340, 100, 91, 20))
        self.leProtomodule5.setObjectName("leProtomodule5")
        self.pbGoTool6 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoTool6.setGeometry(QtCore.QRect(130, 120, 51, 21))
        self.pbGoTool6.setObjectName("pbGoTool6")
        self.sbTool3 = QtWidgets.QSpinBox(self.frame_2)
        self.sbTool3.setGeometry(QtCore.QRect(80, 60, 51, 22))
        self.sbTool3.setMinimum(-1)
        self.sbTool3.setMaximum(2147483647)
        self.sbTool3.setObjectName("sbTool3")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_12.setGeometry(QtCore.QRect(0, 0, 71, 20))
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.pbGoModule5 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoModule5.setGeometry(QtCore.QRect(580, 80, 51, 21))
        self.pbGoModule5.setObjectName("pbGoModule5")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_18.setGeometry(QtCore.QRect(0, 80, 71, 20))
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lePcb3 = QtWidgets.QLineEdit(self.frame_2)
        self.lePcb3.setGeometry(QtCore.QRect(190, 60, 91, 20))
        self.lePcb3.setObjectName("lePcb3")
        self.pbGoModule1 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoModule1.setGeometry(QtCore.QRect(580, 20, 51, 21))
        self.pbGoModule1.setObjectName("pbGoModule1")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_19.setGeometry(QtCore.QRect(0, 100, 71, 20))
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.pbGoTool3 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoTool3.setGeometry(QtCore.QRect(130, 60, 51, 21))
        self.pbGoTool3.setObjectName("pbGoTool3")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_13.setGeometry(QtCore.QRect(80, 0, 101, 20))
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.pbGoProtomodule2 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoProtomodule2.setGeometry(QtCore.QRect(430, 40, 51, 21))
        self.pbGoProtomodule2.setObjectName("pbGoProtomodule2")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_14.setGeometry(QtCore.QRect(490, 0, 141, 20))
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_20.setGeometry(QtCore.QRect(0, 120, 71, 21))
        self.lineEdit_20.setReadOnly(True)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_22.setGeometry(QtCore.QRect(340, 0, 141, 20))
        self.lineEdit_22.setReadOnly(True)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lePcb5 = QtWidgets.QLineEdit(self.frame_2)
        self.lePcb5.setGeometry(QtCore.QRect(190, 100, 91, 20))
        self.lePcb5.setObjectName("lePcb5")
        self.pbGoPcb1 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoPcb1.setGeometry(QtCore.QRect(280, 20, 51, 21))
        self.pbGoPcb1.setObjectName("pbGoPcb1")
        self.leProtomodule6 = QtWidgets.QLineEdit(self.frame_2)
        self.leProtomodule6.setGeometry(QtCore.QRect(340, 120, 91, 20))
        self.leProtomodule6.setObjectName("leProtomodule6")
        self.leModule2 = QtWidgets.QLineEdit(self.frame_2)
        self.leModule2.setGeometry(QtCore.QRect(490, 40, 91, 20))
        self.leModule2.setObjectName("leModule2")
        self.pbGoProtomodule4 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoProtomodule4.setGeometry(QtCore.QRect(430, 80, 51, 21))
        self.pbGoProtomodule4.setObjectName("pbGoProtomodule4")
        self.lePcb4 = QtWidgets.QLineEdit(self.frame_2)
        self.lePcb4.setGeometry(QtCore.QRect(190, 80, 91, 20))
        self.lePcb4.setObjectName("lePcb4")
        self.sbTool6 = QtWidgets.QSpinBox(self.frame_2)
        self.sbTool6.setGeometry(QtCore.QRect(80, 120, 51, 21))
        self.sbTool6.setMinimum(-1)
        self.sbTool6.setMaximum(2147483647)
        self.sbTool6.setObjectName("sbTool6")
        self.leModule4 = QtWidgets.QLineEdit(self.frame_2)
        self.leModule4.setGeometry(QtCore.QRect(490, 80, 91, 20))
        self.leModule4.setObjectName("leModule4")
        self.leProtomodule3 = QtWidgets.QLineEdit(self.frame_2)
        self.leProtomodule3.setGeometry(QtCore.QRect(340, 60, 91, 20))
        self.leProtomodule3.setObjectName("leProtomodule3")
        self.lePcb2 = QtWidgets.QLineEdit(self.frame_2)
        self.lePcb2.setGeometry(QtCore.QRect(190, 40, 91, 20))
        self.lePcb2.setObjectName("lePcb2")
        self.pbGoModule6 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoModule6.setGeometry(QtCore.QRect(580, 100, 51, 21))
        self.pbGoModule6.setObjectName("pbGoModule6")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_17.setGeometry(QtCore.QRect(0, 60, 71, 20))
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.leProtomodule4 = QtWidgets.QLineEdit(self.frame_2)
        self.leProtomodule4.setGeometry(QtCore.QRect(340, 80, 91, 20))
        self.leProtomodule4.setObjectName("leProtomodule4")
        self.leModule1 = QtWidgets.QLineEdit(self.frame_2)
        self.leModule1.setGeometry(QtCore.QRect(490, 20, 91, 20))
        self.leModule1.setObjectName("leModule1")
        self.pbClear6 = QtWidgets.QPushButton(self.frame_2)
        self.pbClear6.setGeometry(QtCore.QRect(640, 120, 51, 21))
        self.pbClear6.setObjectName("pbClear6")
        self.pbGoProtomodule3 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoProtomodule3.setGeometry(QtCore.QRect(430, 60, 51, 21))
        self.pbGoProtomodule3.setObjectName("pbGoProtomodule3")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_15.setGeometry(QtCore.QRect(0, 20, 71, 20))
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lePcb1 = QtWidgets.QLineEdit(self.frame_2)
        self.lePcb1.setGeometry(QtCore.QRect(190, 20, 91, 20))
        self.lePcb1.setObjectName("lePcb1")
        self.leProtomodule2 = QtWidgets.QLineEdit(self.frame_2)
        self.leProtomodule2.setGeometry(QtCore.QRect(340, 40, 91, 20))
        self.leProtomodule2.setObjectName("leProtomodule2")
        self.pbGoPcb3 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoPcb3.setGeometry(QtCore.QRect(280, 60, 51, 21))
        self.pbGoPcb3.setObjectName("pbGoPcb3")
        self.pbClear5 = QtWidgets.QPushButton(self.frame_2)
        self.pbClear5.setGeometry(QtCore.QRect(640, 100, 51, 21))
        self.pbClear5.setObjectName("pbClear5")
        self.pbGoProtomodule5 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoProtomodule5.setGeometry(QtCore.QRect(430, 100, 51, 21))
        self.pbGoProtomodule5.setObjectName("pbGoProtomodule5")
        self.pbGoProtomodule6 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoProtomodule6.setGeometry(QtCore.QRect(430, 120, 51, 21))
        self.pbGoProtomodule6.setObjectName("pbGoProtomodule6")
        self.pbGoPcb2 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoPcb2.setGeometry(QtCore.QRect(280, 40, 51, 21))
        self.pbGoPcb2.setObjectName("pbGoPcb2")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_16.setGeometry(QtCore.QRect(0, 40, 71, 20))
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.sbTool4 = QtWidgets.QSpinBox(self.frame_2)
        self.sbTool4.setGeometry(QtCore.QRect(80, 80, 51, 22))
        self.sbTool4.setMinimum(-1)
        self.sbTool4.setMaximum(2147483647)
        self.sbTool4.setObjectName("sbTool4")
        self.pbGoPcb6 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoPcb6.setGeometry(QtCore.QRect(280, 120, 51, 21))
        self.pbGoPcb6.setObjectName("pbGoPcb6")
        self.pbClear2 = QtWidgets.QPushButton(self.frame_2)
        self.pbClear2.setGeometry(QtCore.QRect(640, 40, 51, 21))
        self.pbClear2.setObjectName("pbClear2")
        self.pbGoTool4 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoTool4.setGeometry(QtCore.QRect(130, 80, 51, 21))
        self.pbGoTool4.setObjectName("pbGoTool4")
        self.leModule6 = QtWidgets.QLineEdit(self.frame_2)
        self.leModule6.setGeometry(QtCore.QRect(490, 120, 91, 20))
        self.leModule6.setObjectName("leModule6")
        self.pbGoPcb5 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoPcb5.setGeometry(QtCore.QRect(280, 100, 51, 21))
        self.pbGoPcb5.setObjectName("pbGoPcb5")
        self.pbGoTool5 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoTool5.setGeometry(QtCore.QRect(130, 100, 51, 21))
        self.pbGoTool5.setObjectName("pbGoTool5")
        self.pbGoPcb4 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoPcb4.setGeometry(QtCore.QRect(280, 80, 51, 21))
        self.pbGoPcb4.setObjectName("pbGoPcb4")
        self.leProtomodule1 = QtWidgets.QLineEdit(self.frame_2)
        self.leProtomodule1.setGeometry(QtCore.QRect(340, 20, 91, 20))
        self.leProtomodule1.setObjectName("leProtomodule1")
        self.sbTool1 = QtWidgets.QSpinBox(self.frame_2)
        self.sbTool1.setGeometry(QtCore.QRect(80, 20, 51, 22))
        self.sbTool1.setMinimum(-1)
        self.sbTool1.setMaximum(2147483647)
        self.sbTool1.setObjectName("sbTool1")
        self.pbGoProtomodule1 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoProtomodule1.setGeometry(QtCore.QRect(430, 20, 51, 21))
        self.pbGoProtomodule1.setObjectName("pbGoProtomodule1")
        self.pbClear3 = QtWidgets.QPushButton(self.frame_2)
        self.pbClear3.setGeometry(QtCore.QRect(640, 60, 51, 21))
        self.pbClear3.setObjectName("pbClear3")
        self.pbClear4 = QtWidgets.QPushButton(self.frame_2)
        self.pbClear4.setGeometry(QtCore.QRect(640, 80, 51, 21))
        self.pbClear4.setObjectName("pbClear4")
        self.pbGoTool2 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoTool2.setGeometry(QtCore.QRect(130, 40, 51, 21))
        self.pbGoTool2.setObjectName("pbGoTool2")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(10, 320, 281, 61))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.leBatchAraldite = QtWidgets.QLineEdit(self.frame_3)
        self.leBatchAraldite.setGeometry(QtCore.QRect(160, 40, 71, 20))
        self.leBatchAraldite.setObjectName("leBatchAraldite")
        self.pbGoTrayAssembly = QtWidgets.QPushButton(self.frame_3)
        self.pbGoTrayAssembly.setGeometry(QtCore.QRect(230, 20, 51, 21))
        self.pbGoTrayAssembly.setObjectName("pbGoTrayAssembly")
        self.pbGoTrayComponent = QtWidgets.QPushButton(self.frame_3)
        self.pbGoTrayComponent.setGeometry(QtCore.QRect(230, 0, 51, 21))
        self.pbGoTrayComponent.setObjectName("pbGoTrayComponent")
        self.sbTrayComponent = QtWidgets.QSpinBox(self.frame_3)
        self.sbTrayComponent.setGeometry(QtCore.QRect(160, 0, 71, 21))
        self.sbTrayComponent.setMinimum(-1)
        self.sbTrayComponent.setMaximum(999999)
        self.sbTrayComponent.setObjectName("sbTrayComponent")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_11.setGeometry(QtCore.QRect(0, 40, 161, 21))
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_24.setGeometry(QtCore.QRect(0, 0, 161, 21))
        self.lineEdit_24.setReadOnly(True)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.sbTrayAssembly = QtWidgets.QSpinBox(self.frame_3)
        self.sbTrayAssembly.setGeometry(QtCore.QRect(160, 20, 71, 21))
        self.sbTrayAssembly.setMinimum(-1)
        self.sbTrayAssembly.setMaximum(999999)
        self.sbTrayAssembly.setObjectName("sbTrayAssembly")
        self.pbGoBatchAraldite = QtWidgets.QPushButton(self.frame_3)
        self.pbGoBatchAraldite.setGeometry(QtCore.QRect(230, 40, 51, 21))
        self.pbGoBatchAraldite.setObjectName("pbGoBatchAraldite")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_21.setGeometry(QtCore.QRect(0, 20, 161, 21))
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(380, 320, 331, 91))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_10.setGeometry(QtCore.QRect(0, 50, 91, 21))
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_27.setGeometry(QtCore.QRect(0, 70, 91, 21))
        self.lineEdit_27.setReadOnly(True)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.dtRunStop = QtWidgets.QDateTimeEdit(self.frame_4)
        self.dtRunStop.setGeometry(QtCore.QRect(90, 70, 151, 21))
        self.dtRunStop.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dtRunStop.setMaximumDate(QtCore.QDate(2030, 12, 31))
        self.dtRunStop.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dtRunStop.setCalendarPopup(True)
        self.dtRunStop.setObjectName("dtRunStop")
        self.dtRunStart = QtWidgets.QDateTimeEdit(self.frame_4)
        self.dtRunStart.setGeometry(QtCore.QRect(90, 50, 151, 21))
        self.dtRunStart.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dtRunStart.setMaximumDate(QtCore.QDate(2030, 12, 31))
        self.dtRunStart.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dtRunStart.setCalendarPopup(True)
        self.dtRunStart.setObjectName("dtRunStart")
        self.cbUserPerformed = QtWidgets.QComboBox(self.frame_4)
        self.cbUserPerformed.setGeometry(QtCore.QRect(160, 0, 171, 21))
        self.cbUserPerformed.setObjectName("cbUserPerformed")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 161, 21))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(0, 20, 161, 21))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.leLocation = QtWidgets.QLineEdit(self.frame_4)
        self.leLocation.setGeometry(QtCore.QRect(160, 20, 171, 20))
        self.leLocation.setObjectName("leLocation")
        self.pbRunStopNow = QtWidgets.QPushButton(self.frame_4)
        self.pbRunStopNow.setGeometry(QtCore.QRect(240, 70, 91, 21))
        self.pbRunStopNow.setObjectName("pbRunStopNow")
        self.pbRunStartNow = QtWidgets.QPushButton(self.frame_4)
        self.pbRunStartNow.setGeometry(QtCore.QRect(240, 50, 91, 21))
        self.pbRunStartNow.setObjectName("pbRunStartNow")
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setGeometry(QtCore.QRect(750, 140, 281, 251))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.pbAddPart = QtWidgets.QPushButton(self.frame_5)
        self.pbAddPart.setGeometry(QtCore.QRect(0, 230, 101, 21))
        self.pbAddPart.setObjectName("pbAddPart")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_29.setGeometry(QtCore.QRect(0, 200, 61, 20))
        self.lineEdit_29.setReadOnly(True)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.pbCancelSearch = QtWidgets.QPushButton(self.frame_5)
        self.pbCancelSearch.setGeometry(QtCore.QRect(120, 230, 101, 21))
        self.pbCancelSearch.setObjectName("pbCancelSearch")
        self.lwPartList = QtWidgets.QListWidget(self.frame_5)
        self.lwPartList.setGeometry(QtCore.QRect(0, 0, 281, 201))
        self.lwPartList.setObjectName("lwPartList")
        self.leSearchStatus = QtWidgets.QLineEdit(self.frame_5)
        self.leSearchStatus.setGeometry(QtCore.QRect(60, 200, 221, 20))
        self.leSearchStatus.setText("")
        self.leSearchStatus.setReadOnly(True)
        self.leSearchStatus.setObjectName("leSearchStatus")

        self.retranslateUi(Form)
        self.cbInstitution.setCurrentIndex(-1)
        self.cbUserPerformed.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_26.setText(_translate("Form", "Status:"))
        self.listIssues.setToolTip(_translate("Form", "list of issues"))
        self.label.setText(_translate("Form", "Warning:  all parts must be downloaded locally\n"
"before assembly"))
        self.ckCheckFeet.setText(_translate("Form", "Check:  correct feet are installed on pickup tool"))
        self.label_2.setText(_translate("Form", "Assembly run"))
        self.lineEdit.setText(_translate("Form", "PCB step ID"))
        self.lineEdit_28.setText(_translate("Form", "Institution"))
        self.pbSave.setText(_translate("Form", "Save"))
        self.pbCancel.setText(_translate("Form", "Cancel"))
        self.pbNew.setText(_translate("Form", "New"))
        self.pbEdit.setText(_translate("Form", "Edit"))
        self.cbInstitution.setItemText(0, _translate("Form", "CERN"))
        self.cbInstitution.setItemText(1, _translate("Form", "FNAL"))
        self.cbInstitution.setItemText(2, _translate("Form", "UCSB"))
        self.cbInstitution.setItemText(3, _translate("Form", "UMN"))
        self.cbInstitution.setItemText(4, _translate("Form", "HEPHY"))
        self.cbInstitution.setItemText(5, _translate("Form", "HPK"))
        self.cbInstitution.setItemText(6, _translate("Form", "IHEP"))
        self.label_4.setText(_translate("Form", "Parts to add:"))
        self.label_3.setText(_translate("Form", "Assembly info"))
        self.pbClear1.setText(_translate("Form", "clear"))
        self.pbGoModule4.setText(_translate("Form", "go to"))
        self.lineEdit_23.setText(_translate("Form", "PCB ID"))
        self.pbGoTool1.setText(_translate("Form", "go to"))
        self.pbGoModule3.setText(_translate("Form", "go to"))
        self.pbGoModule2.setText(_translate("Form", "go to"))
        self.pbGoTool6.setText(_translate("Form", "go to"))
        self.lineEdit_12.setText(_translate("Form", "position"))
        self.pbGoModule5.setText(_translate("Form", "go to"))
        self.lineEdit_18.setText(_translate("Form", "4 (2, 2)"))
        self.pbGoModule1.setText(_translate("Form", "go to"))
        self.lineEdit_19.setText(_translate("Form", "5 (3, 1)"))
        self.pbGoTool3.setText(_translate("Form", "go to"))
        self.lineEdit_13.setText(_translate("Form", "PCB tool ID"))
        self.pbGoProtomodule2.setText(_translate("Form", "go to"))
        self.lineEdit_14.setText(_translate("Form", "Module ID assigned"))
        self.lineEdit_20.setText(_translate("Form", "6 (3, 2)"))
        self.lineEdit_22.setText(_translate("Form", "Protomodule ID"))
        self.pbGoPcb1.setText(_translate("Form", "go to"))
        self.pbGoProtomodule4.setText(_translate("Form", "go to"))
        self.pbGoModule6.setText(_translate("Form", "go to"))
        self.lineEdit_17.setText(_translate("Form", "3 (2, 1)"))
        self.pbClear6.setText(_translate("Form", "clear"))
        self.pbGoProtomodule3.setText(_translate("Form", "go to"))
        self.lineEdit_15.setText(_translate("Form", "1 (1, 1)"))
        self.pbGoPcb3.setText(_translate("Form", "go to"))
        self.pbClear5.setText(_translate("Form", "clear"))
        self.pbGoProtomodule5.setText(_translate("Form", "go to"))
        self.pbGoProtomodule6.setText(_translate("Form", "go to"))
        self.pbGoPcb2.setText(_translate("Form", "go to"))
        self.lineEdit_16.setText(_translate("Form", "2 (1, 2)"))
        self.pbGoPcb6.setText(_translate("Form", "go to"))
        self.pbClear2.setText(_translate("Form", "clear"))
        self.pbGoTool4.setText(_translate("Form", "go to"))
        self.pbGoPcb5.setText(_translate("Form", "go to"))
        self.pbGoTool5.setText(_translate("Form", "go to"))
        self.pbGoPcb4.setText(_translate("Form", "go to"))
        self.pbGoProtomodule1.setText(_translate("Form", "go to"))
        self.pbClear3.setText(_translate("Form", "clear"))
        self.pbClear4.setText(_translate("Form", "clear"))
        self.pbGoTool2.setText(_translate("Form", "go to"))
        self.pbGoTrayAssembly.setText(_translate("Form", "go to"))
        self.pbGoTrayComponent.setText(_translate("Form", "go to"))
        self.lineEdit_11.setText(_translate("Form", "araldite batch"))
        self.lineEdit_24.setText(_translate("Form", "component tray (PCB)"))
        self.pbGoBatchAraldite.setText(_translate("Form", "go to"))
        self.lineEdit_21.setText(_translate("Form", "assembly tray"))
        self.lineEdit_10.setText(_translate("Form", "run start"))
        self.lineEdit_27.setText(_translate("Form", "run stop"))
        self.lineEdit_2.setText(_translate("Form", "who performed step"))
        self.lineEdit_3.setText(_translate("Form", "location"))
        self.pbRunStopNow.setText(_translate("Form", "set to now"))
        self.pbRunStartNow.setText(_translate("Form", "set to now"))
        self.pbAddPart.setText(_translate("Form", "Add part"))
        self.lineEdit_29.setText(_translate("Form", "Status:"))
        self.pbCancelSearch.setText(_translate("Form", "Cancel"))
