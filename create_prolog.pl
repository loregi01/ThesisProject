execute(A, SR) :- ask_execute(A, SR).
exog_occurs(_) :- fail.

max_quantity(100000).
qt(Q) :- max_quantity(M), between(0,M,Q).

prim_fluent(orderreceived).
prim_fluent(confirmorder).
prim_fluent(preparationoftheproductinthewarehouse).
prim_fluent(confirmpayment).
prim_fluent(preparationofshipment).
prim_fluent(orderreadyforshipping).
prim_fluent(rejectorder).
prim_fluent(orderrejected).
prim_fluent(itemsinwarehouse(Q)) :- qt(Q).
prim_fluent(totalprofit(Q)) :- qt(Q).
prim_fluent(itemsshipped(Q)) :- qt(Q).
prim_fluent(ordersrejected(Q)) :- qt(Q).

prim_action(actionorderreceived).
prim_action(actionconfirmorder).
prim_action(actionpreparationoftheproductinthewarehouse(Q0)) :- qt(Q0).
prim_action(actionconfirmpayment(Q0)) :- qt(Q0).
prim_action(actionpreparationofshipment).
prim_action(actionorderreadyforshipping(Q0)) :- qt(Q0).
prim_action(actionrejectorder(Q0)) :- qt(Q0).
prim_action(actionorderrejected).

initially(itemsinwarehouse(10),true).
initially(totalprofit(0),true).
initially(itemsshipped(0),true).
initially(ordersrejected(0),true).

poss(actionorderreceived,true).
poss(actionconfirmorder,orderreceived).
poss(actionpreparationoftheproductinthewarehouse(Q0),and(confirmorder,and(itemsinwarehouse(Q1),Q1 is Q0 + 1))) :- qt(Q0),qt(Q1).
poss(actionconfirmpayment(Q0),and(confirmorder,and(totalprofit(Q1),Q1 is Q0 - 10))) :- qt(Q0),qt(Q1).
poss(actionpreparationofshipment,preparationoftheproductinthewarehouse).
poss(actionorderreadyforshipping(Q0),and(preparationofshipment,and(itemsshipped(Q1),Q1 is Q0 - 1))) :- qt(Q0),qt(Q1).
poss(actionrejectorder(Q0),and(orderreceived,and(ordersrejected(Q1),Q1 is Q0 - 1))) :- qt(Q0),qt(Q1).
poss(actionorderrejected,rejectorder).

causes_val(actionorderreceived,orderreceived,true,true).
causes_val(actionconfirmorder,orderreceived,false,true).
causes_val(actionconfirmorder,confirmorder,true,true).
causes_val(actionpreparationoftheproductinthewarehouse(Q0),confirmorder,false,true) :- qt(Q0).
causes_val(actionpreparationoftheproductinthewarehouse(Q0),preparationoftheproductinthewarehouse,true,true) :- qt(Q0).
causes_val(actionpreparationoftheproductinthewarehouse(Q0),itemsinwarehouse(Q0),true,true) :- qt(Q0).
causes_val(actionpreparationoftheproductinthewarehouse(Q0),itemsinwarehouse(Q1),false,Q0 \= Q1) :- qt(Q0), qt(Q1).
causes_val(actionconfirmpayment(Q0),confirmorder,false,true) :- qt(Q0).
causes_val(actionconfirmpayment(Q0),confirmpayment,true,true) :- qt(Q0).
causes_val(actionconfirmpayment(Q0),totalprofit(Q0),true,true) :- qt(Q0).
causes_val(actionconfirmpayment(Q0),totalprofit(Q1),false,Q0 \= Q1) :- qt(Q0), qt(Q1).
causes_val(actionpreparationofshipment,preparationoftheproductinthewarehouse,false,true).
causes_val(actionpreparationofshipment,preparationofshipment,true,true).
causes_val(actionorderreadyforshipping(Q0),preparationofshipment,false,true) :- qt(Q0).
causes_val(actionorderreadyforshipping(Q0),orderreadyforshipping,true,true) :- qt(Q0).
causes_val(actionorderreadyforshipping(Q0),itemsshipped(Q0),true,true) :- qt(Q0).
causes_val(actionorderreadyforshipping(Q0),itemsshipped(Q1),false,Q0 \= Q1) :- qt(Q0), qt(Q1).
causes_val(actionrejectorder(Q0),orderreceived,false,true) :- qt(Q0).
causes_val(actionrejectorder(Q0),rejectorder,true,true) :- qt(Q0).
causes_val(actionrejectorder(Q0),ordersrejected(Q0),true,true) :- qt(Q0).
causes_val(actionrejectorder(Q0),ordersrejected(Q1),false,Q0 \= Q1) :- qt(Q0), qt(Q1).
causes_val(actionorderrejected,rejectorder,false,true).
causes_val(actionorderrejected,orderrejected,true,true).


proc(simulateprocess, [
while(neg(rejectorder), [

                                    actionorderreceived,
  if(orderreceived,actionconfirmorder,no_op),
  if(confirmorder,actionpreparationoftheproductinthewarehouse(N0),no_op),
  if(confirmorder,actionconfirmpayment(N1),no_op),
  if(preparationoftheproductinthewarehouse,actionpreparationofshipment,no_op),
  if(preparationofshipment,actionorderreadyforshipping(N2),no_op),
  if(orderreceived,actionrejectorder(N3),no_op),
  if(rejectorder,actionorderrejected,no_op)
])]).