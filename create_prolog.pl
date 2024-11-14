execute(A, SR) :- ask_execute(A, SR).
exog_occurs(_) :- fail.

max_quantity(100000).
qt(Q) :- max_quantity(M), between(0,M,Q).

prim_fluent(devicereceived0).
prim_fluent(verifywarranty0).
prim_fluent(sendrepairestimate0).
prim_fluent(checkestimationacceptance0).
prim_fluent(checksparepartsavailability0).
prim_fluent(checkestimationacceptance1).
prim_fluent(checksparepartsavailability1).
prim_fluent(updateticketstatus0).
prim_fluent(checkestimationacceptance2).
prim_fluent(repairfailure0).
prim_fluent(delaynotification0).
prim_fluent(verifywarranty1).
prim_fluent(assistanceticketgeneration0).
prim_fluent(generatedticket(Q0)) :- qt(Q0).
prim_fluent(sparepartsinwarehouse(Q0)) :- qt(Q0).
prim_fluent(repaireditems(Q0)) :- qt(Q0).
prim_fluent(delaynotifications(Q0)) :- qt(Q0).
prim_fluent(repairsfailed(Q0)) :- qt(Q0).
prim_fluent(repairtheproduct0).
prim_fluent(repaircarriedout0).
prim_fluent(repairfailed0).

prim_action(actiondevicereceived).
prim_action(actionverifywarranty).
prim_action(actionsendrepairestimate).
prim_action(actioncheckestimationacceptance).
prim_action(actionrepairtheproduct(Q0)) :- qt(Q0).
prim_action(actionupdateticketstatus).
prim_action(actionrepaircarriedout(Q0)) :- qt(Q0).
prim_action(actionrepairfailure).
prim_action(actionrepairfailed(Q0)) :- qt(Q0).
prim_action(actionassistanceticketgeneration(Q0)) :- qt(Q0).
prim_action(actionchecksparepartsavailability).
prim_action(actiondelaynotification(Q0)) :- qt(Q0).

initially(generatedticket(0),true).
initially(sparepartsinwarehouse(30),true).
initially(repaireditems(0),true).
initially(delaynotifications(0),true).
initially(repairsfailed(0),true).

poss(actiondevicereceived,true).
poss(actionverifywarranty,devicereceived0).
poss(actionsendrepairestimate,verifywarranty0).
poss(actioncheckestimationacceptance,sendrepairestimate0).
poss(actionrepairtheproduct(Q0),and(or(checkestimationacceptance0,checksparepartsavailability0),and(sparepartsinwarehouse(Q1),Q1 is Q0 + 1))) :- qt(Q0),qt(Q1).
poss(actionupdateticketstatus,or(checkestimationacceptance1,checksparepartsavailability1)).
poss(actionrepaircarriedout(Q0),and(updateticketstatus0,and(repaireditems(Q1),Q1 is Q0 - 1))) :- qt(Q0),qt(Q1).
poss(actionrepairfailure,checkestimationacceptance2).
poss(actionrepairfailed(Q0),and(or(repairfailure0,delaynotification0),and(repairsfailed(Q1),Q1 is Q0 - 1))) :- qt(Q0),qt(Q1).
poss(actionassistanceticketgeneration(Q0),and(verifywarranty1,and(generatedticket(Q1),Q1 is Q0 - 1))) :- qt(Q0),qt(Q1).
poss(actionchecksparepartsavailability,assistanceticketgeneration0).
poss(actiondelaynotification(Q0),and(checksparepartsavailability0,and(delaynotifications(Q1),Q1 is Q0 - 1))) :- qt(Q0),qt(Q1).

causes_val(actiondevicereceived,devicereceived0,true,true).
causes_val(actionverifywarranty,devicereceived0,false,true).
causes_val(actionverifywarranty,verifywarranty0,true,true).
causes_val(actionverifywarranty,verifywarranty1,true,true).
causes_val(actionsendrepairestimate,verifywarranty0,false,true).
causes_val(actionsendrepairestimate,sendrepairestimate0,true,true).
causes_val(actioncheckestimationacceptance,sendrepairestimate0,false,true).
causes_val(actioncheckestimationacceptance,checkestimationacceptance0,true,true).
causes_val(actioncheckestimationacceptance,checkestimationacceptance1,true,true).
causes_val(actioncheckestimationacceptance,checkestimationacceptance2,true,true).
causes_val(actionrepairtheproduct(Q0),checkestimationacceptance0,false,true) :- qt(Q0).
causes_val(actionrepairtheproduct(Q0),checksparepartsavailability0,false,true) :- qt(Q0).
causes_val(actionrepairtheproduct(Q0),repairtheproduct0,true,true) :- qt(Q0).
causes_val(actionrepairtheproduct(Q0),sparepartsinwarehouse(Q0),true,true) :- qt(Q0).
causes_val(actionrepairtheproduct(Q0),sparepartsinwarehouse(Q1),false,Q0 \= Q1) :- qt(Q0), qt(Q1).
causes_val(actionupdateticketstatus,checkestimationacceptance1,false,true).
causes_val(actionupdateticketstatus,checksparepartsavailability1,false,true).
causes_val(actionupdateticketstatus,updateticketstatus0,true,true).
causes_val(actionrepaircarriedout(Q0),updateticketstatus0,false,true) :- qt(Q0).
causes_val(actionrepaircarriedout(Q0),repaircarriedout0,true,true) :- qt(Q0).
causes_val(actionrepaircarriedout(Q0),repaireditems(Q0),true,true) :- qt(Q0).
causes_val(actionrepaircarriedout(Q0),repaireditems(Q1),false,Q0 \= Q1) :- qt(Q0), qt(Q1).
causes_val(actionrepairfailure,checkestimationacceptance2,false,true).
causes_val(actionrepairfailure,repairfailure0,true,true).
causes_val(actionrepairfailed(Q0),repairfailure0,false,true) :- qt(Q0).
causes_val(actionrepairfailed(Q0),delaynotification0,false,true) :- qt(Q0).
causes_val(actionrepairfailed(Q0),repairfailed0,true,true) :- qt(Q0).
causes_val(actionrepairfailed(Q0),repairsfailed(Q0),true,true) :- qt(Q0).
causes_val(actionrepairfailed(Q0),repairsfailed(Q1),false,Q0 \= Q1) :- qt(Q0), qt(Q1).
causes_val(actionassistanceticketgeneration(Q0),verifywarranty1,false,true) :- qt(Q0).
causes_val(actionassistanceticketgeneration(Q0),assistanceticketgeneration0,true,true) :- qt(Q0).
causes_val(actionassistanceticketgeneration(Q0),generatedticket(Q0),true,true) :- qt(Q0).
causes_val(actionassistanceticketgeneration(Q0),generatedticket(Q1),false,Q0 \= Q1) :- qt(Q0), qt(Q1).
causes_val(actionchecksparepartsavailability,assistanceticketgeneration0,false,true).
causes_val(actionchecksparepartsavailability,checksparepartsavailability0,true,true).
causes_val(actionchecksparepartsavailability,checksparepartsavailability1,true,true).
causes_val(actionchecksparepartsavailability,checksparepartsavailability2,true,true).
causes_val(actiondelaynotification(Q0),checksparepartsavailability0,false,true) :- qt(Q0).
causes_val(actiondelaynotification(Q0),delaynotification0,true,true) :- qt(Q0).
causes_val(actiondelaynotification(Q0),delaynotifications(Q0),true,true) :- qt(Q0).
causes_val(actiondelaynotification(Q0),delaynotifications(Q1),false,Q0 \= Q1) :- qt(Q0), qt(Q1).
