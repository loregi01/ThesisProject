import csv
import os
from faker import Faker
import random

data = []

models_available = ['easy_level_model', 'mid_level_model', 'hard_level_model']
model = input(f"Insert the model on which you want to test the software (between {models_available}): ")
while model not in models_available:
    print('Model not available!\n')
    model = input(f"Insert the model on which you want to test the software (between {models_available}): ")
print(f'You\'ve correctly selected the model {model}')

action_list = []
fluent_list = []
if model == 'easy_level_model':
    action_list = ['actionorderreceived', 'actionconfirmorder', 'actionpreparationoftheproductinthewarehouse(Q0)', 'actionconfirmpayment(Q0)', 'actionpreparationofshipment', 'actionorderreadyforshipping(Q0)', 'actionrejectorder(Q0)', 'actionorderrejected']
    fluent_list = ['orderreceived0', 'confirmorder0', 'confirmorder1', 'preparationoftheproductinthewarehouse0', 'preparationofshipment0', 'orderreceived1', 'rejectorder0', 'itemsinwarehouse(Q0)', 'totalprofit(Q0)', 'itemsshipped(Q0)', 'ordersrejected(Q0)', 'confirmpayment0', 'orderreadyforshipping0', 'orderrejected0']
elif model == 'mid_level_model':
    action_list = ['actionreceiveapplication(Q0)', 'actionchecktheprofileskills', 'actionperforminterview(Q0)', 'actionapplicationrejected(Q0)', 'actionrejectapplication', 'actionregistersthecandidateinthesystems', 'actionsendingdocumentation', 'actioncorporateaccountcreation', 'actiontrainingplanning', 'actioncollectionofsigneddocumentation', 'actionconfigurationofworktools', 'actionassignmentofamentor', 'actioninclusioninthepayslip', 'actionitsecurityverification', 'actionorganizationofawelcomemeeting', 'actionconfirmationofonboardingcompletion', 'actiononboardingcompleted(Q0)']
    fluent_list = ['receiveapplication0', 'checktheprofileskills0', 'performinterview0', 'rejectapplication0', 'checktheprofileskills1', 'performinterview1', 'registersthecandidateinthesystems0', 'registersthecandidateinthesystems1', 'registersthecandidateinthesystems2', 'sendingdocumentation0', 'corporateaccountcreation0', 'trainingplanning0', 'collectionofsigneddocumentation0', 'configurationofworktools0', 'assignmentofamentor0', 'organizationofawelcomemeeting0', 'confirmationofonboardingcompletion0', 'applicationrejected(Q0)', 'interviewperformed(Q0)', 'candidateshired(Q0)', 'applicationreceived(Q0)', 'applicationreceived(Q0)', 'interviewperformed(Q0)', 'applicationrejected(Q0)', 'candidateshired(Q0)', 'inclusioninthepayslip0', 'itsecurityverification0', 'onboardingcompleted0']
else:
    action_list = ['actiondevicereceived', 'actionverifywarranty', 'actionsendrepairestimate', 'actioncheckestimationacceptance', 'actionrepairtheproduct(Q0)', 'actionupdateticketstatus', 'actionrepaircarriedout(Q0)', 'actionrepairfailure', 'actionrepairfailed(Q0)', 'actionassistanceticketgeneration(Q0)', 'actionchecksparepartsavailability', 'actiondelaynotification(Q0)']
    fluent_list = ['devicereceived0', 'verifywarranty0', 'sendrepairestimate0', 'checkestimationacceptance0', 'checksparepartsavailability0', 'checkestimationacceptance1', 'checksparepartsavailability1', 'updateticketstatus0', 'checkestimationacceptance2', 'repairfailure0', 'delaynotification0', 'verifywarranty1', 'assistanceticketgeneration0', 'generatedticket(Q0)', 'sparepartsinwarehouse(Q0)', 'repaireditems(Q0)', 'delaynotifications(Q0)', 'repairsfailed(Q0)', 'repairtheproduct0', 'repaircarriedout0', 'repairfailed0']

# Random sentences creation
fake = Faker()
for _ in range(200):
    sentence = str(fake.sentence()) 
    data.append([f"{sentence}","No result"])

# Legality Task questions creation
for _ in range (50):
    selected_actions = []
    num_actions = random.randint(2,5)
    for _ in range (num_actions):
        element = random.choice(action_list)
        if element not in selected_actions:
            element = element.replace("Q0",str(random.randint(0, 10)))
            selected_actions.append(element)
    input_string = ''
    counter = 0
    for elem in selected_actions:
        if counter < len(selected_actions)-1:
            input_string += "\'" + elem + "\'" + ","
        else:
            input_string += "\'" + elem + "\'"
        counter += 1

    question_string = input_string.replace('\'','')
        
    q1 = f"Hi, I would like to understand if the following sequence of actions {question_string} is executable"
    q2 = f"Is the sequence of actions {question_string} executable??"
    parsed_string = input_string.split(',')
    parsed_string = parsed_string[:len(parsed_string)-1]
    counter = 0
    string = ''
    for actions in parsed_string:
        if counter < len(parsed_string)-1:
            string += actions + ','
        else:
            string += actions
        counter += 1

    q3 = f"Can I execute the action {selected_actions[-1]} after executing {string}"
    q4 = f"Considering the sequence {question_string}, can it be completed successfully?"

    data.append([q1,f"(\'legality_task\',[{input_string}])"])
    data.append([q2,f"(\'legality_task\',[{input_string}])"])
    data.append([q3,f"(\'legality_task\',[{input_string}])"])
    data.append([q4,f"(\'legality_task\',[{input_string}])"])

# Projection Task questions creation
for _ in range (50):
    selected_fluent = random.choice(fluent_list)
    selected_fluent = '\'' + selected_fluent + '\''
    selected_actions = []
    num_actions = random.randint(2,5)
    for _ in range (num_actions):
        element = random.choice(action_list)
        if element not in selected_actions:
            element = element.replace("Q0",str(random.randint(0, 10)))
            selected_actions.append(element)

    input_string = ''
    counter = 0
    for elem in selected_actions:
        if counter < len(selected_actions)-1:
            input_string += "\'" + elem + "\'" + ','
        else:
            input_string += "\'" + elem + "\'"
        counter += 1

    q1 = f"Hi, I would like to know whether the fluent {selected_fluent} is true after executing the actions {input_string}"
    q2 = f"Is the fluent {selected_fluent} true if I execute the actions {input_string}"
    q3 = f"The sequence of actions {input_string} guarantees that the fluent {selected_fluent} is true"
    q4 = f"If I execute {input_string}, is it possible to conclude that {selected_fluent} will be true when finished?"

    data.append([q1,f"(\'projection_task\',[{input_string}],{selected_fluent})"])
    data.append([q2,f"(\'projection_task\',[{input_string}],{selected_fluent})"])
    data.append([q3,f"(\'projection_task\',[{input_string}],{selected_fluent})"])
    data.append([q4,f"(\'projection_task\',[{input_string}],{selected_fluent})"])

file_path = 'test/test_csv.csv'
other_file_path = 'test/script_test.py'

with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open(other_file_path, mode='r', encoding='utf-8') as file:
    contenuto = file.readlines()  

contenuto_prepend = [f'action_list = {action_list}\n',  
                     f'fluent_list = {fluent_list}\n']  

contenuto_prepend.extend(contenuto)

with open(other_file_path, mode='w', encoding='utf-8') as file:
    file.writelines(contenuto_prepend)  