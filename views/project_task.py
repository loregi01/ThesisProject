from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QWidget)

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
        self.label.setGeometry(QRect(260, 40, 361, 31))
        self.label.setStyleSheet(u"font: 14pt \"Segoe UI\"; color: white;")  # Testo bianco
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Prima Label (ex scrollArea_2)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 90, 351, 161))  # Posizionamento simile alla scrollArea_2
        self.label_2.setStyleSheet(u"border: 1px solid white; color: white;")  # Bordo bianco
        
        # Seconda Label (ex scrollArea_5)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(470, 90, 351, 161))  # Posizionamento simile alla scrollArea_5
        self.label_5.setStyleSheet(u"border: 1px solid white; color: white;")  # Bordo bianco

        # ComboBox
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 320, 271, 16))
        self.label_3.setStyleSheet("color: white;")  # Testo bianco per la label
        
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(50, 340, 281, 30))
        self.comboBox.setStyleSheet(u"""
            border: 1px solid white;
            color: white;
            background-color: transparent;
        """)  # Stile per la combo box

        # Input Sequence
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 390, 281, 16))
        self.label_4.setStyleSheet("color: white;")  # Testo bianco per la label
        
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(50, 410, 581, 30))
        self.lineEdit.setStyleSheet(u"""
            border: 1px solid white;
            color: white;
            background-color: transparent;
        """)  # Stile per LineEdit con il placeholder visibile
        self.lineEdit.setPlaceholderText("Insert the sequence of actions ([<a1>,<a2>,...])")  # Imposta il testo del placeholder

        # Output
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 460, 281, 16))
        self.label_6.setStyleSheet("color: white;")  # Testo bianco per la label
        
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(50, 480, 151, 30))
        self.lineEdit_2.setStyleSheet(u"""
            border: 1px solid white;
            color: white;
            background-color: transparent;
        """)  # Stile per LineEdit con il placeholder visibile
        self.lineEdit_2.setPlaceholderText("Output")  # Imposta il testo del placeholder
        self.lineEdit_2.setReadOnly(True)

        # Bottone sopra il bottone esistente
        self.pushButtonAbove = QPushButton(self.centralwidget)
        self.pushButtonAbove.setObjectName(u"pushButtonAbove")
        self.pushButtonAbove.setGeometry(QRect(380, 540, 141, 31))  # Posizionato sopra il bottone esistente
        self.pushButtonAbove.setStyleSheet(u"""
            border: 1px solid white;
            color: white;
            background-color: transparent;
        """)
        self.pushButtonAbove.setText("Submit")  # Testo del bottone sopra

        # Bottone esistente
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(380, 580, 141, 31))
        
        # Stile per il bottone
        self.pushButton.setStyleSheet(u"""
            border: 1px solid white;
            color: white;
            background-color: transparent;
        """)
        self.pushButton.setText("Go to the legality task")  # Testo del bottone esistente

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Projection task", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Select the fluent", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Insert the sequence of actions ([<a1>,<a2>,...])", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Go to the legality task", None))  # Nessuna modifica su questi
