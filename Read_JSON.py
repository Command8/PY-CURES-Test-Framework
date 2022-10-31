from email.headerregistry import Address
from multiprocessing.sharedctypes import Value
import json
from ntpath import join
from turtle import pd

#Procedure to import file from different folder using sys, path, append
import sys
sys.path.append(".")
from Functions.fhir_functions import getResourceFile

#Using os, Import filepath of directory that file resides in
import os
dir_path = os.path.dirname((__file__))

# Open JSON to read data to make comparisons

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
pfileinput = (dir_path + '/' +'PATIENT/SnowflakePat.json')

print("////////////////////////////PATIENT SNOWFLAKE JSON Data///////////////////////////////////////////")
# Open JSON to read data to make comparisons

#Loading file into function using defined path
dataSnwPatInput = getResourceFile(pfileinput)

#Traversing through json to identify the key values for validation
print(dataSnwPatInput['MEMBER_LAST_NAME']) 
print(dataSnwPatInput['MEMBER_FIRST_NAME'])
print(dataSnwPatInput['MEMBER_MIDDLE_NAME']) 
print(dataSnwPatInput['MEMBER_COUNTY']) 
print(dataSnwPatInput['CENSEOID']) 
print(dataSnwPatInput['MEMBER_ADDRESS1'])
print(dataSnwPatInput['MEMBER_ADDRESS2'])
print(dataSnwPatInput['MEMBER_CITY'])
print(dataSnwPatInput['MEMBER_DATE_OF_BIRTH'].split(' ')[0])
print(dataSnwPatInput['MEMBER_ZIP'])
print(dataSnwPatInput['ETHNICITY'])         
print(dataSnwPatInput['PCP_FIRSTNAME'])
print(dataSnwPatInput['PCP_LASTNAME'])

#Member Gender logic
if (dataSnwPatInput['MEMBER_GENDER']) =='M':
        input_memgender ="male"
elif (dataSnwPatInput['MEMBER_GENDER']) =='F':
        input_memgender ="female"
elif (dataSnwPatInput['MEMBER_GENDER']) =='U':
        input_memgender ="unknown"
else: input_memgender ="other"
print (input_memgender)

print("////////////////////////////PATIENT Transformed JSON Data///////////////////////////////////////////")
# Open Transformed JSON and retrieve values

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
pfileoutput = (dir_path + '/' +'PATIENT/Pat_TransformedPatient.json')

#Loading transformed JSON using function
dataTransformerpat = getResourceFile(pfileoutput)

# pulling key value MEMBER_LAST_NAME from patient profile
print(dataTransformerpat['name'][0]['family'])      

# pulling key value MEMBER_FIRST_NAME from patient profile
print(dataTransformerpat['name'][0]['given'][0])    

# pulling key value MEMBER_MIDDLE_NAME from patient profile
print(dataTransformerpat['name'][0]['given'][1])   

# pulling key value county from patient profile
print(dataTransformerpat['address'][0]['district'])

# pulling key value CENSEOID from patient profile
print(dataTransformerpat['identifier'][0]['value']) 

# pulling key value MEMBER_ADDRESS1 from patient profile
print(dataTransformerpat['address'][0]['line'].split(',')[0]) 

# pulling key value MEMBER_ADDRESS2 from patient profile
print(dataTransformerpat['address'][0]['line'].split(',')[1].strip()) 

# pulling key value CITY from patient profile
print(dataTransformerpat['address'][0]['city'])

# pulling key value state from patient profile
print(dataTransformerpat['address'][0]['state'])

# pulling key value DOB from patient profile
print(dataTransformerpat['birthDate'])

#pulling key value zip from patient profile
print(dataTransformerpat['address'][0]['postalCode'])

# pulling key value ETHNICITY from patient profile
print(dataTransformerpat['extension'][0]['extension'][0]['valueString'])

# pulling key value PCP_firstname from patient profile
print(dataTransformerpat['generalPractitioner'][0]['display'].split(' ')[0])

# pulling key value PCP_lastname from patient profile
print(dataTransformerpat['generalPractitioner'][0]['display'].split(' ')[1])    

# pulling key value GENDER from patient profile
print(dataTransformerpat['gender'])

print("////////////////////////////PRACTITIONER SNOWFLAKE JSON Data///////////////////////////////////////////")
# Open Snowflake JSON to read data to make comparisons

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
fileinput = (dir_path + '/' +'PRACTITIONER/Prac_SampleData_Input.json')

#Another way to access parent directory to reference files into function
#fileinput = pathlib.Path(__file__).parent/'SnowflakePrac.json'

#Loading file into function using defined path
dataSnwPracInput = getResourceFile(fileinput)

#Traversing through json to identify the key values for validation        
print(dataSnwPracInput['PROVIDER_ID']) 
print(dataSnwPracInput['PROVIDER_NPI'])
print(dataSnwPracInput['PROVIDER_PIN'])
print(dataSnwPracInput['PROVIDER_TAXID'])
print(dataSnwPracInput['PROVIDER_FIRSTNAME']) 
print(dataSnwPracInput['PROVIDER_LASTNAME']) 
print(dataSnwPracInput['PROVIDER_MIDDLE_Initial'])
print(dataSnwPracInput['PCP_ID']) 
print(dataSnwPracInput['IPA'])
print(dataSnwPracInput['IPA_IDENTIFIER'])
print(dataSnwPracInput['LPO'])
print(dataSnwPracInput['LPO_IDENTIFIER'])
print(dataSnwPracInput['SUBSCRIBER_ID'])
      
print("////////////////////////////PRACTITIONER Transformed JSON Data///////////////////////////////////////////")
# Open Transformed JSON and retrieve values

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
fileoutput = (dir_path + '/' +'PRACTITIONER/Prac_TransformedPrac.json')

#Another way to access parent directory to reference files into function
#fileoutput = pathlib.Path(__file__).parent/'TransformedPrac.json'

#Loading transformed JSON using function
dataTransformerPrac= getResourceFile(fileoutput)

# pulling key value PROVIDER_ID from Practitioner profile
print(dataTransformerPrac['identifier'][10]['value']) 

# pulling key value PROVIDER_NPI from Practitioner profile
print(dataTransformerPrac['identifier'][1]['value']) 

# pulling key value PROVIDER_PIN from Practitioner profile
print(dataTransformerPrac['identifier'][2]['value']) 

# pulling key value PROVIDER_NPI from Practitioner profile
print(dataTransformerPrac['identifier'][3]['value']) 

# pulling key value PROVIDER_FIRSTNAME from Practitioner profile
print(dataTransformerPrac['name'][0]['given'][0])    

# pulling key value PROVIDER_LASTNAME from Practitioner profile
print(dataTransformerPrac['name'][0]['family'])   

# pulling key value PROVIDER_MIDDLE_Initial from Practitioner profile
print(dataTransformerPrac['name'][0]['given'][1]) 

# pulling key value PCP_ID from Practitioner profile
print(dataTransformerPrac['identifier'][0]['value']) 

# pulling key value IPA from Practitioner profile
print(dataTransformerPrac['identifier'][4]['value']) 

# pulling key value IPA_IDENTIFIER from Practitioner profile
print(dataTransformerPrac['identifier'][5]['value']) 

# pulling key value LPO from Practitioner profile
print(dataTransformerPrac['identifier'][6]['value'])  

# pulling key value LPO_IDENTIFIER from Practitioner profile
print(dataTransformerPrac['identifier'][7]['value']) 

# pulling key value SUBSCRIBER_ID from Practitioner profile
print(dataTransformerPrac['identifier'][8]['value'])

print("////////////////////////////PRACTITIONER ROLE SNOWFLAKE JSON Data///////////////////////////////////////////")
# Open Snowflake JSON to read data to make comparisons

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
fileinput = (dir_path + '/' +'PRACTITIONER ROLE/PracRole_SampleData_Input.json')

#Another way to access parent directory to reference files into function
#fileinput = pathlib.Path(__file__).parent/'SnowflakePrac.json'

#Loading file into function using defined path
dataPracRoleInput = getResourceFile(fileinput)


#Traversing through json to identify the key values for validation 

    
print(dataPracRoleInput['PROVIDER_ROLE_ID']) 
print(dataPracRoleInput['PROVIDER_ACTIVE'])
print(dataPracRoleInput['PROVIDER_ACTIVE_START'])
print(dataPracRoleInput['PROVIDER_ACTIVE_END'])
print(dataPracRoleInput['PRACTITIONER']) 
print(dataPracRoleInput['PROVIDER_ORGANIZATION']) 
print(dataPracRoleInput['PROVIDER_ROLE_CODE'])
print(dataPracRoleInput['PROVIDER_ROLE_CODE_DESC']) 
print(dataPracRoleInput['PROVIDER_SPECIALITY_CODE'])
print(dataPracRoleInput['PROVIDER_SPECIALITY_DESC'])
print(dataPracRoleInput['PROVIDER_LOCATION'])
print(dataPracRoleInput['PROVIDER_HEALTHCARE_SERVICE'])
print(dataPracRoleInput['PROVIDER_PHONEPRIMARY'])
print(dataPracRoleInput['PROVIDER_PHONESECONDARY'])
print(dataPracRoleInput['PROVIDER_FAX'])
print(dataPracRoleInput['PROVIDER_CONTACT'])
print(dataPracRoleInput['PROVIDER_AVAILABLE_STARTTIME'])
print(dataPracRoleInput['PROVIDER_AVAILABLE_ENDTIME'])
print(dataPracRoleInput['PROVIDER_SERVICE_NOT_AVAILABLE_FROM'])
print(dataPracRoleInput['PROVIDER_SERVICE_NOT_AVAILABLE_TO'])
print(dataPracRoleInput['AVAILABILIY_EXCEPTION'])
print(dataPracRoleInput['ENDPOINT_ACCESS'])
        
print("////////////////////////////PRACTITIONER ROLE Transformed JSON Data///////////////////////////////////////////")
# Open Transformed JSON and retrieve values

#Loading the absolute path to be passed into function
#Access parent directory and create path to load json input file into function
prfileoutput = (dir_path + '/' +'PRACTITIONER ROLE/PracRole_Transformed.json')

#Another way to access parent directory to reference files into function
#fileoutput = pathlib.Path(__file__).parent/'TransformedPrac.json'

#Loading transformed JSON using function
prdataTransformer= getResourceFile(prfileoutput)

# pulling key value PROVIDER_ROLE_ID from practitioner role fhir resource
print(prdataTransformer['identifier'][0]['value']) 

# pulling key value PROVIDER_ACTIVE from practitioner role fhir resource
print(prdataTransformer['active']) 

# pulling key value PROVIDER_ACTIVE_START  from practitioner role fhir resource
print(prdataTransformer['period'][0]['start']) 

# pulling key value PROVIDER_ACTIVE_END  from practitioner role fhir resource
print(prdataTransformer['period'][0]['start']) 

# pulling key value Practitioner/id  from practitioner role fhir resource
print(prdataTransformer['practitioner'][0]['reference']) 

# pulling key value PRACTITIONER from practitioner role fhir resource
print(prdataTransformer['practitioner'][0]['display'])

# pulling key value PROVIDER_ORGANIZATION from practitioner role fhir resource
print(prdataTransformer['organization']['reference'])

# pulling key value PROVIDER_ORGANIZATION from practitioner role fhir resource
print(prdataTransformer['organization']['display'])

# pulling key code.coding value PROVIDER_ROLE_CODE from practitioner role fhir resource
print(prdataTransformer['code'][0]['coding'][0]['code'])

# pulling key code.coding value PROVIDER_ROLE_CODE_DESC from practitioner role fhir resource
print(prdataTransformer['code'][0]['text'])

# pulling key value PROVIDER_SPECIALITY_CODE from practitioner role fhir resource
print(prdataTransformer['specialty'][0]['coding'][0]['code'])

# pulling key value PROVIDER_SPECIALITY_DESC from practitioner role fhir resource
print(prdataTransformer['specialty'][0]['text'])

#pulling key value PROVIDER_LOCATION from practitioner role fhir resource
print(prdataTransformer['location']['reference'])

#pulling key value PROVIDER_LOCATION from practitioner role fhir resource
print(prdataTransformer['location']['display'])

#pulling key value PROVIDER_HEALTHCARE_SERVICE from practitioner role fhir resource
print(prdataTransformer['healthcareService']['reference'])

#pulling key value PROVIDER_HEALTHCARE_SERVICE from practitioner role fhir resource
print(prdataTransformer['healthcareService']['display'])

#pulling key value PROVIDER_PHONEPRIMARY from practitioner role fhir resource
print(prdataTransformer['telecom'][0]['value'])

#pulling key value PROVIDER_PHONESECONDARY from practitioner role fhir resource
print(prdataTransformer['telecom'][1]['value'])

#pulling key value PROVIDER_CONTACT from practitioner role fhir resource
print(prdataTransformer['telecom'][2]['value'])

#pulling key value PROVIDER_FAX from practitioner role fhir resource
print(prdataTransformer['telecom'][3]['value'])

#pulling key value PROVIDER_AVAILABLE_STARTTIME from practitioner role fhir resource
print(prdataTransformer['availableTime'][0]['availableStartTime'])

#pulling key value PROVIDER_AVAILABLE_ENDTIME from practitioner role fhir resource
print(prdataTransformer['availableTime'][0]['availableEndTime'])

#pulling key value PROVIDER_SERVICE_NOT_AVAILABLE_FROM from practitioner role fhir resource
print(prdataTransformer['notAvailable'][0]['during']['start'])

#pulling key value PROVIDER_SERVICE_NOT_AVAILABLE_TO from practitioner role fhir resource
print(prdataTransformer['notAvailable'][0]['during']['end'])

# pulling key value AVAILABILIY_EXCEPTION from practitioner role fhir resource
print(prdataTransformer['availabilityExceptions']) 

# pulling key value ENDPOINT_ACCESS from practitioner role fhir resource
print(prdataTransformer['endpoint'][0]['reference']) 

# pulling key value ENDPOINT_ACCESS from practitioner role fhir resource
print(prdataTransformer['endpoint'][0]['display']) 

print("////////////////////////////ENCOUNTER SNOWFLAKE JSON Data///////////////////////////////////////////")
# Open JSON to read data to make comparisons

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
pfileEncinput = (dir_path + '/' +'ENCOUNTER/Encounter_SampleData_Input.json')

# Open JSON to read data to make comparisons

#Loading file into function using defined path
dataSnwEncInput = getResourceFile(pfileEncinput)

#Traversing through json to identify the key values for validation
print(dataSnwEncInput['Status']) 
print(dataSnwEncInput['AdmissionDate'])
print(dataSnwEncInput['AdmitSource']) 
print(dataSnwEncInput['DiagnosisCode']) 
print(dataSnwEncInput['PatientId']) 
print(dataSnwEncInput['EncounterType'])
print(dataSnwEncInput['ReasonCode'])
print(dataSnwEncInput['EpisodeOfCareId'])
print(dataSnwEncInput['basedOn'])
print(dataSnwEncInput['PCP_ID'])         
print(dataSnwEncInput['apptId'])
print(dataSnwEncInput['reasonref'])
print(dataSnwEncInput['locationId'])
print(dataSnwEncInput['FacilityName'])
print(dataSnwEncInput['encId'])

#Member Gender logic
if (dataSnwEncInput['Status']) =='planned':
        input_status ="planned"
elif (dataSnwEncInput['Status']) =='arrived':
        input_status ="arrived"
elif (dataSnwEncInput['Status']) =='triaged':
        input_status ="triaged"
elif (dataSnwEncInput['Status']) =='in-progress':
        input_status ="in-progress"
elif (dataSnwEncInput['Status']) =='onleave':
        input_status ="onleave"
elif (dataSnwEncInput['Status']) =='finished':
        input_status ="finished"
elif (dataSnwEncInput['Status']) =='cancelled':
        input_status ="cancelled"
elif (dataSnwEncInput['Status']) =='other':
        input_status ="unknown"
print (input_status)

print("////////////////////////////ENCOUNTER Transformed JSON Data///////////////////////////////////////////")
# Open Transformed JSON and retrieve values

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
pfileEncoutput = (dir_path + '/' +'ENCOUNTER/Encounter_Transformed.json')

#Loading transformed JSON using function
dataTransformerEnc = getResourceFile(pfileEncoutput)

# pulling key value Status from patient profile
print(dataTransformerEnc['status'])      

# pulling key value AdmissionDate from patient profile
print(dataTransformerEnc['period']['start'])   

# pulling key value AdmitSource from patient profile
print(dataTransformerEnc['hospitalization']['admitSource']['coding'][0]['display'])

# pulling key value Diagnosis from patient profile      
print(dataTransformerEnc['diagnosis'][0]['use']['coding'][0]['code'])   

# pulling key value PatientId from patient profile
print(dataTransformerEnc['subject']['reference'].split('/')[1])

# pulling key value EncounterType from patient profile
print(dataTransformerEnc['type'][0]['coding'][0]['display']) 

# pulling key value ReasonCode from patient profile
print(dataTransformerEnc['reasonCode'][0]['coding'][0]['display']) 

# pulling key value EpisodeOfCareId from patient profile
print(dataTransformerEnc['episodeOfCare']['reference'].split('/')[1]) 

# pulling key value basedOn from patient profile
print(dataTransformerEnc['basedOn']['reference'].split('/')[1])

# pulling key value PCP_ID from patient profile
print(dataTransformerEnc['participant'][0]['individual']['reference'].split('/')[1])

# pulling key value apptId from patient profile
print(dataTransformerEnc['appointment']['reference'].split('/')[1])

#pulling key value reasonref from patient profile
print(dataTransformerEnc['reasonReference']['reference'].split('/')[1])

# pulling key value locationId from patient profile
print(dataTransformerEnc['location']['location']['reference'].split('/')[1])

# pulling key value FacilityName from patient profile
print(dataTransformerEnc['serviceProvider']['display'])

# pulling key value encId from patient profile
print(dataTransformerEnc['partOf']['display'])    


print("////////////////////////////CLAIMS SNOWFLAKE(INPUT) JSON Data///////////////////////////////////////////")
# Open Snowflake JSON to read data to make comparisons

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
fileinput = (dir_path + '/' +'CLAIM/Claims_SampleData_Input.json')

#Another way to access parent directory to reference files into function
#fileinput = pathlib.Path(__file__).parent/'SnowflakePrac.json'

#Loading file into function using defined path
ClaimsDataInput = getResourceFile(fileinput)


#Traversing through json to identify the key values for validation    
print(ClaimsDataInput['Provider_ID']) 
print(ClaimsDataInput['RenderingProviderID'])
print(ClaimsDataInput['RenderingProviderNPI'])
print(ClaimsDataInput['AdmissionDate'])
print(ClaimsDataInput['AdmitDiag']) 
print(ClaimsDataInput['AdmitSource']) 
print(ClaimsDataInput['AdmitType'])
print(ClaimsDataInput['BillAmount']) 
print(ClaimsDataInput['BillingProvideID'])
print(ClaimsDataInput['BillingProviderNPI'])
print(ClaimsDataInput['BillType'])
print(ClaimsDataInput['CarePlan'])
print(ClaimsDataInput['CenseoID'])
print(ClaimsDataInput['ClaimEntryDate'])
print(ClaimsDataInput['ClaimLineNumber'])
print(ClaimsDataInput['ClaimNumber'])
print(ClaimsDataInput['ClaimPaymentStatus'])
print(ClaimsDataInput['DiagnosisCode'])
print(ClaimsDataInput['DiagnosisCodeDecimal'])
print(ClaimsDataInput['DiagnosisFilter'])
print(ClaimsDataInput['DiagnosisFullDescription'])
print(ClaimsDataInput['DiagnosisLongDescription'])
print(ClaimsDataInput['DiagnosisShortDescription'])
print(ClaimsDataInput['DiagnosisIndicator'])
print(ClaimsDataInput['DiagnosisVersionCode'])
print(ClaimsDataInput['DiagnosisVersionDescription'])
print(ClaimsDataInput['DimDiagnosisKey'])
print(ClaimsDataInput['DischargeDate'])
print(ClaimsDataInput['DRG'])
print(ClaimsDataInput['DX_1'])
print(ClaimsDataInput['DX_2'])
print(ClaimsDataInput['DX_3'])
print(ClaimsDataInput['EvaluationKey'])
print(ClaimsDataInput['Exception'])
print(ClaimsDataInput['HasInvalidResult'])
print(ClaimsDataInput['HICN'])
print(ClaimsDataInput['ICDVersion'])
print(ClaimsDataInput['IsBillable'])
print(ClaimsDataInput['lab_results'])
print(ClaimsDataInput['LabResultsDateReceived'])
print(ClaimsDataInput['LeftSeverity'])
print(ClaimsDataInput['Medicare_Adjusted'])
print(ClaimsDataInput['Medicare_Unadjusted'])
print(ClaimsDataInput['Member_Number'])
print(ClaimsDataInput['Modifier'])
print(ClaimsDataInput['NPI'])
print(ClaimsDataInput['ODSAnswerID'])
print(ClaimsDataInput['ODSDiagnosisID'])
print(ClaimsDataInput['ODSEvaluationID'])
print(ClaimsDataInput['ODSEvaluationResponseID'])
print(ClaimsDataInput['ODSQuestionID'])
print(ClaimsDataInput['PaidAmount'])
print(ClaimsDataInput['PaidDate'])
print(ClaimsDataInput['PatientPayPortion'])
print(ClaimsDataInput['PlaceOfService'])
print(ClaimsDataInput['ProcedureCode_CPTCode_Primary'])
print(ClaimsDataInput['ProcedureCode2'])
print(ClaimsDataInput['ProductKey'])
print(ClaimsDataInput['RenderingProviderSpecialty'])
print(ClaimsDataInput['ResponseValue'])
print(ClaimsDataInput['RevenueCode'])
print(ClaimsDataInput['RightSeverity'])
print(ClaimsDataInput['ServiceCategory'])
print(ClaimsDataInput['ServiceFromDate_Date_of_Service'])
print(ClaimsDataInput['ServiceThruDate'])
print(ClaimsDataInput['Specialty_Code'])
print(ClaimsDataInput['Specialty_Name'])
        
print("////////////////////////////CLAIMS Transformed JSON Data///////////////////////////////////////////")
# Open Transformed JSON and retrieve values

#Loading the absolute path to be passed into function
#Access parent directory and create path to load json input file into function
clmsfileoutput = (dir_path + '/' +'CLAIM/Claims_Transformed.json')
#Another way to access parent directory to reference files into function
#fileoutput = pathlib.Path(__file__).parent/'Transformedclmsac.json'
#Loading transformed JSON using function
clmsdataTransformer= getResourceFile(clmsfileoutput)

#RESOURCETYPE
# pulling key value RESOURCE_TYPE from claim fhir resource
print(clmsdataTransformer['resourceType'])

#IDENTIFIER
# pulling key value CLAIM_NUMBER from claim identifier.use fhir resource
print(clmsdataTransformer['identifier']['use'])
# pulling key value CLAIM_NUMBER from claim identifier.value fhir resource
print(clmsdataTransformer['identifier']['value'])

#STATUS
#pulling key value ClaimPaymentStatus from claim.status  fhir resource // R!  active | cancelled | draft | entered-in-error
print(clmsdataTransformer['status'])

#PATIENT
# pulling key value CENSEO_ID identifer.use Claim patient.reference fhir resource
print(clmsdataTransformer['patient']['reference'])

#BILLABLEPERIOD
# pulling key value BILLABLE_PERIOD CLAIM from claim.billablePeriod.start fhir resource
#ServiceFromDate_Date_of_Service
print(clmsdataTransformer['billablePeriod']['start']) 
# pulling key value BILLABLE_PERIOD CLAIM ServiceThruDate from claim.billablePeriod.end fhir resource
print(clmsdataTransformer['billablePeriod']['end']) 

#CREATED
# pulling key value status ClaimEntryDate from claim fhir resource
print(clmsdataTransformer['created']) 

#ENTERER
# pulling key value status Provider_ID from claim enterer.reference fhir resource
print(clmsdataTransformer['enterer']['reference']) 

#PROVIDER
# pulling key value status Provider_ID from claim provider.reference fhir resource
print(clmsdataTransformer['provider']['reference']) 

#PRIORITY
# pulling key value RenderingProviderNPI from claim priority.coding.code fhir resource //R!  Desired processing ugency"
print(clmsdataTransformer['priority']['coding'][0]['code'])

#PRESCRIPTION
# pulling key value prescription.reference from claim prescription.reference fhir resource //R!  Desired processing ugency"
print(clmsdataTransformer['prescription']['reference'])

#PAYEE
# pulling key value payee.reference from claim prescription.reference fhir resource
print(clmsdataTransformer['payee']['type']['coding'][0]['code'])
print(clmsdataTransformer['payee']['type']['coding'][0]['display'])


#FACILITY
#pulling key PlaceOfServicevalue CLAIM_TYPE from claim facility.identifier.value fhir resource
print(clmsdataTransformer['facility']['identifier']['value'])

#CARETEAM
#pulling key value status Provider_ID from claim careTeam.sequence value fhir resource
print(clmsdataTransformer['careTeam'][0]['sequence'])
# pulling key value status Provider_ID from claim careTeam.provider.reference value fhir resource
print(clmsdataTransformer['careTeam'][0]['provider'])  

#DIAGNOSIS
# pulling key value  from claim diagnosis.sequence fhir resource
print(clmsdataTransformer['diagnosis'][0]['sequence'])
# pulling key DX_1 value from claim diagnosis.sequence.diagnosisCodeableConcept.coding.code fhir resource
print(clmsdataTransformer['diagnosis'][0]['diagnosisCodeableConcept']['coding'][0]['code'])

# pulling key DX_2 value from claim diagnosis.diagnosisCodeableConcept.coding.code fhir resource
print(clmsdataTransformer['diagnosis'][1]['diagnosisCodeableConcept']['coding'][0]['code'])

# pulling key DX_3 value from claim diagnosis.diagnosisCodeableConcept.coding.code fhir resource
print(clmsdataTransformer['diagnosis'][2]['diagnosisCodeableConcept']['coding'][0]['code'])

#PROCEDURE
#pulling key value  "1"   from claim procedure.sequence fhir resource
print(clmsdataTransformer['procedure'][0]['sequence']) 
#pulling key value  "primary" from claim procedure.type.coding.code fhir resource
print(clmsdataTransformer['procedure'][0]['type'][0]['coding'][0]['code'])
#pulling key value ServiceFromDate from claim.prodecure.date fhir resource

print(clmsdataTransformer['procedure'][0]['date'])
#pulling key value CPTCode_Primary from claim fhir resource
print(clmsdataTransformer['procedure'][0]['procedureCodeableConcept']['coding'][0]['code'])

# pulling key value "2" from claim procedure.sequence fhir resource
print(clmsdataTransformer['procedure'][1]['sequence']) 
#pulling key value ProcedureCode2 from claim fhir resource
#pulling key value  "secondary" from claim procedure.type.coding.code fhir resource
print(clmsdataTransformer['procedure'][1]['procedureCodeableConcept']['coding'][0]['code'])
#pulling key value ServiceFromDate from claim.prodecure.date fhir resource
#print(clmsdataTransformer['procedure'][1]['date'])

#INSURANCE
# pulling key value "1" from claim insurance.sequence fhir resource
print(clmsdataTransformer['insurance'][0]['sequence'])
# pulling key value "true" from claim insurance.focal fhir resource
print(clmsdataTransformer['insurance'][0]['focal'])
# pulling key value  from claim insurance.coverage.reference fhir resource
print(clmsdataTransformer['insurance'][0]['coverage']['reference']) 

#TOTAL
#pulling key vaalue BillAmount from claims total.value fhir resource
print(clmsdataTransformer['total']['value'])

# Open JSON to read data to make comparisons

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
pfilecovinput = (dir_path + '/' +'COVERAGE/Coverage_SampleData_Input.json')

print("////////////////////////////COVERAGE SNOWFLAKE JSON Data///////////////////////////////////////////")
# Open JSON to read data to make comparisons

#Loading file into function using defined path
dataSnwCovInput = getResourceFile(pfilecovinput)

#Traversing through json to identify the key values for validation
print(dataSnwCovInput['PLAN_NUMBER']) 
print(dataSnwCovInput['HICN'])
print(dataSnwCovInput['COVERAGE_STATUS']) 
print(dataSnwCovInput['COVERAGE_TYPE']) 
print(dataSnwCovInput['COVERAGE_TYPE_DESC']) 
print(dataSnwCovInput['POLICY_HOLDER'])
print(dataSnwCovInput['SUBSCRIBER'])
print(dataSnwCovInput['CENSEOID'])
print(dataSnwCovInput['CMSID_HIC_NUMBER'])
print(dataSnwCovInput['MEMBER_NUMBER'])
print(dataSnwCovInput['MEMBERID'])
print(dataSnwCovInput['SUBSCRIBER'])
print(dataSnwCovInput['SUBSCRIBER'])
print(dataSnwCovInput['BENEFICIARY'])
print(dataSnwCovInput['DEPENDENT'])         
print(dataSnwCovInput['RELATIONSHIP'])
print(dataSnwCovInput['COVERAGE_START_DATE'])
print(dataSnwCovInput['COVERAGE_STOP_DATE'])
print(dataSnwCovInput['PAYOR'])
print(dataSnwCovInput['PLAN_TYPE'])
print(dataSnwCovInput['PLAN_VALUE'])         
print(dataSnwCovInput['PLAN_DESCRIPTION'])
print(dataSnwCovInput['ORDER'])
print(dataSnwCovInput['NETWORK'])
print(dataSnwCovInput['COST_TO_BENEFICIARY_TYPE'])
print(dataSnwCovInput['COST_TO_BENEFICIARY_TYPE_DESC'])
print(dataSnwCovInput['COST_QUANTITY_VALUE'])
print(dataSnwCovInput['COST_QUANTITY_CURRENCY'])         
print(dataSnwCovInput['BENEFICIARY_EXCEPTION_TYPE'])
print(dataSnwCovInput['BENEFICIARY_EXCEPTION_PERIOD_START'])
print(dataSnwCovInput['BENEFICIARY_EXCEPTION_PERIOD_END'])
print(dataSnwCovInput['SUBROGATION'])
print(dataSnwCovInput['CONTRACT'])


#Member Gender logic
if (dataSnwCovInput['CENSEOID']) !="":
        input_covsubid = dataSnwCovInput['CENSEOID']
elif (dataSnwCovInput['CMSID_HIC_NUMBER']) !="":
        input_covsubid = dataSnwCovInput['CMSID_HIC_NUMBER']
elif (dataSnwCovInput['MEMBER_NUMBER']) !="":
        input_covsubid = dataSnwCovInput['MEMBER_NUMBER']
elif (dataSnwCovInput['MEMBERID']) !="":
        input_covsubid = dataSnwCovInput['MEMBERID']        
else: input_covsubid =""
print (input_covsubid)

print("////////////////////////////COVERAGE Transformed JSON Data///////////////////////////////////////////")
# Open Transformed JSON and retrieve values

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
pfileCovoutput = (dir_path + '/' +'COVERAGE/Coverage_Transformed.json')

#Loading transformed JSON using function
dataTransformerCov = getResourceFile(pfileCovoutput)

# pulling key value PLAN_NUMBER from patient profile
print(dataTransformerCov['identifier'][0]['value'])    

# pulling key value HICN from patient profile
print(dataTransformerCov['identifier'][1]['value'])  

# pulling key value COVERAGE_STATUS from patient profile
print(dataTransformerCov['status'])   

# pulling key value COVERAGE_TYPE from patient profile
print(dataTransformerCov['type']['coding'][0]['code'])

# pulling key value COVERAGE_TYPE_DESC from patient profile      
print(dataTransformerCov['type']['coding'][0]['display'])   

# pulling key value POLICY_HOLDER from patient profile
print(dataTransformerCov['policyHolder']['display'])

# pulling key value SUBSCRIBER from patient profile
print(dataTransformerCov['subscriber']['display'])

# pulling key value CMSID_HIC_Number from patient profile
print(dataTransformerCov['subscriberId']) 

# pulling key value BENEFICIARY from patient profile
print(dataTransformerCov['beneficiary']['display']) 

# pulling key value DEPENDENT from patient profile
print(dataTransformerCov['dependent']) 

# pulling key value RELATIONSHIP from patient profile
print(dataTransformerCov['relationship']['coding'][0]['code'])

# pulling key value COVERAGE_START_DATE from patient profile
print(dataTransformerCov['period']['start'])

# pulling key value COVERAGE_STOP_DATE from patient profile
print(dataTransformerCov['period']['end'])

#pulling key value PAYOR from patient profile
print(dataTransformerCov['payor'][0]['display'])

# pulling key value PLAN_TYPE from patient profile
print(dataTransformerCov['class'][0]['type']['coding'][0]['code'])

# pulling key value PLAN_VALUE from patient profile
print(dataTransformerCov['class'][0]['value'])

# pulling key value PLAN_DESCRIPTION from patient profile
print(dataTransformerCov['class'][0]['name'])   

# pulling key value ORDER from patient profile
print(dataTransformerCov['order']) 

# pulling key value NETWORK from patient profile
print(dataTransformerCov['network']) 

# pulling key value COST_TO_BENEFICIARY_TYPE from patient profile
print(dataTransformerCov['costToBeneficiary'][0]['type']['coding'][0]['code'])

# pulling key value COST_TO_BENEFICIARY_TYPE_DESC from patient profile
print(dataTransformerCov['costToBeneficiary'][0]['type']['coding'][0]['display']) 

# pulling key value COST_VALUE_MONEY_VALUE from patient profile
#print(dataTransformerCov['costToBeneficiary'][0]['valueMoney']['value']) 

# pulling key value COST_VALUE_MONEY_CURRENCY from patient profile
#print(dataTransformerCov['costToBeneficiary'][0]['valueMoney']['currency']) 

# pulling key value COST_QUANTITY_CURRENCY from patient profile
print(dataTransformerCov['costToBeneficiary'][0]['valueQuantity']['code']) 

# pulling key value COST_QUANTITY_VALUE from patient profile
print(dataTransformerCov['costToBeneficiary'][0]['valueQuantity']['value']) 

# pulling key value BENEFICIARY_EXCEPTION_TYPE from patient profile
print(dataTransformerCov['costToBeneficiary'][0]['exception'][0]['type']['coding'][0]['code']) 

# pulling key value BENEFICIARY_EXCEPTION_PERIOD_START from patient profile
print(dataTransformerCov['costToBeneficiary'][0]['exception'][0]['period']['start']) 

# pulling key value BENEFICIARY_EXCEPTION_PERIOD_END from patient profile
print(dataTransformerCov['costToBeneficiary'][0]['exception'][0]['period']['end']) 

# pulling key value SUBROGATION from patient profile
print(dataTransformerCov['subrogation']) 

# pulling key value CONTRACT from patient profile
print(dataTransformerCov['contract'][0]['display']) 

# Open JSON to read data to make comparisons

print("/////////////////////////////MEDICATION REQUEST Transformed JSON Data///////////////////////////////////////////")
# Open Snowflake JSON to read data to make comparisons

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
fileinput = (dir_path + '/' +'MEDICATION REQUEST/MedicationRequest_SampleData_Input.json')

#Another way to access parent directory to reference files into function
#fileinput = pathlib.Path(__file__).parent/'SnowflakePrac.json'

#Loading file into function using defined path
MedRequestDataInput = getResourceFile(fileinput)


#Traversing through json to identify the key values for validation    

print(MedRequestDataInput['NDC_CODE'])
print(MedRequestDataInput['NDC_DESCRIPTION'])
print(MedRequestDataInput['DATE_OF_SERVICE']) 
print(MedRequestDataInput['QUANTITY'])
print(MedRequestDataInput['CENSEOID'])

print("////////////////////////////MEDICATIONREQUEST Transformed JSON Data///////////////////////////////////////////")
# Open Transformed JSON and retrieve values

#Another way to access parent directory to reference files into function
#fileoutput = pathlib.Path(__file__).parent/'Transformedclmsac.json'

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
medreqfileoutput = (dir_path + '/' +'MEDICATION REQUEST/MedicationRequest_Transformed.json')

#Loading transformed JSON using function
medreqdataTransformer= getResourceFile(medreqfileoutput)

#RESOURCETYPE
#pulling key value RESOURCE_TYPE from medicationrequest.resourcetype fhir resource
print(medreqdataTransformer['resourceType'])

#pulling key value TEXT STATUS from medicationrequest.text.status fhir resource
print(medreqdataTransformer['text']['status'])

#pulling key value CONTAINED from medicationrequest.contained.resourceType fhir resource
print(medreqdataTransformer['contained'][0]['resourceType'])

#IDENTIFIER
#pulling key value IDENTIFIER from medicationrequest.identifier fhir resource
print(medreqdataTransformer['identifier'])


#STATUS
#pulling key value STATUS from medicationrequest.medicationReference.reference  fhir resource // R!  active | cancelled | draft | entered-in-error
print(medreqdataTransformer['status'])

#STATUS REASON  
#pulling key value STATUSREASON medicationrequest.statusreason fhir resource
#print(medreqdataTransformer['statusReason'])

#CATAGORY
#pulling key value CATAGORY medicationrequest.catagory fhir resource
#print(medreqdataTransformer['category'][0]['coding'][0]['system'])
#pulling key value CATAGORY medicationrequest.catagory fhir resource
#print(medreqdataTransformer['category'][0]['coding'][0]['code'])
#pulling key value CATAGORY medicationrequest.catagory fhir resource
#print(medreqdataTransformer['category'][0]['coding'][0]['display'])

#INTENT
#pulling key value MEDICATION_REFERENCE from medicationrequest.intent fhir resource
print(medreqdataTransformer['intent']) 

#PRIORITY
#pulling key value PRIORITY from medicationrequest.priority fhir resource
#print(medreqdataTransformer['priority']) 

#DONOTPERFORM
# pulling key value DONOTPERFORM  from medicationrequest.doNotPerform fhir resource
#print(medreqdataTransformer['doNotPerform']) 

#REPORTEDBOOLEAN
#pulling key value reportedBoolean from medicationrequest.reportedBoolean fhir resource
#print(medreqdataTransformer['reportedBoolean']) 

#REPORTEDREFERENCE
#pulling key value REPORTEDREFERENCE from medicationrequest.reportedReference fhir resource
print(medreqdataTransformer['reportedReference']) 

#PRACTIONERROLE
#pulling key value PRACTIONERROLE from medicationrequest.PractitionerRole fhir resource //R!  Desired processing ugency"
#print(medreqdataTransformer['PractitionerRole'])

#MEDICATIONCODEABLECONCEPT
#pulling key value NDC_CODE from medicationrequest.medicationCodeableConcept fhir resource //R!  Desired processing ugency"
print(medreqdataTransformer['medicationCodeableConcept']['coding'][0]['code'])

#pulling key value NDC_DESCRIPTION from medicationrequest.medicationCodeableConcept fhir resource //R!  Desired processing ugency"
print(medreqdataTransformer['medicationCodeableConcept']['coding'][0]['display'])

#MEDICATIONREFERENCE
#pulling key value MEDICATIONREFERENCE from medicationrequest.medicationReference fhir resource
#print(medreqdataTransformer['medicationReference'])


#SUBJECT
#pulling key value SUBJECT from medicationrequest.subject value fhir resource
print(medreqdataTransformer['subject'])

#ENCOUNTER
#pulling key value ENCOUNTER from medicationrequest.encounter value fhir resource
print(medreqdataTransformer['encounter'])

#SUPPORTINGINFORMATION
# pulling key value SUPPORTINGINFORMATION from medication request.supportingInformation value fhir resource
print(medreqdataTransformer['supportingInformation'])  

#AUTHOREDON
# pulling key value DATE_OF_SERVICE from medicationrequest.authoredOn fhir resource
print(medreqdataTransformer['authoredOn'])

#REQUESTER
# pulling key REQUESTER value from medication request.requester fhir resource
print(medreqdataTransformer['requester'])

#PERFORMER
#pulling key PERFORMER value from medication request.performer fhir resource
print(medreqdataTransformer['performer'])


#PERFORMERTYPE
#pulling key PERFORMERTYPE value from medicationrequest.performerType fhir resource
#print(medreqdataTransformer['performerType']) 

#RECORDER
#pulling key RECORDER value from medicationrequest.recorder fhir resource
print(medreqdataTransformer['recorder'])

#REASONCODE
#pulling key REASONCODE value from medicationrequest.reasonCode fhir resource
#print(medreqdataTransformer['reasonCode'])

#REASONREFERENCE
#pulling key REASONREFERENCE value from medicationrequest.reasonReference fhir resource
print(medreqdataTransformer['reasonReference'])

#INSTANTIATESCANONICAL
# pulling key INSTANTIATESCANONICAL value from medication request.instantiatesCanonical fhir resource
#print(medreqdataTransformer['instantiatesCanonical']['value']) 

#INSTANTIATESURI
#pulling key INSTANTIATESURI value from medication request.instantiatesUri fhir resource
#print(medreqdataTransformer['instantiatesUri'])

#BASEDON
#pulling key BASEDON value from medicationrequest.basedOn fhir resource
print(medreqdataTransformer['basedOn'])

#GROUPIDENTIFIER
#pulling key GROUPIDENTIFIER value from medicationrequest.groupIdentifier fhir resource
#print(medreqdataTransformer['groupIdentifier'])

#COURSEOFTHERAPYTYPE
#pulling key COURSEOFTHERAPYTYPE value from medication request.courseOfTherapyType fhir resource
#print(medreqdataTransformer['courseOfTherapyType'])

#INSURANCE
#pulling key INSURANCE value from medication request.insurance fhir resource
print(medreqdataTransformer['insurance']) 

#NOTE
#pulling key NOTE value  from medicationrequests.note fhir resource
#print(medreqdataTransformer['note'])

#DOSAGEINSTRUCTION

#pulling key SEQUENCE value from medicationrequests.dosageInstruction.sequence fhir resource
print(medreqdataTransformer['dosageInstruction'][0]['sequence'])
#pulling key text value from medicationrequests.dosageInstruction.text fhir resource
#print(medreqdataTransformer['dosageInstruction'][0]['text'])

#pulling key frequency value from medicationrequests.dosageInstruction.timing.repeat.frequency fhir resource
#print(medreqdataTransformer['dosageInstruction'][0]['timing']['repeat']['frequency'])
#pulling key period value from medicationrequests.dosageInstruction.timing.repeat.period fhir resource
#print(medreqdataTransformer['dosageInstruction'][0]['timing']['repeat']['period'])
#pulling key periodUnit value from medicationrequests.dosageInstruction.timing.repeat.periodUnit fhir resource
#print(medreqdataTransformer['dosageInstruction'][0]['timing']['repeat']['periodUnit'])

#pulling key system value from medicationrequests.dosageInstruction.doseAndRate.type.coding.system fhir resource
#print(medreqdataTransformer['dosageInstruction'][0]['doseAndRate'][0]['type']['coding']['system'])
#pulling key code value from medicationrequests.dosageInstruction fhir resource
#print(medreqdataTransformer['dosageInstruction'][0]['doseAndRate']['type']['coding']['code'])
#pulling key display value from medicationrequests.dosageInstruction fhir resource
#print(medreqdataTransformer['dosageInstruction'][0]['doseAndRate']['type']['coding']['display'])

#pulling key value value from medicationrequests.dosageInstruction.doseQuantity.value fhir resource
print(medreqdataTransformer['dosageInstruction'][0]['doseAndRate'][0]['doseQuantity']['value'])
#pulling key unit value from medicationrequests.dosageInstruction.doseQuantity.unit fhir resource
#print(medreqdataTransformer['dosageInstruction'][0]['doseAndRate'][0]['doseQuantity']['unit'])
#pulling key system value from medicationrequests.dosageInstruction.doseQuantity.system fhir resource
#print(medreqdataTransformer['dosageInstruction'][0]['doseAndRate'][0]['doseQuantity']['system'])

#pulling key quantity value from medicationrequests.dispenseRequest.doseQuantity.value fhir resource
#print(medreqdataTransformer['dispenseRequest'][0]['initialFill']['quantity'])
#pulling key duration value from medicationrequests.dispenseRequest.doseQuantity.unit fhir resource
#print(medreqdataTransformer['dispenseRequest'][0]['initialFill']['duration'])

#pulling key start value from medicationrequests.dispenseRequest.dispenseInterval.validityPeriod.start fhir resource
#print(medreqdataTransformer['dispenseRequest'][0]['dispenseInterval']['validityPeriod']['start'])
#pulling key end value from medicationrequests.dispenseRequest.dispenseInterval.code.validityPeriod.end fhir resource
#print(medreqdataTransformer['dispenseRequest'][0]['dispenseInterval']['validityPeriod']['end'])

#pulling key value value from medicationrequests.dispenseRequest.numberOfRepeatsAllowed.validityPeriod.value fhir resource
#print(medreqdataTransformer['dispenseRequest'][0]['numberOfRepeatsAllowed']['quantity']['value'])
#pulling key unit value from medicationrequests.dispenseRequest.numberOfRepeatsAllowed.code.validityPeriod.unit fhir resource
#print(medreqdataTransformer['dispenseRequest'][0]['numberOfRepeatsAllowed']['quantity']['unit'])
#pulling key system value from medicationrequests.dispenseRequest.numberOfRepeatsAllowed.validityPeriod.system fhir resource
#print(medreqdataTransformer['dispenseRequest'][0]['numberOfRepeatsAllowed']['quantity']['system'])
#pulling key code value from medicationrequests.dispenseRequest.numberOfRepeatsAllowed.code.validityPeriod.code fhir resource
#print(medreqdataTransformer['dispenseRequest'][0]['numberOfRepeatsAllowed']['quantity']['code'])

#pulling key value value from medicationrequests.dispenseRequest.expectedSupplyDuration.validityPeriod.value fhir resource
#print(medreqdataTransformer['dispenseRequest'][0]['expectedSupplyDuration']['quantity']['value'])
#pulling key unit value from medicationrequests.dispenseRequest.expectedSupplyDuration.code.validityPeriod.unit fhir resource
#print(medreqdataTransformer['dispenseRequest'][0]['expectedSupplyDuration']['quantity']['unit'])
#pulling key system value from medicationrequests.dispenseRequest.expectedSupplyDuration.validityPeriod.system fhir resource
#print(medreqdataTransformer['dispenseRequest'][0]['expectedSupplyDuration']['quantity']['system'])
#pulling key code value from medicationrequests.dispenseRequest.expectedSupplyDuration.code.validityPeriod.code fhir resource
#print(medreqdataTransformer['dispenseRequest'][0]['expectedSupplyDuration']['quantity']['code'])

#pulling key value value from medicationrequests.substitution.allowedBoolean.validityPeriod.value fhir resource
#print(medreqdataTransformer['substitution'][0]['allowedBoolean']['value'])

#pulling key system value from medicationrequests.substitution.allowedCodeableConcept.coding.system fhir resource
#print(medreqdataTransformer['substitution']['allowedCodeableConcept']['coding'][0]['system'])
#pulling key code value from medicationrequests.substitution.allowedCodeableConcept.coding.code fhir resource
#print(medreqdataTransformer['substitution'][0]['allowedCodeableConcept']['coding'][0]['code'])
#pulling key display value from medicationrequests.substitution.allowedCodeableConcept.coding.display fhir resource
#print(medreqdataTransformer['substitution'][0]['allowedCodeableConcept']['coding'][0]['display'])

#pulling key system value from medicationrequests.reason.allowedCodeableConcept.coding.system fhir resource
#print(medreqdataTransformer['substitution']['reason']['coding'][0]['system'])
#pulling key code value from medicationrequests.reason.allowedCodeableConcept.coding.code fhir resource
#print(medreqdataTransformer['substitution']['reason']['coding'][0]['code'])
#pulling key display value from medicationrequests.reason.allowedCodeableConcept.coding.display fhir resource
#print(medreqdataTransformer['substitution']['reason']['coding'][0]['display'])


#PRIORPRESCRIPTION
#pulling key PRIORPRESCRIPTION value from medicationrequests.priorPrescription.reference fhir resource
print(medreqdataTransformer['priorPrescription']['reference'])
#pulling key PRIORPRESCRIPTION value from medicationrequests.priorPrescription.display fhir resource
#print(medreqdataTransformer['priorPrescription']['display'])


#DETECTEDISSUE
#pulling key DETECTEDISSUE value from medicationrequests.detectedIssue.reference fhir resource
print(medreqdataTransformer['detectedIssue']['reference'])
#pulling key DETECTEDISSUE value from medicationrequests.detectedIssue.display fhir resource
#print(medreqdataTransformer['detectedIssue']['display'])

#EVENTHISTORY
#pulling key reference value  from medicationrequests.eventHistory.reference fhir resource
print(medreqdataTransformer['eventHistory']['reference'])
#pulling key display value  from medicationrequests.eventHistory.display fhir resource
#print(medreqdataTransformer['eventHistory']['display'])

print("////////////////////////////MEDICATION STATEMENT SNOWFLAKE JSON Data///////////////////////////////////////////")
# Open JSON to read data to make comparisons

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
pfilemedstatinput = (dir_path + '/' +'MEDICATION STATEMENT/MedicationStatement_SampleData_Input.json')

#Loading file into function using defined path
dataMedstatInput = getResourceFile(pfilemedstatinput)

#Traversing through json to identify the key values for validation
print(dataMedstatInput['NDC_CODE']) 
print(dataMedstatInput['NDC_DESCRIPTION'])
print(dataMedstatInput['FIRSTNAME']) 
print(dataMedstatInput['MIDDLENAME']) 
print(dataMedstatInput['LASTNAME']) 

print("////////////////////////////MEDICATION STATEMENT Transformed JSON Data///////////////////////////////////////////")
# Open Transformed JSON and retrieve values

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
pfilemedstatoutput = (dir_path + '/' +'MEDICATION STATEMENT/MedicationStatement_Transformed.json')

#Loading transformed JSON using function
dataTransformermedstat = getResourceFile(pfilemedstatoutput)

# pulling key value NDC_CODE from patient profile
print(dataTransformermedstat['contained'][0]['code']['coding'][0]['code'])    

# pulling key value NDC_DESCRIPTION from patient profile
print(dataTransformermedstat['contained'][0]['code']['coding'][0]['display'])  

# pulling key value FIRSTNAME from patient profile
print(dataTransformermedstat['subject']['display'].split(' ')[0])   

# pulling key value MIDDLENAME from patient profile
print(dataTransformermedstat['subject']['display'].split(' ')[1])

# pulling key value LASTNAME from patient profile      
print(dataTransformermedstat['subject']['display'].split(' ')[2])  

# Open JSON to read data to make comparisons

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
pfileepiinput = (dir_path + '/' +'EPISODEOFCARE/EpisodeOfCare_SampleData_Input.json')

print("////////////////////////////EPISODEOFCARE SNOWFLAKE JSON Data///////////////////////////////////////////")
# Open JSON to read data to make comparisons

#Loading file into function using defined path
dataSnwEpiInput = getResourceFile(pfileepiinput)

#Traversing through json to identify the key values for validation
print(dataSnwEpiInput['CENSEOID']) 
print(dataSnwEpiInput['STATUS_CODE'])
print(dataSnwEpiInput['DATE_OF_SERVICE']) 
#print(dataSnwEpiInput['DX_1']) 
print(dataSnwEpiInput['MEMBER_NAME']) 

#rank logic
if dataSnwEpiInput['DX_1'] == '':
        Epirank = '0'
else: 
        Epirank = '1'
print (Epirank)

print("////////////////////////////EPISODEOFCARE Transformed JSON Data///////////////////////////////////////////")
# Open Transformed JSON and retrieve values

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
pfileEpioutput = (dir_path + '/' +'EPISODEOFCARE/EpisodeOfCare_Transformed.json')

#Loading transformed JSON using function
dataTransformerEpi = getResourceFile(pfileEpioutput)

# pulling key value CENSEOID from patient profile
print(dataTransformerEpi['identifier'][0]['value'])    

# pulling key value STATUS_CODE from patient profile
print(dataTransformerEpi['status'])  

# pulling key value DATE_OF_SERVICE from patient profile
print(dataTransformerEpi['statusHistory'][0]['period']['start'])   

# pulling key value DX_1 from patient profile
print(dataTransformerEpi['diagnosis'][0]['rank'])

# pulling key value MEMBER_NAME from patient profile      
print(dataTransformerEpi['patient']['display'])   

# Open JSON to read data to make comparisons

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
pfileProcinput = (dir_path + '/' +'PROCEDURE/Procedure_SampleData_Input.json')

print("////////////////////////////PROCEDURE SNOWFLAKE JSON Data///////////////////////////////////////////")
# Open JSON to read data to make comparisons

#Loading file into function using defined path
dataSnwProcInput = getResourceFile(pfileProcinput)

Dx_count =0
#Traversing through json to identify the key values for validation
print(dataSnwProcInput['CPTCODE_PRIMARY'])
print(dataSnwProcInput['PROCEDURE_CODE_2'])
print(dataSnwProcInput['DATE_OF_SERVICE'].split(' ')[0]) 
print(dataSnwProcInput['CENSEOID'])
print(dataSnwProcInput['MEMBER_NUMBER'])
print(dataSnwProcInput['HICN'])

#Printing all DX_codes that are not Null
for x in range(30):
      if dataSnwProcInput['DX_'+ str(x+1)]!='':
        Dx_count+=1
        print(dataSnwProcInput['DX_'+ str(x+1)])


print("////////////////////////////PROCEDURE Transformed JSON Data///////////////////////////////////////////")
# Open Transformed JSON and retrieve values

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
pfileProcoutput = (dir_path + '/' +'PROCEDURE/Procedure_Transformed.json')

#Loading transformed JSON using function
dataTransformerProc = getResourceFile(pfileProcoutput)

#pulling key value CPTCODE_PRIMARY from patient profile
print(dataTransformerProc['code']['coding'][0]['code'])  

#pulling key value PROCEDURE_CODE_2 from patient profile
print(dataTransformerProc['code']['coding'][1]['code'])  

#pulling key value Date of Service from patient profile
print(dataTransformerProc['performedPeriod']['start'])  

#pulling key value CENSEOID from patient profile
print(dataTransformerProc['identifier'][0]['value'])  

#pulling key value MEMBER_NUMBER from patient profile
print(dataTransformerProc['identifier'][1]['value'])  

#pulling key value HICN from patient profile
print(dataTransformerProc['identifier'][2]['value'])  

#Printing all DX_codes that are not Null
for y in range(Dx_count):
        if dataTransformerProc['reasonCode'][0]['coding'][y]['code']!='':
                # pulling key value AdmissionDate from patient profile
                print(dataTransformerProc['reasonCode'][0]['coding'][y]['code']) 

print("////////////////////////////OBSERVATION SNOWFLAKE JSON Data///////////////////////////////////////////")
# Open JSON to read data to make comparisons

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
pfileObservinput = (dir_path + '/' +'OBSERVATION/Observation_SampleData_input.json')

print("////////////////////////////OBSERVATION SNOWFLAKE JSON Data///////////////////////////////////////////")
# Open JSON to read data to make comparisons

#Loading file into function using defined path
dataSnwObservInput = getResourceFile(pfileObservinput) 

print(dataSnwObservInput['CENSEOID'])
print(dataSnwObservInput['HICN'])
print(dataSnwObservInput['LABTESTID'])
print(dataSnwObservInput['LOINC'])
#print(dataSnwObservInput['PATIENT_FHIR_ID'])
#print(dataSnwObservInput['MEMBER_NAME'])
print(dataSnwObservInput['LABRESULTSDATECOLLECTED'].split(' ')[0])
print(dataSnwObservInput['LABRESULTSDATERELEASED'].split(' ')[0])
print(dataSnwObservInput['ABNORMALINDICATOR'])
print(dataSnwObservInput['LABRESULTSCOMMENT'])
print(dataSnwObservInput['NORMALSLOW'])
print(dataSnwObservInput['RESULTSUNITS'])
print(dataSnwObservInput['NORMALSHIGH'])
print(dataSnwObservInput['RESULTSUNITS'])

#Abnormal Indicator logic
if (dataSnwObservInput['ABNORMALINDICATOR']) =='N':
        input_abnormalIndicator ="Normal"
elif (dataSnwObservInput['ABNORMALINDICATOR']) =='A':
        input_abnormalIndicator ="Abnormal"
elif (dataSnwObservInput['ABNORMALINDICATOR']) =='H':
        input_abnormalIndicator ="High"
elif (dataSnwObservInput['ABNORMALINDICATOR']) =='L':
        input_abnormalIndicator ="Low"
else: input_abnormalIndicator ="other"
print (input_abnormalIndicator)

# Open Transformed JSON and retrieve values

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
pfileObservoutput = (dir_path + '/' +'OBSERVATION/Observation_Transformed.json')

#Loading transformed JSON using function
dataTransformerObserv = getResourceFile(pfileObservoutput)



#pulling key value CENSEOID from observation profile
print(dataTransformerObserv['identifier'][0]['value'])  

#pulling key value HICN from observation profile
print(dataTransformerObserv['identifier'][1]['value'])     

#pulling key value LOINC from observation profile
print(dataTransformerObserv['code']['coding'][0]['code'])  

#pulling key value PATIENT_FHIR_ID from observation profile
print(dataTransformerObserv['subject']['reference'])  

#pulling key value MEMBER_NAME from observation profile
#print(dataTransformerObserv['subject']['display'])  

#pulling key value LABRESULTSDATECOLLECTED from observation profile
print(dataTransformerObserv['effectiveDateTime'])  

#pulling key value LABRESULTSDATERELEASED from observation profile
print(dataTransformerObserv['issued'])  

#pulling key value LABRESULTVALUE from observation profile
print(dataTransformerObserv['valueQuantity']['value']) 

#pulling key value RESULTSUNITS from observation profile
print(dataTransformerObserv['valueQuantity']['unit'])  

#pulling key value ABNORMALINDICATOR from observation profile
print(dataTransformerObserv['interpretation'][0]['coding'][0]['display']) 


#pulling key value LABRESULTSCOMMENTS from observation profile
print(dataTransformerObserv['note'][0]['text'])  

#pulling key value NORMALSLOW from observation profile
print(dataTransformerObserv['referenceRange'][0]['low']['value'])  

#pulling key value RESULTSUNITS from observation profile
print(dataTransformerObserv['referenceRange'][0]['low']['unit'])   

#pulling key value NORMALSHIGH from observation profile
print(dataTransformerObserv['referenceRange'][0]['high']['value'])

#pulling key value RESULTSUNITS from observation profile
print(dataTransformerObserv['referenceRange'][0]['high']['unit'])   



print("////////////////////////////IMMUNIZATION SNOWFLAKE JSON Data///////////////////////////////////////////")
# Open JSON to read data to make comparisons

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
pfileImmuninput = (dir_path + '/' +'IMMUNIZATION/Immunization_SampleData_Input.json')

print("////////////////////////////IMMUNIZATION SNOWFLAKE JSON Data///////////////////////////////////////////")
# Open JSON to read data to make comparisons

#Loading file into function using defined path
dataSnwImmunInput = getResourceFile(pfileImmuninput) 

print(dataSnwImmunInput['DATEOFSERVICE'])
print(dataSnwImmunInput['CENSEOID'])
print(dataSnwImmunInput['CLIENTID'])
print(dataSnwImmunInput['LASTNAME'])
print(dataSnwImmunInput['FIRSTNAME'])
print(dataSnwImmunInput['DOB'])
print(dataSnwImmunInput['SECTIONDISPLAYTEXT'])
print(dataSnwImmunInput['QUESTIONTEXT'])
print(dataSnwImmunInput['ANSWERTEXT'])

#ANSWERTEXT logic
if (dataSnwImmunInput['ANSWERTEXT']) =='Yes':
        input_immunstatus ="Normal"
elif (dataSnwImmunInput['ANSWERTEXT']) =='No':
        input_immunstatus ="Abnormal"
else: input_immunstatus =""
print (input_immunstatus)

# Open Transformed JSON and retrieve values

#Loading the absolute path to be passed into function
#Access parent directory and create path to load snowflake input file into function
pfileImmunoutput = (dir_path + '/' +'IMMUNIZATION/Immunization_Transformed.json')

#Loading transformed JSON using function
dataTransformerImmun = getResourceFile(pfileImmunoutput)

#pulling key value DATEOFSERVICE from Immunization profile
print(dataTransformerImmun['note'][0]['time']) 

#pulling key value CENSEOID from Immunization profile
print(dataTransformerImmun['identifier'][0]['value'])  

#pulling key value QUESTIONTEXT from Immunization profile
print(dataTransformerImmun['vaccineCode']['text'].split(' ')[0])

#pulling key value ANSWERTEXT from Immunization profile
print(dataTransformerImmun['vaccineCode']['text'].split(' ')[1])


#pulling key value SECTIONDISPLAYTEXT from Immunization profile
print(dataTransformerImmun['note'][0]['text'].split(' ')[0], dataTransformerImmun['note'][0]['text'].split(' ')[1])

#pulling key value QUESTIONTEXT2 from Immunization profile
print(dataTransformerImmun['note'][0]['text'].split(' ')[2])

#pulling key value ANSWERTEXT from Immunization profile
print(dataTransformerImmun['note'][0]['text'].split(' ')[3]) 

trans_noteText = dataTransformerImmun['note'][0]['text'].split(' ')[0] + ' ' + dataTransformerImmun['note'][0]['text'].split(' ')[1] +  ' ' + dataTransformerImmun['note'][0]['text'].split(' ')[2] +  ' ' + dataTransformerImmun['note'][0]['text'].split(' ')[3]
print(trans_noteText)

#pulling key value PATIENT_FHIR_ID from Immunization profile
print(dataTransformerImmun['patient']['reference'])  







