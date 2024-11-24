from PySide6.QtCore import QCoreApplication, QRect, Qt
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
        self.label.setStyleSheet("color: white;")  # Imposta il colore del testo a bianco

        # Solleva la label sopra gli altri widget
        self.label.raise_()

        # Aree di testo affiancate (nuove)
        self.plainTextEdit_left = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_left.setObjectName(u"plainTextEdit_left")
        self.plainTextEdit_left.setGeometry(QRect(200, 70, 240, 105))  # Area di testo sinistra, altezza maggiore
        self.plainTextEdit_left.setStyleSheet("color: white;")
        self.plainTextEdit_left.setReadOnly(True)  # Non editabile

        self.plainTextEdit_right = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_right.setObjectName(u"plainTextEdit_right")
        self.plainTextEdit_right.setGeometry(QRect(450, 70, 240, 105))  # Area di testo destra, altezza maggiore
        self.plainTextEdit_right.setStyleSheet("color: white;")
        self.plainTextEdit_right.setReadOnly(True)  # Non editabile

        # Primo QPlainTextEdit
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(250, 250, 401, 221))
        self.plainTextEdit.setStyleSheet("color: white;")

        # Bottone sotto l'area 1, centrato
        button_width = 75
        button_height = 31
        button_x = (MainWindow.width() - button_width) // 2  # Calcola la posizione X per centrare
        self.button = QPushButton(self.centralwidget)
        self.button.setObjectName(u"button")
        self.button.setText("Submit")  # Il testo del bottone
        self.button.setGeometry(QRect(button_x, 480, button_width, button_height))  # Posizionato sotto il QPlainTextEdit
        self.button.setStyleSheet(u"QPushButton {"
                                  "background-color: transparent; "
                                  "color: white; "
                                  "border: 2px solid white; "
                                  "border-radius: 9px; "
                                  "} "
                                  "QPushButton:hover {"
                                  "background-color: rgba(255, 255, 255, 0.2); "
                                  "} ")

        # Secondo Label (messo sopra il QPlainTextEdit, più in alto)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 230, 301, 16))  # Posizionata più in alto sopra il QPlainTextEdit
        self.label_2.setStyleSheet("color: white;")

        # Solleva la seconda label sopra gli altri widget
        self.label_2.raise_()

        # Terzo Label (messo sopra il secondo QPlainTextEdit)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 510, 51, 21))  # Posizionata sopra il secondo QPlainTextEdit
        self.label_3.setStyleSheet("color: white;")

        # Secondo QPlainTextEdit
        self.plainTextEdit_2 = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(250, 530, 401, 51))
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setStyleSheet("color: white;")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Thesis Project", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Reasoner", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Write the query in natural language", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Output:", None))
