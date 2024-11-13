import sys
import ast
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from views.home_page import Ui_ThesisProject
from views.page_condition import Ui_ThesisProject as PageCondition
from views.choise_page import Ui_MainWindow as ChoisePage
from views.project_task import Ui_MainWindow as ProjPage
from PySide6.QtCore import Signal, Slot
import os,time,subprocess
from pyswip import Prolog

global condition_string
condition_string = ""
global procedure_string
procedure_string = ""
global counter 
counter = 0

os.environ["QT_QPA_PLATFORM"] = "xcb"
os.environ["DISPLAY"] = ":0"

class MainWindow(QMainWindow):

    choise_page_signal = Signal()

    def __init__(self):
        super().__init__()

        self.ui = Ui_ThesisProject()
        self.ui.setupUi(self) 

        self.ui.pushButton.clicked.connect(self.open_file_dialog)
        self.choise_page_signal.connect(self.open_choise_page)

        self.choise_page_window = None

    def open_file_dialog(self):
        options = QFileDialog.Options()
        selected_file, _ = QFileDialog.getOpenFileName(None, "Select a .xes file", "", "XES Files (*.xes)", options=options)
        self.ui.lineEdit.setText(selected_file)
        self.ui.label.setText("File correctly loaded (wait just few seconds...)")
        self.ui.label.repaint()
        self.ui.lineEdit.repaint()
        print(self.ui.label.isVisible())
        with open(selected_file, 'r') as source_file:
            content = source_file.read()
        with open('user_file.xes', 'w') as dest_file:
            dest_file.write(content)
        time.sleep(2)
        result = subprocess.run(['python3', 'parser_xes_automated.py'], check=True, text=True, capture_output=True)
        print(result.stdout)
        #time.sleep(2)
        result = subprocess.run(['python3', 'create_prolog.py'], check=True, text=True, capture_output=True)
        print(result)
        #time.sleep(2)
        self.choise_page_signal.emit()
    
    def open_choise_page(self):
        self.close()
        self.choise_page_window = SelectionPage()
        self.choise_page_window.show()

class SelectionPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = ChoisePage()
        self.ui.setupUi(self) 
        self.ui.pushButton.clicked.connect(self.on_confirm_button_clicked)
        self.projection_task_window = None

    def on_confirm_button_clicked(self):
        self.close()
        self.projection_task_window = ProjectionPage()
        self.projection_task_window.show()


class ProjectionPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = ProjPage()
        self.ui.setupUi(self) 
        self.ui.pushButtonAbove.clicked.connect(self.on_button_clicked)

        from interactive_program import input_string
        from interactive_program import action_list
        global condition_string
        condition_string = input_string
        condition_string_mod = condition_string.replace('[','').replace(']','').split(',')
        string_to_print = ''
        action_string = ''
        for act in action_list:
            action_string += act + '\n'
        for elem in condition_string_mod:
            elem = elem.replace('\'','')
            string_to_print += elem + '\n'
            self.ui.comboBox.addItem(elem)
        self.ui.label_2.setText(f"Extracted Fluents:\n{string_to_print}")
        self.ui.label_5.setText(f"Extracted Actions:\n{action_string}")

    def on_button_clicked (self):
        self.ui.lineEdit_2.setText('')
        if self.ui.lineEdit.text() == '':
            print('errore')
        else:
            prolog = Prolog()
            # Carica i file Prolog necessari
            prolog.consult("config.pl")  # Carica il file config.pl
            prolog.consult("main.pl")    # Carica il file main.pl

            try:
                result = list(prolog.query(f"holds({self.ui.comboBox.currentText()}, {self.ui.lineEdit.text()}).")) 

                if result:
                    if len(result[0]) == 0: 
                        self.ui.lineEdit_2.setText("True")
                    else:
                        dictionary = result[0]
                        value = dictionary['Q0']
                        self.ui.lineEdit_2.setText('Q0='+str(value))
                else:
                    self.ui.lineEdit_2.setText("False")
        
            
            except Exception as e:
                print(f"Si è verificato un errore imprevisto: {e}")
                self.ui.lineEdit.setText(f"ERROR: bad write")



class WhilePage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = PageCondition()
        self.ui.setupUi(self) 
        self.ui.pushButton.clicked.connect(self.on_confirm_button_clicked)
        from interactive_program import input_string
        global condition_string
        condition_string = input_string
        condition_string_mod = condition_string.replace('[','').replace(']','').split(',')
        string_to_print = ''
        for elem in condition_string_mod:
            string_to_print += elem + '\n'
        self.ui.label.setText(f"Select the condition to end the process:\n{string_to_print}")

    def on_confirm_button_clicked(self):
        user_input = self.ui.lineEdit.text()
        global condition_string
        list_conditions = ast.literal_eval(condition_string)
        print(list_conditions)
        if user_input not in list_conditions:
            self.ui.lineEdit.setText('')
            self.ui.lineEdit.setPlaceholderText('Condition not valid')
        else:
            self.ui.lineEdit.setText('')
            from interactive_program import procedure_calculation
            global procedure_string
            procedure_string = procedure_calculation
            global counter
            procedure = f'''\n\nproc(simulateprocess{counter}, [\nwhile(neg({user_input}), [\n
                                    {procedure_calculation}])]).'''

            with open('main.pl', 'r') as file:
                lines = file.readlines()

            if lines: 
                lines.pop()

            with open('main.pl', 'w') as file:
                file.writelines(lines)
                file.write(f"main() :- 	indigolog(simulateprocess{counter}).")
            counter += 1
            # with open("create_prolog.pl", "a") as file:
                # file.write(f"{procedure}")
            self.close()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()  
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()