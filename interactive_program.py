# Auto generated program
input_string = "['orderreceived','confirmorder','itemsinwarehouse(Q)','preparationoftheproductinthewarehouse','totalprofit(Q)','confirmpayment','preparationofshipment','itemsshipped(Q)','orderreadyforshipping','ordersrejected(Q)','rejectorder','orderrejected']"
action_list=['actionorderreceived', 'actionconfirmorder', 'actionpreparationoftheproductinthewarehouse', 'actionconfirmpayment', 'actionpreparationofshipment', 'actionorderreadyforshipping', 'actionrejectorder', 'actionorderrejected']
procedure_calculation = '''actionorderreceived,
  if(orderreceived,actionconfirmorder,no_op),
  if(confirmorder,actionpreparationoftheproductinthewarehouse(N0),no_op),
  if(confirmorder,actionconfirmpayment(N1),no_op),
  if(preparationoftheproductinthewarehouse,actionpreparationofshipment,no_op),
  if(preparationofshipment,actionorderreadyforshipping(N2),no_op),
  if(orderreceived,actionrejectorder(N3),no_op),
  if(rejectorder,actionorderrejected,no_op)
'''