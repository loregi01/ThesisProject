# ThesisProject
# Idea
The idea is to start from an event log describing an industrial project and after a processing phase to perform reasoning to achieve several goals.
# Installation
This project is thought to run on WSL. To execute it, install XTerm (on your native OS) and flag "Multiple Windows", select 1 as Display number, flag "Start no client", flag "Disable access control" (do not change the default settings) and save the settings in the default path. You need also to install both PySide6:
```bash
pip install PySide6
```
Then you've simple to execute app.py. 
```bash
python3 app.py
```
In order to test the prolog file, you need to install swipl, so execute the following commands: 
```bash
sudo apt-add-repository ppa:swi-prolog/stable
sudo apt-get update
sudo apt-get install swi-prolog
```
# Something about the files
The file "easy_level_test.xes" is a toy file used to avoid the user to download a .xes file that can result too heavy, but you can delete it. Instead the "user_file.xes" cannot be deleted in any case since it's the file used to copy the content of the file selected by the user, so it's rewritten every time the user selects a new .xes file. "easy_level_test.xes" contains the log representing a basic industrial project, if you want to use something more complex, use either the "mid_level_test.xes" or the "hard_level_test.xes" file.
# How to change the industrial process
The .xes files represent a specific industrial process. If you want to change the variables the process changes, keep the corresponding .bpmn file, transform it into a .xes file (I used ProM for this purpose) and then add manually the objects by following the correct syntax (look at the .xes file in the repository)
# How to test
Before performing reasoning is a good practice to test if the obtained syntax is correct, so append at the end of the create_prolog.pl file a procedure called simulateprocess0 
```prolog
proc(simulateprocess0,[<sequence of actions>]). 
```
Then run the command
```bash
swipl config.pl main.pl
```
and, by assumning the procedure syntax is correct, if swipl returns you true after printing the sequence of actions inserted in the procedure, the prolog BAT is correct, otherwise you have to debug it manually. N.B. Very unfortunately the second case will verify (in this case I apologize for the inconvenience), so check carefully the procedure syntax is correct in the case swipl return you false.