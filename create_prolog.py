import ast

with open('OCEL_output_automated.txt', 'r') as file:
    content = file.read()

content = content.split('\n')
content_correct = []
for elem in content:
    if elem != '':
        content_correct.append(elem)

fluents = []
prim_fluents = []
for elem in content_correct:
    elem = elem.split(':')
    elem[1] = elem[1].replace(' ','')
    if elem[0] not in fluents:
        fluents.append(elem[0])
        elem[0] = elem[0].replace(' ','')
        elem[0] = elem[0].lower()
        if isinstance(eval(elem[1]),tuple):
            new_fluent = f'prim_fluent({elem[0]}).'
            prim_fluents.append(new_fluent)
        else:
            new_fluent = f'prim_fluent({elem[0]}(Q)) :- qt(Q).'
            prim_fluents.append(new_fluent)

actions = []
prim_actions = []
for elem in content_correct:
    elem = elem.split(':')
    elem[1] = elem[1].replace(' ','')
    if elem[0] not in actions and isinstance(eval(elem[1]),tuple):
        actions.append(elem[0])
        elem[0] = elem[0].replace(' ','')
        elem[0] = elem[0].lower()
        elem[0] = 'action'+elem[0]
        tupl = ast.literal_eval(elem[1])
        if tupl[1] == []:
            new_action = f'prim_action({elem[0]}).'
            prim_actions.append(new_action)
        else:
            counter = 0
            args = '('
            typing = ''
            for elems in tupl[1]:
                args += f'Q{counter}'
                if counter == len(tupl[1])-1:
                    typing += f'qt(Q{counter})'
                else:
                    typing += f'qt(Q{counter}),'
                counter += 1
            args += ')'
            new_action = f'prim_action({elem[0]}{args}) :- {typing}.'
            prim_actions.append(new_action)

# Chiedere come inizializzare initially (in questo caso items(Q) = true e non items = Q)
initially = []
for elem in content_correct:
    elem = elem.split(':')
    elem[1] = elem[1].replace(' ','')
    if not isinstance(eval(elem[1]),tuple) and (elem[1][0] != '+' and elem[1][0] != '-' and elem[1][0] != 't'):
        elem[0] = elem[0].lower()
        new_init = f'initially({elem[0]}({elem[1]}),true).'
        initially.append(new_init)

poss = []
for elem in content_correct:
    elem = elem.split(':')
    elem[1] = elem[1].replace(' ','')
    if isinstance(eval(elem[1]),tuple):
        elem[0] = elem[0].replace(' ','')
        elem[0] = elem[0].lower()
        elem[0] = 'action'+elem[0]
        tupl = ast.literal_eval(elem[1])
        if tupl[1] == []:
            if len(tupl[0]) == 1:
                for pre in tupl[0]:
                    pre = pre.lower()
                    new_poss = f'poss({elem[0]},{pre}).'
                poss.append(new_poss)
            else:
                preconditions = 'or('
                counter = 0
                for pre in tupl[0]:
                    pre = pre.lower()
                    if counter != len(tupl[0])-1:
                        preconditions+=pre + ','
                    else:
                        preconditions+=pre + ')'
                    if len(tupl[0]) - 1 - counter >= 2:
                        prec += 'or('

                if len(tupl[0])-2 >= 0:
                    preconditions += ')' * (len(tupl[0])-2)
                new_poss = f'poss({elem[0]},{preconditions}).'
                poss.append(new_poss)
        else:
            counter = 0
            args = '('
            typing = ''
            for elems in tupl[1]:
                args += f'Q{counter}'
                counter += 1
            args += ')'
            new_action = f'{elem[0]}{args}'
            
            prec = ''
            if len(tupl[0]) == 1:
                for pre in tupl[0]:
                    pre = pre.lower()
                    prec = pre
            else:
                prec += 'or('
                counter = 0
                for pre in tupl[0]:
                    pre = pre.lower()
                    if counter == len(tupl[0])-1:
                        prec += pre
                    else:
                        prec += pre + ','
                    if len(tupl[0]) - 1 - counter >= 2:
                        prec += 'or('
                    counter += 1
                
                prec += ')' 
                if len(tupl[0])-2 >= 0:
                    prec += ')' * (len(tupl[0])-2)
            
            mods = {}
            for elems in content_correct:
                elems = elems.split(':')
                elems[1] = elems[1].replace(' ','')
                if elems[1][0] == '+':
                    mods[elems[0]] = elems[1]
                if elems[1][0] == '-':
                    mods[elems[0]] = elems[1] 
                if elems[1][0] == 't':
                    mods[elems[0]] = elems[1]
            
            cond1 = ''
            counter = 0
            for eff in tupl[1]:
                if counter == len(tupl[1])-1:
                    cond1 += eff.lower() + f'(Q{counter+1})'
                else:
                    cond1 += eff.lower() + f'(Q{counter+1}),'
                counter += 1

            cond2 = ''
            counter = 0
            for eff in tupl[1]:
                if mods[eff][0] == '-' or mods[eff][0] == '+':
                    if mods[eff][0] == '-':
                        cond2 = f'Q{counter+1} is Q0 + {mods[eff][1:]}'
                    else:
                        cond2 = f'Q{counter+1} is Q0 - {mods[eff][1:]}'
                else:
                    # verificare come si può cambiare la condizione bool (dovrei scrivere was al posto di is)
                    cond2 = f'Q{counter+1} is {mods[tupl[1][0]][1:]}'
                counter += 1
            
            final_condition = f'and({prec},and({cond1},{cond2}))'
            typing = 'qt(Q0),'
            counter = 0
            for eff in tupl[1]:
                if counter == len(tupl[1])-1:
                    typing += f'qt(Q{counter+1}).'
                else:
                    typing += f'qt(Q{counter+1}),' 
                counter += 1
            new_poss = f'poss({elem[0]}(Q0),{final_condition}) :- {typing}'
            poss.append(new_poss)

causes_val = []
for elem in content_correct:
    elem = elem.split(':')
    elem[1] = elem[1].replace(' ','')
    if isinstance(eval(elem[1]),tuple):
        action = 'action'+elem[0].replace(' ','').lower()
        tupl = ast.literal_eval(elem[1])
        eff = tupl[1]
        pre = tupl[0]
        if len(eff) > 0:
            counter = 0
            action += '('
            for vars in eff:
                if counter == len(eff)-1:
                    action += f'Q{counter}'
                else:
                    action += f'Q{counter},'
                counter += 1
            action += ')'
            
        for flu in pre:
            flu = flu.lower()
            if len(eff) == 0:
                if flu != 'true':
                    new_causes_val = f'causes_val({action},{flu},false,true).'
                    causes_val.append(new_causes_val)
            else:
                if flu != 'true':
                    counter = 0
                    typing = ''
                    for vars in eff:
                        if counter == len(eff)-1:
                            typing += f'qt(Q{counter}).'
                        else:
                            typing += f'qt(Q{counter}), '
                        counter += 1
                    new_causes_val = f'causes_val({action},{flu},false,true) :- {typing}' 
                    causes_val.append(new_causes_val)

        flu = elem[0].replace(' ','').lower()
        if len(eff) == 0:
            new_causes_val = f'causes_val({action},{flu},true,true).'
            causes_val.append(new_causes_val)
        else:
            typing = ''
            counter = 0
            for vars in eff:
                if counter == len(eff)-1:
                    typing += f'qt(Q{counter}).'
                else:
                    typing += f'qt(Q{counter}), '
            new_causes_val = f'causes_val({action},{flu},true,true) :- {typing}'
            causes_val.append(new_causes_val)

        if len(eff) == 0:
            counter = 0
            for vars in eff:
                flu = f'{vars.lower()}(Q{counter})' 
                new_causes_val = f'causes_val({action},{flu},true,true).'
                causes_val.append(new_causes_val)
                counter += 1
        else:
            counter = 0
            for vars in eff:
                flu = f'{vars.lower()}(Q{counter})' 
                new_causes_val = f'causes_val({action},{flu},true,true) :- qt(Q{counter}).'
                causes_val.append(new_causes_val)
                counter += 1

        if len(eff) == 0:
            counter = 0
            for vars in eff:
                var_num = counter + len(eff)
                flu = f'{vars.lower()}(Q{var_num})' 
                cond = f'Q{counter} \= Q{var_num}'
                new_causes_val = f'causes_val({action},{flu},false,{cond}).'
                causes_val.append(new_causes_val)
                counter += 1
        else:
            counter = 0
            for vars in eff:
                var_num = counter + len(eff)
                flu = f'{vars.lower()}(Q{var_num})' 
                cond = f'Q{counter} \= Q{var_num}'
                new_causes_val = f'causes_val({action},{flu},false,{cond}) :- qt(Q{counter}), qt(Q{var_num}).'
                causes_val.append(new_causes_val)
                counter += 1

with open("create_prolog.pl", "w") as file:
    file.write('execute(A, SR) :- ask_execute(A, SR).\n')
    file.write('exog_occurs(_) :- fail.\n\n')
    file.write('max_quantity(100000).\n')
    file.write('qt(Q) :- max_quantity(M), between(0,M,Q).\n\n')
    for elem in prim_fluents:
        file.write(elem)
        file.write('\n')
    file.write('\n')
    for elem in prim_actions:
        file.write(elem)
        file.write('\n')
    file.write('\n')
    for elem in initially:
        file.write(elem)
        file.write('\n')
    file.write('\n')
    for elem in poss:
        file.write(elem)
        file.write('\n')
    file.write('\n')
    for elem in causes_val:
        file.write(elem)
        file.write('\n')