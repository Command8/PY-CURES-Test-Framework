import unittest
import json

#Procedure to import file from different folder using sys, path, append
import sys
sys.path.append(".")
from Read_JSON import dataSnwObservInput,dataTransformerObserv

#Write class to run unit tests. These are created to retrieve the values from Snowflake and transformed JSONs and perform comparison 
#between them to ensure that the snowflake JSON transformation is successful when created using liquid FHIR template

class TestTransform (unittest.TestCase):  
    # if statements are written to display message in vs code for all passed tests   
    
    # Observation Tests start here
    #Validation of CENSEOID between snowflake JSON and transformed JSON
    def test_observcenseiod(self):
        if dataSnwObservInput['CENSEOID'] == dataTransformerObserv['identifier'][0]['value']:
            print('CENSEOID Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwObservInput['CENSEOID'],dataTransformerObserv['identifier'][0]['value'],"CENSEOID not Matched")

    #Validation of HICN between snowflake JSON and transformed JSON
    def test_observhicn(self):
        if dataSnwObservInput['HICN'] == dataTransformerObserv['identifier'][1]['value']:
            print('HICN Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwObservInput['HICN'],dataTransformerObserv['identifier'][1]['value'],"HICN not Matched")

    
    #Validation of LOINC between snowflake JSON and transformed JSON
    def test_observloinc(self):
        if dataSnwObservInput['LOINC'] == dataTransformerObserv['code']['coding'][0]['code']:
            print('LOINC Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwObservInput['LOINC'],dataTransformerObserv['code']['coding'][0]['code'],"LOINC not Matched")

   #Validation of PATIENT_FHIR_ID between snowflake JSON and transformed JSON
   # def test_observpatfhirid(self):
    #    if dataSnwObservInput['PATIENT_FHIR_ID'] == dataTransformerObserv['subject']['reference']:
            #print('PATIENT_FHIR_ID Matched')
        #Prints message if the test fails for comparison
        #self.assertEqual(dataSnwObservInput['PATIENT_FHIR_ID'],dataTransformerObserv['subject']['reference'],"PATIENT_FHIR_ID not Matched")

   #Validation of MEMBER_NAME between snowflake JSON and transformed JSON
    #def test_observmembername(self):
        #if dataSnwObservInput['MEMBER_NAME'] == dataTransformerObserv['subject'][0]['display']:
            #print('MEMBER_NAME Matched')
        #Prints message if the test fails for comparison
        #self.assertEqual(dataSnwObservInput['MEMBER_NAME'],dataTransformerObserv['subject'][0]['display'],"MEMBER_NAME not Matched")

   #Validation of LABRESULTSDATECOLLECTED between snowflake JSON and transformed JSON
    def test_observlabresultsdatecollected(self):
        if dataSnwObservInput['LABRESULTSDATECOLLECTED'].split(' ')[0]== dataTransformerObserv['effectiveDateTime']:
            print('LABRESULTSDATECOLLECTED Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwObservInput['LABRESULTSDATECOLLECTED'].split(' ')[0],dataTransformerObserv['effectiveDateTime'],"LABRESULTSDATECOLLECTED not Matched")

   #Validation of LABRESULTSDATERELEASED between snowflake JSON and transformed JSON
    def test_observlabresultsdatereleased(self):
        if dataSnwObservInput['LABRESULTSDATERELEASED'].split(' ')[0]== dataTransformerObserv['issued']:
            print('LABRESULTSDATERELEASED Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwObservInput['LABRESULTSDATERELEASED'].split(' ')[0],dataTransformerObserv['issued'],"LABRESULTSDATERELEASED not Matched")

 #Validation of LABRESULTSDATERELEASED between snowflake JSON and transformed JSON
    def test_observlabresultsdatereleased(self):
        if dataSnwObservInput['LABRESULTSDATERELEASED'].split(' ')[0]== dataTransformerObserv['issued']:
            print('LABRESULTSDATERELEASED Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwObservInput['LABRESULTSDATERELEASED'].split(' ')[0],dataTransformerObserv['issued'],"LABRESULTSDATERELEASED not Matched")

 #Validation of LABRESULTVALUE between snowflake JSON and transformed JSON
    def test_observlabresltvalue(self):
        if dataSnwObservInput['LABRESULTVALUE']== dataTransformerObserv['valueQuantity']['value']:
            print('LABRESULTVALUE Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwObservInput['LABRESULTVALUE'],dataTransformerObserv['valueQuantity']['value'],"LABRESULTVALUE not Matched")

 #Validation of RESULTSUNITS between snowflake JSON and transformed JSON
    def test_observresultsunit(self):
        if dataSnwObservInput['RESULTSUNITS']== dataTransformerObserv['valueQuantity']['unit']:
            print('RESULTSUNITS Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwObservInput['RESULTSUNITS'],dataTransformerObserv['valueQuantity']['unit'],"RESULTSUNITS not Matched")

 #Validation of ABNORMALINDICATOR between snowflake JSON and transformed JSON
    def test_observabnormalindicator(self):
        if dataSnwObservInput['ABNORMALINDICATOR']== dataTransformerObserv['interpretation'][0]['coding'][0]['code']:
            print('ABNORMALINDICATOR Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwObservInput['ABNORMALINDICATOR'],dataTransformerObserv['interpretation'][0]['coding'][0]['code'],"ABNORMALINDICATOR not Matched")

 #Validation of LABRESULTSCOMMENTS between snowflake JSON and transformed JSON
    def test_observlabresultscomments(self):
        if dataSnwObservInput['LABRESULTSCOMMENT']== dataTransformerObserv['note'][0]['text']:
            print('LABRESULTSCOMMENT Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwObservInput['LABRESULTSCOMMENT'],dataTransformerObserv['note'][0]['text'],"LABRESULTSCOMMENT not Matched")

 #Validation of NORMALSLOW between snowflake JSON and transformed JSON
    def test_observnormalslow(self):
        if dataSnwObservInput['NORMALSLOW']== dataTransformerObserv['referenceRange'][0]['low']['value']:
            print('NORMALSLOW Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwObservInput['NORMALSLOW'],dataTransformerObserv['referenceRange'][0]['low']['value'],"NORMALSLOW not Matched")


 #Validation of RESULTSUNITS between snowflake JSON and transformed JSON
    def test_observresultsunits1(self):
        if dataSnwObservInput['RESULTSUNITS']== dataTransformerObserv['referenceRange'][0]['low']['unit']:
            print('RESULTSUNITS Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwObservInput['RESULTSUNITS'],dataTransformerObserv['referenceRange'][0]['low']['unit'],"RESULTSUNITS not Matched")

 #Validation of NORMALSHIGH between snowflake JSON and transformed JSON
    def test_observnormalshigh(self):
        if dataSnwObservInput['NORMALSHIGH']== dataTransformerObserv['referenceRange'][0]['high']['value']:
            print('NORMALSHIGH Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwObservInput['NORMALSHIGH'],dataTransformerObserv['referenceRange'][0]['high']['value'],"NORMALSHIGH not Matched")

 #Validation of RESULTSUNITS between snowflake JSON and transformed JSON
    def test_observresultsunits2(self):
        if dataSnwObservInput['RESULTSUNITS']== dataTransformerObserv['referenceRange'][0]['high']['unit']:
            print('RESULTSUNITS Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwObservInput['RESULTSUNITS'],dataTransformerObserv['referenceRange'][0]['high']['unit'],"RESULTSUNITS not Matched")

if __name__ == '__main__':
    unittest.main()