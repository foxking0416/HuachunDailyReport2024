# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtCreateProjectPage1Dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(267, 259)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label)

        self.qtProjectNumberLineEdit = QLineEdit(Dialog)
        self.qtProjectNumberLineEdit.setObjectName(u"qtProjectNumberLineEdit")

        self.horizontalLayout_6.addWidget(self.qtProjectNumberLineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(50, 30, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.qtProjectNumberWarningLabel = QLabel(Dialog)
        self.qtProjectNumberWarningLabel.setObjectName(u"qtProjectNumberWarningLabel")
        self.qtProjectNumberWarningLabel.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout_5.addWidget(self.qtProjectNumberWarningLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_7.addWidget(self.label_2)

        self.qtProjectNameLineEdit = QLineEdit(Dialog)
        self.qtProjectNameLineEdit.setObjectName(u"qtProjectNameLineEdit")

        self.horizontalLayout_7.addWidget(self.qtProjectNameLineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_2 = QSpacerItem(50, 30, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.qtProjectNameWarningLabel = QLabel(Dialog)
        self.qtProjectNameWarningLabel.setObjectName(u"qtProjectNameWarningLabel")
        self.qtProjectNameWarningLabel.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout_8.addWidget(self.qtProjectNameWarningLabel)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_9.addWidget(self.label_3)

        self.qtContractNumberLineEdit = QLineEdit(Dialog)
        self.qtContractNumberLineEdit.setObjectName(u"qtContractNumberLineEdit")

        self.horizontalLayout_9.addWidget(self.qtContractNumberLineEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_3 = QSpacerItem(70, 30, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)

        self.qtContractNumberWarningLabel = QLabel(Dialog)
        self.qtContractNumberWarningLabel.setObjectName(u"qtContractNumberWarningLabel")
        self.qtContractNumberWarningLabel.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout_10.addWidget(self.qtContractNumberWarningLabel)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.qtNextStepPushButton = QPushButton(Dialog)
        self.qtNextStepPushButton.setObjectName(u"qtNextStepPushButton")

        self.horizontalLayout_4.addWidget(self.qtNextStepPushButton)

        self.qtCancelPushButton = QPushButton(Dialog)
        self.qtCancelPushButton.setObjectName(u"qtCancelPushButton")

        self.horizontalLayout_4.addWidget(self.qtCancelPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u65b0\u589e\u5de5\u7a0b\u8cc7\u6599", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u5de5\u7a0b\u7de8\u865f", None))
        self.qtProjectNumberWarningLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u5de5\u7a0b\u540d\u7a31", None))
        self.qtProjectNameWarningLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u6848\u865f\u53ca\u5951\u7d04\u865f", None))
        self.qtContractNumberWarningLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.qtNextStepPushButton.setText(QCoreApplication.translate("Dialog", u"\u4e0b\u4e00\u6b65", None))
        self.qtCancelPushButton.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

