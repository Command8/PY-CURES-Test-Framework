from pickle import FALSE
import unittest
#Procedure to import file from different folder using sys, path, append
import sys
sys.path.append(".")
from Read_JSON import medreqdataTransformer,MedRequestDataInput
import datetime



class TestTransform (unittest.TestCase):  
 #IDENTIFIER   
 #Validation of MedicationRequest - CENSEOID value between input json and transformed JSON    
    def test_medreqidentifier(self):
        if MedRequestDataInput['CENSEOID'] == medreqdataTransformer['identifier'][0]['value']:
            print(MedRequestDataInput['CENSEOID'])
        self.assertEqual(MedRequestDataInput['CENSEOID'],medreqdataTransformer['identifier'][0]['value'],"CENSEOID not present in the fhir resource") 

#AUTHOREDON
#Validation of MedicationRequest - DATE_OF_SERVICE value between input json and transformed JSON    
    def test_medreqauthoredon(self):
        if MedRequestDataInput['DATE_OF_SERVICE'] == medreqdataTransformer['authoredOn']:
            print(MedRequestDataInput['DATE_OF_SERVICE'])
        self.assertEqual(MedRequestDataInput['DATE_OF_SERVICE'],medreqdataTransformer['authoredOn'],"DATE_OF_SERVICE not present in the fhir resource") 

#MEDICATIONCODEABLECONCEPT1
#Validationn of MedicationRequest - NDC_CODE value between input json and transformed JSON    
    def test_medreqcodeableconcept1(self):
        if MedRequestDataInput['NDC_CODE'] == medreqdataTransformer['medicationCodeableConcept']['coding'][0]['code']:
            print(MedRequestDataInput['NDC_CODE'])
        self.assertEqual(MedRequestDataInput['NDC_CODE'],medreqdataTransformer['medicationCodeableConcept']['coding'][0]['code'],"NDC_CODE not present in the fhir resource") 

#MEDICATIONCODEABLECONCEPT2
#Validationn of MedicationRequest - NDC_DESCRIPTION value between input json and transformed JSON    
    def test_medreqcodableconcept2(self):
        if MedRequestDataInput['NDC_DESCRIPTION'] == medreqdataTransformer['medicationCodeableConcept']['coding'][0]['display']:
            print(MedRequestDataInput['NDC_DESCRIPTION'])
        self.assertEqual(MedRequestDataInput['NDC_DESCRIPTION'],medreqdataTransformer['medicationCodeableConcept']['coding'][0]['display'],"NDC_DESCRIPTION not present in the fhir resource") 




if __name__ == '__main__':
    unittest.main()