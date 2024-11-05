from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(902, 655)

        MainWindow.setStyleSheet("background-image: url(views/graphics/sfondo_tesi.jpeg);")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        layout = QVBoxLayout(self.centralwidget)
        self.centralwidget.setLayout(layout)

        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignCenter)  
        self.title.setStyleSheet("font: 20pt 'Times New Roman'; color: white;")  

        layout.addWidget(self.title)  

        layout.addStretch(1)  

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Thesis Project", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"TESTO DI PROVA", None))
