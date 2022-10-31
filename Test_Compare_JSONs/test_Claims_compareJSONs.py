from pickle import FALSE
import unittest
import json
#Procedure to import file from different folder using sys, path, append
import sys
sys.path.append(".")
from Read_JSON import clmsdataTransformer,ClaimsDataInput
import datetime



class TestTransform (unittest.TestCase):  
 #IDENTIFIER   
 #Validation of Claims - ClaimNumber value between input json and transformed Claims JSON    
    def test_claimclaimnum(self):
        if ClaimsDataInput['ClaimNumber'] == clmsdataTransformer['identifier']['value']:
            print(ClaimsDataInput['ClaimNumber'])
        self.assertEqual(ClaimsDataInput['ClaimNumber'],clmsdataTransformer['identifier']['value'],"ClaimNumber not present in the fhir resource") 

#STATUS
#Validation of Claims - ClaimPaymentStatus value between input json and transformed Claims JSON    
    def test_claimstatus(self):
        if ClaimsDataInput['ClaimPaymentStatus'] == clmsdataTransformer['status']:
            print(ClaimsDataInput['ClaimPaymentStatus'])
        self.assertEqual(ClaimsDataInput['ClaimPaymentStatus'],clmsdataTransformer['status'],"ClaimPaymentStatus not present in the fhir resource") 

#Validation of Claim - CenseoID value between input json and transformed Claims JSON    
    def test_claimpatientid(self):
        if ClaimsDataInput['CenseoID'] == clmsdataTransformer['patient']['reference'].split('/')[1].strip():
            print(ClaimsDataInput['CenseoID'])
        self.assertEqual(ClaimsDataInput['CenseoID'],clmsdataTransformer['patient']['reference'].split('/')[1].strip(),"claim status not present in the fhir resource") 

#Validation of Claims - ServiceFromDate_Date_of_Service value between input json and transformed Claims JSON    
    def test_claimbillablstart(self):
        d = datetime.datetime.strptime(ClaimsDataInput['ServiceFromDate_Date_of_Service'], '%m/%d/%Y').strftime('%Y-%m-%d')
        print(d)
        if d == clmsdataTransformer['billablePeriod']['start']:
            print(ClaimsDataInput['ServiceFromDate_Date_of_Service'])
        self.assertEqual(d,clmsdataTransformer['billablePeriod']['start'],"ServiceFromDate_Date_of_Service not present in the fhir resource") 

#Validation of Claims - ServiceThruDate value between input json and transformed Claims JSON    
    def test_claimbillableend(self):
        d = datetime.datetime.strptime(ClaimsDataInput['ServiceThruDate'], '%m/%d/%Y').strftime('%Y-%m-%d')
        print(d)
        if d == clmsdataTransformer['billablePeriod']['end']:
            print(ClaimsDataInput['ServiceThruDate'])
        self.assertEqual(d,clmsdataTransformer['billablePeriod']['end'],"ServiceThruDate not present in the fhir resource") 

#Validation of Claims - ClaimEntryDate value between input json and transformed Claims JSON    
    def test_claimcreated(self):
        d = datetime.datetime.strptime(ClaimsDataInput['ClaimEntryDate'], '%m/%d/%Y').strftime('%Y-%m-%d')
        print(d)
        if d == print(clmsdataTransformer['created']) :
            print("Converted date: ",ClaimsDataInput['ClaimEntryDate'])
        self.assertEqual(d, clmsdataTransformer['created'] ,"ClaimEntryDate not present in the fhir resource") 

#Validation of Claims - Provider_ID value between input json and transformed Claims JSON    
    def test_claimeenterer(self):
        if ClaimsDataInput['Provider_ID'] == print(clmsdataTransformer['enterer']['reference'].split('/')[1].strip()) :
            print(ClaimsDataInput['Provider_ID'])
        self.assertEqual(ClaimsDataInput['Provider_ID'], clmsdataTransformer['enterer']['reference'].split('/')[1].strip() ,"Provider_ID not present in the fhir resource") 

#Validation of Claims - RenderingProviderNPI value between input json and transformed Claims JSON    
    def test_claimspayee(self):
        if ClaimsDataInput['RenderingProviderNPI'] == print(clmsdataTransformer['payee']['type']['coding'][0]['display']) :
            print(ClaimsDataInput['RenderingProviderNPI'])
        self.assertEqual(ClaimsDataInput['RenderingProviderNPI'], clmsdataTransformer['payee']['type']['coding'][0]['display'],"RenderingProviderNPI not present in the fhir resource") 

#Validation of Claims - PlaceOfService value between input json and transformed Claims JSON    
    def test_claimfacility(self):
        if ClaimsDataInput['PlaceOfService'] == print(clmsdataTransformer['facility']['identifier']['value']) :
            print(ClaimsDataInput['PlaceOfService'])
        self.assertEqual(ClaimsDataInput['PlaceOfService'], clmsdataTransformer['facility']['identifier']['value'],"PlaceOfService not present in the fhir resource") 

#Validation of Claims - careTeam value between input json and transformed Claims JSON    
    def test_claimcareteamref(self):
        if ClaimsDataInput['Provider_ID'] == print(clmsdataTransformer['careTeam'][0]['provider']['reference'].split('/')[1].strip()) :
            print(ClaimsDataInput['Provider_ID'])
        self.assertEqual(ClaimsDataInput['Provider_ID'], clmsdataTransformer['careTeam'][0]['provider']['reference'].split('/')[1].strip(),"Provider_ID not present in the fhir resource") 

#Validation of Claims - DX_1 value between input json and transformed Claims JSON    
    def test_claimdiagnosis1(self):
        if ClaimsDataInput['DX_1'] == print(clmsdataTransformer['diagnosis'][0]['diagnosisCodeableConcept']['coding'][0]['code']) :
            print(ClaimsDataInput['DX_1'])
        self.assertEqual(ClaimsDataInput['DX_1'], clmsdataTransformer['diagnosis'][0]['diagnosisCodeableConcept']['coding'][0]['code'],"DX_1 not present in the fhir resource") 
#Validation of Claims - DX_2 value between input json and transformed Claims JSON    
    def test_claimdiagnosis2(self):
        if ClaimsDataInput['DX_2'] == print(clmsdataTransformer['diagnosis'][1]['diagnosisCodeableConcept']['coding'][0]['code']) :
            print(ClaimsDataInput['DX_2'])
        self.assertEqual(ClaimsDataInput['DX_2'], clmsdataTransformer['diagnosis'][1]['diagnosisCodeableConcept']['coding'][0]['code'],"DX_2 not present in the fhir resource") 
#Validation of Claims - DX_3 value between input json and transformed Claims JSON    
    def test_claimdiagnosis3(self):
        if ClaimsDataInput['DX_3'] == print(clmsdataTransformer['diagnosis'][2]['diagnosisCodeableConcept']['coding'][0]['code']) :
            print(ClaimsDataInput['DX_3'])
        self.assertEqual(ClaimsDataInput['DX_3'], clmsdataTransformer['diagnosis'][2]['diagnosisCodeableConcept']['coding'][0]['code'],"DX_3 not present in the fhir resource") 

#Validation of Claims - ServiceFromDate value between input json and transformed Claims JSON    
    def test_claimsprocedurestart(self):
        if ClaimsDataInput['ServiceFromDate'] == print(clmsdataTransformer['procedure'][0]['date']) :
            print(ClaimsDataInput['ServiceFromDate'])
        self.assertEqual(ClaimsDataInput['ServiceFromDate'],clmsdataTransformer['procedure'][0]['date'],"ServiceFromDate not present in the fhir resource") 
#Validation of Claims - CPTCode_Primary value between input json and transformed Claims JSON    
    def test_claimsprocedurestart(self):
        if ClaimsDataInput['ProcedureCode_CPTCode_Primary'] == print(clmsdataTransformer['procedure'][0]['procedureCodeableConcept']['coding'][0]['code']):
            print(ClaimsDataInput['ProcedureCode_CPTCode_Primary'])
        self.assertEqual(ClaimsDataInput['ProcedureCode_CPTCode_Primary'],clmsdataTransformer['procedure'][0]['procedureCodeableConcept']['coding'][0]['code'],"CPTCode_Primary not present in the fhir resource") 

#Validation of Claims - BillAmount value between input json and transformed Claims JSON    
    def test_claimstotal(self):
        if ClaimsDataInput['BillAmount'] == print(clmsdataTransformer['total']['value']):
            print(ClaimsDataInput['BillAmount'])
        self.assertEqual(ClaimsDataInput['BillAmount'],clmsdataTransformer['total']['value'],"BillAmount not present in the fhir resource") 



if __name__ == '__main__':
    unittest.main()