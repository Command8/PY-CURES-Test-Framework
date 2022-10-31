import unittest
import json

#Procedure to import file from different folder using sys, path, append
import sys
sys.path.append(".")
from Read_JSON import dataSnwProcInput,dataTransformerProc,Dx_count

#Write class to run unit tests. These are created to retrieve the values from Snowflake and transformed JSONs and perform comparison 
#between them to ensure that the snowflake JSON transformation is successful when created using liquid FHIR template

class TestTransform (unittest.TestCase):    
    
    # if statements are written to display message in vs code for all passed tests   
    
    #Procedure Tests start here    
    #Validation of CPTCODE_PRIMARY between snowflake JSON and transformed JSON
    def test_procprimcpt(self):
        if dataSnwProcInput['CPTCODE_PRIMARY'] == dataTransformerProc['code']['coding'][0]['code']:
            print('CPTCODE_PRIMARY Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwProcInput['CPTCODE_PRIMARY'],dataTransformerProc['code']['coding'][0]['code'],"CPTCODE_PRIMARY not Matched")


    #Validation of PROCEDURE_CODE_2 between snowflake JSON and transformed JSON
    def test_proccd2(self):
        if dataSnwProcInput['PROCEDURE_CODE_2'] == dataTransformerProc['code']['coding'][1]['code']:
            print('PROCEDURE_CODE_2 Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwProcInput['PROCEDURE_CODE_2'],dataTransformerProc['code']['coding'][1]['code'],"PROCEDURE_CODE_2 not Matched")


    #Validation of DATE OF SERVICE between snowflake JSON and transformed JSON
    def test_procdos(self):
        if dataSnwProcInput['DATE_OF_SERVICE'].split(' ')[0] == dataTransformerProc['performedPeriod']['start']:
            print('DATE_OF_SERVICE Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwProcInput['DATE_OF_SERVICE'].split(' ')[0],dataTransformerProc['performedPeriod']['start'],"DATE_OF_SERVICE not Matched")

    
    #Validation of CENSEOID between snowflake JSON and transformed JSON
    def test_proccensid(self):
        if dataSnwProcInput['CENSEOID'] == dataTransformerProc['identifier'][0]['value']:
            print('CENSEOID Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwProcInput['CENSEOID'],dataTransformerProc['identifier'][0]['value'],"CENSEOID not Matched")
    

    #Validation of MEMBER_NUMBER between snowflake JSON and transformed JSON
    def test_procmemnm(self):
        if dataSnwProcInput['MEMBER_NUMBER'] == dataTransformerProc['identifier'][1]['value']:
            print('MEMBER_NUMBER Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwProcInput['MEMBER_NUMBER'],dataTransformerProc['identifier'][1]['value'],"MEMBER_NUMBER not Matched")

    
    #Validation of HICN between snowflake JSON and transformed JSON
    def test_prochicn(self):
        if dataSnwProcInput['HICN'] == str(dataTransformerProc['identifier'][2]['value']):
            print('HICN Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwProcInput['HICN'],str(dataTransformerProc['identifier'][2]['value']),"HICN not Matched")

    #Validation of DX Codes between snowflake JSON and transformed JSON
    #def test_procdx1(self):
     #   if dataSnwProcInput['DX_1'] == dataTransformerProc['reasonCode'][0]['coding'][0]['code']:
      #      print('AdmissionDate Matched')
        #Prints message if the test fails for comparison
       # self.assertEqual(dataSnwProcInput['DX_1'],dataTransformerProc['reasonCode'][0]['coding'][0]['code'],"AdmissionDate not Matched") 

    #Validation of DX Codes between snowflake JSON and transformed JSON
    def test_procdx(self):
        #Loop runs from 0 till Dx_count
        for y in range(Dx_count):
            if dataSnwProcInput['DX_'+str(y+1)] == dataTransformerProc['reasonCode'][0]['coding'][y]['code']:
                print('Diagnosis Code Matched for DX_' + str(y+1))
            #Prints message if the test fails for comparison
            self.assertEqual(dataSnwProcInput['DX_'+ str(y+1)],dataTransformerProc['reasonCode'][0]['coding'][y]['code'],"Diagnosis Code not Matched for 'DX_'" + str(y+1)) 
        

if __name__ == '__main__':
    unittest.main()