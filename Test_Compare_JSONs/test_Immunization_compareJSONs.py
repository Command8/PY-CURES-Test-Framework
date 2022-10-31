from pickle import FALSE
import unittest
import json
#Procedure to import file from different folder using sys, path, append
import sys
sys.path.append(".")
from Read_JSON import dataSnwImmunInput,dataTransformerImmun
import datetime


#Write class to run unit tests. These are created to retrieve the values from Snowflake and transformed JSONs and perform comparison 
#between them to ensure that the snowflake JSON transformation is successful when created using liquid FHIR template

class TestTransform (unittest.TestCase): 

    # if statements are written to display message in vs code for all passed tests   
    
    # Immunizations Tests start here
    #Validation of DATEOFSERVICE between snowflake JSON and transformed JSON
    def test_Innumdateofservice(self):
        d = datetime.datetime.strptime(dataSnwImmunInput['DATEOFSERVICE'],'%Y%m%d').strftime('%Y-%m-%d')
        print (d)
        if d == dataTransformerImmun['note'][0]['time']:
            print('DATEOFSERVICE Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(d, dataTransformerImmun['note'][0]['time'],"DATEOFSERVICE not Matched")

    #Validation of CENSEOID between snowflake JSON and transformed JSON
    def test_Innumcenseiod(self):
        if dataSnwImmunInput['CENSEOID'] == dataTransformerImmun['identifier'][0]['value']:
            print('CENSEOID Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwImmunInput['CENSEOID'],dataTransformerImmun['identifier'][0]['value'],"CENSEOID not Matched")

    #Validation of DOB between snowflake JSON and transformed JSON
    def test_Innumdob(self):
        sectiondisplay = dataSnwImmunInput['SECTIONDISPLAYTEXT'] + ' ' +dataSnwImmunInput['QUESTIONTEXT2'] + ' ' + dataSnwImmunInput['ANSWERTEXT']
        if sectiondisplay == dataTransformerImmun['note'][0]['text']:
            print('SECTIONDISPLAYTEXT, QUESTIONTEXT2, ANSWERTEXT  Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(sectiondisplay,dataTransformerImmun['note'][0]['text'],"SECTIONDISPLAYTEXT not Matched")







if __name__ == '__main__':
    unittest.main()