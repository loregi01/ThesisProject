from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QWidget, QVBoxLayout)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(902, 655)
        MainWindow.setStyleSheet(u"background-image: url(views/graphics/sfondo_tesi.jpeg);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # Label di titolo
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 40, 362, 31))
        self.label.setStyleSheet(u"font: 14pt 'Segoe UI'; color: white;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.raise_()

        # Altre label
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 310, 391, 16))
        self.label_2.setStyleSheet(u"color: white;")
        self.label_2.raise_()

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 400, 81, 20))
        self.label_3.setStyleSheet(u"color: white;")
        self.label_3.raise_()

        # Prima ScrollArea
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(50, 90, 351, 161))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 349, 159))
        
        # QLabel vuota da sovrascrivere (senza testo)
        self.label_fluents = QLabel(self.scrollAreaWidgetContents)
        self.label_fluents.setObjectName(u"label_fluents")
        self.label_fluents.setStyleSheet(u"color: white;")
        self.label_fluents.setWordWrap(True)  # Per consentire di andare a capo se necessario
        layout1 = QVBoxLayout(self.scrollAreaWidgetContents)
        layout1.addWidget(self.label_fluents)
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # Seconda ScrollArea
        self.scrollArea_2 = QScrollArea(self.centralwidget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(470, 90, 351, 161))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 349, 159))

        # QLabel vuota da sovrascrivere (senza testo)
        self.label_actions = QLabel(self.scrollAreaWidgetContents_2)
        self.label_actions.setObjectName(u"label_actions")
        self.label_actions.setStyleSheet(u"color: white;")
        self.label_actions.setWordWrap(True)
        layout2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        layout2.addWidget(self.label_actions)
        
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        # LineEdit con bordo e colore testo visibile
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(50, 330, 771, 31))
        self.lineEdit.setStyleSheet(u"border: 1px solid white; color: white;")
        self.lineEdit.raise_()

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(50, 420, 151, 31))
        self.lineEdit_2.setStyleSheet(u"border: 1px solid white; color: white;")
        self.lineEdit_2.raise_()

        # Pulsanti
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(380, 540, 141, 35))
        self.pushButton.setStyleSheet(u"border: 1px solid white; color: white;")
        self.pushButton.raise_()

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(380, 580, 141, 35))
        self.pushButton_2.setStyleSheet(u"border: 1px solid white; color: white;")
        self.pushButton_2.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Legality Task", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sequence of actions ([<a1>,<a2>,...]", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Is executable?", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Go to the Projection Task", None))
