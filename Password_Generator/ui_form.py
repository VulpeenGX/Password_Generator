# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(380, 439)
        Widget.setMinimumSize(QSize(0, 0))
        Widget.setMaximumSize(QSize(1000, 1001))
        Widget.setStyleSheet(u".QLabel{\n"
"	font-family: \"Roboto\";\n"
"}")
        self.gridLayout_2 = QGridLayout(Widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.label, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_5, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.contrasena = QLabel(self.frame_9)
        self.contrasena.setObjectName(u"contrasena")
        self.contrasena.setStyleSheet(u"QLabel {\n"
"    font-size: 10pt;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLabel span.letters {\n"
"    color: black;  /* Letras en negro */\n"
"}\n"
"\n"
"QLabel span.digits {\n"
"    color: red;  /* D\u00edgitos en rojo */\n"
"}\n"
"\n"
"QLabel span.special {\n"
"    color: blue;  /* Caracteres especiales en azul */\n"
"}\n"
"")
        self.contrasena.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_6.addWidget(self.contrasena)

        self.horizontalSpacer_6 = QSpacerItem(136, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.copiar = QPushButton(self.frame_9)
        self.copiar.setObjectName(u"copiar")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditPaste))
        self.copiar.setIcon(icon)

        self.horizontalLayout_6.addWidget(self.copiar)


        self.gridLayout_3.addWidget(self.frame_9, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.letras_checkbox = QCheckBox(self.frame_3)
        self.letras_checkbox.setObjectName(u"letras_checkbox")
        self.letras_checkbox.setAutoFillBackground(True)
        self.letras_checkbox.setStyleSheet(u"font-family: \"Roboto\";\n"
"/* Estilo para CheckBox */\n"
"")
        self.letras_checkbox.setCheckable(True)
        self.letras_checkbox.setChecked(True)
        self.letras_checkbox.setTristate(False)

        self.horizontalLayout_3.addWidget(self.letras_checkbox)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.numeros_checkbox = QCheckBox(self.frame_4)
        self.numeros_checkbox.setObjectName(u"numeros_checkbox")
        self.numeros_checkbox.setStyleSheet(u"font-family: \"Roboto\";")

        self.horizontalLayout_4.addWidget(self.numeros_checkbox)


        self.gridLayout_4.addWidget(self.frame_4, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.caracteres_checkbox = QCheckBox(self.frame_5)
        self.caracteres_checkbox.setObjectName(u"caracteres_checkbox")
        self.caracteres_checkbox.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.caracteres_checkbox)


        self.gridLayout_5.addWidget(self.frame_5, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_5)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.slider = QSlider(self.frame_7)
        self.slider.setObjectName(u"slider")
        self.slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #ccc;\n"
"    background: #ecf0f1; /* Fondo de la l\u00ednea */\n"
"    height: 2px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #3498db; /* Color azul claro */\n"
"    border: 2px solid #2980b9; /* Borde azul oscuro */\n"
"    width: 20px; /* Tama\u00f1o del bot\u00f3n circular */\n"
"    height: 20px;\n"
"    margin: -6px 0; /* Posici\u00f3n del bot\u00f3n circular */\n"
"    border-radius: 10px; /* Hace el bot\u00f3n completamente circular */\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #85c1e9; /* Parte activa del slider (a la izquierda del bot\u00f3n) */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #d5dbdb; /* Parte inactiva del slider (a la derecha del bot\u00f3n) */\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout.addWidget(self.slider)

        self.sliderL = QLabel(self.frame_7)
        self.sliderL.setObjectName(u"sliderL")

        self.horizontalLayout.addWidget(self.sliderL)


        self.verticalLayout_2.addWidget(self.frame_7)


        self.gridLayout_6.addWidget(self.frame_6, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_6)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_8)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.generarB = QPushButton(self.frame_8)
        self.generarB.setObjectName(u"generarB")
        self.generarB.setStyleSheet(u"font-family: \"Roboto\"")

        self.gridLayout_16.addWidget(self.generarB, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_8, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_8)


        self.gridLayout_2.addWidget(self.frame, 0, 1, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Generador de contrase\u00f1as", None))
        self.contrasena.setText(QCoreApplication.translate("Widget", u"Contrase\u00f1a generada", None))
        self.copiar.setText("")
        self.label_2.setText(QCoreApplication.translate("Widget", u"Letras (p. ej., Aa)", None))
        self.letras_checkbox.setText("")
        self.label_3.setText(QCoreApplication.translate("Widget", u"N\u00fameros (por ejemplo, 2,3,4)", None))
        self.numeros_checkbox.setText("")
        self.label_4.setText(QCoreApplication.translate("Widget", u"Caracteres especiales (por ejemplo, !@$)", None))
        self.caracteres_checkbox.setText("")
        self.label_5.setText(QCoreApplication.translate("Widget", u"Longitud de la contrase\u00f1a", None))
        self.sliderL.setText(QCoreApplication.translate("Widget", u"N", None))
        self.generarB.setText(QCoreApplication.translate("Widget", u"Generar Contrase\u00f1a", None))
    # retranslateUi

