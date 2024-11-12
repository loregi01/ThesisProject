from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QMainWindow, QPushButton,
    QSizePolicy, QWidget, QLabel)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(902, 655)
        MainWindow.setStyleSheet(u"background-image: url(views/graphics/sfondo_tesi.jpeg);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        # QLabel (label sopra la ComboBox)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setText("Select the type of reasoning you want")
        self.label.setStyleSheet("color: white;")
        self.label.setGeometry(QRect(280, 260, 391, 16))  # Posizione della label
        
        # ComboBox
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("Projection Task")  # Prima opzione
        self.comboBox.addItem("Legality Task")   # Seconda opzione
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(280, 280, 331, 31))  # Posizione della ComboBox
        self.comboBox.setStyleSheet(u"""
            QComboBox {
                border: 1px solid white;
                color: white; 
                padding: 5px;
                background-color: black;  
            }
            QComboBox::item {
                color: black;  
                background-color: white;
            }
            QComboBox::item:selected {
                background-color: lightgray; 
                color: black; 
            }
            QComboBox::drop-down {
                border: 1px solid white;
                background-color: white; 
            }
            QComboBox::placeholderText {
                color: white;  
            }
        """)
        
        # PushButton
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(620, 280, 75, 31))  # Posizione del bottone
        self.pushButton.setStyleSheet(u"""
            QPushButton {
                border: 1px solid white;
                color: white;
                padding: 5px;
            }
        """)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Thesis Project", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
