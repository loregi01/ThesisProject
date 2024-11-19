# Auto generated program
action_list=['actiondevicereceived', 'actionverifywarranty', 'actionsendrepairestimate', 'actioncheckestimationacceptance', 'actionrepairtheproduct(Q0)', 'actionupdateticketstatus', 'actionrepaircarriedout(Q0)', 'actionrepairfailure', 'actionrepairfailed(Q0)', 'actionassistanceticketgeneration(Q0)', 'actionchecksparepartsavailability', 'actiondelaynotification(Q0)']
procedure_calculation = '''actiondevicereceived,
  if(devicereceived,actionverifywarranty,no_op),
  if(verifywarranty,actionsendrepairestimate,no_op),
  if(sendrepairestimate,actioncheckestimationacceptance,no_op),
  if(check estimation acceptance,check spare parts availability),actionrepairtheproduct(N0),no_op),
  if(check estimation acceptance,check spare parts availability),actionupdateticketstatus,no_op),
  if(updateticketstatus,actionrepaircarriedout(N1),no_op),
  if(checkestimationacceptance,actionrepairfailure,no_op),
  if(repair failure,delay notification),actionrepairfailed(N2),no_op),
  if(verifywarranty,actionassistanceticketgeneration(N3),no_op),
  if(assistanceticketgeneration,actionchecksparepartsavailability,no_op),
  if(checksparepartsavailability,actiondelaynotification(N4),no_op)
'''
input_string = "['devicereceived0', 'verifywarranty0', 'sendrepairestimate0', 'checkestimationacceptance0', 'checksparepartsavailability0', 'checkestimationacceptance1', 'checksparepartsavailability1', 'updateticketstatus0', 'checkestimationacceptance2', 'repairfailure0', 'delaynotification0', 'verifywarranty1', 'assistanceticketgeneration0', 'generatedticket(Q0)', 'sparepartsinwarehouse(Q0)', 'repaireditems(Q0)', 'delaynotifications(Q0)', 'repairsfailed(Q0)', 'repairtheproduct0', 'repaircarriedout0', 'repairfailed0']"
