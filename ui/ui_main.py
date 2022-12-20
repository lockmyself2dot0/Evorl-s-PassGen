# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpinBox, QVBoxLayout,
    QWidget)
# import rsc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 420)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u":/icons/pngegg.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon1)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: white;\n"
"    color: black;\n"
"    font-family: Verdana;\n"
"    font-size: 16pt;\n"
"    margin: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#btn_lower, #btn_upper, #btn_special,#btn_digits  {\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-color: lightseagreen;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 4px solid lightseagreen;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border-color: lightseagreen;\n"
"    background-color: rgb(21, 110, 106);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"    background-color: white;\n"
"    color: black;\n"
"    font-family: Verdana;\n"
"    font-size: 16pt;\n"
"    margin: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#btn_lower, #btn_upper, #btn_special,#btn_digits  {\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-color: lightseagreen;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 4px solid lightseagreen;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border-color: lightseagreen;\n"
"    background-color: rgb(21, 110, 106);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.icon = QPushButton(self.centralwidget)
        self.icon.setObjectName(u"icon")
        self.icon.setEnabled(True)
        self.icon.setStyleSheet(u"border: none;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/pngeggg.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.icon.setIcon(icon2)
        self.icon.setIconSize(QSize(200, 100))

        self.verticalLayout.addWidget(self.icon)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_pass = QFrame(self.centralwidget)
        self.frame_pass.setObjectName(u"frame_pass")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_pass.sizePolicy().hasHeightForWidth())
        self.frame_pass.setSizePolicy(sizePolicy1)
        self.frame_pass.setStyleSheet(u"QPushButton:checked {\n"
"    border-color: lightseagreen;\n"
"    background-color: rgb(21, 110, 106);\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    border: 2px solid lightseagreen;\n"
"    border-radius: 5px;\n"
"    margin-right: 0;\n"
"}\n"
"QFrame {\n"
"    border: 2px solid gray;\n"
"	border-radius: 5px;\n"
"	margin-right: 0;\n"
"}")
        self.frame_pass.setFrameShape(QFrame.StyledPanel)
        self.frame_pass.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_pass)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.line_pass = QLineEdit(self.frame_pass)
        self.line_pass.setObjectName(u"line_pass")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line_pass.sizePolicy().hasHeightForWidth())
        self.line_pass.setSizePolicy(sizePolicy2)
        self.line_pass.setStyleSheet(u"QLineEdit {\n"
"    border: none;\n"
"    margin: 0;\n"
"    font-size: 20pt;\n"
"}")

        self.horizontalLayout_6.addWidget(self.line_pass)

        self.btn_visi = QPushButton(self.frame_pass)
        self.btn_visi.setObjectName(u"btn_visi")
        self.btn_visi.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_visi.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    margin: 0;\n"
"    background-color: transparent;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/visibility_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icons/visibility_off_black_24dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_visi.setIcon(icon3)
        self.btn_visi.setIconSize(QSize(30, 30))
        self.btn_visi.setCheckable(True)
        self.btn_visi.setChecked(True)

        self.horizontalLayout_6.addWidget(self.btn_visi)


        self.horizontalLayout.addWidget(self.frame_pass)

        self.btn_refresh = QPushButton(self.centralwidget)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_refresh.setStyleSheet(u"QPushButton {\n"
"    margin-left: 0;\n"
"    margin-right: 0;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/refresh_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refresh.setIcon(icon4)
        self.btn_refresh.setIconSize(QSize(50, 52))

        self.horizontalLayout.addWidget(self.btn_refresh)

        self.btn_copy = QPushButton(self.centralwidget)
        self.btn_copy.setObjectName(u"btn_copy")
        self.btn_copy.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_copy.setStyleSheet(u"QPushButton {\n"
"    margin-left: 0;\n"
"    margin-right: 10;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/content_copy_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/icons/content_copy_white_24dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_copy.setIcon(icon5)
        self.btn_copy.setIconSize(QSize(50, 52))

        self.horizontalLayout.addWidget(self.btn_copy)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.text_strengt = QLabel(self.centralwidget)
        self.text_strengt.setObjectName(u"text_strengt")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.text_strengt.sizePolicy().hasHeightForWidth())
        self.text_strengt.setSizePolicy(sizePolicy3)
        self.text_strengt.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.text_strengt)

        self.text_entropy = QLabel(self.centralwidget)
        self.text_entropy.setObjectName(u"text_entropy")
        sizePolicy3.setHeightForWidth(self.text_entropy.sizePolicy().hasHeightForWidth())
        self.text_entropy.setSizePolicy(sizePolicy3)
        self.text_entropy.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.text_entropy)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.layout_lenght = QHBoxLayout()
        self.layout_lenght.setObjectName(u"layout_lenght")
        self.slider_lenght = QSlider(self.centralwidget)
        self.slider_lenght.setObjectName(u"slider_lenght")
        self.slider_lenght.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    background-color: transparent;\n"
"    height: 5px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color:  rgb(21, 110, 106);\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background-color:  gray;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color:  black;\n"
"    width: 10px;\n"
"    border-radius: 3px;\n"
"    margin-top: -10px;\n"
"    margin-bottom: -10px;\n"
"}")
        self.slider_lenght.setMinimum(0)
        self.slider_lenght.setMaximum(100)
        self.slider_lenght.setValue(12)
        self.slider_lenght.setOrientation(Qt.Horizontal)

        self.layout_lenght.addWidget(self.slider_lenght)

        self.spinbox_lenght = QSpinBox(self.centralwidget)
        self.spinbox_lenght.setObjectName(u"spinbox_lenght")
        self.spinbox_lenght.setStyleSheet(u"QSpinBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    background: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border-color: lightseagreen;\n"
"}")
        self.spinbox_lenght.setAlignment(Qt.AlignCenter)
        self.spinbox_lenght.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinbox_lenght.setMaximum(100)
        self.spinbox_lenght.setValue(12)

        self.layout_lenght.addWidget(self.spinbox_lenght)


        self.verticalLayout.addLayout(self.layout_lenght)

        self.layout_char = QHBoxLayout()
        self.layout_char.setObjectName(u"layout_char")
        self.btn_lower = QPushButton(self.centralwidget)
        self.btn_lower.setObjectName(u"btn_lower")
        self.btn_lower.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_lower.setCheckable(True)
        self.btn_lower.setChecked(True)

        self.layout_char.addWidget(self.btn_lower)

        self.btn_upper = QPushButton(self.centralwidget)
        self.btn_upper.setObjectName(u"btn_upper")
        self.btn_upper.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_upper.setCheckable(True)
        self.btn_upper.setChecked(True)

        self.layout_char.addWidget(self.btn_upper)

        self.btn_digits = QPushButton(self.centralwidget)
        self.btn_digits.setObjectName(u"btn_digits")
        self.btn_digits.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_digits.setCheckable(True)
        self.btn_digits.setChecked(True)

        self.layout_char.addWidget(self.btn_digits)

        self.btn_special = QPushButton(self.centralwidget)
        self.btn_special.setObjectName(u"btn_special")
        self.btn_special.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_special.setCheckable(True)
        self.btn_special.setChecked(False)

        self.layout_char.addWidget(self.btn_special)


        self.verticalLayout.addLayout(self.layout_char)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Evorl's passgen", None))
        self.icon.setText("")
        self.btn_visi.setText("")
        self.btn_refresh.setText("")
#if QT_CONFIG(shortcut)
        self.btn_refresh.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.btn_copy.setText("")
#if QT_CONFIG(shortcut)
        self.btn_copy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.text_strengt.setText("")
        self.text_entropy.setText("")
        self.btn_lower.setText(QCoreApplication.translate("MainWindow", u"a-z", None))
        self.btn_upper.setText(QCoreApplication.translate("MainWindow", u"A-Z", None))
        self.btn_digits.setText(QCoreApplication.translate("MainWindow", u"0-9", None))
        self.btn_special.setText(QCoreApplication.translate("MainWindow", u"*%@", None))
    # retranslateUi

