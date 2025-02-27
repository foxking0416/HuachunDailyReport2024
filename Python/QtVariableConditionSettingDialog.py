# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtVariableConditionSettingDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QHBoxLayout,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(950, 575)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.qtWeatherConditionGroupBox = QGroupBox(Dialog)
        self.qtWeatherConditionGroupBox.setObjectName(u"qtWeatherConditionGroupBox")
        self.horizontalLayout = QHBoxLayout(self.qtWeatherConditionGroupBox)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(7, 7, -1, -1)
        self.qtRainGroupBox = QGroupBox(self.qtWeatherConditionGroupBox)
        self.qtRainGroupBox.setObjectName(u"qtRainGroupBox")
        self.verticalLayout_2 = QVBoxLayout(self.qtRainGroupBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.qtMorningRainGroupBox = QGroupBox(self.qtRainGroupBox)
        self.qtMorningRainGroupBox.setObjectName(u"qtMorningRainGroupBox")
        self.verticalLayout_3 = QVBoxLayout(self.qtMorningRainGroupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.qtMorningRainOneDayOffRadioButton = QRadioButton(self.qtMorningRainGroupBox)
        self.qtMorningRainOneDayOffRadioButton.setObjectName(u"qtMorningRainOneDayOffRadioButton")
        self.qtMorningRainOneDayOffRadioButton.setChecked(True)

        self.verticalLayout_3.addWidget(self.qtMorningRainOneDayOffRadioButton)

        self.qtMorningRainHalfDayOffRadioButton = QRadioButton(self.qtMorningRainGroupBox)
        self.qtMorningRainHalfDayOffRadioButton.setObjectName(u"qtMorningRainHalfDayOffRadioButton")

        self.verticalLayout_3.addWidget(self.qtMorningRainHalfDayOffRadioButton)

        self.qtMorningRainNoDayOffRadioButton = QRadioButton(self.qtMorningRainGroupBox)
        self.qtMorningRainNoDayOffRadioButton.setObjectName(u"qtMorningRainNoDayOffRadioButton")

        self.verticalLayout_3.addWidget(self.qtMorningRainNoDayOffRadioButton)


        self.verticalLayout_2.addWidget(self.qtMorningRainGroupBox)

        self.qtAfternoonRainGroupBox = QGroupBox(self.qtRainGroupBox)
        self.qtAfternoonRainGroupBox.setObjectName(u"qtAfternoonRainGroupBox")
        self.verticalLayout_4 = QVBoxLayout(self.qtAfternoonRainGroupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.qtAfternoonRainOneDayOffRadioButton = QRadioButton(self.qtAfternoonRainGroupBox)
        self.qtAfternoonRainOneDayOffRadioButton.setObjectName(u"qtAfternoonRainOneDayOffRadioButton")

        self.verticalLayout_4.addWidget(self.qtAfternoonRainOneDayOffRadioButton)

        self.qtAfternoonRainHalfDayOffRadioButton = QRadioButton(self.qtAfternoonRainGroupBox)
        self.qtAfternoonRainHalfDayOffRadioButton.setObjectName(u"qtAfternoonRainHalfDayOffRadioButton")
        self.qtAfternoonRainHalfDayOffRadioButton.setChecked(True)

        self.verticalLayout_4.addWidget(self.qtAfternoonRainHalfDayOffRadioButton)

        self.qtAfternoonRainNoDayOffRadioButton = QRadioButton(self.qtAfternoonRainGroupBox)
        self.qtAfternoonRainNoDayOffRadioButton.setObjectName(u"qtAfternoonRainNoDayOffRadioButton")

        self.verticalLayout_4.addWidget(self.qtAfternoonRainNoDayOffRadioButton)


        self.verticalLayout_2.addWidget(self.qtAfternoonRainGroupBox)


        self.horizontalLayout.addWidget(self.qtRainGroupBox)

        self.qtHeavyRainGroupBox = QGroupBox(self.qtWeatherConditionGroupBox)
        self.qtHeavyRainGroupBox.setObjectName(u"qtHeavyRainGroupBox")
        self.verticalLayout_5 = QVBoxLayout(self.qtHeavyRainGroupBox)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.qtMorningHeavyRainGroupBox = QGroupBox(self.qtHeavyRainGroupBox)
        self.qtMorningHeavyRainGroupBox.setObjectName(u"qtMorningHeavyRainGroupBox")
        self.verticalLayout_6 = QVBoxLayout(self.qtMorningHeavyRainGroupBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.qtMorningHeavyRainOneDayOffRadioButton = QRadioButton(self.qtMorningHeavyRainGroupBox)
        self.qtMorningHeavyRainOneDayOffRadioButton.setObjectName(u"qtMorningHeavyRainOneDayOffRadioButton")
        self.qtMorningHeavyRainOneDayOffRadioButton.setChecked(True)

        self.verticalLayout_6.addWidget(self.qtMorningHeavyRainOneDayOffRadioButton)

        self.qtMorningHeavyRainHalfDayOffRadioButton = QRadioButton(self.qtMorningHeavyRainGroupBox)
        self.qtMorningHeavyRainHalfDayOffRadioButton.setObjectName(u"qtMorningHeavyRainHalfDayOffRadioButton")

        self.verticalLayout_6.addWidget(self.qtMorningHeavyRainHalfDayOffRadioButton)

        self.qtMorningHeavyRainNoDayOffRadioButton = QRadioButton(self.qtMorningHeavyRainGroupBox)
        self.qtMorningHeavyRainNoDayOffRadioButton.setObjectName(u"qtMorningHeavyRainNoDayOffRadioButton")

        self.verticalLayout_6.addWidget(self.qtMorningHeavyRainNoDayOffRadioButton)


        self.verticalLayout_5.addWidget(self.qtMorningHeavyRainGroupBox)

        self.qtAfternoonHeavyRainGroupBox = QGroupBox(self.qtHeavyRainGroupBox)
        self.qtAfternoonHeavyRainGroupBox.setObjectName(u"qtAfternoonHeavyRainGroupBox")
        self.verticalLayout_7 = QVBoxLayout(self.qtAfternoonHeavyRainGroupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.qtAfternoonHeavyRainOneDayOffRadioButton = QRadioButton(self.qtAfternoonHeavyRainGroupBox)
        self.qtAfternoonHeavyRainOneDayOffRadioButton.setObjectName(u"qtAfternoonHeavyRainOneDayOffRadioButton")

        self.verticalLayout_7.addWidget(self.qtAfternoonHeavyRainOneDayOffRadioButton)

        self.qtAfternoonHeavyRainHalfDayOffRadioButton = QRadioButton(self.qtAfternoonHeavyRainGroupBox)
        self.qtAfternoonHeavyRainHalfDayOffRadioButton.setObjectName(u"qtAfternoonHeavyRainHalfDayOffRadioButton")
        self.qtAfternoonHeavyRainHalfDayOffRadioButton.setChecked(True)

        self.verticalLayout_7.addWidget(self.qtAfternoonHeavyRainHalfDayOffRadioButton)

        self.qtAfternoonHeavyRainNoDayOffRadioButton = QRadioButton(self.qtAfternoonHeavyRainGroupBox)
        self.qtAfternoonHeavyRainNoDayOffRadioButton.setObjectName(u"qtAfternoonHeavyRainNoDayOffRadioButton")

        self.verticalLayout_7.addWidget(self.qtAfternoonHeavyRainNoDayOffRadioButton)


        self.verticalLayout_5.addWidget(self.qtAfternoonHeavyRainGroupBox)


        self.horizontalLayout.addWidget(self.qtHeavyRainGroupBox)

        self.qtTyphoonGroupBox = QGroupBox(self.qtWeatherConditionGroupBox)
        self.qtTyphoonGroupBox.setObjectName(u"qtTyphoonGroupBox")
        self.verticalLayout_8 = QVBoxLayout(self.qtTyphoonGroupBox)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.qtMorningTyphoonGroupBox = QGroupBox(self.qtTyphoonGroupBox)
        self.qtMorningTyphoonGroupBox.setObjectName(u"qtMorningTyphoonGroupBox")
        self.verticalLayout_9 = QVBoxLayout(self.qtMorningTyphoonGroupBox)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.qtMorningTyphoonOneDayOffRadioButton = QRadioButton(self.qtMorningTyphoonGroupBox)
        self.qtMorningTyphoonOneDayOffRadioButton.setObjectName(u"qtMorningTyphoonOneDayOffRadioButton")
        self.qtMorningTyphoonOneDayOffRadioButton.setChecked(True)

        self.verticalLayout_9.addWidget(self.qtMorningTyphoonOneDayOffRadioButton)

        self.qtMorningTyphoonHalfDayOffRadioButton = QRadioButton(self.qtMorningTyphoonGroupBox)
        self.qtMorningTyphoonHalfDayOffRadioButton.setObjectName(u"qtMorningTyphoonHalfDayOffRadioButton")

        self.verticalLayout_9.addWidget(self.qtMorningTyphoonHalfDayOffRadioButton)

        self.qtMorningTyphoonNoDayOffRadioButton = QRadioButton(self.qtMorningTyphoonGroupBox)
        self.qtMorningTyphoonNoDayOffRadioButton.setObjectName(u"qtMorningTyphoonNoDayOffRadioButton")

        self.verticalLayout_9.addWidget(self.qtMorningTyphoonNoDayOffRadioButton)


        self.verticalLayout_8.addWidget(self.qtMorningTyphoonGroupBox)

        self.qtAfternoonTyphoonGroupBox = QGroupBox(self.qtTyphoonGroupBox)
        self.qtAfternoonTyphoonGroupBox.setObjectName(u"qtAfternoonTyphoonGroupBox")
        self.verticalLayout_10 = QVBoxLayout(self.qtAfternoonTyphoonGroupBox)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.qtAfternoonTyphoonOneDayOffRadioButton = QRadioButton(self.qtAfternoonTyphoonGroupBox)
        self.qtAfternoonTyphoonOneDayOffRadioButton.setObjectName(u"qtAfternoonTyphoonOneDayOffRadioButton")
        self.qtAfternoonTyphoonOneDayOffRadioButton.setChecked(True)

        self.verticalLayout_10.addWidget(self.qtAfternoonTyphoonOneDayOffRadioButton)

        self.qtAfternoonTyphoonHalfDayOffRadioButton = QRadioButton(self.qtAfternoonTyphoonGroupBox)
        self.qtAfternoonTyphoonHalfDayOffRadioButton.setObjectName(u"qtAfternoonTyphoonHalfDayOffRadioButton")
        self.qtAfternoonTyphoonHalfDayOffRadioButton.setChecked(False)

        self.verticalLayout_10.addWidget(self.qtAfternoonTyphoonHalfDayOffRadioButton)

        self.qtAfternoonTyphoonNoDayOffRadioButton = QRadioButton(self.qtAfternoonTyphoonGroupBox)
        self.qtAfternoonTyphoonNoDayOffRadioButton.setObjectName(u"qtAfternoonTyphoonNoDayOffRadioButton")

        self.verticalLayout_10.addWidget(self.qtAfternoonTyphoonNoDayOffRadioButton)


        self.verticalLayout_8.addWidget(self.qtAfternoonTyphoonGroupBox)


        self.horizontalLayout.addWidget(self.qtTyphoonGroupBox)

        self.qtHotGroupBox = QGroupBox(self.qtWeatherConditionGroupBox)
        self.qtHotGroupBox.setObjectName(u"qtHotGroupBox")
        self.verticalLayout_13 = QVBoxLayout(self.qtHotGroupBox)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.qtMorningHotGroupBox = QGroupBox(self.qtHotGroupBox)
        self.qtMorningHotGroupBox.setObjectName(u"qtMorningHotGroupBox")
        self.verticalLayout_20 = QVBoxLayout(self.qtMorningHotGroupBox)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.qtMorningHotOneDayOffRadioButton = QRadioButton(self.qtMorningHotGroupBox)
        self.qtMorningHotOneDayOffRadioButton.setObjectName(u"qtMorningHotOneDayOffRadioButton")

        self.verticalLayout_20.addWidget(self.qtMorningHotOneDayOffRadioButton)

        self.qtMorningHotHalfDayOffRadioButton = QRadioButton(self.qtMorningHotGroupBox)
        self.qtMorningHotHalfDayOffRadioButton.setObjectName(u"qtMorningHotHalfDayOffRadioButton")

        self.verticalLayout_20.addWidget(self.qtMorningHotHalfDayOffRadioButton)

        self.qtMorningHotNoDayOffRadioButton = QRadioButton(self.qtMorningHotGroupBox)
        self.qtMorningHotNoDayOffRadioButton.setObjectName(u"qtMorningHotNoDayOffRadioButton")
        self.qtMorningHotNoDayOffRadioButton.setChecked(True)

        self.verticalLayout_20.addWidget(self.qtMorningHotNoDayOffRadioButton)


        self.verticalLayout_13.addWidget(self.qtMorningHotGroupBox)

        self.qtAfternoonHotGroupBox = QGroupBox(self.qtHotGroupBox)
        self.qtAfternoonHotGroupBox.setObjectName(u"qtAfternoonHotGroupBox")
        self.verticalLayout_21 = QVBoxLayout(self.qtAfternoonHotGroupBox)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.qtAfternoonHotOneDayOffRadioButton = QRadioButton(self.qtAfternoonHotGroupBox)
        self.qtAfternoonHotOneDayOffRadioButton.setObjectName(u"qtAfternoonHotOneDayOffRadioButton")

        self.verticalLayout_21.addWidget(self.qtAfternoonHotOneDayOffRadioButton)

        self.qtAfternoonHotHalfDayOffRadioButton = QRadioButton(self.qtAfternoonHotGroupBox)
        self.qtAfternoonHotHalfDayOffRadioButton.setObjectName(u"qtAfternoonHotHalfDayOffRadioButton")

        self.verticalLayout_21.addWidget(self.qtAfternoonHotHalfDayOffRadioButton)

        self.qtAfternoonHotNoDayOffRadioButton = QRadioButton(self.qtAfternoonHotGroupBox)
        self.qtAfternoonHotNoDayOffRadioButton.setObjectName(u"qtAfternoonHotNoDayOffRadioButton")
        self.qtAfternoonHotNoDayOffRadioButton.setChecked(True)

        self.verticalLayout_21.addWidget(self.qtAfternoonHotNoDayOffRadioButton)


        self.verticalLayout_13.addWidget(self.qtAfternoonHotGroupBox)


        self.horizontalLayout.addWidget(self.qtHotGroupBox)

        self.qtMuddyGroupBox = QGroupBox(self.qtWeatherConditionGroupBox)
        self.qtMuddyGroupBox.setObjectName(u"qtMuddyGroupBox")
        self.verticalLayout_11 = QVBoxLayout(self.qtMuddyGroupBox)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.qtMorningMuddyGroupBox = QGroupBox(self.qtMuddyGroupBox)
        self.qtMorningMuddyGroupBox.setObjectName(u"qtMorningMuddyGroupBox")
        self.verticalLayout_16 = QVBoxLayout(self.qtMorningMuddyGroupBox)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.qtMorningMuddyOneDayOffRadioButton = QRadioButton(self.qtMorningMuddyGroupBox)
        self.qtMorningMuddyOneDayOffRadioButton.setObjectName(u"qtMorningMuddyOneDayOffRadioButton")

        self.verticalLayout_16.addWidget(self.qtMorningMuddyOneDayOffRadioButton)

        self.qtMorningMuddyHalfDayOffRadioButton = QRadioButton(self.qtMorningMuddyGroupBox)
        self.qtMorningMuddyHalfDayOffRadioButton.setObjectName(u"qtMorningMuddyHalfDayOffRadioButton")

        self.verticalLayout_16.addWidget(self.qtMorningMuddyHalfDayOffRadioButton)

        self.qtMorningMuddyNoDayOffRadioButton = QRadioButton(self.qtMorningMuddyGroupBox)
        self.qtMorningMuddyNoDayOffRadioButton.setObjectName(u"qtMorningMuddyNoDayOffRadioButton")
        self.qtMorningMuddyNoDayOffRadioButton.setChecked(True)

        self.verticalLayout_16.addWidget(self.qtMorningMuddyNoDayOffRadioButton)


        self.verticalLayout_11.addWidget(self.qtMorningMuddyGroupBox)

        self.qtAfternoonMuddyGroupBox = QGroupBox(self.qtMuddyGroupBox)
        self.qtAfternoonMuddyGroupBox.setObjectName(u"qtAfternoonMuddyGroupBox")
        self.verticalLayout_18 = QVBoxLayout(self.qtAfternoonMuddyGroupBox)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.qtAfternoonMuddyOneDayOffRadioButton = QRadioButton(self.qtAfternoonMuddyGroupBox)
        self.qtAfternoonMuddyOneDayOffRadioButton.setObjectName(u"qtAfternoonMuddyOneDayOffRadioButton")

        self.verticalLayout_18.addWidget(self.qtAfternoonMuddyOneDayOffRadioButton)

        self.qtAfternoonMuddyHalfDayOffRadioButton = QRadioButton(self.qtAfternoonMuddyGroupBox)
        self.qtAfternoonMuddyHalfDayOffRadioButton.setObjectName(u"qtAfternoonMuddyHalfDayOffRadioButton")

        self.verticalLayout_18.addWidget(self.qtAfternoonMuddyHalfDayOffRadioButton)

        self.qtAfternoonMuddyNoDayOffRadioButton = QRadioButton(self.qtAfternoonMuddyGroupBox)
        self.qtAfternoonMuddyNoDayOffRadioButton.setObjectName(u"qtAfternoonMuddyNoDayOffRadioButton")
        self.qtAfternoonMuddyNoDayOffRadioButton.setChecked(True)

        self.verticalLayout_18.addWidget(self.qtAfternoonMuddyNoDayOffRadioButton)


        self.verticalLayout_11.addWidget(self.qtAfternoonMuddyGroupBox)


        self.horizontalLayout.addWidget(self.qtMuddyGroupBox)

        self.qtWeatherOtherGroupBox = QGroupBox(self.qtWeatherConditionGroupBox)
        self.qtWeatherOtherGroupBox.setObjectName(u"qtWeatherOtherGroupBox")
        self.verticalLayout_26 = QVBoxLayout(self.qtWeatherOtherGroupBox)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.qtMorningWeatherOtherGroupBox = QGroupBox(self.qtWeatherOtherGroupBox)
        self.qtMorningWeatherOtherGroupBox.setObjectName(u"qtMorningWeatherOtherGroupBox")
        self.verticalLayout_27 = QVBoxLayout(self.qtMorningWeatherOtherGroupBox)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.qtMorningWeatherOtherOneDayOffRadioButton = QRadioButton(self.qtMorningWeatherOtherGroupBox)
        self.qtMorningWeatherOtherOneDayOffRadioButton.setObjectName(u"qtMorningWeatherOtherOneDayOffRadioButton")

        self.verticalLayout_27.addWidget(self.qtMorningWeatherOtherOneDayOffRadioButton)

        self.qtMorningWeatherOtherHalfDayOffRadioButton = QRadioButton(self.qtMorningWeatherOtherGroupBox)
        self.qtMorningWeatherOtherHalfDayOffRadioButton.setObjectName(u"qtMorningWeatherOtherHalfDayOffRadioButton")

        self.verticalLayout_27.addWidget(self.qtMorningWeatherOtherHalfDayOffRadioButton)

        self.qtMorningWeatherOtherNoDayOffRadioButton = QRadioButton(self.qtMorningWeatherOtherGroupBox)
        self.qtMorningWeatherOtherNoDayOffRadioButton.setObjectName(u"qtMorningWeatherOtherNoDayOffRadioButton")
        self.qtMorningWeatherOtherNoDayOffRadioButton.setChecked(True)

        self.verticalLayout_27.addWidget(self.qtMorningWeatherOtherNoDayOffRadioButton)


        self.verticalLayout_26.addWidget(self.qtMorningWeatherOtherGroupBox)

        self.qtAfternoonWeatherOtherGroupBox = QGroupBox(self.qtWeatherOtherGroupBox)
        self.qtAfternoonWeatherOtherGroupBox.setObjectName(u"qtAfternoonWeatherOtherGroupBox")
        self.verticalLayout_28 = QVBoxLayout(self.qtAfternoonWeatherOtherGroupBox)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.qtAfternoonWeatherOtherOneDayOffRadioButton = QRadioButton(self.qtAfternoonWeatherOtherGroupBox)
        self.qtAfternoonWeatherOtherOneDayOffRadioButton.setObjectName(u"qtAfternoonWeatherOtherOneDayOffRadioButton")

        self.verticalLayout_28.addWidget(self.qtAfternoonWeatherOtherOneDayOffRadioButton)

        self.qtAfternoonWeatherOtherHalfDayOffRadioButton = QRadioButton(self.qtAfternoonWeatherOtherGroupBox)
        self.qtAfternoonWeatherOtherHalfDayOffRadioButton.setObjectName(u"qtAfternoonWeatherOtherHalfDayOffRadioButton")

        self.verticalLayout_28.addWidget(self.qtAfternoonWeatherOtherHalfDayOffRadioButton)

        self.qtAfternoonWeatherOtherNoDayOffRadioButton = QRadioButton(self.qtAfternoonWeatherOtherGroupBox)
        self.qtAfternoonWeatherOtherNoDayOffRadioButton.setObjectName(u"qtAfternoonWeatherOtherNoDayOffRadioButton")
        self.qtAfternoonWeatherOtherNoDayOffRadioButton.setChecked(True)

        self.verticalLayout_28.addWidget(self.qtAfternoonWeatherOtherNoDayOffRadioButton)


        self.verticalLayout_26.addWidget(self.qtAfternoonWeatherOtherGroupBox)


        self.horizontalLayout.addWidget(self.qtWeatherOtherGroupBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.qtWeatherConditionGroupBox)

        self.qtHumanConditionGroupBox = QGroupBox(Dialog)
        self.qtHumanConditionGroupBox.setObjectName(u"qtHumanConditionGroupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.qtHumanConditionGroupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(7, 7, -1, -1)
        self.qtSuspendGroupBox = QGroupBox(self.qtHumanConditionGroupBox)
        self.qtSuspendGroupBox.setObjectName(u"qtSuspendGroupBox")
        self.verticalLayout_15 = QVBoxLayout(self.qtSuspendGroupBox)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.qtMorningSuspendGroupBox = QGroupBox(self.qtSuspendGroupBox)
        self.qtMorningSuspendGroupBox.setObjectName(u"qtMorningSuspendGroupBox")
        self.verticalLayout_19 = QVBoxLayout(self.qtMorningSuspendGroupBox)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.qtMorningSuspendOneDayOffRadioButton = QRadioButton(self.qtMorningSuspendGroupBox)
        self.qtMorningSuspendOneDayOffRadioButton.setObjectName(u"qtMorningSuspendOneDayOffRadioButton")
        self.qtMorningSuspendOneDayOffRadioButton.setChecked(True)

        self.verticalLayout_19.addWidget(self.qtMorningSuspendOneDayOffRadioButton)

        self.qtMorningSuspendHalfDayOffRadioButton = QRadioButton(self.qtMorningSuspendGroupBox)
        self.qtMorningSuspendHalfDayOffRadioButton.setObjectName(u"qtMorningSuspendHalfDayOffRadioButton")

        self.verticalLayout_19.addWidget(self.qtMorningSuspendHalfDayOffRadioButton)

        self.qtMorningSuspendNoDayOffRadioButton = QRadioButton(self.qtMorningSuspendGroupBox)
        self.qtMorningSuspendNoDayOffRadioButton.setObjectName(u"qtMorningSuspendNoDayOffRadioButton")

        self.verticalLayout_19.addWidget(self.qtMorningSuspendNoDayOffRadioButton)


        self.verticalLayout_15.addWidget(self.qtMorningSuspendGroupBox)

        self.qtAfternoonSuspendGroupBox = QGroupBox(self.qtSuspendGroupBox)
        self.qtAfternoonSuspendGroupBox.setObjectName(u"qtAfternoonSuspendGroupBox")
        self.verticalLayout_23 = QVBoxLayout(self.qtAfternoonSuspendGroupBox)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.qtAfternoonSuspendOneDayOffRadioButton = QRadioButton(self.qtAfternoonSuspendGroupBox)
        self.qtAfternoonSuspendOneDayOffRadioButton.setObjectName(u"qtAfternoonSuspendOneDayOffRadioButton")
        self.qtAfternoonSuspendOneDayOffRadioButton.setChecked(True)

        self.verticalLayout_23.addWidget(self.qtAfternoonSuspendOneDayOffRadioButton)

        self.qtAfternoonSuspendHalfDayOffRadioButton = QRadioButton(self.qtAfternoonSuspendGroupBox)
        self.qtAfternoonSuspendHalfDayOffRadioButton.setObjectName(u"qtAfternoonSuspendHalfDayOffRadioButton")

        self.verticalLayout_23.addWidget(self.qtAfternoonSuspendHalfDayOffRadioButton)

        self.qtAfternoonSuspendNoDayOffRadioButton = QRadioButton(self.qtAfternoonSuspendGroupBox)
        self.qtAfternoonSuspendNoDayOffRadioButton.setObjectName(u"qtAfternoonSuspendNoDayOffRadioButton")

        self.verticalLayout_23.addWidget(self.qtAfternoonSuspendNoDayOffRadioButton)


        self.verticalLayout_15.addWidget(self.qtAfternoonSuspendGroupBox)


        self.horizontalLayout_2.addWidget(self.qtSuspendGroupBox)

        self.qtPowerOffGroupBox = QGroupBox(self.qtHumanConditionGroupBox)
        self.qtPowerOffGroupBox.setObjectName(u"qtPowerOffGroupBox")
        self.verticalLayout_12 = QVBoxLayout(self.qtPowerOffGroupBox)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.qtMorningPowerOffGroupBox = QGroupBox(self.qtPowerOffGroupBox)
        self.qtMorningPowerOffGroupBox.setObjectName(u"qtMorningPowerOffGroupBox")
        self.verticalLayout_17 = QVBoxLayout(self.qtMorningPowerOffGroupBox)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.qtMorningPowerOffOneDayOffRadioButton = QRadioButton(self.qtMorningPowerOffGroupBox)
        self.qtMorningPowerOffOneDayOffRadioButton.setObjectName(u"qtMorningPowerOffOneDayOffRadioButton")
        self.qtMorningPowerOffOneDayOffRadioButton.setChecked(True)

        self.verticalLayout_17.addWidget(self.qtMorningPowerOffOneDayOffRadioButton)

        self.qtMorningPowerOffHalfDayOffRadioButton = QRadioButton(self.qtMorningPowerOffGroupBox)
        self.qtMorningPowerOffHalfDayOffRadioButton.setObjectName(u"qtMorningPowerOffHalfDayOffRadioButton")

        self.verticalLayout_17.addWidget(self.qtMorningPowerOffHalfDayOffRadioButton)

        self.qtMorningPowerOffNoDayOffRadioButton = QRadioButton(self.qtMorningPowerOffGroupBox)
        self.qtMorningPowerOffNoDayOffRadioButton.setObjectName(u"qtMorningPowerOffNoDayOffRadioButton")

        self.verticalLayout_17.addWidget(self.qtMorningPowerOffNoDayOffRadioButton)


        self.verticalLayout_12.addWidget(self.qtMorningPowerOffGroupBox)

        self.qtAfternoonPowerOffGroupBox = QGroupBox(self.qtPowerOffGroupBox)
        self.qtAfternoonPowerOffGroupBox.setObjectName(u"qtAfternoonPowerOffGroupBox")
        self.verticalLayout_22 = QVBoxLayout(self.qtAfternoonPowerOffGroupBox)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.qtAfternoonPowerOffOneDayOffRadioButton = QRadioButton(self.qtAfternoonPowerOffGroupBox)
        self.qtAfternoonPowerOffOneDayOffRadioButton.setObjectName(u"qtAfternoonPowerOffOneDayOffRadioButton")

        self.verticalLayout_22.addWidget(self.qtAfternoonPowerOffOneDayOffRadioButton)

        self.qtAfternoonPowerOffHalfDayOffRadioButton = QRadioButton(self.qtAfternoonPowerOffGroupBox)
        self.qtAfternoonPowerOffHalfDayOffRadioButton.setObjectName(u"qtAfternoonPowerOffHalfDayOffRadioButton")
        self.qtAfternoonPowerOffHalfDayOffRadioButton.setChecked(True)

        self.verticalLayout_22.addWidget(self.qtAfternoonPowerOffHalfDayOffRadioButton)

        self.qtAfternoonPowerOffNoDayOffRadioButton = QRadioButton(self.qtAfternoonPowerOffGroupBox)
        self.qtAfternoonPowerOffNoDayOffRadioButton.setObjectName(u"qtAfternoonPowerOffNoDayOffRadioButton")

        self.verticalLayout_22.addWidget(self.qtAfternoonPowerOffNoDayOffRadioButton)


        self.verticalLayout_12.addWidget(self.qtAfternoonPowerOffGroupBox)


        self.horizontalLayout_2.addWidget(self.qtPowerOffGroupBox)

        self.qtHumanOtherGroupBox = QGroupBox(self.qtHumanConditionGroupBox)
        self.qtHumanOtherGroupBox.setObjectName(u"qtHumanOtherGroupBox")
        self.verticalLayout_14 = QVBoxLayout(self.qtHumanOtherGroupBox)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.qtMorningHumanOtherGroupBox = QGroupBox(self.qtHumanOtherGroupBox)
        self.qtMorningHumanOtherGroupBox.setObjectName(u"qtMorningHumanOtherGroupBox")
        self.verticalLayout_24 = QVBoxLayout(self.qtMorningHumanOtherGroupBox)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.qtMorningHumanOtherOneDayOffRadioButton = QRadioButton(self.qtMorningHumanOtherGroupBox)
        self.qtMorningHumanOtherOneDayOffRadioButton.setObjectName(u"qtMorningHumanOtherOneDayOffRadioButton")

        self.verticalLayout_24.addWidget(self.qtMorningHumanOtherOneDayOffRadioButton)

        self.qtMorningHumanOtherHalfDayOffRadioButton = QRadioButton(self.qtMorningHumanOtherGroupBox)
        self.qtMorningHumanOtherHalfDayOffRadioButton.setObjectName(u"qtMorningHumanOtherHalfDayOffRadioButton")

        self.verticalLayout_24.addWidget(self.qtMorningHumanOtherHalfDayOffRadioButton)

        self.qtMorningHumanOtherNoDayOffRadioButton = QRadioButton(self.qtMorningHumanOtherGroupBox)
        self.qtMorningHumanOtherNoDayOffRadioButton.setObjectName(u"qtMorningHumanOtherNoDayOffRadioButton")
        self.qtMorningHumanOtherNoDayOffRadioButton.setChecked(True)

        self.verticalLayout_24.addWidget(self.qtMorningHumanOtherNoDayOffRadioButton)


        self.verticalLayout_14.addWidget(self.qtMorningHumanOtherGroupBox)

        self.qtAfternoonHumanOtherGroupBox = QGroupBox(self.qtHumanOtherGroupBox)
        self.qtAfternoonHumanOtherGroupBox.setObjectName(u"qtAfternoonHumanOtherGroupBox")
        self.verticalLayout_25 = QVBoxLayout(self.qtAfternoonHumanOtherGroupBox)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.qtAfternoonHumanOtherOneDayOffRadioButton = QRadioButton(self.qtAfternoonHumanOtherGroupBox)
        self.qtAfternoonHumanOtherOneDayOffRadioButton.setObjectName(u"qtAfternoonHumanOtherOneDayOffRadioButton")

        self.verticalLayout_25.addWidget(self.qtAfternoonHumanOtherOneDayOffRadioButton)

        self.qtAfternoonHumanOtherHalfDayOffRadioButton = QRadioButton(self.qtAfternoonHumanOtherGroupBox)
        self.qtAfternoonHumanOtherHalfDayOffRadioButton.setObjectName(u"qtAfternoonHumanOtherHalfDayOffRadioButton")

        self.verticalLayout_25.addWidget(self.qtAfternoonHumanOtherHalfDayOffRadioButton)

        self.qtAfternoonHumanOtherNoDayOffRadioButton = QRadioButton(self.qtAfternoonHumanOtherGroupBox)
        self.qtAfternoonHumanOtherNoDayOffRadioButton.setObjectName(u"qtAfternoonHumanOtherNoDayOffRadioButton")
        self.qtAfternoonHumanOtherNoDayOffRadioButton.setChecked(True)

        self.verticalLayout_25.addWidget(self.qtAfternoonHumanOtherNoDayOffRadioButton)


        self.verticalLayout_14.addWidget(self.qtAfternoonHumanOtherGroupBox)


        self.horizontalLayout_2.addWidget(self.qtHumanOtherGroupBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.qtHumanConditionGroupBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.qtOkPushButton = QPushButton(Dialog)
        self.qtOkPushButton.setObjectName(u"qtOkPushButton")

        self.horizontalLayout_3.addWidget(self.qtOkPushButton)

        self.qtCancelPushButton = QPushButton(Dialog)
        self.qtCancelPushButton.setObjectName(u"qtCancelPushButton")

        self.horizontalLayout_3.addWidget(self.qtCancelPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.qtWeatherConditionGroupBox.setTitle(QCoreApplication.translate("Dialog", u"\u5929\u5019\u56e0\u7d20", None))
        self.qtRainGroupBox.setTitle("")
        self.qtMorningRainGroupBox.setTitle(QCoreApplication.translate("Dialog", u"\u4e0a\u5348\u4e0b\u96e8", None))
        self.qtMorningRainOneDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f1\u5929", None))
        self.qtMorningRainHalfDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f0.5\u5929", None))
        self.qtMorningRainNoDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u7167\u8a08\u5de5\u671f", None))
        self.qtAfternoonRainGroupBox.setTitle(QCoreApplication.translate("Dialog", u"\u4e0b\u5348\u4e0b\u96e8", None))
        self.qtAfternoonRainOneDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f1\u5929", None))
        self.qtAfternoonRainHalfDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f0.5\u5929", None))
        self.qtAfternoonRainNoDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u7167\u8a08\u5de5\u671f", None))
        self.qtHeavyRainGroupBox.setTitle("")
        self.qtMorningHeavyRainGroupBox.setTitle(QCoreApplication.translate("Dialog", u"\u4e0a\u5348\u8c6a\u96e8", None))
        self.qtMorningHeavyRainOneDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f1\u5929", None))
        self.qtMorningHeavyRainHalfDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f0.5\u5929", None))
        self.qtMorningHeavyRainNoDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u7167\u8a08\u5de5\u671f", None))
        self.qtAfternoonHeavyRainGroupBox.setTitle(QCoreApplication.translate("Dialog", u"\u4e0b\u5348\u8c6a\u96e8", None))
        self.qtAfternoonHeavyRainOneDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f1\u5929", None))
        self.qtAfternoonHeavyRainHalfDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f0.5\u5929", None))
        self.qtAfternoonHeavyRainNoDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u7167\u8a08\u5de5\u671f", None))
        self.qtTyphoonGroupBox.setTitle("")
        self.qtMorningTyphoonGroupBox.setTitle(QCoreApplication.translate("Dialog", u"\u4e0a\u5348\u98b1\u98a8", None))
        self.qtMorningTyphoonOneDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f1\u5929", None))
        self.qtMorningTyphoonHalfDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f0.5\u5929", None))
        self.qtMorningTyphoonNoDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u7167\u8a08\u5de5\u671f", None))
        self.qtAfternoonTyphoonGroupBox.setTitle(QCoreApplication.translate("Dialog", u"\u4e0b\u5348\u98b1\u98a8", None))
        self.qtAfternoonTyphoonOneDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f1\u5929", None))
        self.qtAfternoonTyphoonHalfDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f0.5\u5929", None))
        self.qtAfternoonTyphoonNoDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u7167\u8a08\u5de5\u671f", None))
        self.qtHotGroupBox.setTitle("")
        self.qtMorningHotGroupBox.setTitle(QCoreApplication.translate("Dialog", u"\u4e0a\u5348\u9177\u71b1", None))
        self.qtMorningHotOneDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f1\u5929", None))
        self.qtMorningHotHalfDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f0.5\u5929", None))
        self.qtMorningHotNoDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u7167\u8a08\u5de5\u671f", None))
        self.qtAfternoonHotGroupBox.setTitle(QCoreApplication.translate("Dialog", u"\u4e0b\u5348\u9177\u71b1", None))
        self.qtAfternoonHotOneDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f1\u5929", None))
        self.qtAfternoonHotHalfDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f0.5\u5929", None))
        self.qtAfternoonHotNoDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u7167\u8a08\u5de5\u671f", None))
        self.qtMuddyGroupBox.setTitle("")
        self.qtMorningMuddyGroupBox.setTitle(QCoreApplication.translate("Dialog", u"\u4e0a\u5348\u6ce5\u6fd8", None))
        self.qtMorningMuddyOneDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f1\u5929", None))
        self.qtMorningMuddyHalfDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f0.5\u5929", None))
        self.qtMorningMuddyNoDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u7167\u8a08\u5de5\u671f", None))
        self.qtAfternoonMuddyGroupBox.setTitle(QCoreApplication.translate("Dialog", u"\u4e0b\u5348\u6ce5\u6fd8", None))
        self.qtAfternoonMuddyOneDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f1\u5929", None))
        self.qtAfternoonMuddyHalfDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f0.5\u5929", None))
        self.qtAfternoonMuddyNoDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u7167\u8a08\u5de5\u671f", None))
        self.qtWeatherOtherGroupBox.setTitle("")
        self.qtMorningWeatherOtherGroupBox.setTitle(QCoreApplication.translate("Dialog", u"\u4e0a\u5348\u5176\u4ed6", None))
        self.qtMorningWeatherOtherOneDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f1\u5929", None))
        self.qtMorningWeatherOtherHalfDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f0.5\u5929", None))
        self.qtMorningWeatherOtherNoDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u7167\u8a08\u5de5\u671f", None))
        self.qtAfternoonWeatherOtherGroupBox.setTitle(QCoreApplication.translate("Dialog", u"\u4e0b\u5348\u5176\u4ed6", None))
        self.qtAfternoonWeatherOtherOneDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f1\u5929", None))
        self.qtAfternoonWeatherOtherHalfDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f0.5\u5929", None))
        self.qtAfternoonWeatherOtherNoDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u7167\u8a08\u5de5\u671f", None))
        self.qtHumanConditionGroupBox.setTitle(QCoreApplication.translate("Dialog", u"\u4eba\u70ba\u56e0\u7d20", None))
        self.qtSuspendGroupBox.setTitle("")
        self.qtMorningSuspendGroupBox.setTitle(QCoreApplication.translate("Dialog", u"\u4e0a\u5348\u505c\u5de5", None))
        self.qtMorningSuspendOneDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f1\u5929", None))
        self.qtMorningSuspendHalfDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f0.5\u5929", None))
        self.qtMorningSuspendNoDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u7167\u8a08\u5de5\u671f", None))
        self.qtAfternoonSuspendGroupBox.setTitle(QCoreApplication.translate("Dialog", u"\u4e0b\u5348\u505c\u5de5", None))
        self.qtAfternoonSuspendOneDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f1\u5929", None))
        self.qtAfternoonSuspendHalfDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f0.5\u5929", None))
        self.qtAfternoonSuspendNoDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u7167\u8a08\u5de5\u671f", None))
        self.qtPowerOffGroupBox.setTitle("")
        self.qtMorningPowerOffGroupBox.setTitle(QCoreApplication.translate("Dialog", u"\u4e0a\u5348\u505c\u96fb", None))
        self.qtMorningPowerOffOneDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f1\u5929", None))
        self.qtMorningPowerOffHalfDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f0.5\u5929", None))
        self.qtMorningPowerOffNoDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u7167\u8a08\u5de5\u671f", None))
        self.qtAfternoonPowerOffGroupBox.setTitle(QCoreApplication.translate("Dialog", u"\u4e0b\u5348\u505c\u96fb", None))
        self.qtAfternoonPowerOffOneDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f1\u5929", None))
        self.qtAfternoonPowerOffHalfDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f0.5\u5929", None))
        self.qtAfternoonPowerOffNoDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u7167\u8a08\u5de5\u671f", None))
        self.qtHumanOtherGroupBox.setTitle("")
        self.qtMorningHumanOtherGroupBox.setTitle(QCoreApplication.translate("Dialog", u"\u4e0a\u5348\u5176\u4ed6", None))
        self.qtMorningHumanOtherOneDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f1\u5929", None))
        self.qtMorningHumanOtherHalfDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f0.5\u5929", None))
        self.qtMorningHumanOtherNoDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u7167\u8a08\u5de5\u671f", None))
        self.qtAfternoonHumanOtherGroupBox.setTitle(QCoreApplication.translate("Dialog", u"\u4e0b\u5348\u5176\u4ed6", None))
        self.qtAfternoonHumanOtherOneDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f1\u5929", None))
        self.qtAfternoonHumanOtherHalfDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8a08\u5de5\u671f0.5\u5929", None))
        self.qtAfternoonHumanOtherNoDayOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u7167\u8a08\u5de5\u671f", None))
        self.qtOkPushButton.setText(QCoreApplication.translate("Dialog", u"\u78ba\u8a8d", None))
        self.qtCancelPushButton.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

