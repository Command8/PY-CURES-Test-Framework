import unittest
import json

#Procedure to import file from different folder using sys, path, append
import sys
sys.path.append(".")
from Read_JSON import dataSnwPracInput,dataTransformerPrac

#Write class to run unit tests. These are created to retrieve the values from Snowflake and transformed JSONs and perform comparison 
#between them to ensure that the snowflake JSON transformation is successful when created using liquid FHIR template

class TestTransform (unittest.TestCase):    
    
    #Validation of Member last name between snowflake JSON and transformed patient JSON 
    # if statements are written to display message in vs code for all passed tests   
    
    # Practitioner Tests start here
    #Validation of PROVIDER_ID between snowflake JSON and transformed practitioner JSON
    def test_practitionerid(self):
        if dataSnwPracInput['PROVIDER_ID'] == dataTransformerPrac['identifier'][10]['value']:
            print('PROVIDER_ID Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwPracInput['PROVIDER_ID'],dataTransformerPrac['identifier'][10]['value'],"PROVIDER_ID not Matched")

    #Validation of PROVIDER_NPI between snowflake JSON and transformed practitioner JSON
    def test_practitionernpi(self):
        if dataSnwPracInput['PROVIDER_NPI'] == dataTransformerPrac['identifier'][1]['value']:
            print('PROVIDER_NPI Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwPracInput['PROVIDER_NPI'],dataTransformerPrac['identifier'][1]['value'],"PROVIDER_NPI not Matched") 

    #Validation of PROVIDER_PIN between snowflake JSON and transformed practitioner JSON
    def test_practitionerpin(self):
        if dataSnwPracInput['PROVIDER_PIN'] == dataTransformerPrac['identifier'][2]['value']:
            print('PROVIDER_PIN Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwPracInput['PROVIDER_PIN'],dataTransformerPrac['identifier'][2]['value'],"PROVIDER_PIN not Matched") 

    #Validation of PROVIDER_TAXID between snowflake JSON and transformed practitioner JSON
    def test_practitionertxid(self):
        if dataSnwPracInput['PROVIDER_TAXID'] == dataTransformerPrac['identifier'][3]['value']:
            print('PROVIDER_TAXID Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwPracInput['PROVIDER_TAXID'],dataTransformerPrac['identifier'][3]['value'],"PROVIDER_TAXID not Matched")

    #Validation of PROVIDER_FIRSTNAME between snowflake JSON and transformed practitioner JSON
    def test_practitionerfname(self):
        if dataSnwPracInput['PROVIDER_FIRSTNAME'] == dataTransformerPrac['name'][0]['given'][0]:
            print('PROVIDER_FIRSTNAME Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwPracInput['PROVIDER_FIRSTNAME'],dataTransformerPrac['name'][0]['given'][0],"PROVIDER_FIRSTNAME not Matched")
     
    #Validation of PROVIDER_LASTNAME between snowflake JSON and transformed practitioner JSON 
    def test_practitionerlname(self):
        if dataSnwPracInput['PROVIDER_LASTNAME'] == dataTransformerPrac['name'][0]['family']:
            print('PROVIDER_LASTNAME Matched')        
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwPracInput['PROVIDER_LASTNAME'],dataTransformerPrac['name'][0]['family'],"PROVIDER_LASTNAME not Matched")   

    #Validation of PROVIDER_MIDDLE_Initial between snowflake JSON and transformed practitioner JSON 
    def test_practitionermi(self):
        if dataSnwPracInput['PROVIDER_MIDDLE_Initial'] == dataTransformerPrac['name'][0]['given'][1]:
            print('PROVIDER_MIDDLE_Initial Matched')        
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwPracInput['PROVIDER_MIDDLE_Initial'],dataTransformerPrac['name'][0]['given'][1],"PROVIDER_MIDDLE_Initial not Matched")        

    #Validation of PCP_ID between snowflake JSON and transformed practitioner JSON
    def test_practitionerpcpid(self):
        if dataSnwPracInput['PCP_ID'] == dataTransformerPrac['identifier'][0]['value']:
            print('PCP_ID Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwPracInput['PCP_ID'],dataTransformerPrac['identifier'][0]['value'],"PCP_ID not Matched")

    #Validation of IPA between snowflake JSON and transformed practitioner JSON
    def test_practitioneripa(self):
        if dataSnwPracInput['IPA'] == dataTransformerPrac['identifier'][4]['value']:
            print('IPA Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwPracInput['IPA'],dataTransformerPrac['identifier'][4]['value'],"IPA not Matched")

    #Validation of IPA_IDENTIFIER between snowflake JSON and transformed practitioner JSON
    def test_practitioneripaid(self):
        if dataSnwPracInput['IPA_IDENTIFIER'] == dataTransformerPrac['identifier'][5]['value']:
            print('IPA_IDENTIFIER Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwPracInput['IPA_IDENTIFIER'],dataTransformerPrac['identifier'][5]['value'],"IPA_IDENTIFIER not Matched")

    #Validation of LPO between snowflake JSON and transformed practitioner JSON
    def test_practitionerlpo(self):
        if dataSnwPracInput['LPO'] == dataTransformerPrac['identifier'][6]['value']:
            print('LPO Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwPracInput['LPO'],dataTransformerPrac['identifier'][6]['value'],"LPO not Matched")

    #Validation of LPO_IDENTIFIER between snowflake JSON and transformed practitioner JSON
    def test_practitionerlpoid(self):
        if dataSnwPracInput['LPO_IDENTIFIER'] == dataTransformerPrac['identifier'][7]['value']:
            print('LPO_IDENTIFIER Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwPracInput['LPO_IDENTIFIER'],dataTransformerPrac['identifier'][7]['value'],"LPO_IDENTIFIER not Matched")

    #Validation of SUBSCRIBER_ID between snowflake JSON and transformed practitioner JSON
    def test_practitionersbid(self):
        if dataSnwPracInput['SUBSCRIBER_ID'] == dataTransformerPrac['identifier'][8]['value']:
            print('SUBSCRIBER_ID Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwPracInput['SUBSCRIBER_ID'],dataTransformerPrac['identifier'][8]['value'],"SUBSCRIBER_ID not Matched")        
     

if __name__ == '__main__':
    unittest.main()