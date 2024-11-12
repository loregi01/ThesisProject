execute(A, SR) :- ask_execute(A, SR).
exog_occurs(_) :- fail.

max_quantity(100000).
qt(Q) :- max_quantity(M), between(0,M,Q).

prim_fluent(orderreceived0).
prim_fluent(confirmorder0).
prim_fluent(confirmorder1).
prim_fluent(preparationoftheproductinthewarehouse0).
prim_fluent(preparationofshipment0).
prim_fluent(orderreceived1).
prim_fluent(rejectorder0).
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
poss(actionconfirmorder,orderreceived0).
poss(actionpreparationoftheproductinthewarehouse(Q0),and(confirmorder0,and(itemsinwarehouse(Q1),Q1 is Q0 + 1))) :- qt(Q0),qt(Q1).
poss(actionconfirmpayment(Q0),and(confirmorder1,and(totalprofit(Q1),Q1 is Q0 - 10))) :- qt(Q0),qt(Q1).
poss(actionpreparationofshipment,preparationoftheproductinthewarehouse0).
poss(actionorderreadyforshipping(Q0),and(preparationofshipment0,and(itemsshipped(Q1),Q1 is Q0 - 1))) :- qt(Q0),qt(Q1).
poss(actionrejectorder(Q0),and(orderreceived1,and(ordersrejected(Q1),Q1 is Q0 - 1))) :- qt(Q0),qt(Q1).
poss(actionorderrejected,rejectorder0).

causes_val(actionorderreceived,orderreceived0,true,true).
causes_val(actionorderreceived,orderreceived1,true,true).
causes_val(actionconfirmorder,orderreceived0,false,true).
causes_val(actionconfirmorder,confirmorder0,true,true).
causes_val(actionconfirmorder,confirmorder1,true,true).
causes_val(actionpreparationoftheproductinthewarehouse(Q0),confirmorder0,false,true) :- qt(Q0).
causes_val(actionpreparationoftheproductinthewarehouse(Q0),preparationoftheproductinthewarehouse0,true,true) :- qt(Q0).
causes_val(actionpreparationoftheproductinthewarehouse(Q0),itemsinwarehouse(Q0),true,true) :- qt(Q0).
causes_val(actionpreparationoftheproductinthewarehouse(Q0),itemsinwarehouse(Q1),false,Q0 \= Q1) :- qt(Q0), qt(Q1).
causes_val(actionconfirmpayment(Q0),confirmorder1,false,true) :- qt(Q0).
causes_val(actionconfirmpayment(Q0),totalprofit(Q0),true,true) :- qt(Q0).
causes_val(actionconfirmpayment(Q0),totalprofit(Q1),false,Q0 \= Q1) :- qt(Q0), qt(Q1).
causes_val(actionpreparationofshipment,preparationoftheproductinthewarehouse0,false,true).
causes_val(actionpreparationofshipment,preparationofshipment0,true,true).
causes_val(actionorderreadyforshipping(Q0),preparationofshipment0,false,true) :- qt(Q0).
causes_val(actionorderreadyforshipping(Q0),itemsshipped(Q0),true,true) :- qt(Q0).
causes_val(actionorderreadyforshipping(Q0),itemsshipped(Q1),false,Q0 \= Q1) :- qt(Q0), qt(Q1).
causes_val(actionrejectorder(Q0),orderreceived1,false,true) :- qt(Q0).
causes_val(actionrejectorder(Q0),rejectorder0,true,true) :- qt(Q0).
causes_val(actionrejectorder(Q0),ordersrejected(Q0),true,true) :- qt(Q0).
causes_val(actionrejectorder(Q0),ordersrejected(Q1),false,Q0 \= Q1) :- qt(Q0), qt(Q1).
causes_val(actionorderrejected,rejectorder0,false,true).
