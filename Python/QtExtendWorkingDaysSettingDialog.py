# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtExtendWorkingDaysSettingDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QTableView, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(450, 414)
        Dialog.setMinimumSize(QSize(450, 0))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.qtDateEdit = QDateEdit(Dialog)
        self.qtDateEdit.setObjectName(u"qtDateEdit")

        self.horizontalLayout.addWidget(self.qtDateEdit)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.qtExtensionDaysSpinBox = QSpinBox(Dialog)
        self.qtExtensionDaysSpinBox.setObjectName(u"qtExtensionDaysSpinBox")
        self.qtExtensionDaysSpinBox.setMaximum(9999)

        self.horizontalLayout.addWidget(self.qtExtensionDaysSpinBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.qtReasonLineEdit = QLineEdit(Dialog)
        self.qtReasonLineEdit.setObjectName(u"qtReasonLineEdit")
        self.qtReasonLineEdit.setMinimumSize(QSize(125, 0))

        self.horizontalLayout_2.addWidget(self.qtReasonLineEdit)

        self.qtAddPushButton = QPushButton(Dialog)
        self.qtAddPushButton.setObjectName(u"qtAddPushButton")
        self.qtAddPushButton.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_2.addWidget(self.qtAddPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.qtTableView = QTableView(Dialog)
        self.qtTableView.setObjectName(u"qtTableView")

        self.horizontalLayout_3.addWidget(self.qtTableView)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.qtExitPushButton = QPushButton(Dialog)
        self.qtExitPushButton.setObjectName(u"qtExitPushButton")

        self.horizontalLayout_5.addWidget(self.qtExitPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u8ffd\u52a0\u5de5\u671f\u8a2d\u5b9a", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u8ffd\u52a0\u8d77\u59cb\u65e5", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u8ffd\u52a0\u5de5\u671f", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u7406\u7531", None))
        self.qtAddPushButton.setText(QCoreApplication.translate("Dialog", u"\u65b0\u589e", None))
        self.qtExitPushButton.setText(QCoreApplication.translate("Dialog", u"\u96e2\u958b", None))
    # retranslateUi

