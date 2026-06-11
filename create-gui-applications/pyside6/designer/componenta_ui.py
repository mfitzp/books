# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'componenta.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QLineEdit, QSizePolicy,
    QSlider, QSpinBox, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_ComponentA(object):
    def setupUi(self, ComponentA):
        if not ComponentA.objectName():
            ComponentA.setObjectName(u"ComponentA")
        ComponentA.resize(388, 333)
        self.verticalLayout = QVBoxLayout(ComponentA)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(ComponentA)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.spinBox = QSpinBox(ComponentA)
        self.spinBox.setObjectName(u"spinBox")

        self.verticalLayout.addWidget(self.spinBox)

        self.textEdit = QTextEdit(ComponentA)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.doubleSpinBox = QDoubleSpinBox(ComponentA)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.verticalLayout.addWidget(self.doubleSpinBox)

        self.horizontalSlider = QSlider(ComponentA)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider)


        self.retranslateUi(ComponentA)

        QMetaObject.connectSlotsByName(ComponentA)
    # setupUi

    def retranslateUi(self, ComponentA):
        ComponentA.setWindowTitle(QCoreApplication.translate("ComponentA", u"Form", None))
    # retranslateUi

