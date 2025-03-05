# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtDailyReportPerDayDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(883, 604)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_20 = QLabel(Dialog)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_5.addWidget(self.label_20)

        self.qtProjectNumberLineEdit = QLineEdit(Dialog)
        self.qtProjectNumberLineEdit.setObjectName(u"qtProjectNumberLineEdit")

        self.horizontalLayout_5.addWidget(self.qtProjectNumberLineEdit)

        self.label_21 = QLabel(Dialog)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_5.addWidget(self.label_21)

        self.qtProjectNameLineEdit = QLineEdit(Dialog)
        self.qtProjectNameLineEdit.setObjectName(u"qtProjectNameLineEdit")

        self.horizontalLayout_5.addWidget(self.qtProjectNameLineEdit)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_22 = QLabel(self.groupBox)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_6.addWidget(self.label_22)

        self.qtMorningWeatherComboBox = QComboBox(self.groupBox)
        self.qtMorningWeatherComboBox.addItem("")
        self.qtMorningWeatherComboBox.addItem("")
        self.qtMorningWeatherComboBox.addItem("")
        self.qtMorningWeatherComboBox.addItem("")
        self.qtMorningWeatherComboBox.addItem("")
        self.qtMorningWeatherComboBox.addItem("")
        self.qtMorningWeatherComboBox.addItem("")
        self.qtMorningWeatherComboBox.setObjectName(u"qtMorningWeatherComboBox")

        self.horizontalLayout_6.addWidget(self.qtMorningWeatherComboBox)

        self.label_23 = QLabel(self.groupBox)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_6.addWidget(self.label_23)

        self.qtAfternoonWeatherComboBox = QComboBox(self.groupBox)
        self.qtAfternoonWeatherComboBox.addItem("")
        self.qtAfternoonWeatherComboBox.addItem("")
        self.qtAfternoonWeatherComboBox.addItem("")
        self.qtAfternoonWeatherComboBox.addItem("")
        self.qtAfternoonWeatherComboBox.addItem("")
        self.qtAfternoonWeatherComboBox.addItem("")
        self.qtAfternoonWeatherComboBox.addItem("")
        self.qtAfternoonWeatherComboBox.setObjectName(u"qtAfternoonWeatherComboBox")

        self.horizontalLayout_6.addWidget(self.qtAfternoonWeatherComboBox)


        self.horizontalLayout_5.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_24 = QLabel(self.groupBox_2)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_7.addWidget(self.label_24)

        self.qtMorningHumanComboBox = QComboBox(self.groupBox_2)
        self.qtMorningHumanComboBox.addItem("")
        self.qtMorningHumanComboBox.addItem("")
        self.qtMorningHumanComboBox.addItem("")
        self.qtMorningHumanComboBox.addItem("")
        self.qtMorningHumanComboBox.setObjectName(u"qtMorningHumanComboBox")

        self.horizontalLayout_7.addWidget(self.qtMorningHumanComboBox)

        self.label_25 = QLabel(self.groupBox_2)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_7.addWidget(self.label_25)

        self.qtAfternoonHumanComboBox = QComboBox(self.groupBox_2)
        self.qtAfternoonHumanComboBox.addItem("")
        self.qtAfternoonHumanComboBox.addItem("")
        self.qtAfternoonHumanComboBox.addItem("")
        self.qtAfternoonHumanComboBox.addItem("")
        self.qtAfternoonHumanComboBox.setObjectName(u"qtAfternoonHumanComboBox")

        self.horizontalLayout_7.addWidget(self.qtAfternoonHumanComboBox)


        self.horizontalLayout_5.addWidget(self.groupBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_19 = QLabel(Dialog)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_4.addWidget(self.label_19)

        self.qtTodayDateEdit = QDateEdit(Dialog)
        self.qtTodayDateEdit.setObjectName(u"qtTodayDateEdit")

        self.horizontalLayout_4.addWidget(self.qtTodayDateEdit)

        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_4.addWidget(self.label_11)

        self.label_16 = QLabel(Dialog)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_4.addWidget(self.label_16)

        self.label_17 = QLabel(Dialog)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_4.addWidget(self.label_17)

        self.qtStartDateEdit = QDateEdit(Dialog)
        self.qtStartDateEdit.setObjectName(u"qtStartDateEdit")

        self.horizontalLayout_4.addWidget(self.qtStartDateEdit)

        self.label_18 = QLabel(Dialog)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_4.addWidget(self.label_18)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_3.addWidget(self.label_10)

        self.lineEdit_9 = QLineEdit(Dialog)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.horizontalLayout_3.addWidget(self.lineEdit_9)

        self.label_12 = QLabel(Dialog)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_3.addWidget(self.label_12)

        self.lineEdit_10 = QLineEdit(Dialog)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.horizontalLayout_3.addWidget(self.lineEdit_10)

        self.label_13 = QLabel(Dialog)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_3.addWidget(self.label_13)

        self.lineEdit_11 = QLineEdit(Dialog)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.horizontalLayout_3.addWidget(self.lineEdit_11)

        self.label_14 = QLabel(Dialog)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_3.addWidget(self.label_14)

        self.lineEdit_12 = QLineEdit(Dialog)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.horizontalLayout_3.addWidget(self.lineEdit_12)

        self.label_15 = QLabel(Dialog)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_3.addWidget(self.label_15)

        self.dateEdit_2 = QDateEdit(Dialog)
        self.dateEdit_2.setObjectName(u"dateEdit_2")

        self.horizontalLayout_3.addWidget(self.dateEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.lineEdit_7 = QLineEdit(Dialog)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.horizontalLayout_2.addWidget(self.lineEdit_7)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_2.addWidget(self.label_8)

        self.lineEdit_8 = QLineEdit(Dialog)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.horizontalLayout_2.addWidget(self.lineEdit_8)

        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_2.addWidget(self.label_9)

        self.dateEdit = QDateEdit(Dialog)
        self.dateEdit.setObjectName(u"dateEdit")

        self.horizontalLayout_2.addWidget(self.dateEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout.addWidget(self.lineEdit_3)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(Dialog)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout.addWidget(self.lineEdit_4)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.lineEdit_5 = QLineEdit(Dialog)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout.addWidget(self.lineEdit_5)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.lineEdit_6 = QLineEdit(Dialog)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout.addWidget(self.lineEdit_6)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.qtOkPushButton = QPushButton(Dialog)
        self.qtOkPushButton.setObjectName(u"qtOkPushButton")

        self.horizontalLayout_8.addWidget(self.qtOkPushButton)

        self.qtCancelPushButton = QPushButton(Dialog)
        self.qtCancelPushButton.setObjectName(u"qtCancelPushButton")

        self.horizontalLayout_8.addWidget(self.qtCancelPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u65e5\u5831\u8868", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"\u5de5\u7a0b\u7de8\u865f", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"\u5de5\u7a0b\u540d\u7a31", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u5929\u6c23\u72c0\u6cc1", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"\u4e0a\u5348", None))
        self.qtMorningWeatherComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"\u6674", None))
        self.qtMorningWeatherComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"\u96e8", None))
        self.qtMorningWeatherComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"\u8c6a\u96e8", None))
        self.qtMorningWeatherComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"\u98b1\u98a8", None))
        self.qtMorningWeatherComboBox.setItemText(4, QCoreApplication.translate("Dialog", u"\u9177\u71b1", None))
        self.qtMorningWeatherComboBox.setItemText(5, QCoreApplication.translate("Dialog", u"\u6ce5\u6fd8", None))
        self.qtMorningWeatherComboBox.setItemText(6, QCoreApplication.translate("Dialog", u"\u5176\u4ed6", None))

        self.label_23.setText(QCoreApplication.translate("Dialog", u"\u4e0b\u5348", None))
        self.qtAfternoonWeatherComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"\u6674", None))
        self.qtAfternoonWeatherComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"\u96e8", None))
        self.qtAfternoonWeatherComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"\u8c6a\u96e8", None))
        self.qtAfternoonWeatherComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"\u98b1\u98a8", None))
        self.qtAfternoonWeatherComboBox.setItemText(4, QCoreApplication.translate("Dialog", u"\u9177\u71b1", None))
        self.qtAfternoonWeatherComboBox.setItemText(5, QCoreApplication.translate("Dialog", u"\u6ce5\u6fd8", None))
        self.qtAfternoonWeatherComboBox.setItemText(6, QCoreApplication.translate("Dialog", u"\u5176\u4ed6", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"\u5176\u4ed6\u72c0\u6cc1", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"\u4e0a\u5348", None))
        self.qtMorningHumanComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"\u7121", None))
        self.qtMorningHumanComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"\u505c\u5de5", None))
        self.qtMorningHumanComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"\u505c\u96fb", None))
        self.qtMorningHumanComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"\u5176\u4ed6", None))

        self.label_25.setText(QCoreApplication.translate("Dialog", u"\u4e0b\u5348", None))
        self.qtAfternoonHumanComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"\u7121", None))
        self.qtAfternoonHumanComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"\u505c\u5de5", None))
        self.qtAfternoonHumanComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"\u505c\u96fb", None))
        self.qtAfternoonHumanComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"\u5176\u4ed6", None))

        self.label_19.setText(QCoreApplication.translate("Dialog", u"\u4eca\u65e5\u65e5\u671f", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u5de5\u671f\u8a08\u7b97\u65b9\u5f0f\u70ba\uff1a", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"\u958b\u5de5\u65e5\u671f", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"\u672c\u65e5\u4e0d\u8a08", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u5951\u7d04\u5de5\u671f", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u4eca\u65e5\u958b\u59cb\u8ffd\u52a0\u5de5\u671f", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u7d2f\u8a08\u8ffd\u52a0\u5de5\u671f", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"\u5de5\u671f\u7e3d\u8a08", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"\u5951\u7d04\u5b8c\u5de5\u65e5", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u5951\u7d04\u5929\u6578", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u8ffd\u52a0\u5de5\u671f\u5f8c\u7e3d\u5929\u6578", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u8b8a\u52d5\u5b8c\u5de5\u65e5", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u958b\u5de5\u8fc4\u4eca\u5929\u6578", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u5be6\u969b\u5de5\u671f", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u5269\u9918\u5de5\u671f", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u5269\u9918\u5929\u6578", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u903e\u671f\u5929\u6578", None))
        self.qtOkPushButton.setText(QCoreApplication.translate("Dialog", u"\u78ba\u8a8d", None))
        self.qtCancelPushButton.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

