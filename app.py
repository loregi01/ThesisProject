import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from views.home_page import Ui_MainWindow
import os

os.environ["QT_QPA_PLATFORM"] = "xcb"
os.environ["DISPLAY"] = ":0"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  

def main():
    app = QApplication(sys.argv)
    window = MainWindow()  
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()