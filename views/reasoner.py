from PySide6.QtCore import QCoreApplication, QRect, Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPlainTextEdit, QWidget, QPushButton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(902, 655)
        MainWindow.setStyleSheet(u"background-image: url(views/graphics/sfondo_tesi.jpeg);")
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # Primo Label (resta alla stessa posizione)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 30, 331, 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Solleva la label sopra gli altri widget
        self.label.raise_()

        # Primo QPlainTextEdit
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(250, 150, 401, 221))

        # Bottone sotto l'area 1, centrato
        button_width = 75
        button_height = 31
        button_x = (MainWindow.width() - button_width) // 2  # Calcola la posizione X per centrare
        self.button = QPushButton(self.centralwidget)
        self.button.setObjectName(u"button")
        self.button.setText("Submit")  # Il testo del bottone
        self.button.setGeometry(QRect(button_x, 380, button_width, button_height))  # Posizionato sotto il QPlainTextEdit
        self.button.setStyleSheet(u"QPushButton {"
                                  "background-color: transparent; "
                                  "color: white; "
                                  "border: 2px solid white; "
                                  "border-radius: 9px; "
                                  "} "
                                  "QPushButton:hover {"
                                  "background-color: rgba(255, 255, 255, 0.2); "
                                  "}")

        # Secondo Label (messo sopra il QPlainTextEdit, più in alto)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 130, 301, 16))  # Posizionata più in alto sopra il QPlainTextEdit

        # Solleva la seconda label sopra gli altri widget
        self.label_2.raise_()

        # Terzo Label (messo sopra il secondo QPlainTextEdit)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 410, 51, 21))  # Posizionata sopra il secondo QPlainTextEdit

        # Secondo QPlainTextEdit
        self.plainTextEdit_2 = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(250, 430, 401, 51))
        self.plainTextEdit_2.setReadOnly(True)

        self.label.setStyleSheet("color: white;")  # Imposta il colore del testo a bianco
        self.label_2.setStyleSheet("color: white;")  # Imposta il colore del testo a bianco
        self.label_3.setStyleSheet("color: white;")  # Imposta il colore del testo a bianco
        self.plainTextEdit.setStyleSheet("color: white;")
        self.plainTextEdit_2.setStyleSheet("color: white;")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Reasoner", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Write the query in natural language", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Output:", None))
