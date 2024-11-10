execute(A, SR) :- ask_execute(A, SR).
exog_occurs(_) :- fail.

max_quantity(100000).
qt(Q) :- max_quantity(M), between(0,M,Q).

prim_fluent(receiveapplication0).
prim_fluent(checktheprofileskills0).
prim_fluent(performinterview0).
prim_fluent(rejectapplication0).
prim_fluent(checktheprofileskills1).
prim_fluent(performinterview1).
prim_fluent(registersthecandidateinthesystems0).
prim_fluent(registersthecandidateinthesystems1).
prim_fluent(registersthecandidateinthesystems2).
prim_fluent(sendingdocumentation0).
prim_fluent(corporateaccountcreation0).
prim_fluent(trainingplanning0).
prim_fluent(collectionofsigneddocumentation0).
prim_fluent(configurationofworktools0).
prim_fluent(assignmentofamentor0).
prim_fluent(organizationofawelcomemeeting0).
prim_fluent(confirmationofonboardingcompletion0).
prim_fluent(applicationrejected(Q)) :- qt(Q).
prim_fluent(interviewperformed(Q)) :- qt(Q).
prim_fluent(candidateshired(Q)) :- qt(Q).
prim_fluent(applicationreceived(Q)) :- qt(Q).
prim_fluent(applicationreceived(Q)) :- qt(Q).
prim_fluent(interviewperformed(Q)) :- qt(Q).
prim_fluent(applicationrejected(Q)) :- qt(Q).
prim_fluent(candidateshired(Q)) :- qt(Q).

prim_action(actionreceiveapplication(Q0)) :- qt(Q0).
prim_action(actionchecktheprofileskills).
prim_action(actionperforminterview(Q0)) :- qt(Q0).
prim_action(actionapplicationrejected(Q0)) :- qt(Q0).
prim_action(actionrejectapplication).
prim_action(actionregistersthecandidateinthesystems).
prim_action(actionsendingdocumentation).
prim_action(actioncorporateaccountcreation).
prim_action(actiontrainingplanning).
prim_action(actioncollectionofsigneddocumentation).
prim_action(actionconfigurationofworktools).
prim_action(actionassignmentofamentor).
prim_action(actioninclusioninthepayslip).
prim_action(actionitsecurityverification).
prim_action(actionorganizationofawelcomemeeting).
prim_action(actionconfirmationofonboardingcompletion).
prim_action(actiononboardingcompleted(Q0)) :- qt(Q0).

initially(applicationrejected(0),true).
initially(interviewperformed(0),true).
initially(candidateshired(0),true).
initially(applicationreceived(0),true).

poss(actionreceiveapplication(Q0),and(true,and(applicationreceived(Q1),Q1 is Q0 - 1))) :- qt(Q0),qt(Q1).
poss(actionchecktheprofileskills,receiveapplication0).
poss(actionperforminterview(Q0),and(checktheprofileskills0,and(interviewperformed(Q1),Q1 is Q0 - 1))) :- qt(Q0),qt(Q1).
poss(actionapplicationrejected(Q0),and(or(performinterview0,rejectapplication0),and(applicationrejected(Q1),Q1 is Q0 - 1))) :- qt(Q0),qt(Q1).
poss(actionrejectapplication,checktheprofileskills1).
poss(actionregistersthecandidateinthesystems,performinterview1).
poss(actionsendingdocumentation,registersthecandidateinthesystems0).
poss(actioncorporateaccountcreation,registersthecandidateinthesystems1).
poss(actiontrainingplanning,registersthecandidateinthesystems2).
poss(actioncollectionofsigneddocumentation,sendingdocumentation0).
poss(actionconfigurationofworktools,corporateaccountcreation0).
poss(actionassignmentofamentor,trainingplanning0).
poss(actioninclusioninthepayslip,collectionofsigneddocumentation0).
poss(actionitsecurityverification,configurationofworktools0).
poss(actionorganizationofawelcomemeeting,assignmentofamentor0).
poss(actionconfirmationofonboardingcompletion,organizationofawelcomemeeting0).
poss(actiononboardingcompleted(Q0),and(confirmationofonboardingcompletion0,and(candidateshired(Q1),Q1 is Q0 - 1))) :- qt(Q0),qt(Q1).

causes_val(actionreceiveapplication(Q0),receiveapplication0,true,true) :- qt(Q0).
causes_val(actionreceiveapplication(Q0),applicationreceived(Q0),true,true) :- qt(Q0).
causes_val(actionreceiveapplication(Q0),applicationreceived(Q1),false,Q0 \= Q1) :- qt(Q0), qt(Q1).
causes_val(actionchecktheprofileskills,receiveapplication0,false,true).
causes_val(actionchecktheprofileskills,checktheprofileskills0,true,true).
causes_val(actionchecktheprofileskills,checktheprofileskills1,true,true).
causes_val(actionperforminterview(Q0),checktheprofileskills0,false,true) :- qt(Q0).
causes_val(actionperforminterview(Q0),performinterview0,true,true) :- qt(Q0).
causes_val(actionperforminterview(Q0),performinterview1,true,true) :- qt(Q0).
causes_val(actionperforminterview(Q0),interviewperformed(Q0),true,true) :- qt(Q0).
causes_val(actionperforminterview(Q0),interviewperformed(Q1),false,Q0 \= Q1) :- qt(Q0), qt(Q1).
causes_val(actionapplicationrejected(Q0),performinterview0,false,true) :- qt(Q0).
causes_val(actionapplicationrejected(Q0),rejectapplication0,false,true) :- qt(Q0).
causes_val(actionapplicationrejected(Q0),applicationrejected(Q0),true,true) :- qt(Q0).
causes_val(actionapplicationrejected(Q0),applicationrejected(Q1),false,Q0 \= Q1) :- qt(Q0), qt(Q1).
causes_val(actionrejectapplication,checktheprofileskills1,false,true).
causes_val(actionrejectapplication,rejectapplication0,true,true).
causes_val(actionregistersthecandidateinthesystems,performinterview1,false,true).
causes_val(actionregistersthecandidateinthesystems,registersthecandidateinthesystems0,true,true).
causes_val(actionregistersthecandidateinthesystems,registersthecandidateinthesystems1,true,true).
causes_val(actionregistersthecandidateinthesystems,registersthecandidateinthesystems2,true,true).
causes_val(actionsendingdocumentation,registersthecandidateinthesystems0,false,true).
causes_val(actionsendingdocumentation,sendingdocumentation0,true,true).
causes_val(actioncorporateaccountcreation,registersthecandidateinthesystems1,false,true).
causes_val(actioncorporateaccountcreation,corporateaccountcreation0,true,true).
causes_val(actiontrainingplanning,registersthecandidateinthesystems2,false,true).
causes_val(actiontrainingplanning,trainingplanning0,true,true).
causes_val(actioncollectionofsigneddocumentation,sendingdocumentation0,false,true).
causes_val(actioncollectionofsigneddocumentation,collectionofsigneddocumentation0,true,true).
causes_val(actionconfigurationofworktools,corporateaccountcreation0,false,true).
causes_val(actionconfigurationofworktools,configurationofworktools0,true,true).
causes_val(actionassignmentofamentor,trainingplanning0,false,true).
causes_val(actionassignmentofamentor,assignmentofamentor0,true,true).
causes_val(actioninclusioninthepayslip,collectionofsigneddocumentation0,false,true).
causes_val(actionitsecurityverification,configurationofworktools0,false,true).
causes_val(actionorganizationofawelcomemeeting,assignmentofamentor0,false,true).
causes_val(actionorganizationofawelcomemeeting,organizationofawelcomemeeting0,true,true).
causes_val(actionconfirmationofonboardingcompletion,organizationofawelcomemeeting0,false,true).
causes_val(actionconfirmationofonboardingcompletion,confirmationofonboardingcompletion0,true,true).
causes_val(actiononboardingcompleted(Q0),confirmationofonboardingcompletion0,false,true) :- qt(Q0).
causes_val(actiononboardingcompleted(Q0),candidateshired(Q0),true,true) :- qt(Q0).
causes_val(actiononboardingcompleted(Q0),candidateshired(Q1),false,Q0 \= Q1) :- qt(Q0), qt(Q1).

proc(simulateprocess0, 
                  [actionreceiveapplication(Q0),
                   actionchecktheprofileskills,
                   actionperforminterview(Q2),
                   actionregistersthecandidateinthesystems,
                   actioncorporateaccountcreation,
                   actionsendingdocumentation,
                   actiontrainingplanning,
                   actioncollectionofsigneddocumentation,
                   actionconfigurationofworktools,
                   actionassignmentofamentor,
                   actionorganizationofawelcomemeeting,
                   actioninclusioninthepayslip,
                   actionitsecurityverification,
                   actionconfirmationofonboardingcompletion,
                   actiononboardingcompleted(Q3)
                  ]).
