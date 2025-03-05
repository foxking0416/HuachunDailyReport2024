# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtCreateProjectDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QDoubleSpinBox,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(570, 476)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.qtProjectNumberLineEdit = QLineEdit(Dialog)
        self.qtProjectNumberLineEdit.setObjectName(u"qtProjectNumberLineEdit")

        self.horizontalLayout_5.addWidget(self.qtProjectNumberLineEdit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_7)

        self.qtProjectNumberWarningLabel = QLabel(Dialog)
        self.qtProjectNumberWarningLabel.setObjectName(u"qtProjectNumberWarningLabel")

        self.horizontalLayout_21.addWidget(self.qtProjectNumberWarningLabel)


        self.verticalLayout_7.addLayout(self.horizontalLayout_21)


        self.horizontalLayout_20.addLayout(self.verticalLayout_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_14 = QLabel(Dialog)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_18.addWidget(self.label_14)

        self.qtProjectNameLineEdit = QLineEdit(Dialog)
        self.qtProjectNameLineEdit.setObjectName(u"qtProjectNameLineEdit")

        self.horizontalLayout_18.addWidget(self.qtProjectNameLineEdit)


        self.horizontalLayout_23.addLayout(self.horizontalLayout_18)


        self.verticalLayout_9.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_8)

        self.qtProjectNameWarningLabel = QLabel(Dialog)
        self.qtProjectNameWarningLabel.setObjectName(u"qtProjectNameWarningLabel")

        self.horizontalLayout_24.addWidget(self.qtProjectNameWarningLabel)


        self.verticalLayout_9.addLayout(self.horizontalLayout_24)


        self.horizontalLayout_22.addLayout(self.verticalLayout_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout_19.addWidget(self.label)

        self.qtContractNumberLineEdit = QLineEdit(Dialog)
        self.qtContractNumberLineEdit.setObjectName(u"qtContractNumberLineEdit")

        self.horizontalLayout_19.addWidget(self.qtContractNumberLineEdit)


        self.horizontalLayout_26.addLayout(self.horizontalLayout_19)


        self.verticalLayout_10.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_9)

        self.qtContractNumberWarningLabel = QLabel(Dialog)
        self.qtContractNumberWarningLabel.setObjectName(u"qtContractNumberWarningLabel")

        self.horizontalLayout_27.addWidget(self.qtContractNumberWarningLabel)


        self.verticalLayout_10.addLayout(self.horizontalLayout_27)


        self.horizontalLayout_25.addLayout(self.verticalLayout_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.qtProjectLocationLineEdit = QLineEdit(Dialog)
        self.qtProjectLocationLineEdit.setObjectName(u"qtProjectLocationLineEdit")

        self.horizontalLayout_6.addWidget(self.qtProjectLocationLineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.qtContractValueSpinBox = QSpinBox(Dialog)
        self.qtContractValueSpinBox.setObjectName(u"qtContractValueSpinBox")
        self.qtContractValueSpinBox.setMaximum(999999999)

        self.horizontalLayout_7.addWidget(self.qtContractValueSpinBox)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_8.addWidget(self.label_11)

        self.qtBidDateEdit = QDateEdit(Dialog)
        self.qtBidDateEdit.setObjectName(u"qtBidDateEdit")
        self.qtBidDateEdit.setCalendarPopup(True)

        self.horizontalLayout_8.addWidget(self.qtBidDateEdit)

        self.qtBidWeekdayLabel = QLabel(Dialog)
        self.qtBidWeekdayLabel.setObjectName(u"qtBidWeekdayLabel")

        self.horizontalLayout_8.addWidget(self.qtBidWeekdayLabel)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.qtOwnerLineEdit = QLineEdit(Dialog)
        self.qtOwnerLineEdit.setObjectName(u"qtOwnerLineEdit")

        self.horizontalLayout_9.addWidget(self.qtOwnerLineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_10.addWidget(self.label_8)

        self.qtSupervisorLineEdit = QLineEdit(Dialog)
        self.qtSupervisorLineEdit.setObjectName(u"qtSupervisorLineEdit")

        self.horizontalLayout_10.addWidget(self.qtSupervisorLineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_11.addWidget(self.label_9)

        self.qtDesignerLineEdit = QLineEdit(Dialog)
        self.qtDesignerLineEdit.setObjectName(u"qtDesignerLineEdit")

        self.horizontalLayout_11.addWidget(self.qtDesignerLineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.qtContractorLineEdit = QLineEdit(Dialog)
        self.qtContractorLineEdit.setObjectName(u"qtContractorLineEdit")

        self.horizontalLayout_12.addWidget(self.qtContractorLineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_17 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.qtWorkingDayRadioButton = QRadioButton(self.groupBox_2)
        self.qtWorkingDayRadioButton.setObjectName(u"qtWorkingDayRadioButton")
        self.qtWorkingDayRadioButton.setChecked(True)

        self.horizontalLayout_17.addWidget(self.qtWorkingDayRadioButton)

        self.qtCalendarDayRadioButton = QRadioButton(self.groupBox_2)
        self.qtCalendarDayRadioButton.setObjectName(u"qtCalendarDayRadioButton")

        self.horizontalLayout_17.addWidget(self.qtCalendarDayRadioButton)

        self.qtFixedDeadlineRadioButton = QRadioButton(self.groupBox_2)
        self.qtFixedDeadlineRadioButton.setObjectName(u"qtFixedDeadlineRadioButton")

        self.horizontalLayout_17.addWidget(self.qtFixedDeadlineRadioButton)


        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.qtWorkingDayGroupBox = QGroupBox(self.groupBox)
        self.qtWorkingDayGroupBox.setObjectName(u"qtWorkingDayGroupBox")
        self.horizontalLayout_16 = QHBoxLayout(self.qtWorkingDayGroupBox)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.qtNoDayOffRadioButton = QRadioButton(self.qtWorkingDayGroupBox)
        self.qtNoDayOffRadioButton.setObjectName(u"qtNoDayOffRadioButton")

        self.horizontalLayout_16.addWidget(self.qtNoDayOffRadioButton)

        self.qtOneDayOffRadioButton = QRadioButton(self.qtWorkingDayGroupBox)
        self.qtOneDayOffRadioButton.setObjectName(u"qtOneDayOffRadioButton")
        self.qtOneDayOffRadioButton.setChecked(True)

        self.horizontalLayout_16.addWidget(self.qtOneDayOffRadioButton)

        self.qtTwoDayOffRadioButton = QRadioButton(self.qtWorkingDayGroupBox)
        self.qtTwoDayOffRadioButton.setObjectName(u"qtTwoDayOffRadioButton")

        self.horizontalLayout_16.addWidget(self.qtTwoDayOffRadioButton)


        self.verticalLayout_5.addWidget(self.qtWorkingDayGroupBox)

        self.qtConstantConditionSettingPushButton = QPushButton(self.groupBox)
        self.qtConstantConditionSettingPushButton.setObjectName(u"qtConstantConditionSettingPushButton")

        self.verticalLayout_5.addWidget(self.qtConstantConditionSettingPushButton)

        self.qtVariableConditionSettingPushButton = QPushButton(self.groupBox)
        self.qtVariableConditionSettingPushButton.setObjectName(u"qtVariableConditionSettingPushButton")

        self.verticalLayout_5.addWidget(self.qtVariableConditionSettingPushButton)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.qtStartDateEdit = QDateEdit(Dialog)
        self.qtStartDateEdit.setObjectName(u"qtStartDateEdit")
        self.qtStartDateEdit.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.qtStartDateEdit)

        self.qtStartWeekdayLabel = QLabel(Dialog)
        self.qtStartWeekdayLabel.setObjectName(u"qtStartWeekdayLabel")

        self.horizontalLayout_3.addWidget(self.qtStartWeekdayLabel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_13.addWidget(self.label_3)

        self.qtContractWorkingDaysDoubleSpinBox = QDoubleSpinBox(Dialog)
        self.qtContractWorkingDaysDoubleSpinBox.setObjectName(u"qtContractWorkingDaysDoubleSpinBox")
        self.qtContractWorkingDaysDoubleSpinBox.setDecimals(1)
        self.qtContractWorkingDaysDoubleSpinBox.setMinimum(1.000000000000000)
        self.qtContractWorkingDaysDoubleSpinBox.setMaximum(10000.000000000000000)
        self.qtContractWorkingDaysDoubleSpinBox.setValue(1.000000000000000)

        self.horizontalLayout_13.addWidget(self.qtContractWorkingDaysDoubleSpinBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_12 = QLabel(Dialog)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_14.addWidget(self.label_12)

        self.qtContractFinishDateEdit = QDateEdit(Dialog)
        self.qtContractFinishDateEdit.setObjectName(u"qtContractFinishDateEdit")
        self.qtContractFinishDateEdit.setCalendarPopup(True)

        self.horizontalLayout_14.addWidget(self.qtContractFinishDateEdit)

        self.qtFinishWeekdayLabel = QLabel(Dialog)
        self.qtFinishWeekdayLabel.setObjectName(u"qtFinishWeekdayLabel")

        self.horizontalLayout_14.addWidget(self.qtFinishWeekdayLabel)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_13 = QLabel(Dialog)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_15.addWidget(self.label_13)

        self.qtTotalDaysDoubleSpinBox = QDoubleSpinBox(Dialog)
        self.qtTotalDaysDoubleSpinBox.setObjectName(u"qtTotalDaysDoubleSpinBox")
        self.qtTotalDaysDoubleSpinBox.setDecimals(1)
        self.qtTotalDaysDoubleSpinBox.setMinimum(1.000000000000000)
        self.qtTotalDaysDoubleSpinBox.setMaximum(10000.000000000000000)
        self.qtTotalDaysDoubleSpinBox.setValue(1.000000000000000)

        self.horizontalLayout_15.addWidget(self.qtTotalDaysDoubleSpinBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_15)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.qtOkPushButton = QPushButton(Dialog)
        self.qtOkPushButton.setObjectName(u"qtOkPushButton")

        self.horizontalLayout_4.addWidget(self.qtOkPushButton)

        self.qtCancelPushButton = QPushButton(Dialog)
        self.qtCancelPushButton.setObjectName(u"qtCancelPushButton")

        self.horizontalLayout_4.addWidget(self.qtCancelPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u65b0\u589e\u5de5\u7a0b\u8cc7\u6599", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u5de5\u7a0b\u7de8\u865f", None))
        self.qtProjectNumberLineEdit.setText("")
        self.qtProjectNumberWarningLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"\u5de5\u7a0b\u540d\u7a31", None))
        self.qtProjectNameLineEdit.setText("")
        self.qtProjectNameWarningLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u6848\u865f\u53ca\u5951\u7d04\u865f", None))
        self.qtContractNumberLineEdit.setText("")
        self.qtContractNumberWarningLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u5de5\u7a0b\u5730\u9ede", None))
        self.qtProjectLocationLineEdit.setText("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u5951\u7d04\u91d1\u984d", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u6c7a\u6a19\u65e5\u671f", None))
        self.qtBidWeekdayLabel.setText(QCoreApplication.translate("Dialog", u"\u65e5", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u696d\u4e3b", None))
        self.qtOwnerLineEdit.setText("")
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u76e3\u9020\u55ae\u4f4d", None))
        self.qtSupervisorLineEdit.setText("")
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u8a2d\u8a08\u55ae\u4f4d", None))
        self.qtDesignerLineEdit.setText("")
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u627f\u652c\u5ee0\u5546", None))
        self.qtContractorLineEdit.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u5de5\u671f\u689d\u4ef6", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"\u57fa\u672c\u5de5\u671f\u8a2d\u5b9a", None))
        self.qtWorkingDayRadioButton.setText(QCoreApplication.translate("Dialog", u"\u5de5\u4f5c\u5929", None))
        self.qtCalendarDayRadioButton.setText(QCoreApplication.translate("Dialog", u"\u65e5\u66c6\u5929", None))
        self.qtFixedDeadlineRadioButton.setText(QCoreApplication.translate("Dialog", u"\u9650\u671f\u5b8c\u5de5", None))
        self.qtWorkingDayGroupBox.setTitle(QCoreApplication.translate("Dialog", u"\u5468\u4f11\u5de5\u671f", None))
        self.qtNoDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u7121\u5468\u4f11", None))
        self.qtOneDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u5468\u4f11\u4e00\u65e5", None))
        self.qtTwoDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u5468\u4f11\u4e8c\u65e5", None))
        self.qtConstantConditionSettingPushButton.setText(QCoreApplication.translate("Dialog", u"\u56fa\u5b9a\u56e0\u7d20\u8a2d\u5b9a(\u570b\u5b9a\u5047\u65e5)", None))
        self.qtVariableConditionSettingPushButton.setText(QCoreApplication.translate("Dialog", u"\u8b8a\u52d5\u56e0\u7d20\u8a2d\u5b9a(\u5929\u5019\u3001\u4eba\u70ba)", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u958b\u5de5\u65e5\u671f", None))
        self.qtStartWeekdayLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u5951\u7d04\u5de5\u671f", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u5951\u7d04\u5b8c\u5de5\u65e5", None))
        self.qtFinishWeekdayLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u5de5\u7a0b\u7e3d\u5929\u6578", None))
        self.qtOkPushButton.setText(QCoreApplication.translate("Dialog", u"\u78ba\u5b9a", None))
        self.qtCancelPushButton.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

