# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\aptanaWorkspace\plot_gui.ui'
#
# Created: Tue May 28 10:47:13 2013
#      by: PyQt4 UI code generator 4.10.1
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(557, 415)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 491, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.widget = matplotlibWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 70, 491, 301))
        self.widget.setObjectName(_fromUtf8("widget"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "PushButton", None))

from matplotlibwidgetFile import matplotlibWidget
