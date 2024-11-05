import xml.etree.ElementTree as ET
import numbers

output = {}
inital_values = {}
changes = {}
action_effect = {}

def is_number(value):
    try:
        float(value)  
        return True
    except ValueError:
        return False

def extract_events_and_lifecycle(xes_file):
    tree = ET.parse(xes_file)
    root = tree.getroot()
    ns = {'xes': 'http://www.xes-standard.org/'}

    objects = []
    attributes_in_traces = []

    for trace in root.findall('trace'):
        flow = []
        for event in trace.findall('event'):

            # find the action name
            action = event.find('string[@key="concept:name"]', ns).attrib['value']

            attributes_in_xes = []
            for elem in root.iter():
                if 'key' in elem.attrib:
                    attributes_in_xes.append(elem.attrib['key'])
            
            standard_attributes = ['elementId','resourceId','org:resource','concept:name','processId','lifecycle:transition','time:timestamp','lifecycle:model','LogType','source']

            additional_attributes = []
            for elem in attributes_in_xes:
                if elem not in standard_attributes:
                    additional_attributes.append(elem)

            additional_attributes_with_tag = []
            for elem in root.iter():
                if 'key' in elem.attrib and elem.attrib['key'] in additional_attributes:
                    additional_attributes_with_tag.append((elem.attrib['key'],elem.tag))

            objs = {}
            for elem in additional_attributes_with_tag:
                objs[elem[0]] = event.find(f'{elem[1]}[@key="{elem[0]}"]', ns).attrib['value']
            
            lifecycle = event.find('string[@key="lifecycle:transition"]', ns).attrib['value']

            if len(inital_values) == 0:
                for elem in objs.keys():
                    inital_values[elem] = objs[elem]

            if len(changes) == 0:
                for elem in objs.keys():
                    changes[elem] = objs[elem]
            else:
                for elem in objs.keys():
                    if objs[elem] != changes[elem]:
                        if is_number(objs[elem]):
                            change = int(changes[elem]) - int(objs[elem])
                            if change < 0:
                                action_effect[elem] = f'+{int(objs[elem])-int(changes[elem])}'
                            else:
                                action_effect[elem] = f'-{int(changes[elem])-int(objs[elem])}'
                        else:
                                action_effect[elem] = f'to{objs[elem]}'
                        changes[elem] = objs[elem]

            if len(objects) == 0:
                list_val = []
                for elem in objs.keys():
                    list_val.append(objs[elem])
                objects.append(tuple(list_val))
                
            if not output.get(f'{action}'):
                output[f'{action}'] = ([],[])
            

            if not any(tup[0] == action for tup in flow):
                index = len(flow)-1
                if len(flow) == 0:
                    if 'True' not in output[f'{action}'][0]:
                        output[f'{action}'][0].append('True')
                elif len(flow) >= 1:
                    while index >= 0:
                        if flow[index][1] == 'complete':
                            if not flow[index][0] in output[f'{action}'][0]:
                                output[f'{action}'][0].append(flow[index][0])
                            break
                        index -= 1

            counter = 0
            for elem in objs.keys():
                if objs[elem]!= objects[len(objects)-1][counter] and (f'{elem}' not in output[f'{action}'][1]) and objs[elem] != None:
                    output[f'{action}'][1].append(f'{elem}')
                counter += 1
            
            list_val = []
            for elem in objs.keys():
                list_val.append(objs[elem])
                objects.append(tuple(list_val))
            flow.append((action,lifecycle))

    action_string = ""
    action_list = []
    counter = 0
    for key in output.keys():
        act = key
        act = act.replace(' ','').replace("'","").lower()
        if counter == len(output)-1:
            action_string += act
        else:
            action_string += act + ","
        action_list.append(act)
        counter += 1

    procedure_calculation = ''
    counter = 0
    counter_syntax = 0
    for keys in output.keys():
        action = keys
        pre = output[keys][0]
        eff = output[keys][1]
        action = 'action' + action 
        action = action.replace(' ','').lower()
        if counter_syntax == len(output)-1:
            if len(pre) == 1:
                if pre[0] == 'True':
                    procedure_calculation += '  ' + action + '\n'
                else:
                    if len(eff) == 0:
                        pre[0] = pre[0].replace(' ','').lower()
                        procedure_calculation += f'  if({pre[0]},{action},no_op)\n'
                    else:
                        pre[0] = pre[0].replace(' ','').lower()
                        procedure_calculation += f'  if({pre[0]},{action}(N{counter}),no_op)\n'
                        counter += 1
            else:
                prec = ''
                counter_2 = 0
                for p in pre:
                    p = p.lower()
                    if counter_2 == len(pre)-1:
                        prec += p
                    else:
                        prec += p + ','
                    if len(pre) - 1 - counter_2 >= 2:
                        prec += 'or('
                    counter_2 += 1
                prec += ')' 
                if len(pre)-2 >= 0:
                    prec += ')' * (len(pre)-2)
            counter_syntax += 1
        else:
            if len(pre) == 1:
                if pre[0] == 'True':
                    procedure_calculation += '  ' + action + ',\n'
                else:
                    if len(eff) == 0:
                        pre[0] = pre[0].replace(' ','').lower()
                        procedure_calculation += f'  if({pre[0]},{action},no_op),\n'
                    else:
                        pre[0] = pre[0].replace(' ','').lower()
                        procedure_calculation += f'  if({pre[0]},{action}(N{counter}),no_op),\n'
                        counter += 1
            else:
                prec = ''
                counter_2 = 0
                for p in pre:
                    p = p.lower()
                    if counter_2 == len(pre)-1:
                        prec += p
                    else:
                        prec += p + ','
                    if len(pre) - 1 - counter_2 >= 2:
                        prec += 'or('
                    counter_2 += 1
                prec += ')' 
                if len(pre)-2 >= 0:
                    prec += ')' * (len(pre)-2)
                if pre[0] == 'True':
                    procedure_calculation += '  ' + action + ',\n'
                else:
                    if len(eff) == 0:
                        pre[0] = pre[0].replace(' ','').lower()
                        procedure_calculation += f'  if({prec},{action},no_op),\n'
                    else:
                        pre[0] = pre[0].replace(' ','').lower()
                        procedure_calculation += f'  if({prec},{action}(N{counter}),no_op),\n'
                        counter += 1
            counter_syntax += 1
       
    with open("OCEL_output_automated.txt", "w") as file:
        for key, value in output.items():
            file.write(f"{key}: {value}\n")
        file.write("\n")
        for key, value in inital_values.items():
            file.write(f"{key}: {value}\n")
        file.write("\n")
        for key, value in action_effect.items():
            file.write(f"{key}: {value}\n")

    with open("interactive_program.py", "w") as file:
        file.write(f"# Auto generated program\n")
        file.write(f"while_condition = input(\'When do you want to end the execution of the process? choose between [{action_string}]\')\n")
        file.write(f"list_admitted_inputs = {action_list}\n\n")
        file.write(f"while while_condition not in list_admitted_inputs:\n    ")
        file.write(f"while_condition = input(\'When do you want to end the execution of the process? choose between [{action_string}]\')\n\n")
        file.write("\n")
        file.write(f"# Procedure generated in an automated way\n")
        file.write("procedure = f\'\'\'\n\nproc(simulateprocess, [\nwhile(neg({while_condition}), [\n")
        file.write(f"{procedure_calculation}])]).\'\'\'\n\n")
        file.write("with open(\"create_prolog.pl\", \"a\") as file:\n")
        file.write("    file.write(f\"{procedure}\")")
    return "Check the OCEL_output_automated.txt file for the result"

print(extract_events_and_lifecycle('user_file.xes'))