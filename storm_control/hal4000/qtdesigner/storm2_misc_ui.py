# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'storm2-misc.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(391, 201)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(391, 201))
        Dialog.setMaximumSize(QtCore.QSize(391, 201))
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(300, 170, 75, 24))
        self.okButton.setCheckable(False)
        self.okButton.setObjectName("okButton")
        self.filterWheelGroupBox = QtWidgets.QGroupBox(Dialog)
        self.filterWheelGroupBox.setGeometry(QtCore.QRect(10, 110, 371, 51))
        self.filterWheelGroupBox.setObjectName("filterWheelGroupBox")
        self.filter1Button = QtWidgets.QPushButton(self.filterWheelGroupBox)
        self.filter1Button.setGeometry(QtCore.QRect(10, 20, 51, 24))
        self.filter1Button.setCheckable(True)
        self.filter1Button.setAutoExclusive(True)
        self.filter1Button.setObjectName("filter1Button")
        self.filter2Button = QtWidgets.QPushButton(self.filterWheelGroupBox)
        self.filter2Button.setGeometry(QtCore.QRect(70, 20, 51, 24))
        self.filter2Button.setCheckable(True)
        self.filter2Button.setAutoExclusive(True)
        self.filter2Button.setObjectName("filter2Button")
        self.filter3Button = QtWidgets.QPushButton(self.filterWheelGroupBox)
        self.filter3Button.setGeometry(QtCore.QRect(130, 20, 51, 24))
        self.filter3Button.setCheckable(True)
        self.filter3Button.setAutoExclusive(True)
        self.filter3Button.setObjectName("filter3Button")
        self.filter4Button = QtWidgets.QPushButton(self.filterWheelGroupBox)
        self.filter4Button.setGeometry(QtCore.QRect(190, 20, 51, 24))
        self.filter4Button.setCheckable(True)
        self.filter4Button.setAutoExclusive(True)
        self.filter4Button.setObjectName("filter4Button")
        self.filter5Button = QtWidgets.QPushButton(self.filterWheelGroupBox)
        self.filter5Button.setGeometry(QtCore.QRect(250, 20, 51, 24))
        self.filter5Button.setCheckable(True)
        self.filter5Button.setAutoExclusive(True)
        self.filter5Button.setObjectName("filter5Button")
        self.filter6Button = QtWidgets.QPushButton(self.filterWheelGroupBox)
        self.filter6Button.setGeometry(QtCore.QRect(310, 20, 51, 24))
        self.filter6Button.setCheckable(True)
        self.filter6Button.setAutoExclusive(True)
        self.filter6Button.setObjectName("filter6Button")
        self.emGroupBox = QtWidgets.QGroupBox(Dialog)
        self.emGroupBox.setGeometry(QtCore.QRect(10, 20, 371, 81))
        self.emGroupBox.setObjectName("emGroupBox")
        self.emFilter1Button = QtWidgets.QPushButton(self.emGroupBox)
        self.emFilter1Button.setGeometry(QtCore.QRect(10, 20, 51, 24))
        self.emFilter1Button.setCheckable(True)
        self.emFilter1Button.setAutoExclusive(True)
        self.emFilter1Button.setObjectName("emFilter1Button")
        self.emFilter2Button = QtWidgets.QPushButton(self.emGroupBox)
        self.emFilter2Button.setGeometry(QtCore.QRect(70, 20, 51, 24))
        self.emFilter2Button.setCheckable(True)
        self.emFilter2Button.setAutoExclusive(True)
        self.emFilter2Button.setObjectName("emFilter2Button")
        self.emFilter3Button = QtWidgets.QPushButton(self.emGroupBox)
        self.emFilter3Button.setGeometry(QtCore.QRect(130, 20, 51, 24))
        self.emFilter3Button.setCheckable(True)
        self.emFilter3Button.setAutoExclusive(True)
        self.emFilter3Button.setObjectName("emFilter3Button")
        self.emFilter4Button = QtWidgets.QPushButton(self.emGroupBox)
        self.emFilter4Button.setGeometry(QtCore.QRect(190, 20, 51, 24))
        self.emFilter4Button.setCheckable(True)
        self.emFilter4Button.setAutoExclusive(True)
        self.emFilter4Button.setObjectName("emFilter4Button")
        self.emFilter6Button = QtWidgets.QPushButton(self.emGroupBox)
        self.emFilter6Button.setGeometry(QtCore.QRect(310, 20, 51, 24))
        self.emFilter6Button.setCheckable(True)
        self.emFilter6Button.setAutoExclusive(True)
        self.emFilter6Button.setObjectName("emFilter6Button")
        self.emFilter5Button = QtWidgets.QPushButton(self.emGroupBox)
        self.emFilter5Button.setGeometry(QtCore.QRect(250, 20, 51, 24))
        self.emFilter5Button.setCheckable(True)
        self.emFilter5Button.setAutoExclusive(True)
        self.emFilter5Button.setObjectName("emFilter5Button")
        self.emCheckBox = QtWidgets.QCheckBox(self.emGroupBox)
        self.emCheckBox.setGeometry(QtCore.QRect(12, 52, 131, 17))
        self.emCheckBox.setObjectName("emCheckBox")
        self.emSpinBox = QtWidgets.QSpinBox(self.emGroupBox)
        self.emSpinBox.setGeometry(QtCore.QRect(290, 50, 71, 22))
        self.emSpinBox.setMinimum(1)
        self.emSpinBox.setMaximum(1000)
        self.emSpinBox.setObjectName("emSpinBox")
        self.emLabel = QtWidgets.QLabel(self.emGroupBox)
        self.emLabel.setGeometry(QtCore.QRect(201, 51, 81, 20))
        self.emLabel.setObjectName("emLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "HAL-4000 Miscellaneous Controls"))
        self.okButton.setText(_translate("Dialog", "Ok"))
        self.filterWheelGroupBox.setTitle(_translate("Dialog", "Turret Filter Wheel Control"))
        self.filter1Button.setText(_translate("Dialog", "1"))
        self.filter2Button.setText(_translate("Dialog", "2"))
        self.filter3Button.setText(_translate("Dialog", "3"))
        self.filter4Button.setText(_translate("Dialog", "4"))
        self.filter5Button.setText(_translate("Dialog", "5"))
        self.filter6Button.setText(_translate("Dialog", "6"))
        self.emGroupBox.setTitle(_translate("Dialog", "Emission Filter Wheel Control"))
        self.emFilter1Button.setText(_translate("Dialog", "1"))
        self.emFilter2Button.setText(_translate("Dialog", "2"))
        self.emFilter3Button.setText(_translate("Dialog", "3"))
        self.emFilter4Button.setText(_translate("Dialog", "4"))
        self.emFilter6Button.setText(_translate("Dialog", "6"))
        self.emFilter5Button.setText(_translate("Dialog", "5"))
        self.emCheckBox.setText(_translate("Dialog", "Move During Filming"))
        self.emLabel.setText(_translate("Dialog", "Period (frames)"))

