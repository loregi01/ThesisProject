# Auto generated program
input_string = "['receiveapplication','checktheprofileskills','performinterview','applicationrejected','rejectapplication','registersthecandidateinthesystems','sendingdocumentation','corporateaccountcreation','trainingplanning','collectionofsigneddocumentation','configurationofworktools','assignmentofamentor','inclusioninthepayslip','itsecurityverification','organizationofawelcomemeeting','confirmationofonboardingcompletion','onboardingcompleted']"
procedure_calculation = '''actionreceiveapplication,
  if(receiveapplication,actionchecktheprofileskills,no_op),
  if(checktheprofileskills,actionperforminterview(N0),no_op),
  if(perform interview,reject application),actionapplicationrejected(N1),no_op),
  if(checktheprofileskills,actionrejectapplication,no_op),
  if(performinterview,actionregistersthecandidateinthesystems,no_op),
  if(registersthecandidateinthesystems,actionsendingdocumentation,no_op),
  if(registersthecandidateinthesystems,actioncorporateaccountcreation,no_op),
  if(registersthecandidateinthesystems,actiontrainingplanning,no_op),
  if(sendingdocumentation,actioncollectionofsigneddocumentation,no_op),
  if(corporateaccountcreation,actionconfigurationofworktools,no_op),
  if(trainingplanning,actionassignmentofamentor,no_op),
  if(collectionofsigneddocumentation,actioninclusioninthepayslip,no_op),
  if(configurationofworktools,actionitsecurityverification,no_op),
  if(assignmentofamentor,actionorganizationofawelcomemeeting,no_op),
  if(organizationofawelcomemeeting,actionconfirmationofonboardingcompletion,no_op),
  if(confirmationofonboardingcompletion,actiononboardingcompleted(N2),no_op)
'''