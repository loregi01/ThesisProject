from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtWidgets import (QLabel, QLineEdit, QMainWindow, QPushButton, QWidget, QFileDialog)

class Ui_ThesisProject(object):
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
        self.title.setGeometry(QRect(250, 30, 381, 51))
        self.title.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.title.setStyleSheet(u"font: 12pt \"Times New Roman\"; color: white;")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Creazione del QLineEdit
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(280, 280, 331, 31))
        self.lineEdit.setStyleSheet(u"background-color: transparent; color: white; border: 1px solid white; ")
        
        # Creazione del QLabel per le istruzioni
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 260, 191, 16))
        self.label.setStyleSheet(u"color: white;")
        self.lineEdit.setReadOnly(True)
        
        # Creazione del QPushButton per selezionare il file
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(620, 280, 75, 31))
        self.pushButton.setStyleSheet(u"QPushButton {"
                                       "background-color: transparent; "
                                       "color: white; "
                                       "border: 1px solid white; "
                                       "}"
                                       "QPushButton:hover {"
                                       "background-color: rgba(255, 255, 255, 0.2); "
                                       "}")
        self.pushButton.setText("Load file")
        
        ThesisProject.setCentralWidget(self.centralwidget)

        self.retranslateUi(ThesisProject)

        QMetaObject.connectSlotsByName(ThesisProject)

    def retranslateUi(self, ThesisProject):
        ThesisProject.setWindowTitle(QCoreApplication.translate("ThesisProject", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("ThesisProject", u"<INSERIRE TITOLO PROGETTO>", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("ThesisProject", u"Select a .xes file", None))
        self.label.setText(QCoreApplication.translate("ThesisProject", u"Load the .xes file", None)) 

    def open_file_dialog(self):
        options = QFileDialog.Options()
        selected_file, _ = QFileDialog.getOpenFileName(None, "Select a .xes file", "", "XES Files (*.xes)", options=options)
        self.lineEdit.setText(selected_file)
        self.label.setText("File correctly loaded")
        with open(selected_file, 'r') as source_file:
            content = source_file.read()
        with open('user_file.xes', 'w') as dest_file:
            dest_file.write(content)