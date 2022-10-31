import unittest
import json

#Procedure to import file from different folder using sys, path, append
import sys
sys.path.append(".")
from Read_JSON import dataMedstatInput,dataTransformermedstat

#Write class to run unit tests. These are created to retrieve the values from Snowflake and transformed JSONs and perform comparison 
#between them to ensure that the snowflake JSON transformation is successful when created using liquid FHIR template

class TestTransform (unittest.TestCase):    
    
    # if statements are written to display message in vs code for all passed tests   
    
    # Medication Statement Tests start here
    #Validation of NDC_CODE between snowflake JSON and transformed JSON
    def test_medstatndccode(self):
        if dataMedstatInput['NDC_CODE'] == dataTransformermedstat['contained'][0]['code']['coding'][0]['code']:
            print('NDC_CODE Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataMedstatInput['NDC_CODE'],dataTransformermedstat['contained'][0]['code']['coding'][0]['code'],"NDC_CODE not Matched")

    #Validation of HICN between snowflake JSON and transformed JSON
    def test_medstatndcdesc(self):
        if dataMedstatInput['NDC_DESCRIPTION'] == dataTransformermedstat['contained'][0]['code']['coding'][0]['display']:
            print('NDC_DESCRIPTION Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataMedstatInput['NDC_DESCRIPTION'],dataTransformermedstat['contained'][0]['code']['coding'][0]['display']),"NDC_DESCRIPTION not Matched"

    #Validation of FIRSTNAME between snowflake JSON and transformed JSON
    def test_medstatfname(self):
        if dataMedstatInput['FIRSTNAME'] == dataTransformermedstat['subject']['display'].split(' ')[0]:
            print('FIRSTNAME Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataMedstatInput['FIRSTNAME'],dataTransformermedstat['subject']['display'].split(' ')[0],"FIRSTNAME not Matched")

    #Validation of MIDDLENAME between snowflake JSON and transformed JSON
    def test_medstatmname(self):
        if dataMedstatInput['MIDDLENAME'] == dataTransformermedstat['subject']['display'].split(' ')[1]:
            print('MIDDLENAME Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataMedstatInput['MIDDLENAME'],dataTransformermedstat['subject']['display'].split(' ')[1],"MIDDLENAME not Matched") 

    #Validation of LASTNAME between snowflake JSON and transformed JSON
    def test_medstatlname(self):
        if dataMedstatInput['LASTNAME'] == dataTransformermedstat['subject']['display'].split(' ')[2]:
            print('LASTNAME Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataMedstatInput['LASTNAME'],dataTransformermedstat['subject']['display'].split(' ')[2],"LASTNAME not Matched") 
    
if __name__ == '__main__':
    unittest.main()