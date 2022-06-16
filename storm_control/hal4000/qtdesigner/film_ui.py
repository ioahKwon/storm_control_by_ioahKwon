# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'film.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        GroupBox.setObjectName("GroupBox")
        GroupBox.resize(241, 296)
        self.verticalLayout = QtWidgets.QVBoxLayout(GroupBox)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.shuttersLabels = QtWidgets.QLabel(GroupBox)
        self.shuttersLabels.setObjectName("shuttersLabels")
        self.verticalLayout.addWidget(self.shuttersLabels)
        self.shuttersText = QtWidgets.QLabel(GroupBox)
        self.shuttersText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.shuttersText.setObjectName("shuttersText")
        self.verticalLayout.addWidget(self.shuttersText)
        self.directoryLabel = QtWidgets.QLabel(GroupBox)
        self.directoryLabel.setObjectName("directoryLabel")
        self.verticalLayout.addWidget(self.directoryLabel)
        self.directoryText = QtWidgets.QLabel(GroupBox)
        self.directoryText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.directoryText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.directoryText.setObjectName("directoryText")
        self.verticalLayout.addWidget(self.directoryText)
        self.autoIncCheckBox = QtWidgets.QCheckBox(GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autoIncCheckBox.sizePolicy().hasHeightForWidth())
        self.autoIncCheckBox.setSizePolicy(sizePolicy)
        self.autoIncCheckBox.setChecked(True)
        self.autoIncCheckBox.setObjectName("autoIncCheckBox")
        self.verticalLayout.addWidget(self.autoIncCheckBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filenameEdit = QtWidgets.QLineEdit(GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filenameEdit.sizePolicy().hasHeightForWidth())
        self.filenameEdit.setSizePolicy(sizePolicy)
        self.filenameEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.filenameEdit.setObjectName("filenameEdit")
        self.horizontalLayout.addWidget(self.filenameEdit)
        self.indexSpinBox = QtWidgets.QSpinBox(GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.indexSpinBox.sizePolicy().hasHeightForWidth())
        self.indexSpinBox.setSizePolicy(sizePolicy)
        self.indexSpinBox.setMaximumSize(QtCore.QSize(55, 16777215))
        self.indexSpinBox.setMinimum(1)
        self.indexSpinBox.setMaximum(9999)
        self.indexSpinBox.setObjectName("indexSpinBox")
        self.horizontalLayout.addWidget(self.indexSpinBox)
        self.extensionComboBox = QtWidgets.QComboBox(GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extensionComboBox.sizePolicy().hasHeightForWidth())
        self.extensionComboBox.setSizePolicy(sizePolicy)
        self.extensionComboBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.extensionComboBox.setObjectName("extensionComboBox")
        self.horizontalLayout.addWidget(self.extensionComboBox)
        self.filetypeComboBox = QtWidgets.QComboBox(GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filetypeComboBox.sizePolicy().hasHeightForWidth())
        self.filetypeComboBox.setSizePolicy(sizePolicy)
        self.filetypeComboBox.setMaximumSize(QtCore.QSize(45, 16777215))
        self.filetypeComboBox.setObjectName("filetypeComboBox")
        self.horizontalLayout.addWidget(self.filetypeComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.filenameLabel = QtWidgets.QLabel(GroupBox)
        self.filenameLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.filenameLabel.setObjectName("filenameLabel")
        self.verticalLayout.addWidget(self.filenameLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.modeLabel = QtWidgets.QLabel(GroupBox)
        self.modeLabel.setObjectName("modeLabel")
        self.horizontalLayout_2.addWidget(self.modeLabel)
        self.modeComboBox = QtWidgets.QComboBox(GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeComboBox.sizePolicy().hasHeightForWidth())
        self.modeComboBox.setSizePolicy(sizePolicy)
        self.modeComboBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.modeComboBox.setObjectName("modeComboBox")
        self.modeComboBox.addItem("")
        self.modeComboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.modeComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lengthLabel = QtWidgets.QLabel(GroupBox)
        self.lengthLabel.setObjectName("lengthLabel")
        self.horizontalLayout_3.addWidget(self.lengthLabel)
        self.lengthSpinBox = QtWidgets.QSpinBox(GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lengthSpinBox.sizePolicy().hasHeightForWidth())
        self.lengthSpinBox.setSizePolicy(sizePolicy)
        self.lengthSpinBox.setMaximum(1000000)
        self.lengthSpinBox.setObjectName("lengthSpinBox")
        self.horizontalLayout_3.addWidget(self.lengthSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.framesLabel = QtWidgets.QLabel(GroupBox)
        self.framesLabel.setObjectName("framesLabel")
        self.horizontalLayout_4.addWidget(self.framesLabel)
        self.framesText = QtWidgets.QLabel(GroupBox)
        self.framesText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.framesText.setObjectName("framesText")
        self.horizontalLayout_4.addWidget(self.framesText)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.sizeLabel = QtWidgets.QLabel(GroupBox)
        self.sizeLabel.setObjectName("sizeLabel")
        self.horizontalLayout_6.addWidget(self.sizeLabel)
        self.sizeText = QtWidgets.QLabel(GroupBox)
        self.sizeText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sizeText.setObjectName("sizeText")
        self.horizontalLayout_6.addWidget(self.sizeText)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.autoShuttersCheckBox = QtWidgets.QCheckBox(GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autoShuttersCheckBox.sizePolicy().hasHeightForWidth())
        self.autoShuttersCheckBox.setSizePolicy(sizePolicy)
        self.autoShuttersCheckBox.setChecked(True)
        self.autoShuttersCheckBox.setObjectName("autoShuttersCheckBox")
        self.horizontalLayout_5.addWidget(self.autoShuttersCheckBox)
        self.saveMovieCheckBox = QtWidgets.QCheckBox(GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveMovieCheckBox.sizePolicy().hasHeightForWidth())
        self.saveMovieCheckBox.setSizePolicy(sizePolicy)
        self.saveMovieCheckBox.setChecked(True)
        self.saveMovieCheckBox.setObjectName("saveMovieCheckBox")
        self.horizontalLayout_5.addWidget(self.saveMovieCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.liveModeCheckBox = QtWidgets.QCheckBox(GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.liveModeCheckBox.sizePolicy().hasHeightForWidth())
        self.liveModeCheckBox.setSizePolicy(sizePolicy)
        self.liveModeCheckBox.setChecked(True)
        self.liveModeCheckBox.setObjectName("liveModeCheckBox")
        self.verticalLayout.addWidget(self.liveModeCheckBox)

        self.retranslateUi(GroupBox)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)

    def retranslateUi(self, GroupBox):
        _translate = QtCore.QCoreApplication.translate
        GroupBox.setWindowTitle(_translate("GroupBox", "GroupBox"))
        GroupBox.setTitle(_translate("GroupBox", "Film"))
        self.shuttersLabels.setText(_translate("GroupBox", "Shutter Sequence:"))
        self.shuttersText.setText(_translate("GroupBox", "asdf"))
        self.directoryLabel.setText(_translate("GroupBox", "Directory:"))
        self.directoryText.setText(_translate("GroupBox", "asdf"))
        self.autoIncCheckBox.setText(_translate("GroupBox", "Increment Automatically"))
        self.filenameLabel.setText(_translate("GroupBox", "asdf"))
        self.modeLabel.setText(_translate("GroupBox", "Mode:"))
        self.modeComboBox.setItemText(0, _translate("GroupBox", "Run Till Abort"))
        self.modeComboBox.setItemText(1, _translate("GroupBox", "Fixed Length"))
        self.lengthLabel.setText(_translate("GroupBox", "Length:"))
        self.framesLabel.setText(_translate("GroupBox", "Frames:"))
        self.framesText.setText(_translate("GroupBox", "asdf"))
        self.sizeLabel.setText(_translate("GroupBox", "Size:"))
        self.sizeText.setText(_translate("GroupBox", "asdf"))
        self.autoShuttersCheckBox.setText(_translate("GroupBox", "Run Shutters"))
        self.saveMovieCheckBox.setText(_translate("GroupBox", "Save Movie"))
        self.liveModeCheckBox.setText(_translate("GroupBox", "Live Mode"))

