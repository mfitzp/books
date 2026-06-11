# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'componentb.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDial, QSizePolicy,
    QSpinBox, QTimeEdit, QVBoxLayout, QWidget)

class Ui_ComponentB(object):
    def setupUi(self, ComponentB):
        if not ComponentB.objectName():
            ComponentB.setObjectName(u"ComponentB")
        ComponentB.resize(168, 300)
        self.verticalLayout = QVBoxLayout(ComponentB)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.spinBox = QSpinBox(ComponentB)
        self.spinBox.setObjectName(u"spinBox")

        self.verticalLayout.addWidget(self.spinBox)

        self.timeEdit = QTimeEdit(ComponentB)
        self.timeEdit.setObjectName(u"timeEdit")

        self.verticalLayout.addWidget(self.timeEdit)

        self.dateEdit = QDateEdit(ComponentB)
        self.dateEdit.setObjectName(u"dateEdit")

        self.verticalLayout.addWidget(self.dateEdit)

        self.dial = QDial(ComponentB)
        self.dial.setObjectName(u"dial")

        self.verticalLayout.addWidget(self.dial)


        self.retranslateUi(ComponentB)

        QMetaObject.connectSlotsByName(ComponentB)
    # setupUi

    def retranslateUi(self, ComponentB):
        ComponentB.setWindowTitle(QCoreApplication.translate("ComponentB", u"Form", None))
    # retranslateUi

