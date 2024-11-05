# Auto generated program
while_condition = input('When do you want to end the execution of the process? choose between [orderreceived,confirmorder,preparationoftheproductinthewarehouse,confirmpayment,preparationofshipment,orderreadyforshipping,rejectorder,orderrejected]')
list_admitted_inputs = ['orderreceived', 'confirmorder', 'preparationoftheproductinthewarehouse', 'confirmpayment', 'preparationofshipment', 'orderreadyforshipping', 'rejectorder', 'orderrejected']

while while_condition not in list_admitted_inputs:
    while_condition = input('When do you want to end the execution of the process? choose between [orderreceived,confirmorder,preparationoftheproductinthewarehouse,confirmpayment,preparationofshipment,orderreadyforshipping,rejectorder,orderrejected]')


# Procedure generated in an automated way
procedure = f'''

proc(simulateprocess, [
while(neg({while_condition}), [
  actionorderreceived,
  if(orderreceived,actionconfirmorder,no_op),
  if(confirmorder,actionpreparationoftheproductinthewarehouse(N0),no_op),
  if(confirmorder,actionconfirmpayment(N1),no_op),
  if(preparationoftheproductinthewarehouse,actionpreparationofshipment,no_op),
  if(preparationofshipment,actionorderreadyforshipping(N2),no_op),
  if(orderreceived,actionrejectorder(N3),no_op),
  if(rejectorder,actionorderrejected,no_op)
])]).'''

with open("create_prolog.pl", "a") as file:
    file.write(f"{procedure}")