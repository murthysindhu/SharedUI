# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_kapton_step.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(874, 594)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.sbKaptonStepID = QtGui.QSpinBox(Form)
        self.sbKaptonStepID.setGeometry(QtCore.QRect(100, 10, 61, 21))
        self.sbKaptonStepID.setObjectName(_fromUtf8("sbKaptonStepID"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 40, 81, 21))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 60, 81, 21))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 80, 81, 21))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 100, 81, 21))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 120, 81, 21))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(10, 140, 81, 21))
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_8 = QtGui.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(10, 160, 81, 21))
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_9 = QtGui.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(10, 180, 81, 21))
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.sbModule1 = QtGui.QSpinBox(Form)
        self.sbModule1.setGeometry(QtCore.QRect(10, 230, 71, 22))
        self.sbModule1.setMinimum(-1)
        self.sbModule1.setMaximum(2147483647)
        self.sbModule1.setObjectName(_fromUtf8("sbModule1"))
        self.lineEdit_10 = QtGui.QLineEdit(Form)
        self.lineEdit_10.setGeometry(QtCore.QRect(10, 210, 121, 20))
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.pbGoModule1 = QtGui.QPushButton(Form)
        self.pbGoModule1.setGeometry(QtCore.QRect(80, 230, 51, 21))
        self.pbGoModule1.setObjectName(_fromUtf8("pbGoModule1"))
        self.pbGoModule2 = QtGui.QPushButton(Form)
        self.pbGoModule2.setGeometry(QtCore.QRect(80, 250, 51, 21))
        self.pbGoModule2.setObjectName(_fromUtf8("pbGoModule2"))
        self.sbModule2 = QtGui.QSpinBox(Form)
        self.sbModule2.setGeometry(QtCore.QRect(10, 250, 71, 22))
        self.sbModule2.setMinimum(-1)
        self.sbModule2.setMaximum(2147483647)
        self.sbModule2.setObjectName(_fromUtf8("sbModule2"))
        self.sbModule3 = QtGui.QSpinBox(Form)
        self.sbModule3.setGeometry(QtCore.QRect(10, 270, 71, 22))
        self.sbModule3.setMinimum(-1)
        self.sbModule3.setMaximum(2147483647)
        self.sbModule3.setObjectName(_fromUtf8("sbModule3"))
        self.pbGoModule3 = QtGui.QPushButton(Form)
        self.pbGoModule3.setGeometry(QtCore.QRect(80, 270, 51, 21))
        self.pbGoModule3.setObjectName(_fromUtf8("pbGoModule3"))
        self.pbGoModule4 = QtGui.QPushButton(Form)
        self.pbGoModule4.setGeometry(QtCore.QRect(80, 330, 51, 21))
        self.pbGoModule4.setObjectName(_fromUtf8("pbGoModule4"))
        self.pbGoModule5 = QtGui.QPushButton(Form)
        self.pbGoModule5.setGeometry(QtCore.QRect(80, 290, 51, 21))
        self.pbGoModule5.setObjectName(_fromUtf8("pbGoModule5"))
        self.sbModule4 = QtGui.QSpinBox(Form)
        self.sbModule4.setGeometry(QtCore.QRect(10, 330, 71, 22))
        self.sbModule4.setMinimum(-1)
        self.sbModule4.setMaximum(2147483647)
        self.sbModule4.setObjectName(_fromUtf8("sbModule4"))
        self.pbGoModule6 = QtGui.QPushButton(Form)
        self.pbGoModule6.setGeometry(QtCore.QRect(80, 310, 51, 21))
        self.pbGoModule6.setObjectName(_fromUtf8("pbGoModule6"))
        self.sbModule5 = QtGui.QSpinBox(Form)
        self.sbModule5.setGeometry(QtCore.QRect(10, 290, 71, 22))
        self.sbModule5.setMinimum(-1)
        self.sbModule5.setMaximum(2147483647)
        self.sbModule5.setObjectName(_fromUtf8("sbModule5"))
        self.sbModule6 = QtGui.QSpinBox(Form)
        self.sbModule6.setGeometry(QtCore.QRect(10, 310, 71, 22))
        self.sbModule6.setMinimum(-1)
        self.sbModule6.setMaximum(2147483647)
        self.sbModule6.setObjectName(_fromUtf8("sbModule6"))
        self.leWho = QtGui.QLineEdit(Form)
        self.leWho.setGeometry(QtCore.QRect(90, 40, 71, 20))
        self.leWho.setObjectName(_fromUtf8("leWho"))
        self.leDate = QtGui.QLineEdit(Form)
        self.leDate.setGeometry(QtCore.QRect(90, 60, 71, 20))
        self.leDate.setObjectName(_fromUtf8("leDate"))
        self.leTime = QtGui.QLineEdit(Form)
        self.leTime.setGeometry(QtCore.QRect(90, 80, 71, 20))
        self.leTime.setObjectName(_fromUtf8("leTime"))
        self.leCureStart = QtGui.QLineEdit(Form)
        self.leCureStart.setGeometry(QtCore.QRect(90, 100, 71, 20))
        self.leCureStart.setObjectName(_fromUtf8("leCureStart"))
        self.leCureStop = QtGui.QLineEdit(Form)
        self.leCureStop.setGeometry(QtCore.QRect(90, 120, 71, 20))
        self.leCureStop.setObjectName(_fromUtf8("leCureStop"))
        self.leCureDuration = QtGui.QLineEdit(Form)
        self.leCureDuration.setGeometry(QtCore.QRect(90, 140, 71, 20))
        self.leCureDuration.setObjectName(_fromUtf8("leCureDuration"))
        self.leCureTemp = QtGui.QLineEdit(Form)
        self.leCureTemp.setGeometry(QtCore.QRect(90, 160, 71, 20))
        self.leCureTemp.setObjectName(_fromUtf8("leCureTemp"))
        self.leCureHumidity = QtGui.QLineEdit(Form)
        self.leCureHumidity.setGeometry(QtCore.QRect(90, 180, 71, 20))
        self.leCureHumidity.setObjectName(_fromUtf8("leCureHumidity"))
        self.pbKaptonStepNew = QtGui.QPushButton(Form)
        self.pbKaptonStepNew.setGeometry(QtCore.QRect(200, 12, 71, 21))
        self.pbKaptonStepNew.setObjectName(_fromUtf8("pbKaptonStepNew"))
        self.pbKaptonStepEdit = QtGui.QPushButton(Form)
        self.pbKaptonStepEdit.setGeometry(QtCore.QRect(280, 10, 71, 21))
        self.pbKaptonStepEdit.setObjectName(_fromUtf8("pbKaptonStepEdit"))
        self.pbKaptonStepCancel = QtGui.QPushButton(Form)
        self.pbKaptonStepCancel.setGeometry(QtCore.QRect(280, 40, 71, 21))
        self.pbKaptonStepCancel.setObjectName(_fromUtf8("pbKaptonStepCancel"))
        self.pbKaptonStepSave = QtGui.QPushButton(Form)
        self.pbKaptonStepSave.setGeometry(QtCore.QRect(200, 40, 71, 21))
        self.pbKaptonStepSave.setObjectName(_fromUtf8("pbKaptonStepSave"))
        self.leAralditeBatch = QtGui.QLineEdit(Form)
        self.leAralditeBatch.setGeometry(QtCore.QRect(90, 360, 71, 20))
        self.leAralditeBatch.setObjectName(_fromUtf8("leAralditeBatch"))
        self.lineEdit_11 = QtGui.QLineEdit(Form)
        self.lineEdit_11.setGeometry(QtCore.QRect(10, 360, 81, 21))
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.lineEdit.setText(_translate("Form", "Kapton step ID", None))
        self.lineEdit_2.setText(_translate("Form", "who", None))
        self.lineEdit_3.setText(_translate("Form", "date", None))
        self.lineEdit_4.setText(_translate("Form", "time", None))
        self.lineEdit_5.setText(_translate("Form", "cure start", None))
        self.lineEdit_6.setText(_translate("Form", "cure stop", None))
        self.lineEdit_7.setText(_translate("Form", "cure duration", None))
        self.lineEdit_8.setText(_translate("Form", "cure temp", None))
        self.lineEdit_9.setText(_translate("Form", "cure humidity", None))
        self.lineEdit_10.setText(_translate("Form", "Modules included", None))
        self.pbGoModule1.setText(_translate("Form", "go to", None))
        self.pbGoModule2.setText(_translate("Form", "go to", None))
        self.pbGoModule3.setText(_translate("Form", "go to", None))
        self.pbGoModule4.setText(_translate("Form", "go to", None))
        self.pbGoModule5.setText(_translate("Form", "go to", None))
        self.pbGoModule6.setText(_translate("Form", "go to", None))
        self.pbKaptonStepNew.setText(_translate("Form", "New", None))
        self.pbKaptonStepEdit.setText(_translate("Form", "Edit", None))
        self.pbKaptonStepCancel.setText(_translate("Form", "Cancel", None))
        self.pbKaptonStepSave.setText(_translate("Form", "Save", None))
        self.lineEdit_11.setText(_translate("Form", "Araldite batch#", None))

