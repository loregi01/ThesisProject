import sys
import ast
import re
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from views.home_page import Ui_ThesisProject
from views.page_condition import Ui_ThesisProject as PageCondition
from views.choise_page import Ui_MainWindow as ChoisePage
from views.project_task import Ui_MainWindow as ProjPage
from views.legality_task import Ui_MainWindow as LegPage
from views.reasoner import Ui_MainWindow as Reas
from PySide6.QtCore import Signal, Slot
import os,time,subprocess
from pyswip import Prolog
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

global condition_string
condition_string = ""
global procedure_string
procedure_string = ""
global counter 
counter = 0
global result_collection
result_collection = []

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

        self.reasoner_page_window = None

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
        self.reasoner_page_window = Reasoner()
        self.reasoner_page_window.show()

class Reasoner(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Reas()
        self.ui.setupUi(self) 
        self.ui.button.clicked.connect(self.on_submit_clicked)
        from interactive_program import input_string
        from interactive_program import action_list
        global condition_string
        condition_string = input_string
        condition_string_mod = condition_string.replace('[','').replace(']','').split(',')
        for index in range(0,len(condition_string_mod)):
            elem = condition_string_mod[index].replace(' ','')
            condition_string_mod[index] = elem
        string_to_print = ''
        action_string = ''
        for act in action_list:
            action_string += act + '\n'
        for elem in condition_string_mod:
            elem = elem.replace('\'','')
            string_to_print += elem + '\n'
        
        self.ui.plainTextEdit_left.setPlainText(f"Extracted Fluents:\n\n{string_to_print}")
        self.ui.plainTextEdit_right.setPlainText(f"Extracted Actions:\n\n{action_string}")

    def on_submit_clicked(self):
        if self.ui.plainTextEdit.toPlainText() == "":
            self.ui.label_2.setStyleSheet("color: red;")
            self.ui.label_2.setText("The input cannot be empty") 
        else:
            print("Processing the request ...")
            from interactive_program import input_string
            from interactive_program import action_list
            action_list = str(action_list)
            self.ui.label_2.setStyleSheet("color: white;")
            self.ui.label_2.setText("Write the query in natural language") 
            query = self.ui.plainTextEdit.toPlainText()
            OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

            client = OpenAI(
                api_key = OPENAI_API_KEY,
            )

            completion = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f'''You need to help me to analyze the following phrase: {query}. First add by youself the character \'?\'
                 at the end of the phrase if it's not present. Then I want to understand if the user wants to perform the legality task or the projection task. We're talking about
                 legality task if the user wants to understand if a sequence of actions is executable, we're talking about 
                 projection task if the user wants to understand if a fluent is true after the execution of a sequence of actions.
                 you must follow the following rules to the letter:
                 - If you detect the legality task, take all the actions inserted by the user and modify them as follow since they need to have a 
                   precise structure. First add to the name the word \'action\' if is not present (ex. confirm order is changed into action confirm order).
                   Some actions take an input, that input if inserted by the user MUST be kept, do not remove it for any reason and insert it between 
                   brackets if it's not. Finally the action name must not contain spaces, so take what you obtained in the previous point and remove all the spaces. A complete example is the following, 
                   suppose that the action name you detect is \'confirm payment 10\', the name becomes \'actionconfirmpayment(10)\'.
                   The output must be ONLY the following: ('legality_task',['action_name_1','action_name_2',...,'action_name_n']), no explanations or
                   additional text. The action name MUST belong to the list {action_list}, you cannot return to me something that's 
                   not in the list in any case, and in case of params, you've to substitute
                   the parameter in the list with the params inserted by the user.
                 - If you detect the projection task, take all the actions inserted by the user and modify them as follow since they need to have a 
                   precise structure. First add to the name the word \'action\' if is not present (ex. confirm order is changed into action confirm order).
                   Some actions take an input, that input if inserted by the user MUST be kept, do not remove it for any reason and insert it between 
                   brackets if it's not. Finally the action name must not contain spaces, so take what you obtained in the previous point and remove all the spaces. A complete example is the following, 
                   suppose that the action name you detect is \'confirm payment 10\', the name becomes \'actionconfirmpayment(10)\'. Then take the fluent name,
                   some fluent takes an input, that input if inserted by the user MUST be kept, do not remove it for any reason and insert it between 
                   brackets if it's not. At the end remove all the spaces in the name. Notice that the fluent name NEVER contains the word fluent and the \'?\' character. A complete example is the following, suppose that you detect as fluent
                   name items shipped Q0, the name becomes itemsshipped(Q0). The output must be ONLY the following:
                   ('projection_task',['action_name_1','action_name_2',...,'action_name_n'],'fluent_name'), no explanations or
                   additional text. The action name MUST belong to the list {action_list}, you cannot return to me something that's 
                   not in the list in any case, while the fluent name MUST belong to the list {input_string}, you cannot return to me something that's 
                   not in the list in any case, and in case of params, you've to substitute the parameter in the list with the params inserted by the user. 
                 - If you don't detect neither legality task nor projection task, the output must be ONLY the following: \'No result\', no explanations or
                   additional text.
                   '''},
            ]
            )

            if completion.choices[0].message.content.strip() == "No result":
                self.ui.plainTextEdit_2.setPlainText("Sorry, we were not able to parse your request")
            else:
                prolog = Prolog()
                output = completion.choices[0].message.content.strip()
                if output[len(output)-1] == ',':
                    output = output[:-1]
                output = output.replace("fluent","")
                print(output)
                tupl = ast.literal_eval(output)
                if tupl[0] == "legality_task":
                    actions = tupl[1]
                    try:
                        actions = str(actions).replace('\'','')
                        query = f"proc(simulateprocess0, {actions})."
                        print(query)
                        with open("create_prolog.pl", "r") as file:
                            lines = file.readlines()
                        if lines:
                            lines[-1] = f"{query}" + "\n"  # Sostituisci l'ultima riga con quella nuova
                            with open("create_prolog.pl", "w") as file:
                                file.writelines(lines)
                        else:
                            with open("create_prolog.pl", "w") as file:
                                file.write(f"{query}" + "\n")

                        prolog.consult("config.pl")  
                        prolog.consult("main.pl") 
                        result = list(prolog.query(f"main.")) 
                
                        if result:
                            self.ui.plainTextEdit_2.setPlainText("The sequence of actions is executable")
                        else:
                            self.ui.plainTextEdit_2.setPlainText("The sequence of actions is not executable")
        
            
                    except Exception as e:
                        #print(f"Si è verificato un errore imprevisto: {e}")
                        error = str(e).split('\'')
                        print(error)
                        self.ui.plainTextEdit_2.setPlainText(f"{error[3]}")
                else:
                    actions = tupl[1]
                    fluent = tupl[2].replace('?','').replace(' ','')
                    prolog.consult("config.pl")  # Carica il file config.pl
                    prolog.consult("main.pl")    # Carica il file main.pl

                    try:
                        actions.reverse()
                        actions = str(actions)
                        actions = actions.replace('\'','')
                        result = list(prolog.query(f"holds({fluent}, {actions}).")) 
                        print(f"holds({fluent}, {actions}).")
                        if result:
                            if len(result[0]) == 0: 
                                self.ui.plainTextEdit_2.setPlainText("The fluent value is True after the execution of the sequence of actions")
                            else:
                                dictionary = result[0]
                                value = dictionary['Q0']
                                self.ui.plainTextEdit_2.setPlainText('The fluent value is True after the execution of the sequence of actions only if Q0='+str(value))
                        else:
                            self.ui.plainTextEdit_2.setPlainText("The fluent value is False after the execution of the sequence of actions")
        
            
                    except Exception as e:
                        error = str(e).split('\'')
                        print(error)
                        self.ui.plainTextEdit_2.setPlainText(f"{error[3]}")




class SelectionPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = ChoisePage()
        self.ui.setupUi(self) 
        self.ui.pushButton.clicked.connect(self.on_confirm_button_clicked)
        self.projection_task_window = None
        self.legality_task_window = None

    def on_confirm_button_clicked(self):
        if self.ui.comboBox.currentText() == "Projection Task":
            self.close()
            self.projection_task_window = ProjectionPage()
            self.projection_task_window.show()
        else:
            self.close()
            self.legality_task_window = LegalityPage()
            self.legality_task_window.show()


class LegalityPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = LegPage()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.on_proj_clicked) 
        self.ui.pushButton.clicked.connect(self.on_submit_clicked)

        global result_collection 
        result_collection = []
        
        self.projection_window = None

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
        
        self.ui.label_fluents.setText(f"Extracted Fluents:\n{string_to_print}")
        self.ui.label_actions.setText(f"Extracted Actions:\n{action_string}")

    def on_proj_clicked (self):
        self.close()
        self.projection_window = ProjectionPage()
        self.projection_window.show()

    def on_submit_clicked (self):
        #self.ui.lineEdit.setText('')
        if self.ui.lineEdit.text() == '':
            self.ui.label_2.setStyleSheet("color: red;")
            self.ui.label_2.setText("Sequence of actions NOT valid")
        else:
            prolog = Prolog()   
            self.ui.label_2.setStyleSheet("color: white;")
            self.ui.label_2.setText("Sequence of actions ([<a1>,<a2>,...]")
            try:
                query = f"proc(simulateprocess0, {self.ui.lineEdit.text()})."
                with open("create_prolog.pl", "r") as file:
                    lines = file.readlines()

    
                if lines:
                    lines[-1] = f"{query}" + "\n"  # Sostituisci l'ultima riga con quella nuova

                    with open("create_prolog.pl", "w") as file:
                        file.writelines(lines)
                else:
                    with open("create_prolog.pl", "w") as file:
                        file.write(f"{query}" + "\n")

                prolog.consult("config.pl")  
                prolog.consult("main.pl") 
                result = list(prolog.query(f"main.")) 
                
                if result:
                    self.ui.lineEdit_2.setText("True")
                else:
                    self.ui.lineEdit_2.setText("False")
        
            
            except Exception as e:
                print(f"Si è verificato un errore imprevisto: {e}")
                self.ui.lineEdit.setText(f"ERROR: bad write")



class ProjectionPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = ProjPage()
        self.ui.setupUi(self) 
        self.ui.pushButtonAbove.clicked.connect(self.on_button_clicked)
        self.ui.pushButton.clicked.connect(self.on_go_back_clicked)

        self.legality_window = None

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
        
        self.ui.content_widget_2.setText(f"Extracted Fluents:\n{string_to_print}")
        self.ui.content_widget_5.setText(f"Extracted Actions:\n{action_string}")

    def on_go_back_clicked (self):
        self.close()
        self.legality_window = LegalityPage()
        self.legality_window.show()

    def on_button_clicked (self):
        self.ui.lineEdit_2.setText('')
        if self.ui.lineEdit.text() == '':
            self.ui.label_4.setStyleSheet("color: red;")
            self.ui.label_4.setText("Sequence of actions NOT valid")
            print('errore')
        else:
            self.ui.label_4.setStyleSheet("color: white;")
            self.ui.label_4.setText("Insert the sequence of actions ([<a1>,<a2>,...])")
            prolog = Prolog()
            # Carica i file Prolog necessari
            prolog.consult("config.pl")  # Carica il file config.pl
            prolog.consult("main.pl")    # Carica il file main.pl

            try:
                actions = self.ui.lineEdit.text()
                actions = actions.replace("[","").replace("]","").split(",")
                actions.reverse()
                actions = str(actions)
                actions = actions.replace('\'','')
                result = list(prolog.query(f"holds({self.ui.comboBox.currentText()}, {actions}).")) 

                if result:
                    if len(result[0]) == 0: 
                        self.ui.lineEdit_2.setText("True")
                    else:
                        dictionary = result[0]
                        value = dictionary['Q0']
                        self.ui.lineEdit_2.setText('True if Q0='+str(value))
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
        condition_string_mod = condition_string.replace(' ','').replace('[','').replace(']','').split(',')
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