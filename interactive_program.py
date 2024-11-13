# Auto generated program
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
input_string = "['orderreceived0', 'confirmorder0', 'confirmorder1', 'preparationoftheproductinthewarehouse0', 'preparationofshipment0', 'orderreceived1', 'rejectorder0', 'itemsinwarehouse', 'totalprofit', 'itemsshipped', 'ordersrejected', 'confirmpayment0', 'orderreadyforshipping0', 'orderrejected0']"
