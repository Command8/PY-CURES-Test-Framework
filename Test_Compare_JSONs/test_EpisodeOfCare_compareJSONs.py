import unittest
import json

#Procedure to import file from different folder using sys, path, append
import sys
sys.path.append(".")
from Read_JSON import dataSnwEpiInput,dataTransformerEpi,Epirank

#Write class to run unit tests. These are created to retrieve the values from Snowflake and transformed JSONs and perform comparison 
#between them to ensure that the snowflake JSON transformation is successful when created using liquid FHIR template

class TestTransform (unittest.TestCase):    
    
    # if statements are written to display message in vs code for all passed tests   
    
    # EpisodeOfCare Tests start here
    #Validation of CENSEOID between snowflake JSON and transformed JSON
    def test_EpiCenID(self):
        if dataSnwEpiInput['CENSEOID'] == dataTransformerEpi['identifier'][0]['value']:
            print('CENSEOID Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwEpiInput['CENSEOID'],dataTransformerEpi['identifier'][0]['value'],"CENSEOID not Matched")

    #Validation of STATUS_CODE between snowflake JSON and transformed JSON
    def test_Epistscode(self):
        if dataSnwEpiInput['STATUS_CODE'] == dataTransformerEpi['status']:
            print('STATUS_CODE Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwEpiInput['STATUS_CODE'],dataTransformerEpi['status'],"STATUS_CODE not Matched")

    #Validation of DATE_OF_SERVICE between snowflake JSON and transformed JSON
    def test_Epidtofsrvc(self):
        if dataSnwEpiInput['DATE_OF_SERVICE'].split(' ')[0] == dataTransformerEpi['statusHistory'][0]['period']['start']:
            print('DATE_OF_SERVICE Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwEpiInput['DATE_OF_SERVICE'].split(' ')[0],dataTransformerEpi['statusHistory'][0]['period']['start'],"DATE_OF_SERVICE not Matched")

    #Validation of RANK between snowflake JSON and transformed JSON
    def test_EpiRank(self):
        if Epirank == dataTransformerEpi['diagnosis'][0]['rank']:
            print('RANK Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(Epirank,dataTransformerEpi['diagnosis'][0]['rank'],"RANK not Matched") 

    #Validation of MEMBER_NAME between snowflake JSON and transformed JSON
    def test_EpiMemName(self):
        if dataSnwEpiInput['MEMBER_NAME'] == dataTransformerEpi['patient']['display']:
            print('MEMBER_NAME Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwEpiInput['MEMBER_NAME'],dataTransformerEpi['patient']['display'],"MEMBER_NAME not Matched") 
    
    
if __name__ == '__main__':
    unittest.main()