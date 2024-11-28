action_list = ['actionorderreceived', 'actionconfirmorder', 'actionpreparationoftheproductinthewarehouse(Q0)', 'actionconfirmpayment(Q0)', 'actionpreparationofshipment', 'actionorderreadyforshipping(Q0)', 'actionrejectorder(Q0)', 'actionorderrejected']
fluent_list = ['orderreceived0', 'confirmorder0', 'confirmorder1', 'preparationoftheproductinthewarehouse0', 'preparationofshipment0', 'orderreceived1', 'rejectorder0', 'itemsinwarehouse(Q0)', 'totalprofit(Q0)', 'itemsshipped(Q0)', 'ordersrejected(Q0)', 'confirmpayment0', 'orderreadyforshipping0', 'orderrejected0']
import os
from openai import OpenAI
from dotenv import load_dotenv
import csv

load_dotenv()

counter_total = 0
counter_success = 0

file_path = 'test/test_csv.csv'

with open('test/log_test.txt', mode='w', encoding='utf-8') as file:
    file.write("")

with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)  
    
    for riga in reader:  
        counter_total += 1
        print(f"Processing question: {counter_total}")
        question = riga[0]
        expected_answer = riga[1]

        OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

        client = OpenAI(
                api_key = OPENAI_API_KEY,
        )

        completion = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
                {"role": "system", "content": f'''Act as a translator from natural language questions to tuples to execute queries in an indigolog reasoner. 
                 I want to understand if the user wants to perform the legality task or the projection task. We're talking about
                 legality task if the user wants to understand if a sequence of actions is executable, we're talking about 
                 projection task if the user wants to understand if a fluent is true after the execution of a sequence of actions.

                 - In case of legality task, the output must be ONLY the following: ('legality_task',['action_name_1','action_name_2',...,'action_name_n']), no explanations or
                   additional text.
                 - In case of projection task, the output must be ONLY the following: ('projection_task',['action_name_1','action_name_2',...,'action_name_n'],'fluent_name'), no explanations or
                   additional text.
                 - If you don't detect neither legality task nor projection task, the output must be ONLY the following: \'No result\', no explanations or
                   additional text.
                   
                   Examples: 
                   - Input (Natural language question): Is the sequence of actions actionpreparationoftheproductinthewarehouse(0),actionpreparationofshipment executable??
                     Output (Translated tuple): ('legality_task',['actionpreparationoftheproductinthewarehouse(0)','actionpreparationofshipment'])
                   - Input (Natural language question): Is the fluent orderreceived0 true after executing the actions actionorderreceived, actionconfirmorder
                     Output (Translated tuple): ('projection_task',['actionorderreceived','actionconfirmorder'],'orderreceived0')
                
                   The action name MUST belong to the list {action_list}, you cannot return to me something that's 
                   not in the list in any case, and in case of params, you've to substitute the parameter in the list with the params inserted by the user.
                   The fluent name MUST belong to the list {fluent_list}, you cannot return to me something that's 
                   not in the list in any case, and in case of params, you've to substitute the parameter in the list with the params inserted by the user. 
                   '''},
                {"role": "user", "content": f'''You need to help me to analyze the following phrase: {question}.'''},
            ]
            )
        
        output = completion.choices[0].message.content.strip()

        result = None
        if expected_answer == output:
            print("Result: Success")
            result = "Success"
            counter_success += 1
        else:
            print("Result: Fail")
            result = "Fail"

        with open('test/log_test.txt', mode='a', encoding='utf-8') as file:
            file.write("****\n")
            file.write(f"Processed question: {counter_total}\n")
            file.write(f"Question: {question}\n")
            file.write(f"Expected Output: {expected_answer}\n")
            file.write(f"Obtained Output: {output}\n")
            file.write(f"Result: {result}\n\n")

with open('test/log_test.txt', mode='a', encoding='utf-8') as file:
    accuracy = counter_success/counter_total*100
    file.write(f"Accuracy: {accuracy}%")
    print(f"Accuracy: {accuracy}%")

        
