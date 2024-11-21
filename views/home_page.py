from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt, Signal)
from PySide6.QtWidgets import (QLabel, QLineEdit, QMainWindow, QPushButton, QWidget, QFileDialog)
from PySide6.QtGui import QFont, QFontDatabase, QPixmap
import time
import subprocess
from views.page_condition import Ui_ThesisProject as PageCondition
import os

class Ui_ThesisProject(object):
    signal_while_condition = Signal()
    
    def setupUi(self, ThesisProject):
        if not ThesisProject.objectName():
            ThesisProject.setObjectName(u"ThesisProject")
        ThesisProject.resize(902, 655)
        ThesisProject.setStyleSheet(u"background-image: url(views/graphics/sfondo_tesi.jpeg);")
        
        self.centralwidget = QWidget(ThesisProject)
        self.centralwidget.setObjectName(u"centralwidget")
        
        # Creazione del QLabel (titolo)
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        font = QFont("DejaVu Sans", 12)  
        self.title.setFont(font)
        self.title.setGeometry(QRect(250, 30, 381, 51))
        self.title.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.title.setStyleSheet(u"color: white;")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Creazione del QLabel per l'immagine
        self.image_label = QLabel(self.centralwidget)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setGeometry(QRect(300, 120, 300, 150))  # Posizione e dimensioni
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        img_path = os.path.abspath("views/graphics/icona_homepage.jpg")
        pixmap = QPixmap(img_path)

        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)  # Adatta l'immagine alla dimensione
        self.image_label.raise_()  # Porta l'immagine sopra gli altri widget
        
        # Creazione del QLineEdit
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(280, 320, 331, 31))
        self.lineEdit.setStyleSheet(u"background-color: transparent; color: white; border: 2px solid white; border-radius: 9px;")
        
        # Creazione del QLabel per le istruzioni
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 300, 391, 16))
        font = QFont("DejaVu Sans", 10)  
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: white;")
        self.lineEdit.setReadOnly(True)
        
        # Creazione del QPushButton per selezionare il file
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont("DejaVu Sans", 9)  
        self.pushButton.setFont(font)
        self.pushButton.setGeometry(QRect(620, 320, 75, 31))
        self.pushButton.setStyleSheet(u"QPushButton {"
                                       "background-color: transparent; "
                                       "color: white; "
                                       "border: 2px solid white; "
                                       "border-radius: 9px; "
                                       "}"
                                       "QPushButton:hover {"
                                       "background-color: rgba(255, 255, 255, 0.2); "
                                       "}")
        self.pushButton.setText("Load file")
        
        ThesisProject.setCentralWidget(self.centralwidget)

        self.retranslateUi(ThesisProject)

        QMetaObject.connectSlotsByName(ThesisProject)

    def retranslateUi(self, ThesisProject):
        ThesisProject.setWindowTitle(QCoreApplication.translate("ThesisProject", u"Thesis Project", None))
        self.title.setText(QCoreApplication.translate("ThesisProject", u"<INSERIRE TITOLO PROGETTO>", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("ThesisProject", u" Select a .xes file", None))
        self.label.setText(QCoreApplication.translate("ThesisProject", u" Load the .xes file", None))
