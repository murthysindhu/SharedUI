# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_PCB.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1097, 719)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(320, 110, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(320, 220, 141, 16))
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(610, 110, 241, 16))
        self.label_7.setObjectName("label_7")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 160, 261, 471))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cbShape = QtWidgets.QComboBox(self.frame)
        self.cbShape.setGeometry(QtCore.QRect(180, 200, 81, 20))
        self.cbShape.setObjectName("cbShape")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbType = QtWidgets.QComboBox(self.frame)
        self.cbType.setGeometry(QtCore.QRect(130, 140, 131, 21))
        self.cbType.setCurrentText("")
        self.cbType.setObjectName("cbType")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.leManufacturer = QtWidgets.QLineEdit(self.frame)
        self.leManufacturer.setGeometry(QtCore.QRect(180, 100, 81, 21))
        self.leManufacturer.setText("")
        self.leManufacturer.setReadOnly(True)
        self.leManufacturer.setObjectName("leManufacturer")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_23.setGeometry(QtCore.QRect(0, 80, 181, 21))
        self.lineEdit_23.setReadOnly(True)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.sbChannels = QtWidgets.QSpinBox(self.frame)
        self.sbChannels.setGeometry(QtCore.QRect(180, 180, 81, 21))
        self.sbChannels.setReadOnly(True)
        self.sbChannels.setMinimum(-1)
        self.sbChannels.setMaximum(2147483647)
        self.sbChannels.setObjectName("sbChannels")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_15.setGeometry(QtCore.QRect(0, 200, 181, 21))
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setGeometry(QtCore.QRect(0, 100, 181, 21))
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.cbInsertUser = QtWidgets.QComboBox(self.frame)
        self.cbInsertUser.setGeometry(QtCore.QRect(120, 0, 141, 21))
        self.cbInsertUser.setObjectName("cbInsertUser")
        self.leLocation = QtWidgets.QLineEdit(self.frame)
        self.leLocation.setGeometry(QtCore.QRect(120, 40, 141, 21))
        self.leLocation.setText("")
        self.leLocation.setReadOnly(True)
        self.leLocation.setObjectName("leLocation")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_22.setGeometry(QtCore.QRect(0, 120, 181, 21))
        self.lineEdit_22.setReadOnly(True)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.sbNumRocs = QtWidgets.QSpinBox(self.frame)
        self.sbNumRocs.setGeometry(QtCore.QRect(180, 160, 81, 21))
        self.sbNumRocs.setReadOnly(True)
        self.sbNumRocs.setMinimum(0)
        self.sbNumRocs.setMaximum(2147483647)
        self.sbNumRocs.setObjectName("sbNumRocs")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(0, 180, 181, 21))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.cbInstitution = QtWidgets.QComboBox(self.frame)
        self.cbInstitution.setGeometry(QtCore.QRect(120, 20, 141, 21))
        self.cbInstitution.setObjectName("cbInstitution")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_20.setGeometry(QtCore.QRect(0, 20, 121, 21))
        self.lineEdit_20.setReadOnly(True)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_11.setGeometry(QtCore.QRect(0, 40, 121, 21))
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_21.setGeometry(QtCore.QRect(0, 140, 131, 21))
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_16.setGeometry(QtCore.QRect(0, 160, 181, 21))
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_38 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_38.setGeometry(QtCore.QRect(0, 1, 121, 20))
        self.lineEdit_38.setReadOnly(True)
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.cbResolution = QtWidgets.QComboBox(self.frame)
        self.cbResolution.setGeometry(QtCore.QRect(180, 120, 81, 21))
        self.cbResolution.setCurrentText("")
        self.cbResolution.setObjectName("cbResolution")
        self.cbResolution.addItem("")
        self.cbResolution.addItem("")
        self.leBarcode = QtWidgets.QLineEdit(self.frame)
        self.leBarcode.setGeometry(QtCore.QRect(180, 80, 80, 20))
        self.leBarcode.setText("")
        self.leBarcode.setReadOnly(True)
        self.leBarcode.setObjectName("leBarcode")
        self.pbAddComment = QtWidgets.QPushButton(self.frame)
        self.pbAddComment.setGeometry(QtCore.QRect(0, 450, 111, 21))
        self.pbAddComment.setObjectName("pbAddComment")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_14.setGeometry(QtCore.QRect(0, 240, 141, 21))
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.listComments = QtWidgets.QListWidget(self.frame)
        self.listComments.setGeometry(QtCore.QRect(0, 260, 261, 111))
        self.listComments.setObjectName("listComments")
        self.pbDeleteComment = QtWidgets.QPushButton(self.frame)
        self.pbDeleteComment.setGeometry(QtCore.QRect(140, 240, 121, 21))
        self.pbDeleteComment.setObjectName("pbDeleteComment")
        self.pteWriteComment = QtWidgets.QPlainTextEdit(self.frame)
        self.pteWriteComment.setGeometry(QtCore.QRect(0, 380, 261, 71))
        self.pteWriteComment.setPlainText("")
        self.pteWriteComment.setObjectName("pteWriteComment")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(20, 10, 251, 111))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.pbSave = QtWidgets.QPushButton(self.frame_2)
        self.pbSave.setGeometry(QtCore.QRect(50, 60, 71, 21))
        self.pbSave.setObjectName("pbSave")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(0, 1, 121, 20))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pbCancel = QtWidgets.QPushButton(self.frame_2)
        self.pbCancel.setGeometry(QtCore.QRect(130, 60, 71, 21))
        self.pbCancel.setObjectName("pbCancel")
        self.pbNew = QtWidgets.QPushButton(self.frame_2)
        self.pbNew.setGeometry(QtCore.QRect(90, 30, 71, 21))
        self.pbNew.setObjectName("pbNew")
        self.pbEdit = QtWidgets.QPushButton(self.frame_2)
        self.pbEdit.setGeometry(QtCore.QRect(170, 30, 71, 21))
        self.pbEdit.setObjectName("pbEdit")
        self.leID = QtWidgets.QLineEdit(self.frame_2)
        self.leID.setGeometry(QtCore.QRect(120, 0, 131, 20))
        self.leID.setText("")
        self.leID.setReadOnly(True)
        self.leID.setObjectName("leID")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(10, 90, 71, 20))
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.leStatus = QtWidgets.QLineEdit(self.frame_2)
        self.leStatus.setGeometry(QtCore.QRect(80, 90, 161, 20))
        self.leStatus.setText("")
        self.leStatus.setReadOnly(True)
        self.leStatus.setObjectName("leStatus")
        self.pbLoad = QtWidgets.QPushButton(self.frame_2)
        self.pbLoad.setGeometry(QtCore.QRect(10, 30, 71, 21))
        self.pbLoad.setObjectName("pbLoad")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(610, 130, 351, 161))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pbAddFiles = QtWidgets.QPushButton(self.frame_3)
        self.pbAddFiles.setGeometry(QtCore.QRect(130, 120, 101, 31))
        self.pbAddFiles.setObjectName("pbAddFiles")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_24.setGeometry(QtCore.QRect(1, 90, 221, 21))
        self.lineEdit_24.setReadOnly(True)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.listFiles = QtWidgets.QListWidget(self.frame_3)
        self.listFiles.setGeometry(QtCore.QRect(0, 0, 351, 91))
        self.listFiles.setObjectName("listFiles")
        self.pbDeleteFile = QtWidgets.QPushButton(self.frame_3)
        self.pbDeleteFile.setGeometry(QtCore.QRect(220, 90, 131, 21))
        self.pbDeleteFile.setObjectName("pbDeleteFile")
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(320, 240, 261, 41))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.leModule = QtWidgets.QLineEdit(self.frame_4)
        self.leModule.setGeometry(QtCore.QRect(130, 20, 81, 20))
        self.leModule.setText("")
        self.leModule.setReadOnly(True)
        self.leModule.setObjectName("leModule")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_9.setGeometry(QtCore.QRect(0, 0, 131, 21))
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pbGoModule = QtWidgets.QPushButton(self.frame_4)
        self.pbGoModule.setGeometry(QtCore.QRect(210, 20, 51, 21))
        self.pbGoModule.setObjectName("pbGoModule")
        self.sbStepPcb = QtWidgets.QSpinBox(self.frame_4)
        self.sbStepPcb.setGeometry(QtCore.QRect(130, 0, 81, 21))
        self.sbStepPcb.setReadOnly(True)
        self.sbStepPcb.setMinimum(-1)
        self.sbStepPcb.setMaximum(2147483647)
        self.sbStepPcb.setObjectName("sbStepPcb")
        self.pbGoStepPcb = QtWidgets.QPushButton(self.frame_4)
        self.pbGoStepPcb.setGeometry(QtCore.QRect(210, 0, 51, 21))
        self.pbGoStepPcb.setObjectName("pbGoStepPcb")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_8.setGeometry(QtCore.QRect(0, 20, 131, 21))
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setGeometry(QtCore.QRect(320, 130, 261, 61))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.cbGrade = QtWidgets.QComboBox(self.frame_5)
        self.cbGrade.setGeometry(QtCore.QRect(180, 40, 81, 21))
        self.cbGrade.setObjectName("cbGrade")
        self.cbGrade.addItem("")
        self.cbGrade.addItem("")
        self.cbGrade.addItem("")
        self.dsbThickness = QtWidgets.QDoubleSpinBox(self.frame_5)
        self.dsbThickness.setGeometry(QtCore.QRect(180, 20, 81, 21))
        self.dsbThickness.setReadOnly(True)
        self.dsbThickness.setMinimum(-1.0)
        self.dsbThickness.setMaximum(2147483647.0)
        self.dsbThickness.setSingleStep(0.1)
        self.dsbThickness.setObjectName("dsbThickness")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_17.setGeometry(QtCore.QRect(0, 40, 181, 21))
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_3.setGeometry(QtCore.QRect(0, 20, 181, 21))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_4.setGeometry(QtCore.QRect(0, 0, 181, 21))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.dsbFlatness = QtWidgets.QDoubleSpinBox(self.frame_5)
        self.dsbFlatness.setGeometry(QtCore.QRect(180, 0, 81, 21))
        self.dsbFlatness.setReadOnly(True)
        self.dsbFlatness.setMinimum(-1.0)
        self.dsbFlatness.setMaximum(2147483647.0)
        self.dsbFlatness.setSingleStep(0.05)
        self.dsbFlatness.setObjectName("dsbFlatness")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 151, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        self.cbShape.setCurrentIndex(-1)
        self.cbType.setCurrentIndex(-1)
        self.cbInsertUser.setCurrentIndex(-1)
        self.cbInstitution.setCurrentIndex(-1)
        self.cbResolution.setCurrentIndex(-1)
        self.cbGrade.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "PCB qualification"))
        self.label_2.setText(_translate("Form", "PCB placement step"))
        self.label_7.setText(_translate("Form", "Testing data storage"))
        self.cbShape.setItemText(0, _translate("Form", "Full"))
        self.cbShape.setItemText(1, _translate("Form", "Top"))
        self.cbShape.setItemText(2, _translate("Form", "Bottom"))
        self.cbShape.setItemText(3, _translate("Form", "Left"))
        self.cbShape.setItemText(4, _translate("Form", "Right"))
        self.cbShape.setItemText(5, _translate("Form", "Five"))
        self.cbShape.setItemText(6, _translate("Form", "Full+Three"))
        self.cbType.setItemText(0, _translate("Form", "HGCROCV1"))
        self.cbType.setItemText(1, _translate("Form", "HGCROCV2"))
        self.cbType.setItemText(2, _translate("Form", "HGCROCV3"))
        self.cbType.setItemText(3, _translate("Form", "SKIROCV1"))
        self.cbType.setItemText(4, _translate("Form", "SKIROCV2"))
        self.cbType.setItemText(5, _translate("Form", "SKIROCV3"))
        self.cbType.setItemText(6, _translate("Form", "HGCROC dummy"))
        self.lineEdit_23.setText(_translate("Form", "Barcode"))
        self.lineEdit_15.setText(_translate("Form", "Geometry"))
        self.lineEdit_7.setText(_translate("Form", "Manufacturer"))
        self.lineEdit_22.setText(_translate("Form", "Resolution type"))
        self.lineEdit_6.setText(_translate("Form", "Channels"))
        self.cbInstitution.setItemText(0, _translate("Form", "CERN"))
        self.cbInstitution.setItemText(1, _translate("Form", "FNAL"))
        self.cbInstitution.setItemText(2, _translate("Form", "UCSB"))
        self.cbInstitution.setItemText(3, _translate("Form", "UMN"))
        self.cbInstitution.setItemText(4, _translate("Form", "HEPHY"))
        self.cbInstitution.setItemText(5, _translate("Form", "HPK"))
        self.lineEdit_20.setText(_translate("Form", "Institution"))
        self.lineEdit_11.setText(_translate("Form", "Location"))
        self.lineEdit_21.setText(_translate("Form", "ROC type"))
        self.lineEdit_16.setText(_translate("Form", "Number of ROCs"))
        self.lineEdit_38.setToolTip(_translate("Form", "height difference between highest and lowers corners"))
        self.lineEdit_38.setText(_translate("Form", "User name"))
        self.cbResolution.setItemText(0, _translate("Form", "HD"))
        self.cbResolution.setItemText(1, _translate("Form", "LD"))
        self.pbAddComment.setText(_translate("Form", "Add comment"))
        self.lineEdit_14.setText(_translate("Form", "Comments"))
        self.pbDeleteComment.setText(_translate("Form", "Delete selected"))
        self.pbSave.setText(_translate("Form", "Save"))
        self.lineEdit.setText(_translate("Form", "PCB ID"))
        self.pbCancel.setText(_translate("Form", "Cancel"))
        self.pbNew.setText(_translate("Form", "New"))
        self.pbEdit.setText(_translate("Form", "Edit"))
        self.lineEdit_10.setText(_translate("Form", "Status:"))
        self.pbLoad.setText(_translate("Form", "Load"))
        self.pbAddFiles.setText(_translate("Form", "Add files"))
        self.lineEdit_24.setText(_translate("Form", "Testing data files"))
        self.listFiles.setToolTip(_translate("Form", "ID (date sent) (SENDER to RECEIVER)"))
        self.pbDeleteFile.setText(_translate("Form", "Delete selected"))
        self.lineEdit_9.setText(_translate("Form", "PCB step"))
        self.pbGoModule.setText(_translate("Form", "Go to"))
        self.pbGoStepPcb.setText(_translate("Form", "Go to"))
        self.lineEdit_8.setText(_translate("Form", "On module"))
        self.cbGrade.setItemText(0, _translate("Form", "A"))
        self.cbGrade.setItemText(1, _translate("Form", "B"))
        self.cbGrade.setItemText(2, _translate("Form", "C"))
        self.lineEdit_17.setText(_translate("Form", "PCB Grade"))
        self.lineEdit_3.setText(_translate("Form", "Thickness (mm)"))
        self.lineEdit_4.setText(_translate("Form", "Flatness (mm)"))
        self.label_6.setText(_translate("Form", "Standard information"))
