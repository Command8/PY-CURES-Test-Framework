import unittest
import json

#Procedure to import file from different folder using sys, path, append
import sys
sys.path.append(".")
from Read_JSON import dataSnwPatInput,dataTransformerpat,input_memgender

#Write class to run unit tests. These are created to retrieve the values from Snowflake and transformed JSONs and perform comparison 
#between them to ensure that the snowflake JSON transformation is successful when created using liquid FHIR template

class TestTransform (unittest.TestCase):    
    
    #Validation of Member last name between snowflake JSON and transformed patient JSON 
    # if statements are written to display message in vs code for all passed tests   
    
    # Patient Tests start here
    def test_patientlname(self):
        if dataSnwPatInput['MEMBER_LAST_NAME'] == dataTransformerpat['name'][0]['family']:
            print('MEMBER_LAST_NAME Matched')        
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwPatInput['MEMBER_LAST_NAME'],dataTransformerpat['name'][0]['family'],"MEMBER_LAST_NAME not Matched")          
             
    #Validation of Member first name between snowflake JSON and transformed patient JSON
    def test_patientfname(self):
        if dataSnwPatInput['MEMBER_FIRST_NAME'] == dataTransformerpat['name'][0]['given'][0]:
            print('MEMBER_FIRST_NAME Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwPatInput['MEMBER_FIRST_NAME'],dataTransformerpat['name'][0]['given'][0],"MEMBER_FIRST_NAME not Matched")

    #Validation of Member last name between snowflake JSON and transformed patient JSON
    def test_patientmname(self):
        if dataSnwPatInput['MEMBER_MIDDLE_NAME'] == dataTransformerpat['name'][0]['given'][1]:
            print('MEMBER_MIDDLE_NAME Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwPatInput['MEMBER_MIDDLE_NAME'],dataTransformerpat['name'][0]['given'][1],"MEMBER_MIDDLE_NAME not Matched")
    
    #Validation of Member censeoid between snowflake JSON and transformed patient JSON
    def test_patientcenseoid(self):
        if dataSnwPatInput['CENSEOID'] == dataTransformerpat['identifier'][0]['value']:
            print('Member CENSEOID Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwPatInput['CENSEOID'],dataTransformerpat['identifier'][0]['value'],"CENSEOID not Matched")  
    
    #Validation of Member censeoid between snowflake JSON and transformed patient JSON
    def test_patientadd1(self):
        if dataSnwPatInput['MEMBER_ADDRESS1'] == dataTransformerpat['address'][0]['line'].split(',')[0]:
            print('MEMBER_ADDRESS1 Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwPatInput['MEMBER_ADDRESS1'],dataTransformerpat['address'][0]['line'].split(',')[0],"MEMBER_ADDRESS1 not Matched") 
    
    #Validation of Member address 2 between snowflake JSON and transformed patient JSON
    def test_patientadd2(self):
        if str(dataSnwPatInput['MEMBER_ADDRESS2']) == dataTransformerpat['address'][0]['line'].split(',')[1].strip():
            print('MEMBER_ADDRESS2 Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(str(dataSnwPatInput['MEMBER_ADDRESS2']),dataTransformerpat['address'][0]['line'].split(',')[1].strip(),"MEMBER_ADDRESS2 not Matched") 
    
    #Validation of Member city between snowflake JSON and transformed patient JSON
    def test_patientcity(self):
        if dataSnwPatInput['MEMBER_CITY'] == dataTransformerpat['address'][0]['city']:
            print('MEMBER_CITY Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwPatInput['MEMBER_CITY'],dataTransformerpat['address'][0]['city'],"MEMBER_CITY not Matched") 
    
    #Validation of Member state between snowflake JSON and transformed patient JSON
    def test_patientstate(self):
        if dataSnwPatInput['MEMBER_STATE'] == dataTransformerpat['address'][0]['state']:
            print('MEMBER_STATE Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwPatInput['MEMBER_STATE'],dataTransformerpat['address'][0]['state'],"MEMBER_STATE not Matched") 
    
    #Validation of Member county between snowflake JSON and transformed patient JSON
    def test_patientcounty(self):
        if dataSnwPatInput['MEMBER_COUNTY'] == dataTransformerpat['address'][0]['district']:
            print('MEMBER_COUNTY Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwPatInput['MEMBER_COUNTY'],dataTransformerpat['address'][0]['district'],"MEMBER_COUNTY not Matched")
    
    #Validation of Member DOB between snowflake JSON and transformed patient JSON
    def test_patientdob(self):
        if (dataSnwPatInput['MEMBER_DATE_OF_BIRTH'].split(' ')[0]) == dataTransformerpat['birthDate']:
            print('MEMBER_DATE_OF_BIRTH Matched')
        #Prints message if the test fails for comparison
        self.assertEqual((dataSnwPatInput['MEMBER_DATE_OF_BIRTH'].split(' ')[0]),dataTransformerpat['birthDate'],"MEMBER_DATE_OF_BIRTH not Matched")
    
    #Validation of Member DOB between snowflake JSON and transformed patient JSON
    def test_patientzip(self):
        if str(dataSnwPatInput['MEMBER_ZIP']) == dataTransformerpat['address'][0]['postalCode']:
            print('MEMBER_ZIP Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(str(dataSnwPatInput['MEMBER_ZIP']),dataTransformerpat['address'][0]['postalCode'],"MEMBER_ZIP not Matched")
    
    #Validation of Member GENDER between snowflake JSON and transformed patient JSON
    def test_patientgender(self):
        if input_memgender == dataTransformerpat['gender']:
            print('Member GENDER Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(input_memgender,dataTransformerpat['gender'],"MEMBER GENDER not Matched")
    
    #Validation of Member ETHNICITY between snowflake JSON and transformed patient JSON
    def test_patientethnicity(self):
        if dataSnwPatInput['ETHNICITY']== dataTransformerpat['extension'][0]['extension'][0]['valueString']:
            print('Member ETHNICITY Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwPatInput['ETHNICITY'],dataTransformerpat['extension'][0]['extension'][0]['valueString'],"MEMBER ETHNICITY not Matched")
    
    #Validation of PCP_Firstname between snowflake JSON and transformed patient JSON
    def test_pcpfirstname(self):
        if dataSnwPatInput['PCP_FIRSTNAME'] == dataTransformerpat['generalPractitioner'][0]['display'].split(' ')[0]:
            print('PCP_FIRSTNAME Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwPatInput['PCP_FIRSTNAME'],dataTransformerpat['generalPractitioner'][0]['display'].split(' ')[0],"PCP_FIRSTNAME not Matched")
    
    #Validation of PCP_Lastname between snowflake JSON and transformed patient JSON
    def test_pcplastname(self):
        if dataSnwPatInput['PCP_LASTNAME'] == dataTransformerpat['generalPractitioner'][0]['display'].split(' ')[1]:
            print('PCP_LASTNAME Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwPatInput['PCP_LASTNAME'],dataTransformerpat['generalPractitioner'][0]['display'].split(' ')[1],"PCP_LASTNAME not Matched")

if __name__ == '__main__':
    unittest.main()