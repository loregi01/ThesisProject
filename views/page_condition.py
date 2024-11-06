from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_ThesisProject(object):
    def setupUi(self, ThesisProject):
        if not ThesisProject.objectName():
            ThesisProject.setObjectName(u"ThesisProject")
        ThesisProject.resize(902, 655)
        ThesisProject.setStyleSheet(u"background-image: url(views/graphics/sfondo_tesi.jpeg);")
        self.centralwidget = QWidget(ThesisProject)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(250, 30, 381, 51))
        self.title.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.title.setStyleSheet(u"font: 12pt \"Times New Roman\";")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(280, 280, 331, 31))
        self.lineEdit.setStyleSheet(u"background-color: transparent;\n"
"color: white; \n"
"border: 1px solid white; ")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: white;")
        self.label.setGeometry(QRect(270, 100, 341, 151))
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(620, 280, 75, 31))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent; \n"
"    color: white; \n"
"    border: 1px solid white; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2); \n"
"}")
        ThesisProject.setCentralWidget(self.centralwidget)

        self.retranslateUi(ThesisProject)

        QMetaObject.connectSlotsByName(ThesisProject)
    # setupUi

    def retranslateUi(self, ThesisProject):
        ThesisProject.setWindowTitle(QCoreApplication.translate("ThesisProject", u"Thesis Project", None))
        self.title.setText(QCoreApplication.translate("ThesisProject", u"<INSERIRE TITOLO PROGETTO>", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("ThesisProject", u"Insert the condition", None))
        self.label.setText(QCoreApplication.translate("ThesisProject", u"Prova", None))
        self.pushButton.setText(QCoreApplication.translate("ThesisProject", u"Confirm", None))
    # retranslateUi

