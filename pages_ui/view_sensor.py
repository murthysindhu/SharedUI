# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_sensor.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1097, 726)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(20, 160, 261, 501))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setMidLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(1, 41, 121, 20))
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.leLocation = QtWidgets.QLineEdit(self.frame_2)
        self.leLocation.setGeometry(QtCore.QRect(120, 41, 141, 20))
        self.leLocation.setText("")
        self.leLocation.setReadOnly(True)
        self.leLocation.setObjectName("leLocation")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(1, 120, 181, 21))
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(1, 140, 181, 21))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(1, 100, 181, 21))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pbAddComment = QtWidgets.QPushButton(self.frame_2)
        self.pbAddComment.setGeometry(QtCore.QRect(0, 480, 111, 21))
        self.pbAddComment.setObjectName("pbAddComment")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_14.setGeometry(QtCore.QRect(1, 260, 141, 21))
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.pbDeleteComment = QtWidgets.QPushButton(self.frame_2)
        self.pbDeleteComment.setGeometry(QtCore.QRect(140, 260, 121, 21))
        self.pbDeleteComment.setObjectName("pbDeleteComment")
        self.pteWriteComment = QtWidgets.QPlainTextEdit(self.frame_2)
        self.pteWriteComment.setGeometry(QtCore.QRect(0, 410, 261, 71))
        self.pteWriteComment.setObjectName("pteWriteComment")
        self.listComments = QtWidgets.QListWidget(self.frame_2)
        self.listComments.setGeometry(QtCore.QRect(0, 280, 261, 121))
        self.listComments.setObjectName("listComments")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_17.setGeometry(QtCore.QRect(1, 21, 121, 20))
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_18.setGeometry(QtCore.QRect(1, 1, 121, 20))
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.cbType = QtWidgets.QComboBox(self.frame_2)
        self.cbType.setGeometry(QtCore.QRect(180, 100, 81, 21))
        self.cbType.setObjectName("cbType")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.leBarcode = QtWidgets.QLineEdit(self.frame_2)
        self.leBarcode.setGeometry(QtCore.QRect(180, 80, 80, 20))
        self.leBarcode.setText("")
        self.leBarcode.setReadOnly(True)
        self.leBarcode.setObjectName("leBarcode")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_23.setGeometry(QtCore.QRect(0, 80, 181, 21))
        self.lineEdit_23.setReadOnly(True)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.cbInstitution = QtWidgets.QComboBox(self.frame_2)
        self.cbInstitution.setGeometry(QtCore.QRect(120, 20, 141, 21))
        self.cbInstitution.setObjectName("cbInstitution")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInsertUser = QtWidgets.QComboBox(self.frame_2)
        self.cbInsertUser.setGeometry(QtCore.QRect(120, 0, 141, 21))
        self.cbInsertUser.setObjectName("cbInsertUser")
        self.cbChannelDensity = QtWidgets.QComboBox(self.frame_2)
        self.cbChannelDensity.setGeometry(QtCore.QRect(180, 140, 81, 20))
        self.cbChannelDensity.setObjectName("cbChannelDensity")
        self.cbChannelDensity.addItem("")
        self.cbChannelDensity.addItem("")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(0, 230, 181, 21))
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.cbGrade = QtWidgets.QComboBox(self.frame_2)
        self.cbGrade.setGeometry(QtCore.QRect(180, 230, 81, 20))
        self.cbGrade.setObjectName("cbGrade")
        self.cbGrade.addItem("")
        self.cbGrade.addItem("")
        self.cbGrade.addItem("")
        self.cbInspection = QtWidgets.QComboBox(self.frame_2)
        self.cbInspection.setGeometry(QtCore.QRect(140, 190, 121, 21))
        self.cbInspection.setObjectName("cbInspection")
        self.cbInspection.addItem("")
        self.cbInspection.addItem("")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_15.setGeometry(QtCore.QRect(0, 190, 141, 21))
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(0, 170, 141, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_16.setGeometry(QtCore.QRect(0, 210, 181, 20))
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.dsbFlatness = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.dsbFlatness.setGeometry(QtCore.QRect(180, 210, 80, 21))
        self.dsbFlatness.setReadOnly(False)
        self.dsbFlatness.setDecimals(3)
        self.dsbFlatness.setMinimum(0.0)
        self.dsbFlatness.setMaximum(2147483647.0)
        self.dsbFlatness.setSingleStep(0.05)
        self.dsbFlatness.setObjectName("dsbFlatness")
        self.cbShape = QtWidgets.QComboBox(self.frame_2)
        self.cbShape.setGeometry(QtCore.QRect(180, 120, 81, 20))
        self.cbShape.setObjectName("cbShape")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(320, 200, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(320, 110, 131, 16))
        self.label_2.setObjectName("label_2")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(20, 10, 251, 111))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.pbSave = QtWidgets.QPushButton(self.frame_3)
        self.pbSave.setGeometry(QtCore.QRect(50, 60, 71, 21))
        self.pbSave.setObjectName("pbSave")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setGeometry(QtCore.QRect(0, 1, 121, 20))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pbCancel = QtWidgets.QPushButton(self.frame_3)
        self.pbCancel.setGeometry(QtCore.QRect(130, 60, 71, 21))
        self.pbCancel.setObjectName("pbCancel")
        self.pbNew = QtWidgets.QPushButton(self.frame_3)
        self.pbNew.setGeometry(QtCore.QRect(90, 30, 71, 21))
        self.pbNew.setObjectName("pbNew")
        self.pbEdit = QtWidgets.QPushButton(self.frame_3)
        self.pbEdit.setGeometry(QtCore.QRect(170, 30, 71, 21))
        self.pbEdit.setObjectName("pbEdit")
        self.leID = QtWidgets.QLineEdit(self.frame_3)
        self.leID.setGeometry(QtCore.QRect(120, 0, 131, 20))
        self.leID.setText("")
        self.leID.setReadOnly(True)
        self.leID.setObjectName("leID")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_11.setGeometry(QtCore.QRect(10, 90, 71, 20))
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.leStatus = QtWidgets.QLineEdit(self.frame_3)
        self.leStatus.setGeometry(QtCore.QRect(80, 90, 161, 20))
        self.leStatus.setText("")
        self.leStatus.setReadOnly(True)
        self.leStatus.setObjectName("leStatus")
        self.pbLoad = QtWidgets.QPushButton(self.frame_3)
        self.pbLoad.setGeometry(QtCore.QRect(10, 30, 71, 21))
        self.pbLoad.setObjectName("pbLoad")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(320, 130, 251, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.leProtomodule = QtWidgets.QLineEdit(self.frame)
        self.leProtomodule.setGeometry(QtCore.QRect(120, 20, 80, 20))
        self.leProtomodule.setReadOnly(True)
        self.leProtomodule.setObjectName("leProtomodule")
        self.pbGoProtomodule = QtWidgets.QPushButton(self.frame)
        self.pbGoProtomodule.setGeometry(QtCore.QRect(200, 20, 51, 21))
        self.pbGoProtomodule.setObjectName("pbGoProtomodule")
        self.pbGoStepSensor = QtWidgets.QPushButton(self.frame)
        self.pbGoStepSensor.setGeometry(QtCore.QRect(200, 0, 51, 21))
        self.pbGoStepSensor.setObjectName("pbGoStepSensor")
        self.sbStepSensor = QtWidgets.QSpinBox(self.frame)
        self.sbStepSensor.setGeometry(QtCore.QRect(120, 0, 81, 21))
        self.sbStepSensor.setReadOnly(True)
        self.sbStepSensor.setMinimum(-1)
        self.sbStepSensor.setMaximum(2147483647)
        self.sbStepSensor.setObjectName("sbStepSensor")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_13.setGeometry(QtCore.QRect(0, 0, 121, 21))
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_12.setGeometry(QtCore.QRect(0, 20, 121, 21))
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(320, 220, 251, 21))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.leModule = QtWidgets.QLineEdit(self.frame_4)
        self.leModule.setGeometry(QtCore.QRect(120, 0, 80, 20))
        self.leModule.setReadOnly(True)
        self.leModule.setObjectName("leModule")
        self.pbGoModule = QtWidgets.QPushButton(self.frame_4)
        self.pbGoModule.setGeometry(QtCore.QRect(200, 0, 51, 21))
        self.pbGoModule.setObjectName("pbGoModule")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_8.setGeometry(QtCore.QRect(0, 0, 121, 21))
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 151, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        self.cbType.setCurrentIndex(-1)
        self.cbInstitution.setCurrentIndex(-1)
        self.cbInsertUser.setCurrentIndex(-1)
        self.cbChannelDensity.setCurrentIndex(-1)
        self.cbGrade.setCurrentIndex(-1)
        self.cbInspection.setCurrentIndex(-1)
        self.cbShape.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_9.setText(_translate("Form", "Location"))
        self.lineEdit_10.setText(_translate("Form", "Geometry"))
        self.lineEdit_6.setText(_translate("Form", "Resolution type"))
        self.lineEdit_4.setText(_translate("Form", "Type (Si thickness)"))
        self.pbAddComment.setText(_translate("Form", "Add comment"))
        self.lineEdit_14.setText(_translate("Form", "Comments"))
        self.pbDeleteComment.setText(_translate("Form", "Delete selected"))
        self.lineEdit_17.setText(_translate("Form", "Institution"))
        self.lineEdit_18.setText(_translate("Form", "User name"))
        self.cbType.setItemText(0, _translate("Form", "120um"))
        self.cbType.setItemText(1, _translate("Form", "200um"))
        self.cbType.setItemText(2, _translate("Form", "300um"))
        self.lineEdit_23.setText(_translate("Form", "Barcode"))
        self.cbInstitution.setItemText(0, _translate("Form", "CERN"))
        self.cbInstitution.setItemText(1, _translate("Form", "FNAL"))
        self.cbInstitution.setItemText(2, _translate("Form", "UCSB"))
        self.cbInstitution.setItemText(3, _translate("Form", "UMN"))
        self.cbInstitution.setItemText(4, _translate("Form", "HEPHY"))
        self.cbInstitution.setItemText(5, _translate("Form", "HPK"))
        self.cbChannelDensity.setItemText(0, _translate("Form", "HD"))
        self.cbChannelDensity.setItemText(1, _translate("Form", "LD"))
        self.lineEdit_7.setText(_translate("Form", "Sensor grade"))
        self.cbGrade.setItemText(0, _translate("Form", "A"))
        self.cbGrade.setItemText(1, _translate("Form", "B"))
        self.cbGrade.setItemText(2, _translate("Form", "C"))
        self.cbInspection.setItemText(0, _translate("Form", "pass"))
        self.cbInspection.setItemText(1, _translate("Form", "fail"))
        self.lineEdit_15.setText(_translate("Form", "Visual inspection"))
        self.label_3.setText(_translate("Form", "sensor qualification"))
        self.lineEdit_16.setToolTip(_translate("Form", "height difference between highest and lowers corners"))
        self.lineEdit_16.setText(_translate("Form", "Flatness (mm)"))
        self.cbShape.setItemText(0, _translate("Form", "Full"))
        self.cbShape.setItemText(1, _translate("Form", "Top"))
        self.cbShape.setItemText(2, _translate("Form", "Bottom"))
        self.cbShape.setItemText(3, _translate("Form", "Left"))
        self.cbShape.setItemText(4, _translate("Form", "Right"))
        self.cbShape.setItemText(5, _translate("Form", "Five"))
        self.cbShape.setItemText(6, _translate("Form", "Full+Three"))
        self.label.setText(_translate("Form", "Module"))
        self.label_2.setText(_translate("Form", "Sensor placement"))
        self.pbSave.setText(_translate("Form", "Save"))
        self.lineEdit.setText(_translate("Form", "Sensor ID"))
        self.pbCancel.setText(_translate("Form", "Cancel"))
        self.pbNew.setText(_translate("Form", "New"))
        self.pbEdit.setText(_translate("Form", "Edit"))
        self.lineEdit_11.setText(_translate("Form", "Status:"))
        self.pbLoad.setText(_translate("Form", "Load"))
        self.pbGoProtomodule.setText(_translate("Form", "Go to"))
        self.pbGoStepSensor.setText(_translate("Form", "Go to"))
        self.lineEdit_13.setText(_translate("Form", "Placement step"))
        self.lineEdit_12.setText(_translate("Form", "On protomodule"))
        self.pbGoModule.setText(_translate("Form", "Go to"))
        self.lineEdit_8.setText(_translate("Form", "On module"))
        self.label_6.setText(_translate("Form", "Standard information"))
