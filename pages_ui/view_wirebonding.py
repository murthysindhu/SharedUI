# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_wirebonding.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1199, 756)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 140, 211, 21))
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 160, 282, 21))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_29.setGeometry(QtCore.QRect(1, 0, 191, 20))
        self.lineEdit_29.setReadOnly(True)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.cbPreinspection = QtWidgets.QComboBox(self.frame_2)
        self.cbPreinspection.setGeometry(QtCore.QRect(190, 0, 92, 20))
        self.cbPreinspection.setObjectName("cbPreinspection")
        self.cbPreinspection.addItem("")
        self.cbPreinspection.addItem("")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(340, 660, 181, 21))
        self.label_4.setObjectName("label_4")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(340, 680, 241, 41))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.cbWirebondingFinalInspectionOK = QtWidgets.QComboBox(self.frame_3)
        self.cbWirebondingFinalInspectionOK.setGeometry(QtCore.QRect(150, 20, 91, 21))
        self.cbWirebondingFinalInspectionOK.setObjectName("cbWirebondingFinalInspectionOK")
        self.cbWirebondingFinalInspectionOK.addItem("")
        self.cbWirebondingFinalInspectionOK.addItem("")
        self.lineEdit_37 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_37.setGeometry(QtCore.QRect(1, 20, 151, 20))
        self.lineEdit_37.setReadOnly(True)
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.lineEdit_40 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_40.setGeometry(QtCore.QRect(1, 0, 151, 21))
        self.lineEdit_40.setReadOnly(True)
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.cbWirebondingFinalInspectionUser = QtWidgets.QComboBox(self.frame_3)
        self.cbWirebondingFinalInspectionUser.setGeometry(QtCore.QRect(150, 0, 91, 21))
        self.cbWirebondingFinalInspectionUser.setObjectName("cbWirebondingFinalInspectionUser")
        self.lineEdit_37.raise_()
        self.lineEdit_40.raise_()
        self.cbWirebondingFinalInspectionOK.raise_()
        self.cbWirebondingFinalInspectionUser.raise_()
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setGeometry(QtCore.QRect(670, 160, 282, 81))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setObjectName("frame_5")
        self.lineEdit_32 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_32.setGeometry(QtCore.QRect(1, 20, 191, 21))
        self.lineEdit_32.setReadOnly(True)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.ckTestBonds = QtWidgets.QCheckBox(self.frame_5)
        self.ckTestBonds.setGeometry(QtCore.QRect(1, 0, 161, 17))
        self.ckTestBonds.setObjectName("ckTestBonds")
        self.lineEdit_43 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_43.setGeometry(QtCore.QRect(0, 40, 191, 21))
        self.lineEdit_43.setReadOnly(True)
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.lineEdit_44 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_44.setGeometry(QtCore.QRect(0, 60, 191, 21))
        self.lineEdit_44.setReadOnly(True)
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.dsbBondPullAvg = QtWidgets.QDoubleSpinBox(self.frame_5)
        self.dsbBondPullAvg.setGeometry(QtCore.QRect(190, 40, 91, 21))
        self.dsbBondPullAvg.setObjectName("dsbBondPullAvg")
        self.dsbBondPullStd = QtWidgets.QDoubleSpinBox(self.frame_5)
        self.dsbBondPullStd.setGeometry(QtCore.QRect(190, 60, 91, 21))
        self.dsbBondPullStd.setObjectName("dsbBondPullStd")
        self.cbTestBondsPulledUser = QtWidgets.QComboBox(self.frame_5)
        self.cbTestBondsPulledUser.setGeometry(QtCore.QRect(190, 20, 91, 21))
        self.cbTestBondsPulledUser.setObjectName("cbTestBondsPulledUser")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(680, 140, 211, 21))
        self.label_8.setObjectName("label_8")
        self.leErrors = QtWidgets.QLineEdit(Form)
        self.leErrors.setGeometry(QtCore.QRect(340, 30, 611, 21))
        self.leErrors.setText("")
        self.leErrors.setReadOnly(True)
        self.leErrors.setObjectName("leErrors")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(350, 50, 321, 51))
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(340, 10, 181, 16))
        self.label_15.setObjectName("label_15")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(10, 200, 171, 21))
        self.label_7.setObjectName("label_7")
        self.frame_8 = QtWidgets.QFrame(Form)
        self.frame_8.setGeometry(QtCore.QRect(10, 220, 281, 61))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_8.setObjectName("frame_8")
        self.lineEdit_33 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_33.setGeometry(QtCore.QRect(0, 0, 181, 21))
        self.lineEdit_33.setReadOnly(True)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.lineEdit_34 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_34.setGeometry(QtCore.QRect(0, 20, 181, 21))
        self.lineEdit_34.setReadOnly(True)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.lineEdit_35 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_35.setGeometry(QtCore.QRect(0, 40, 181, 21))
        self.lineEdit_35.setReadOnly(True)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.sbBatchSylgard = QtWidgets.QSpinBox(self.frame_8)
        self.sbBatchSylgard.setGeometry(QtCore.QRect(180, 0, 101, 21))
        self.sbBatchSylgard.setMinimum(-1)
        self.sbBatchSylgard.setMaximum(2147483647)
        self.sbBatchSylgard.setObjectName("sbBatchSylgard")
        self.sbBatchBondWire = QtWidgets.QSpinBox(self.frame_8)
        self.sbBatchBondWire.setGeometry(QtCore.QRect(180, 20, 101, 21))
        self.sbBatchBondWire.setMinimum(-1)
        self.sbBatchBondWire.setMaximum(2147483647)
        self.sbBatchBondWire.setObjectName("sbBatchBondWire")
        self.sbBatchWedge = QtWidgets.QSpinBox(self.frame_8)
        self.sbBatchWedge.setGeometry(QtCore.QRect(180, 40, 101, 21))
        self.sbBatchWedge.setMinimum(-1)
        self.sbBatchWedge.setMaximum(2147483647)
        self.sbBatchWedge.setObjectName("sbBatchWedge")
        self.frame_9 = QtWidgets.QFrame(Form)
        self.frame_9.setGeometry(QtCore.QRect(10, 10, 261, 111))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_9.setObjectName("frame_9")
        self.pbSave = QtWidgets.QPushButton(self.frame_9)
        self.pbSave.setGeometry(QtCore.QRect(50, 60, 71, 21))
        self.pbSave.setObjectName("pbSave")
        self.pbEdit = QtWidgets.QPushButton(self.frame_9)
        self.pbEdit.setGeometry(QtCore.QRect(90, 30, 71, 21))
        self.pbEdit.setObjectName("pbEdit")
        self.pbCancel = QtWidgets.QPushButton(self.frame_9)
        self.pbCancel.setGeometry(QtCore.QRect(130, 60, 71, 21))
        self.pbCancel.setObjectName("pbCancel")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit.setGeometry(QtCore.QRect(1, 1, 151, 19))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.leID = QtWidgets.QLineEdit(self.frame_9)
        self.leID.setGeometry(QtCore.QRect(150, 0, 111, 20))
        self.leID.setText("")
        self.leID.setReadOnly(True)
        self.leID.setObjectName("leID")
        self.leStatus = QtWidgets.QLineEdit(self.frame_9)
        self.leStatus.setGeometry(QtCore.QRect(80, 90, 171, 20))
        self.leStatus.setText("")
        self.leStatus.setReadOnly(True)
        self.leStatus.setObjectName("leStatus")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_27.setGeometry(QtCore.QRect(10, 90, 71, 20))
        self.lineEdit_27.setReadOnly(True)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.frame_10 = QtWidgets.QFrame(Form)
        self.frame_10.setGeometry(QtCore.QRect(10, 330, 301, 391))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_2 = QtWidgets.QLabel(self.frame_10)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 171, 21))
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.frame_10)
        self.frame.setGeometry(QtCore.QRect(10, 20, 281, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.ckWirebondsInspectedBack = QtWidgets.QCheckBox(self.frame)
        self.ckWirebondsInspectedBack.setGeometry(QtCore.QRect(1, 120, 241, 17))
        self.ckWirebondsInspectedBack.setObjectName("ckWirebondsInspectedBack")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_31.setGeometry(QtCore.QRect(1, 40, 171, 21))
        self.lineEdit_31.setReadOnly(True)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(2, 70, 141, 16))
        self.label_3.setObjectName("label_3")
        self.ckWirebondingBack = QtWidgets.QCheckBox(self.frame)
        self.ckWirebondingBack.setGeometry(QtCore.QRect(1, 0, 231, 17))
        self.ckWirebondingBack.setObjectName("ckWirebondingBack")
        self.lineEdit_36 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_36.setGeometry(QtCore.QRect(1, 150, 181, 20))
        self.lineEdit_36.setReadOnly(True)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.cbWirebondingUserBack = QtWidgets.QComboBox(self.frame)
        self.cbWirebondingUserBack.setGeometry(QtCore.QRect(170, 40, 111, 21))
        self.cbWirebondingUserBack.setObjectName("cbWirebondingUserBack")
        self.cbWirebondsRepairedUserBack = QtWidgets.QComboBox(self.frame)
        self.cbWirebondsRepairedUserBack.setGeometry(QtCore.QRect(180, 150, 101, 21))
        self.cbWirebondsRepairedUserBack.setObjectName("cbWirebondsRepairedUserBack")
        self.dWirebondingBack = QtWidgets.QDateEdit(self.frame)
        self.dWirebondingBack.setGeometry(QtCore.QRect(170, 20, 111, 21))
        self.dWirebondingBack.setCalendarPopup(True)
        self.dWirebondingBack.setDate(QtCore.QDate(2021, 1, 1))
        self.dWirebondingBack.setObjectName("dWirebondingBack")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_15.setGeometry(QtCore.QRect(0, 20, 171, 21))
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_47 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_47.setGeometry(QtCore.QRect(0, 90, 171, 21))
        self.lineEdit_47.setReadOnly(True)
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.sbUnbondedChannelsBack = QtWidgets.QSpinBox(self.frame)
        self.sbUnbondedChannelsBack.setGeometry(QtCore.QRect(170, 90, 111, 21))
        self.sbUnbondedChannelsBack.setMinimum(-1)
        self.sbUnbondedChannelsBack.setMaximum(18)
        self.sbUnbondedChannelsBack.setObjectName("sbUnbondedChannelsBack")
        self.frame_4 = QtWidgets.QFrame(self.frame_10)
        self.frame_4.setGeometry(QtCore.QRect(10, 240, 281, 141))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.ckEncapsulationBack = QtWidgets.QCheckBox(self.frame_4)
        self.ckEncapsulationBack.setGeometry(QtCore.QRect(0, 0, 191, 17))
        self.ckEncapsulationBack.setObjectName("ckEncapsulationBack")
        self.lineEdit_38 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_38.setGeometry(QtCore.QRect(1, 20, 141, 21))
        self.lineEdit_38.setReadOnly(True)
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.dtCureStartBack = QtWidgets.QDateTimeEdit(self.frame_4)
        self.dtCureStartBack.setGeometry(QtCore.QRect(140, 60, 141, 21))
        self.dtCureStartBack.setDate(QtCore.QDate(2021, 1, 1))
        self.dtCureStartBack.setMaximumDate(QtCore.QDate(2050, 12, 31))
        self.dtCureStartBack.setMinimumDate(QtCore.QDate(2000, 9, 1))
        self.dtCureStartBack.setCalendarPopup(True)
        self.dtCureStartBack.setObjectName("dtCureStartBack")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(1, 80, 141, 21))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pbCureStopNowBack = QtWidgets.QPushButton(self.frame_4)
        self.pbCureStopNowBack.setGeometry(QtCore.QRect(140, 80, 141, 21))
        self.pbCureStopNowBack.setObjectName("pbCureStopNowBack")
        self.pbCureStartNowBack = QtWidgets.QPushButton(self.frame_4)
        self.pbCureStartNowBack.setGeometry(QtCore.QRect(140, 40, 141, 21))
        self.pbCureStartNowBack.setObjectName("pbCureStartNowBack")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(1, 40, 141, 21))
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_39 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_39.setGeometry(QtCore.QRect(1, 120, 161, 20))
        self.lineEdit_39.setReadOnly(True)
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.cbEncapsulationInspectionBack = QtWidgets.QComboBox(self.frame_4)
        self.cbEncapsulationInspectionBack.setGeometry(QtCore.QRect(160, 120, 121, 20))
        self.cbEncapsulationInspectionBack.setObjectName("cbEncapsulationInspectionBack")
        self.cbEncapsulationInspectionBack.addItem("")
        self.cbEncapsulationInspectionBack.addItem("")
        self.dtCureStopBack = QtWidgets.QDateTimeEdit(self.frame_4)
        self.dtCureStopBack.setGeometry(QtCore.QRect(140, 100, 141, 21))
        self.dtCureStopBack.setDate(QtCore.QDate(2021, 1, 1))
        self.dtCureStopBack.setMaximumDate(QtCore.QDate(2050, 12, 31))
        self.dtCureStopBack.setMinimumDate(QtCore.QDate(2000, 9, 1))
        self.dtCureStopBack.setCalendarPopup(True)
        self.dtCureStopBack.setObjectName("dtCureStopBack")
        self.cbEncapsulationUserBack = QtWidgets.QComboBox(self.frame_4)
        self.cbEncapsulationUserBack.setGeometry(QtCore.QRect(140, 20, 141, 21))
        self.cbEncapsulationUserBack.setObjectName("cbEncapsulationUserBack")
        self.label_5 = QtWidgets.QLabel(self.frame_10)
        self.label_5.setGeometry(QtCore.QRect(10, 220, 171, 16))
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(10, 310, 171, 21))
        self.label_10.setObjectName("label_10")
        self.frame_11 = QtWidgets.QFrame(Form)
        self.frame_11.setGeometry(QtCore.QRect(330, 160, 301, 481))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_14 = QtWidgets.QLabel(self.frame_11)
        self.label_14.setGeometry(QtCore.QRect(10, 310, 181, 16))
        self.label_14.setObjectName("label_14")
        self.frame_6 = QtWidgets.QFrame(self.frame_11)
        self.frame_6.setGeometry(QtCore.QRect(10, 20, 281, 261))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setObjectName("frame_6")
        self.ckWirebondsInspectedFront = QtWidgets.QCheckBox(self.frame_6)
        self.ckWirebondsInspectedFront.setGeometry(QtCore.QRect(0, 220, 241, 17))
        self.ckWirebondsInspectedFront.setObjectName("ckWirebondsInspectedFront")
        self.lineEdit_41 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_41.setGeometry(QtCore.QRect(1, 40, 181, 21))
        self.lineEdit_41.setReadOnly(True)
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        self.label_9.setGeometry(QtCore.QRect(2, 140, 141, 16))
        self.label_9.setObjectName("label_9")
        self.ckWirebondingFront = QtWidgets.QCheckBox(self.frame_6)
        self.ckWirebondingFront.setGeometry(QtCore.QRect(0, 0, 231, 17))
        self.ckWirebondingFront.setObjectName("ckWirebondingFront")
        self.lineEdit_42 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_42.setGeometry(QtCore.QRect(1, 240, 181, 20))
        self.lineEdit_42.setReadOnly(True)
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.pteUnbondedChannelsFront = QtWidgets.QPlainTextEdit(self.frame_6)
        self.pteUnbondedChannelsFront.setGeometry(QtCore.QRect(0, 160, 281, 51))
        self.pteUnbondedChannelsFront.setObjectName("pteUnbondedChannelsFront")
        self.pteWirebondingChannelsSkipFront = QtWidgets.QPlainTextEdit(self.frame_6)
        self.pteWirebondingChannelsSkipFront.setGeometry(QtCore.QRect(0, 90, 281, 41))
        self.pteWirebondingChannelsSkipFront.setReadOnly(True)
        self.pteWirebondingChannelsSkipFront.setObjectName("pteWirebondingChannelsSkipFront")
        self.label_13 = QtWidgets.QLabel(self.frame_6)
        self.label_13.setGeometry(QtCore.QRect(0, 70, 251, 16))
        self.label_13.setObjectName("label_13")
        self.cbWirebondingUserFront = QtWidgets.QComboBox(self.frame_6)
        self.cbWirebondingUserFront.setGeometry(QtCore.QRect(180, 40, 101, 21))
        self.cbWirebondingUserFront.setObjectName("cbWirebondingUserFront")
        self.cbWirebondsRepairedUserFront = QtWidgets.QComboBox(self.frame_6)
        self.cbWirebondsRepairedUserFront.setGeometry(QtCore.QRect(180, 240, 101, 21))
        self.cbWirebondsRepairedUserFront.setObjectName("cbWirebondsRepairedUserFront")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_18.setGeometry(QtCore.QRect(0, 20, 171, 21))
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.dWirebondingFront = QtWidgets.QDateEdit(self.frame_6)
        self.dWirebondingFront.setGeometry(QtCore.QRect(170, 20, 111, 21))
        self.dWirebondingFront.setCalendarPopup(True)
        self.dWirebondingFront.setDate(QtCore.QDate(2021, 1, 1))
        self.dWirebondingFront.setObjectName("dWirebondingFront")
        self.label_12 = QtWidgets.QLabel(self.frame_11)
        self.label_12.setGeometry(QtCore.QRect(10, 0, 171, 21))
        self.label_12.setObjectName("label_12")
        self.frame_7 = QtWidgets.QFrame(self.frame_11)
        self.frame_7.setGeometry(QtCore.QRect(10, 330, 281, 141))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_7.setObjectName("frame_7")
        self.ckEncapsulationFront = QtWidgets.QCheckBox(self.frame_7)
        self.ckEncapsulationFront.setGeometry(QtCore.QRect(0, 0, 201, 17))
        self.ckEncapsulationFront.setObjectName("ckEncapsulationFront")
        self.lineEdit_45 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_45.setGeometry(QtCore.QRect(1, 20, 141, 21))
        self.lineEdit_45.setReadOnly(True)
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.dtCureStartFront = QtWidgets.QDateTimeEdit(self.frame_7)
        self.dtCureStartFront.setGeometry(QtCore.QRect(140, 60, 141, 21))
        self.dtCureStartFront.setDate(QtCore.QDate(2021, 1, 1))
        self.dtCureStartFront.setMaximumDate(QtCore.QDate(2050, 12, 31))
        self.dtCureStartFront.setMinimumDate(QtCore.QDate(2000, 9, 1))
        self.dtCureStartFront.setCalendarPopup(True)
        self.dtCureStartFront.setObjectName("dtCureStartFront")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_10.setGeometry(QtCore.QRect(1, 80, 141, 21))
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pbCureStopNowFront = QtWidgets.QPushButton(self.frame_7)
        self.pbCureStopNowFront.setGeometry(QtCore.QRect(140, 80, 141, 21))
        self.pbCureStopNowFront.setObjectName("pbCureStopNowFront")
        self.pbCureStartNowFront = QtWidgets.QPushButton(self.frame_7)
        self.pbCureStartNowFront.setGeometry(QtCore.QRect(140, 40, 141, 21))
        self.pbCureStartNowFront.setObjectName("pbCureStartNowFront")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_11.setGeometry(QtCore.QRect(1, 40, 141, 21))
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_46 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_46.setGeometry(QtCore.QRect(1, 120, 161, 20))
        self.lineEdit_46.setReadOnly(True)
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.cbEncapsulationInspectionFront = QtWidgets.QComboBox(self.frame_7)
        self.cbEncapsulationInspectionFront.setGeometry(QtCore.QRect(160, 120, 121, 20))
        self.cbEncapsulationInspectionFront.setObjectName("cbEncapsulationInspectionFront")
        self.cbEncapsulationInspectionFront.addItem("")
        self.cbEncapsulationInspectionFront.addItem("")
        self.dtCureStopFront = QtWidgets.QDateTimeEdit(self.frame_7)
        self.dtCureStopFront.setGeometry(QtCore.QRect(140, 100, 141, 21))
        self.dtCureStopFront.setDate(QtCore.QDate(2021, 1, 1))
        self.dtCureStopFront.setMaximumDate(QtCore.QDate(2050, 12, 31))
        self.dtCureStopFront.setMinimumDate(QtCore.QDate(2000, 9, 1))
        self.dtCureStopFront.setCalendarPopup(True)
        self.dtCureStopFront.setObjectName("dtCureStopFront")
        self.cbEncapsulationUserFront = QtWidgets.QComboBox(self.frame_7)
        self.cbEncapsulationUserFront.setGeometry(QtCore.QRect(140, 20, 141, 21))
        self.cbEncapsulationUserFront.setObjectName("cbEncapsulationUserFront")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(330, 140, 171, 21))
        self.label_11.setObjectName("label_11")
        self.frame_12 = QtWidgets.QFrame(Form)
        self.frame_12.setGeometry(QtCore.QRect(670, 270, 281, 201))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.pbAddComment = QtWidgets.QPushButton(self.frame_12)
        self.pbAddComment.setGeometry(QtCore.QRect(0, 180, 111, 21))
        self.pbAddComment.setObjectName("pbAddComment")
        self.pteWriteComment = QtWidgets.QPlainTextEdit(self.frame_12)
        self.pteWriteComment.setGeometry(QtCore.QRect(0, 120, 281, 61))
        self.pteWriteComment.setPlainText("")
        self.pteWriteComment.setObjectName("pteWriteComment")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame_12)
        self.lineEdit_16.setGeometry(QtCore.QRect(0, 0, 161, 21))
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.pbDeleteComment = QtWidgets.QPushButton(self.frame_12)
        self.pbDeleteComment.setGeometry(QtCore.QRect(160, 0, 121, 21))
        self.pbDeleteComment.setObjectName("pbDeleteComment")
        self.listComments = QtWidgets.QListWidget(self.frame_12)
        self.listComments.setGeometry(QtCore.QRect(0, 20, 281, 91))
        self.listComments.setObjectName("listComments")
        self.frame_13 = QtWidgets.QFrame(Form)
        self.frame_13.setGeometry(QtCore.QRect(670, 500, 281, 201))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.pbDeleteCommentEncap = QtWidgets.QPushButton(self.frame_13)
        self.pbDeleteCommentEncap.setGeometry(QtCore.QRect(160, 0, 121, 21))
        self.pbDeleteCommentEncap.setObjectName("pbDeleteCommentEncap")
        self.pbAddCommentEncap = QtWidgets.QPushButton(self.frame_13)
        self.pbAddCommentEncap.setGeometry(QtCore.QRect(0, 180, 111, 21))
        self.pbAddCommentEncap.setObjectName("pbAddCommentEncap")
        self.pteWriteCommentEncap = QtWidgets.QPlainTextEdit(self.frame_13)
        self.pteWriteCommentEncap.setGeometry(QtCore.QRect(0, 120, 281, 61))
        self.pteWriteCommentEncap.setPlainText("")
        self.pteWriteCommentEncap.setObjectName("pteWriteCommentEncap")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame_13)
        self.lineEdit_17.setGeometry(QtCore.QRect(0, 0, 161, 21))
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.listCommentsEncap = QtWidgets.QListWidget(self.frame_13)
        self.listCommentsEncap.setGeometry(QtCore.QRect(0, 20, 281, 91))
        self.listCommentsEncap.setObjectName("listCommentsEncap")

        self.retranslateUi(Form)
        self.cbPreinspection.setCurrentIndex(-1)
        self.cbWirebondingFinalInspectionOK.setCurrentIndex(-1)
        self.cbWirebondingFinalInspectionUser.setCurrentIndex(-1)
        self.cbTestBondsPulledUser.setCurrentIndex(-1)
        self.cbWirebondingUserBack.setCurrentIndex(-1)
        self.cbWirebondsRepairedUserBack.setCurrentIndex(-1)
        self.cbEncapsulationInspectionBack.setCurrentIndex(-1)
        self.cbEncapsulationUserBack.setCurrentIndex(-1)
        self.cbWirebondingUserFront.setCurrentIndex(-1)
        self.cbWirebondsRepairedUserFront.setCurrentIndex(-1)
        self.cbEncapsulationInspectionFront.setCurrentIndex(-1)
        self.cbEncapsulationUserFront.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Pre-wirebonding qualification"))
        self.lineEdit_29.setToolTip(_translate("Form", "height difference between highest and lowers corners"))
        self.lineEdit_29.setText(_translate("Form", "Visual inspection"))
        self.cbPreinspection.setItemText(0, _translate("Form", "pass"))
        self.cbPreinspection.setItemText(1, _translate("Form", "fail"))
        self.label_4.setText(_translate("Form", "Wirebonding qualification"))
        self.cbWirebondingFinalInspectionOK.setItemText(0, _translate("Form", "pass"))
        self.cbWirebondingFinalInspectionOK.setItemText(1, _translate("Form", "fail"))
        self.lineEdit_37.setText(_translate("Form", "Final inspection OK?"))
        self.lineEdit_40.setText(_translate("Form", "Final inspection user"))
        self.lineEdit_32.setText(_translate("Form", "Test bond pull user"))
        self.ckTestBonds.setText(_translate("Form", "Is test bond module"))
        self.lineEdit_43.setText(_translate("Form", "Pull strength average (g)"))
        self.lineEdit_44.setText(_translate("Form", "Pull strength stddev (g)"))
        self.label_8.setText(_translate("Form", "Test bonds"))
        self.label_6.setText(_translate("Form", "NOTE:  Format of all text box input should be a comma-separated list of values.  ex. 1, 3, 4, ..."))
        self.label_15.setText(_translate("Form", "Errors:"))
        self.label_7.setText(_translate("Form", "Supply batches"))
        self.lineEdit_33.setText(_translate("Form", "Sylgard batch ID"))
        self.lineEdit_34.setText(_translate("Form", "Bond wire batch ID"))
        self.lineEdit_35.setText(_translate("Form", "Wedge batch ID"))
        self.pbSave.setText(_translate("Form", "Save"))
        self.pbEdit.setText(_translate("Form", "Edit"))
        self.pbCancel.setText(_translate("Form", "Cancel"))
        self.lineEdit.setText(_translate("Form", "Module ID"))
        self.lineEdit_27.setText(_translate("Form", "Status:"))
        self.label_2.setText(_translate("Form", "Wirebonding"))
        self.ckWirebondsInspectedBack.setText(_translate("Form", "Wirebonds inspected"))
        self.lineEdit_31.setText(_translate("Form", "Back wirebonding user"))
        self.label_3.setText(_translate("Form", "Unbonded areas"))
        self.ckWirebondingBack.setText(_translate("Form", "Back wirebonding performed"))
        self.lineEdit_36.setText(_translate("Form", "Wirebonds repaired user"))
        self.lineEdit_15.setText(_translate("Form", "Back wirebonding date"))
        self.lineEdit_47.setText(_translate("Form", "Unbonded areas (/18)"))
        self.ckEncapsulationBack.setText(_translate("Form", "Back encapsulation done"))
        self.lineEdit_38.setText(_translate("Form", "Encpasulation user"))
        self.lineEdit_6.setText(_translate("Form", "oven cure stop"))
        self.pbCureStopNowBack.setText(_translate("Form", "set to now"))
        self.pbCureStartNowBack.setText(_translate("Form", "set to now"))
        self.lineEdit_7.setText(_translate("Form", "oven cure start"))
        self.lineEdit_39.setText(_translate("Form", "Post-curing inspection"))
        self.cbEncapsulationInspectionBack.setItemText(0, _translate("Form", "pass"))
        self.cbEncapsulationInspectionBack.setItemText(1, _translate("Form", "fail"))
        self.label_5.setText(_translate("Form", "Encapsulation"))
        self.label_10.setText(_translate("Form", "BACK SIDE"))
        self.label_14.setText(_translate("Form", "Encapsulation"))
        self.ckWirebondsInspectedFront.setText(_translate("Form", "Wirebonds inspected"))
        self.lineEdit_41.setText(_translate("Form", "Front wirebonding user"))
        self.label_9.setText(_translate("Form", "Unbonded channels"))
        self.ckWirebondingFront.setText(_translate("Form", "Front wirebonding performed"))
        self.lineEdit_42.setText(_translate("Form", "Wirebonds repaired user"))
        self.label_13.setText(_translate("Form", "Channels to skip (currently disabled)"))
        self.lineEdit_18.setText(_translate("Form", "Front wirebonding date"))
        self.label_12.setText(_translate("Form", "Wirebonding"))
        self.ckEncapsulationFront.setText(_translate("Form", "Front encapsulation done"))
        self.lineEdit_45.setText(_translate("Form", "Encpasulation user"))
        self.lineEdit_10.setText(_translate("Form", "oven cure stop"))
        self.pbCureStopNowFront.setText(_translate("Form", "set to now"))
        self.pbCureStartNowFront.setText(_translate("Form", "set to now"))
        self.lineEdit_11.setText(_translate("Form", "oven cure start"))
        self.lineEdit_46.setText(_translate("Form", "Post-curing inspection"))
        self.cbEncapsulationInspectionFront.setItemText(0, _translate("Form", "pass"))
        self.cbEncapsulationInspectionFront.setItemText(1, _translate("Form", "fail"))
        self.label_11.setText(_translate("Form", "FRONT SIDE"))
        self.pbAddComment.setText(_translate("Form", "Add comment"))
        self.lineEdit_16.setText(_translate("Form", "Wirebonding notes"))
        self.pbDeleteComment.setText(_translate("Form", "Delete selected"))
        self.pbDeleteCommentEncap.setText(_translate("Form", "Delete selected"))
        self.pbAddCommentEncap.setText(_translate("Form", "Add comment"))
        self.lineEdit_17.setText(_translate("Form", "Encapsulation notes"))
