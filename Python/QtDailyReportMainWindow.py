# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtDailyReportMainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.qtSignInAction = QAction(MainWindow)
        self.qtSignInAction.setObjectName(u"qtSignInAction")
        self.qtSignOutAction = QAction(MainWindow)
        self.qtSignOutAction.setObjectName(u"qtSignOutAction")
        self.qtMainHolidayDBSettingAction = QAction(MainWindow)
        self.qtMainHolidayDBSettingAction.setObjectName(u"qtMainHolidayDBSettingAction")
        self.qtCreateNewProjectAction = QAction(MainWindow)
        self.qtCreateNewProjectAction.setObjectName(u"qtCreateNewProjectAction")
        self.qtCheckDailyReportAction = QAction(MainWindow)
        self.qtCheckDailyReportAction.setObjectName(u"qtCheckDailyReportAction")
        self.qtExpectFinishFormAction = QAction(MainWindow)
        self.qtExpectFinishFormAction.setObjectName(u"qtExpectFinishFormAction")
        self.qtWeatherFormAction = QAction(MainWindow)
        self.qtWeatherFormAction.setObjectName(u"qtWeatherFormAction")
        self.actiond_3 = QAction(MainWindow)
        self.actiond_3.setObjectName(u"actiond_3")
        self.actiona_2 = QAction(MainWindow)
        self.actiona_2.setObjectName(u"actiona_2")
        self.actiona_3 = QAction(MainWindow)
        self.actiona_3.setObjectName(u"actiona_3")
        self.actiona_4 = QAction(MainWindow)
        self.actiona_4.setObjectName(u"actiona_4")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.qtSearchLineEdit = QLineEdit(self.centralwidget)
        self.qtSearchLineEdit.setObjectName(u"qtSearchLineEdit")

        self.horizontalLayout_2.addWidget(self.qtSearchLineEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.qtProjectListTableView = QTableView(self.centralwidget)
        self.qtProjectListTableView.setObjectName(u"qtProjectListTableView")

        self.verticalLayout.addWidget(self.qtProjectListTableView)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.qtDailyReportListTableView = QTableView(self.centralwidget)
        self.qtDailyReportListTableView.setObjectName(u"qtDailyReportListTableView")

        self.verticalLayout.addWidget(self.qtDailyReportListTableView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.qtAddDailyReportPushButton = QPushButton(self.centralwidget)
        self.qtAddDailyReportPushButton.setObjectName(u"qtAddDailyReportPushButton")

        self.horizontalLayout.addWidget(self.qtAddDailyReportPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_4.addWidget(self.pushButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_5 = QMenu(self.menubar)
        self.menu_5.setObjectName(u"menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menu.addAction(self.qtSignInAction)
        self.menu.addAction(self.qtSignOutAction)
        self.menu_2.addAction(self.qtMainHolidayDBSettingAction)
        self.menu_2.addAction(self.qtCreateNewProjectAction)
        self.menu_4.addAction(self.qtCheckDailyReportAction)
        self.menu_4.addSeparator()
        self.menu_4.addAction(self.qtExpectFinishFormAction)
        self.menu_4.addAction(self.qtWeatherFormAction)
        self.menu_4.addAction(self.actiond_3)
        self.menu_4.addAction(self.actiona_2)
        self.menu_4.addAction(self.actiona_3)
        self.menu_4.addAction(self.actiona_4)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5de5\u7a0b\u65e5\u5831\u8868", None))
        self.qtSignInAction.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5165", None))
        self.qtSignOutAction.setText(QCoreApplication.translate("MainWindow", u"\u767b\u51fa", None))
        self.qtMainHolidayDBSettingAction.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u8cc7\u6599\u5eab\u5047\u65e5\u8a2d\u5b9a", None))
        self.qtCreateNewProjectAction.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u5de5\u7a0b\u8cc7\u6599", None))
        self.qtCheckDailyReportAction.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5831\u8868\u6aa2\u67e5\u4f5c\u696d", None))
        self.qtExpectFinishFormAction.setText(QCoreApplication.translate("MainWindow", u"\u9810\u8a08\u5b8c\u5de5\u8868", None))
        self.qtWeatherFormAction.setText(QCoreApplication.translate("MainWindow", u"\u6674\u96e8\u8868", None))
        self.actiond_3.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5831\u660e\u7d30\u8868", None))
        self.actiona_2.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u8a08\u5de5\u671f\u5716\u8868", None))
        self.actiona_3.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u8a08\u5de5\u671f\u660e\u7d30\u8868", None))
        self.actiona_4.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u8a08\u5de5\u671f\u7d71\u8a08\u8868", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.qtAddDailyReportPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u65e5\u5831\u8868", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u9810\u8a08\u5b8c\u5de5\u8868", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u6674\u96e8\u8868", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u767b\u5165/\u767b\u51fa", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8cc7\u6599\u7dad\u8b77", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u65e5\u5831\u8868\u4f5c\u696d", None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow", u"\u7cfb\u7d71\u7ba1\u7406", None))
    # retranslateUi

