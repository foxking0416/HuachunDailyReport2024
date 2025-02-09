# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtSelectEditProjectDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(335, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.qtSearchNumberRadioButton = QRadioButton(Dialog)
        self.qtSearchNumberRadioButton.setObjectName(u"qtSearchNumberRadioButton")

        self.verticalLayout_2.addWidget(self.qtSearchNumberRadioButton)

        self.qtSearchNameRadioButton = QRadioButton(Dialog)
        self.qtSearchNameRadioButton.setObjectName(u"qtSearchNameRadioButton")

        self.verticalLayout_2.addWidget(self.qtSearchNameRadioButton)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.qtSearchLineEdit = QLineEdit(Dialog)
        self.qtSearchLineEdit.setObjectName(u"qtSearchLineEdit")

        self.horizontalLayout.addWidget(self.qtSearchLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.qtTableView = QTableView(Dialog)
        self.qtTableView.setObjectName(u"qtTableView")

        self.verticalLayout.addWidget(self.qtTableView)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.qtEditPushButton = QPushButton(Dialog)
        self.qtEditPushButton.setObjectName(u"qtEditPushButton")

        self.horizontalLayout_2.addWidget(self.qtEditPushButton)

        self.qtDeletePushButton = QPushButton(Dialog)
        self.qtDeletePushButton.setObjectName(u"qtDeletePushButton")

        self.horizontalLayout_2.addWidget(self.qtDeletePushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.qtExitPushButton = QPushButton(Dialog)
        self.qtExitPushButton.setObjectName(u"qtExitPushButton")

        self.verticalLayout.addWidget(self.qtExitPushButton)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u7de8\u8f2f\u65e2\u6709\u5de5\u7a0b", None))
        self.qtSearchNumberRadioButton.setText(QCoreApplication.translate("Dialog", u"\u641c\u5c0b\u5de5\u7a0b\u7de8\u865f", None))
        self.qtSearchNameRadioButton.setText(QCoreApplication.translate("Dialog", u"\u641c\u5c0b\u5de5\u7a0b\u540d\u7a31", None))
        self.qtEditPushButton.setText(QCoreApplication.translate("Dialog", u"\u7de8\u8f2f", None))
        self.qtDeletePushButton.setText(QCoreApplication.translate("Dialog", u"\u522a\u9664", None))
        self.qtExitPushButton.setText(QCoreApplication.translate("Dialog", u"\u96e2\u958b", None))
    # retranslateUi

