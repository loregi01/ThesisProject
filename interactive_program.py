# Auto generated program
input_string = "['devicereceived','verifywarranty','sendrepairestimate','checkestimationacceptance','repairtheproduct','updateticketstatus','repaircarriedout','repairfailure','repairfailed','assistanceticketgeneration','checksparepartsavailability','delaynotification']"
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