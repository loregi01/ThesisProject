# ThesisProject
# Idea
The idea is to give to the software an Event Log describing an industrial project as input, the software is able to extract from it the information needed to build a SitCal BAT (Basic Action Theory). Then we can use the BAT to perform the two main tasks, the Projection Task (verify if a fluent is true after the execution of a sequence of actions) and the Legality Task (verify if a sequence of actions is indeed executable). Since the Projection Task can potentially execute actions that're not executable, it's suggested to check first if a sequence of action is executable through the Legality Task and then to execute the projection task. The idea is that the software can be 
used by a non expert user since in the middleware is used a LLM that's able to translate the user's requests in natural language into indigolog commands.
# Installation
This project is thought to run on WSL. To execute it, install XTerm (on your native OS) and flag "Multiple Windows", select 1 as Display number, flag "Start no client", flag "Disable access control" (do not change the default settings) and save the settings in the default path. You need also to install PySide6:
```bash
pip install PySide6
```
pyswip
```bash
pip install pyswip
```
python-dotenv
```bash
pip install python-dotenv
```
In order to test the prolog file, you need to install swipl, so execute the following commands (I suggest you to install the 9.x.x version): 
```bash
sudo apt-add-repository ppa:swi-prolog/stable
sudo apt-get update
sudo apt-get install swi-prolog
and openai
```
```bash
pip install openai
```
Then go to the [platform.openai.com site](https://platform.openai.com/), log in and create an API KEY, then create in the repo a .env file and insert in the first row the code
```python
OPENAI_API_KEY='<YOUR_API_KEY>'
```
Then you've simple to execute app.py. 
```bash
python3 app.py
```
# Something about the files
The files "easy_level_test.xes", "mid_level_test.xes" and "hard_level_test.xes" are toy files used to avoid the user to download a .xes file that can result too heavy, but you can delete them. Instead the "user_file.xes" cannot be deleted in any case since it's the file used to copy the content of the file selected by the user, so it's rewritten every time the user selects a new .xes file. "easy_level_test.xes" contains the log representing a basic industrial project, if you want to use something more complex, use either the "mid_level_test.xes" or the "hard_level_test.xes" file.
# How to create a log from scratch
Visit bpmn.io and model the bpmn process. Then download what you created and visit bimp, then upload the .bpmn file. Simulate the process and then convert the simulation into a .xes file and modify it how you prefer. (Suggestion: if you need to create cycles and at the same time you need to modify some object, please insert the modification on the cycle branch, not in the box from which the cycle started. Example: findARoom -> RoomAvailable -> (If not) findARoom, insert the object to modify in a new box created on purpose between RoomAvailable and findARoom, not in findARoom, this because otherwise the algorithm will modify that variable also if RoomAvailable doesn't fail). 
# How to change the industrial process
The .xes file represents a specific industrial process. If you want to change the variables the process changes, keep the corresponding .bpmn file in the bpmn folder, transform it into a .xes file (I used ProM for this purpose) and then add manually the objects by following the correct syntax (look at the .xes file in the repository)
# How to test
Before performing reasoning is a good practice to test if the obtained prolog syntax is correct, so append at the end of the create_prolog.pl file a procedure called simulateprocess0 
```prolog
proc(simulateprocess0,[<sequence of actions>]). 
```
Then run the command
```bash
swipl config.pl main.pl
?- main.
```
and, by assumning the procedure syntax is correct, if swipl returns you true after printing the sequence of actions inserted in the procedure, the prolog BAT is correct, otherwise you have to debug it manually. <br><br>N.B. Very unfortunately the second case will verify (in this case I apologize for the inconvenience), so check carefully whether the procedure syntax is correct in the case swipl returns you false.
