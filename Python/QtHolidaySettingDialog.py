# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtHolidaySettingDialog.ui'
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
    QRadioButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 653)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.qtImportFromMainDBPushButton = QPushButton(Dialog)
        self.qtImportFromMainDBPushButton.setObjectName(u"qtImportFromMainDBPushButton")

        self.verticalLayout.addWidget(self.qtImportFromMainDBPushButton)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.qtDateEdit = QDateEdit(Dialog)
        self.qtDateEdit.setObjectName(u"qtDateEdit")

        self.horizontalLayout.addWidget(self.qtDateEdit)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.qtReasonLineEdit = QLineEdit(Dialog)
        self.qtReasonLineEdit.setObjectName(u"qtReasonLineEdit")

        self.horizontalLayout.addWidget(self.qtReasonLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.qtHolidayRadioButton = QRadioButton(Dialog)
        self.qtHolidayRadioButton.setObjectName(u"qtHolidayRadioButton")
        self.qtHolidayRadioButton.setChecked(True)

        self.horizontalLayout_2.addWidget(self.qtHolidayRadioButton)

        self.qtWorkdayRadioButton = QRadioButton(Dialog)
        self.qtWorkdayRadioButton.setObjectName(u"qtWorkdayRadioButton")

        self.horizontalLayout_2.addWidget(self.qtWorkdayRadioButton)

        self.qtAddPushButton = QPushButton(Dialog)
        self.qtAddPushButton.setObjectName(u"qtAddPushButton")

        self.horizontalLayout_2.addWidget(self.qtAddPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.qtTableView = QTableView(Dialog)
        self.qtTableView.setObjectName(u"qtTableView")

        self.horizontalLayout_3.addWidget(self.qtTableView)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.qtExportFilePushButton = QPushButton(Dialog)
        self.qtExportFilePushButton.setObjectName(u"qtExportFilePushButton")

        self.horizontalLayout_4.addWidget(self.qtExportFilePushButton)

        self.qtImportFilePushButton = QPushButton(Dialog)
        self.qtImportFilePushButton.setObjectName(u"qtImportFilePushButton")

        self.horizontalLayout_4.addWidget(self.qtImportFilePushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

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
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u4e3b\u8cc7\u6599\u5eab\u5047\u65e5\u8a2d\u5b9a", None))
        self.qtImportFromMainDBPushButton.setText(QCoreApplication.translate("Dialog", u"\u5f9e\u4e3b\u8cc7\u6599\u5eab\u8f09\u5165", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u7406\u7531", None))
        self.qtHolidayRadioButton.setText(QCoreApplication.translate("Dialog", u"\u653e\u5047", None))
        self.qtWorkdayRadioButton.setText(QCoreApplication.translate("Dialog", u"\u88dc\u73ed", None))
        self.qtAddPushButton.setText(QCoreApplication.translate("Dialog", u"\u65b0\u589e", None))
        self.qtExportFilePushButton.setText(QCoreApplication.translate("Dialog", u"\u532f\u51fa", None))
        self.qtImportFilePushButton.setText(QCoreApplication.translate("Dialog", u"\u532f\u5165", None))
        self.qtExitPushButton.setText(QCoreApplication.translate("Dialog", u"\u96e2\u958b", None))
    # retranslateUi

