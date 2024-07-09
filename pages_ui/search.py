# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1097, 705)
        self.pbSearch = QtWidgets.QPushButton(Form)
        self.pbSearch.setGeometry(QtCore.QRect(110, 280, 81, 41))
        self.pbSearch.setObjectName("pbSearch")
        self.pbClearParams = QtWidgets.QPushButton(Form)
        self.pbClearParams.setGeometry(QtCore.QRect(220, 290, 111, 21))
        self.pbClearParams.setObjectName("pbClearParams")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(40, 120, 381, 141))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ckUseDate = QtWidgets.QCheckBox(self.frame)
        self.ckUseDate.setEnabled(True)
        self.ckUseDate.setGeometry(QtCore.QRect(310, 100, 71, 21))
        self.ckUseDate.setObjectName("ckUseDate")
        self.cbChannelDensity = QtWidgets.QComboBox(self.frame)
        self.cbChannelDensity.setGeometry(QtCore.QRect(220, 80, 161, 21))
        self.cbChannelDensity.setObjectName("cbChannelDensity")
        self.cbChannelDensity.addItem("")
        self.cbChannelDensity.setItemText(0, "")
        self.cbChannelDensity.addItem("")
        self.cbChannelDensity.addItem("")
        self.cbInstitution = QtWidgets.QComboBox(self.frame)
        self.cbInstitution.setGeometry(QtCore.QRect(220, 0, 161, 21))
        self.cbInstitution.setObjectName("cbInstitution")
        self.cbInstitution.addItem("")
        self.cbInstitution.setItemText(0, "")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.dCreated = QtWidgets.QDateEdit(self.frame)
        self.dCreated.setEnabled(True)
        self.dCreated.setGeometry(QtCore.QRect(220, 100, 91, 21))
        self.dCreated.setMouseTracking(True)
        self.dCreated.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 1, 1), QtCore.QTime(16, 0, 0)))
        self.dCreated.setCalendarPopup(True)
        self.dCreated.setDate(QtCore.QDate(2023, 1, 1))
        self.dCreated.setObjectName("dCreated")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_17.setGeometry(QtCore.QRect(0, 80, 221, 20))
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_13.setGeometry(QtCore.QRect(0, 0, 221, 20))
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_15.setGeometry(QtCore.QRect(0, 40, 221, 20))
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_16.setGeometry(QtCore.QRect(0, 60, 221, 20))
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.cbAssmCol = QtWidgets.QComboBox(self.frame)
        self.cbAssmCol.setEnabled(False)
        self.cbAssmCol.setGeometry(QtCore.QRect(330, 120, 51, 21))
        self.cbAssmCol.setCurrentText("")
        self.cbAssmCol.setObjectName("cbAssmCol")
        self.cbAssmCol.addItem("")
        self.cbAssmCol.setItemText(0, "")
        self.cbAssmCol.addItem("")
        self.cbAssmCol.addItem("")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_18.setGeometry(QtCore.QRect(0, 100, 221, 20))
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.cbShape = QtWidgets.QComboBox(self.frame)
        self.cbShape.setGeometry(QtCore.QRect(220, 20, 161, 20))
        self.cbShape.setObjectName("cbShape")
        self.cbShape.addItem("")
        self.cbShape.setItemText(0, "")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbAssmRow = QtWidgets.QComboBox(self.frame)
        self.cbAssmRow.setEnabled(False)
        self.cbAssmRow.setGeometry(QtCore.QRect(250, 120, 51, 21))
        self.cbAssmRow.setCurrentText("")
        self.cbAssmRow.setObjectName("cbAssmRow")
        self.cbAssmRow.addItem("")
        self.cbAssmRow.setItemText(0, "")
        self.cbAssmRow.addItem("")
        self.cbAssmRow.addItem("")
        self.cbAssmRow.addItem("")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_22.setEnabled(True)
        self.lineEdit_22.setGeometry(QtCore.QRect(300, 120, 31, 20))
        self.lineEdit_22.setReadOnly(True)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.cbThickness = QtWidgets.QComboBox(self.frame)
        self.cbThickness.setGeometry(QtCore.QRect(220, 60, 161, 21))
        self.cbThickness.setObjectName("cbThickness")
        self.cbThickness.addItem("")
        self.cbThickness.setItemText(0, "")
        self.cbThickness.addItem("")
        self.cbThickness.addItem("")
        self.cbThickness.addItem("")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_14.setGeometry(QtCore.QRect(0, 20, 221, 20))
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_20.setGeometry(QtCore.QRect(0, 120, 221, 20))
        self.lineEdit_20.setReadOnly(True)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_21.setEnabled(True)
        self.lineEdit_21.setGeometry(QtCore.QRect(220, 120, 31, 20))
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.cbMaterial = QtWidgets.QComboBox(self.frame)
        self.cbMaterial.setGeometry(QtCore.QRect(220, 40, 161, 21))
        self.cbMaterial.setObjectName("cbMaterial")
        self.cbMaterial.addItem("")
        self.cbMaterial.setItemText(0, "")
        self.cbMaterial.addItem("")
        self.cbMaterial.addItem("")
        self.cbMaterial.addItem("")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 40, 71, 16))
        self.label_7.setObjectName("label_7")
        self.cbPartType = QtWidgets.QComboBox(Form)
        self.cbPartType.setGeometry(QtCore.QRect(30, 60, 121, 21))
        self.cbPartType.setObjectName("cbPartType")
        self.cbPartType.addItem("")
        self.cbPartType.addItem("")
        self.cbPartType.addItem("")
        self.cbPartType.addItem("")
        self.cbPartType.addItem("")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 111, 16))
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(470, 50, 581, 281))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pbGoToPart = QtWidgets.QPushButton(self.frame_2)
        self.pbGoToPart.setGeometry(QtCore.QRect(120, 250, 171, 21))
        self.pbGoToPart.setObjectName("pbGoToPart")
        self.leStatus = QtWidgets.QLineEdit(self.frame_2)
        self.leStatus.setGeometry(QtCore.QRect(70, 220, 501, 20))
        self.leStatus.setText("")
        self.leStatus.setReadOnly(True)
        self.leStatus.setObjectName("leStatus")
        self.lwTypeList = QtWidgets.QListWidget(self.frame_2)
        self.lwTypeList.setGeometry(QtCore.QRect(290, 20, 281, 201))
        self.lwTypeList.setMidLineWidth(1)
        self.lwTypeList.setObjectName("lwTypeList")
        self.lwPartList = QtWidgets.QListWidget(self.frame_2)
        self.lwPartList.setGeometry(QtCore.QRect(10, 20, 281, 201))
        self.lwPartList.setMidLineWidth(1)
        self.lwPartList.setObjectName("lwPartList")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_26.setGeometry(QtCore.QRect(10, 220, 61, 20))
        self.lineEdit_26.setReadOnly(True)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.pbClearResults = QtWidgets.QPushButton(self.frame_2)
        self.pbClearResults.setGeometry(QtCore.QRect(10, 250, 101, 21))
        self.pbClearResults.setObjectName("pbClearResults")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 0, 191, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(300, 0, 191, 16))
        self.label_2.setObjectName("label_2")
        self.pbRefresh = QtWidgets.QPushButton(self.frame_2)
        self.pbRefresh.setGeometry(QtCore.QRect(300, 250, 141, 21))
        self.pbRefresh.setObjectName("pbRefresh")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(40, 380, 111, 16))
        self.label_8.setObjectName("label_8")
        self.cbToolSupplyType = QtWidgets.QComboBox(Form)
        self.cbToolSupplyType.setGeometry(QtCore.QRect(30, 400, 181, 21))
        self.cbToolSupplyType.setObjectName("cbToolSupplyType")
        self.cbToolSupplyType.addItem("")
        self.cbToolSupplyType.addItem("")
        self.cbToolSupplyType.addItem("")
        self.cbToolSupplyType.addItem("")
        self.cbToolSupplyType.addItem("")
        self.cbToolSupplyType.addItem("")
        self.cbToolSupplyType.addItem("")
        self.cbToolSupplyType.addItem("")
        self.cbToolSupplyType.addItem("")
        self.cbToolSupplyType.addItem("")
        self.cbToolSupplyType.addItem("")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 440, 151, 16))
        self.label_4.setObjectName("label_4")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(40, 460, 381, 61))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.cbInstitutionTool = QtWidgets.QComboBox(self.frame_3)
        self.cbInstitutionTool.setGeometry(QtCore.QRect(220, 0, 161, 21))
        self.cbInstitutionTool.setObjectName("cbInstitutionTool")
        self.cbInstitutionTool.addItem("")
        self.cbInstitutionTool.setItemText(0, "")
        self.cbInstitutionTool.addItem("")
        self.cbInstitutionTool.addItem("")
        self.cbInstitutionTool.addItem("")
        self.cbInstitutionTool.addItem("")
        self.cbInstitutionTool.addItem("")
        self.cbInstitutionTool.addItem("")
        self.cbInstitutionTool.addItem("")
        self.cbInstitutionTool.addItem("")
        self.cbInstitutionTool.addItem("")
        self.cbInstitutionTool.addItem("")
        self.cbInstitutionTool.addItem("")
        self.cbInstitutionTool.addItem("")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_23.setGeometry(QtCore.QRect(0, 0, 221, 20))
        self.lineEdit_23.setReadOnly(True)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_24.setGeometry(QtCore.QRect(0, 40, 221, 20))
        self.lineEdit_24.setReadOnly(True)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_29.setGeometry(QtCore.QRect(0, 20, 221, 20))
        self.lineEdit_29.setReadOnly(True)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.cbEmpty = QtWidgets.QComboBox(self.frame_3)
        self.cbEmpty.setGeometry(QtCore.QRect(220, 20, 161, 21))
        self.cbEmpty.setObjectName("cbEmpty")
        self.cbEmpty.addItem("")
        self.cbEmpty.setItemText(0, "")
        self.cbEmpty.addItem("")
        self.cbEmpty.addItem("")
        self.cbExpired = QtWidgets.QComboBox(self.frame_3)
        self.cbExpired.setGeometry(QtCore.QRect(220, 40, 161, 21))
        self.cbExpired.setObjectName("cbExpired")
        self.cbExpired.addItem("")
        self.cbExpired.setItemText(0, "")
        self.cbExpired.addItem("")
        self.cbExpired.addItem("")
        self.pbSearch_2 = QtWidgets.QPushButton(Form)
        self.pbSearch_2.setGeometry(QtCore.QRect(110, 540, 81, 41))
        self.pbSearch_2.setObjectName("pbSearch_2")
        self.pbClearParams_2 = QtWidgets.QPushButton(Form)
        self.pbClearParams_2.setGeometry(QtCore.QRect(220, 550, 111, 21))
        self.pbClearParams_2.setObjectName("pbClearParams_2")
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(470, 390, 581, 281))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pbGoToToolSupply = QtWidgets.QPushButton(self.frame_4)
        self.pbGoToToolSupply.setGeometry(QtCore.QRect(120, 250, 171, 21))
        self.pbGoToToolSupply.setObjectName("pbGoToToolSupply")
        self.leStatusToolSupply = QtWidgets.QLineEdit(self.frame_4)
        self.leStatusToolSupply.setGeometry(QtCore.QRect(70, 220, 221, 20))
        self.leStatusToolSupply.setText("")
        self.leStatusToolSupply.setReadOnly(True)
        self.leStatusToolSupply.setObjectName("leStatusToolSupply")
        self.lwInfoList = QtWidgets.QListWidget(self.frame_4)
        self.lwInfoList.setGeometry(QtCore.QRect(290, 20, 281, 201))
        self.lwInfoList.setMidLineWidth(1)
        self.lwInfoList.setObjectName("lwInfoList")
        self.lwToolSupplyList = QtWidgets.QListWidget(self.frame_4)
        self.lwToolSupplyList.setGeometry(QtCore.QRect(10, 20, 281, 201))
        self.lwToolSupplyList.setMidLineWidth(1)
        self.lwToolSupplyList.setObjectName("lwToolSupplyList")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_27.setGeometry(QtCore.QRect(10, 220, 61, 20))
        self.lineEdit_27.setReadOnly(True)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.pbClearResults_2 = QtWidgets.QPushButton(self.frame_4)
        self.pbClearResults_2.setGeometry(QtCore.QRect(10, 250, 101, 21))
        self.pbClearResults_2.setObjectName("pbClearResults_2")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setGeometry(QtCore.QRect(20, 0, 191, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setGeometry(QtCore.QRect(300, 0, 191, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        self.cbChannelDensity.setCurrentIndex(0)
        self.cbInstitution.setCurrentIndex(0)
        self.cbAssmCol.setCurrentIndex(0)
        self.cbShape.setCurrentIndex(0)
        self.cbAssmRow.setCurrentIndex(0)
        self.cbThickness.setCurrentIndex(0)
        self.cbMaterial.setCurrentIndex(0)
        self.cbPartType.setCurrentIndex(0)
        self.cbToolSupplyType.setCurrentIndex(0)
        self.cbInstitutionTool.setCurrentIndex(0)
        self.cbEmpty.setCurrentIndex(0)
        self.cbExpired.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pbSearch.setText(_translate("Form", "Search"))
        self.pbClearParams.setText(_translate("Form", "Clear params"))
        self.ckUseDate.setText(_translate("Form", "Include"))
        self.cbChannelDensity.setItemText(1, _translate("Form", "HD"))
        self.cbChannelDensity.setItemText(2, _translate("Form", "LD"))
        self.cbInstitution.setItemText(1, _translate("Form", "CERN"))
        self.cbInstitution.setItemText(2, _translate("Form", "FNAL"))
        self.cbInstitution.setItemText(3, _translate("Form", "UCSB"))
        self.cbInstitution.setItemText(4, _translate("Form", "UMN"))
        self.cbInstitution.setItemText(5, _translate("Form", "HEPHY"))
        self.cbInstitution.setItemText(6, _translate("Form", "HPK"))
        self.cbInstitution.setItemText(7, _translate("Form", "CMU"))
        self.cbInstitution.setItemText(8, _translate("Form", "TTU"))
        self.cbInstitution.setItemText(9, _translate("Form", "IHEP"))
        self.cbInstitution.setItemText(10, _translate("Form", "TIFR"))
        self.cbInstitution.setItemText(11, _translate("Form", "NTU"))
        self.cbInstitution.setItemText(12, _translate("Form", "FSU"))
        self.lineEdit_17.setText(_translate("Form", "Resolution type"))
        self.lineEdit_13.setText(_translate("Form", "Institution"))
        self.lineEdit_15.setText(_translate("Form", "Baseplate material"))
        self.lineEdit_16.setText(_translate("Form", "Sensor thickness"))
        self.cbAssmCol.setItemText(1, _translate("Form", "1"))
        self.cbAssmCol.setItemText(2, _translate("Form", "2"))
        self.lineEdit_18.setText(_translate("Form", "Creation date (proto/module)"))
        self.cbShape.setItemText(1, _translate("Form", "Full"))
        self.cbShape.setItemText(2, _translate("Form", "Top"))
        self.cbShape.setItemText(3, _translate("Form", "Bottom"))
        self.cbShape.setItemText(4, _translate("Form", "Left"))
        self.cbShape.setItemText(5, _translate("Form", "Right"))
        self.cbShape.setItemText(6, _translate("Form", "Five"))
        self.cbAssmRow.setItemText(1, _translate("Form", "1"))
        self.cbAssmRow.setItemText(2, _translate("Form", "2"))
        self.cbAssmRow.setItemText(3, _translate("Form", "3"))
        self.lineEdit_22.setText(_translate("Form", "col"))
        self.cbThickness.setItemText(1, _translate("Form", "120um"))
        self.cbThickness.setItemText(2, _translate("Form", "200um"))
        self.cbThickness.setItemText(3, _translate("Form", "300um"))
        self.lineEdit_14.setText(_translate("Form", "Geometry"))
        self.lineEdit_20.setText(_translate("Form", "Assembly posn (proto/module)"))
        self.lineEdit_21.setText(_translate("Form", "row"))
        self.cbMaterial.setItemText(1, _translate("Form", "CuW/Kapton"))
        self.cbMaterial.setItemText(2, _translate("Form", "PCB/Kapton"))
        self.cbMaterial.setItemText(3, _translate("Form", "CF/Kapton"))
        self.label_7.setText(_translate("Form", "Part type:"))
        self.cbPartType.setItemText(0, _translate("Form", "Baseplate"))
        self.cbPartType.setItemText(1, _translate("Form", "Sensor"))
        self.cbPartType.setItemText(2, _translate("Form", "Hexaboard"))
        self.cbPartType.setItemText(3, _translate("Form", "Protomodule"))
        self.cbPartType.setItemText(4, _translate("Form", "Module"))
        self.label_3.setText(_translate("Form", "Part attributes:"))
        self.pbGoToPart.setText(_translate("Form", "Go to selected item"))
        self.lineEdit_26.setText(_translate("Form", "Status:"))
        self.pbClearResults.setText(_translate("Form", "Clear results"))
        self.label.setText(_translate("Form", "Search results:"))
        self.label_2.setText(_translate("Form", "Part type:"))
        self.pbRefresh.setText(_translate("Form", "Refresh remote DB"))
        self.label_8.setText(_translate("Form", "Tool/Supply type:"))
        self.cbToolSupplyType.setItemText(0, _translate("Form", "Sensor tool"))
        self.cbToolSupplyType.setItemText(1, _translate("Form", "PCB tool"))
        self.cbToolSupplyType.setItemText(2, _translate("Form", "Assembly tray"))
        self.cbToolSupplyType.setItemText(3, _translate("Form", "Sensor component tray"))
        self.cbToolSupplyType.setItemText(4, _translate("Form", "PCB component tray"))
        self.cbToolSupplyType.setItemText(5, _translate("Form", "Araldite batch"))
        self.cbToolSupplyType.setItemText(6, _translate("Form", "Wedge batch"))
        self.cbToolSupplyType.setItemText(7, _translate("Form", "Sylgard batch"))
        self.cbToolSupplyType.setItemText(8, _translate("Form", "Bond wire batch"))
        self.cbToolSupplyType.setItemText(9, _translate("Form", "Transfer tape 50um"))
        self.cbToolSupplyType.setItemText(10, _translate("Form", "Transfer tape 125um"))
        self.label_4.setText(_translate("Form", "Tool/Supply attributes:"))
        self.cbInstitutionTool.setItemText(1, _translate("Form", "CERN"))
        self.cbInstitutionTool.setItemText(2, _translate("Form", "FNAL"))
        self.cbInstitutionTool.setItemText(3, _translate("Form", "UCSB"))
        self.cbInstitutionTool.setItemText(4, _translate("Form", "UMN"))
        self.cbInstitutionTool.setItemText(5, _translate("Form", "HEPHY"))
        self.cbInstitutionTool.setItemText(6, _translate("Form", "HPK"))
        self.cbInstitutionTool.setItemText(7, _translate("Form", "CMU"))
        self.cbInstitutionTool.setItemText(8, _translate("Form", "TTU"))
        self.cbInstitutionTool.setItemText(9, _translate("Form", "IHEP"))
        self.cbInstitutionTool.setItemText(10, _translate("Form", "TIFR"))
        self.cbInstitutionTool.setItemText(11, _translate("Form", "NTU"))
        self.cbInstitutionTool.setItemText(12, _translate("Form", "FSU"))
        self.lineEdit_23.setText(_translate("Form", "Institution (necessary for tools)"))
        self.lineEdit_24.setText(_translate("Form", "Expired or not (supply)"))
        self.lineEdit_29.setText(_translate("Form", "Empty or not (supply)"))
        self.cbEmpty.setItemText(1, _translate("Form", "not empty"))
        self.cbEmpty.setItemText(2, _translate("Form", "empty"))
        self.cbExpired.setItemText(1, _translate("Form", "not expired"))
        self.cbExpired.setItemText(2, _translate("Form", "expired"))
        self.pbSearch_2.setText(_translate("Form", "Search"))
        self.pbClearParams_2.setText(_translate("Form", "Clear params"))
        self.pbGoToToolSupply.setText(_translate("Form", "Go to selected item"))
        self.lineEdit_27.setText(_translate("Form", "Status:"))
        self.pbClearResults_2.setText(_translate("Form", "Clear results"))
        self.label_5.setText(_translate("Form", "Search results:"))
        self.label_6.setText(_translate("Form", "Tool/Supply info:"))