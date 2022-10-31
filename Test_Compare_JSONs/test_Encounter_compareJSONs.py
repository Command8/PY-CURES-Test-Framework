import unittest
import json

#Procedure to import file from different folder using sys, path, append
import sys
sys.path.append(".")
from Read_JSON import dataSnwEncInput,dataTransformerEnc,input_status

#Write class to run unit tests. These are created to retrieve the values from Snowflake and transformed JSONs and perform comparison 
#between them to ensure that the snowflake JSON transformation is successful when created using liquid FHIR template

class TestTransform (unittest.TestCase):    
    
    # if statements are written to display message in vs code for all passed tests   
    
    # Encounter Tests start here
    #Validation of Status between snowflake JSON and transformed Encounter JSON
    def test_encstatus(self):
        if input_status == dataTransformerEnc['status']:
            print('Status Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(input_status,dataTransformerEnc['status'],"Status not Matched")

    #Validation of AdmissionDate between snowflake JSON and transformed Encounter JSON
    def test_encadmdate(self):
        if dataSnwEncInput['AdmissionDate'] == dataTransformerEnc['period']['start']:
            print('AdmissionDate Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwEncInput['AdmissionDate'],dataTransformerEnc['period']['start'],"AdmissionDate not Matched") 

    #Validation of AdmitSource between snowflake JSON and transformed Encounter JSON
    def test_encadmsrc(self):
        if dataSnwEncInput['AdmitSource'] == dataTransformerEnc['hospitalization']['admitSource']['coding'][0]['display']:
            print('AdmitSource Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwEncInput['AdmitSource'],dataTransformerEnc['hospitalization']['admitSource']['coding'][0]['display'],"AdmitSource not Matched") 

    #Validation of Diagnosis between snowflake JSON and transformed Encounter JSON
    def test_encdiagnosis(self):
        if dataSnwEncInput['DiagnosisCode'] == dataTransformerEnc['diagnosis'][0]['use']['coding'][0]['code']:
            print('Diagnosis Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwEncInput['DiagnosisCode'],dataTransformerEnc['diagnosis'][0]['use']['coding'][0]['code'],"Diagnosis not Matched")

    #Validation of PatientId between snowflake JSON and transformed Encounter JSON
    def test_encpatiendid(self):
        if str(dataSnwEncInput['PatientId']) == dataTransformerEnc['subject']['reference'].split('/')[1]:
            print('PatientId Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(str(dataSnwEncInput['PatientId']),dataTransformerEnc['subject']['reference'].split('/')[1],"PatientId not Matched")
     
    #Validation of EncounterType between snowflake JSON and transformed Encounter JSON 
    def test_enctype(self):
        if dataSnwEncInput['EncounterType'] == dataTransformerEnc['type'][0]['coding'][0]['display']:
            print('EncounterType Matched')        
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwEncInput['EncounterType'],dataTransformerEnc['type'][0]['coding'][0]['display'],"EncounterType not Matched")   

    #Validation of ReasonCode between snowflake JSON and transformed Encounter JSON 
    def test_encrsncd(self):
        if dataSnwEncInput['ReasonCode'] == dataTransformerEnc['reasonCode'][0]['coding'][0]['display']:
            print('ReasonCode Matched')        
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwEncInput['ReasonCode'],dataTransformerEnc['reasonCode'][0]['coding'][0]['display'],"ReasonCode not Matched")        

    #Validation of EpisodeOfCareId between snowflake JSON and transformed Encounter JSON
    def test_encepisodecareid(self):
        if dataSnwEncInput['EpisodeOfCareId'] == dataTransformerEnc['episodeOfCare']['reference'].split('/')[1]:
            print('EpisodeOfCareId Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwEncInput['EpisodeOfCareId'],dataTransformerEnc['episodeOfCare']['reference'].split('/')[1],"EpisodeOfCareId not Matched")

    #Validation of basedOn between snowflake JSON and transformed Encounter JSON
    def test_encbasedon(self):
        if dataSnwEncInput['basedOn'] == dataTransformerEnc['basedOn']['reference'].split('/')[1]:
            print('basedOn Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwEncInput['basedOn'],dataTransformerEnc['basedOn']['reference'].split('/')[1],"basedOn not Matched")

    #Validation of PCP_ID between snowflake JSON and transformed Encounter JSON
    def test_encpcpid(self):
        if str(dataSnwEncInput['PCP_ID']) == dataTransformerEnc['participant'][0]['individual']['reference'].split('/')[1]:
            print('PCP_ID Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(str(dataSnwEncInput['PCP_ID']),dataTransformerEnc['participant'][0]['individual']['reference'].split('/')[1],"PCP_ID not Matched")

    #Validation of apptId between snowflake JSON and transformed Encounter JSON
    def test_encappid(self):
        if str(dataSnwEncInput['apptId']) == dataTransformerEnc['appointment']['reference'].split('/')[1]:
            print('apptId Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(str(dataSnwEncInput['apptId']),dataTransformerEnc['appointment']['reference'].split('/')[1],"apptId not Matched")

    #Validation of reasonref between snowflake JSON and transformed Encounter JSON
    def test_encreasonref(self):
        if dataSnwEncInput['reasonref'] == dataTransformerEnc['reasonReference']['reference'].split('/')[1]:
            print('reasonref Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwEncInput['reasonref'],dataTransformerEnc['reasonReference']['reference'].split('/')[1],"reasonref not Matched")

    #Validation of locationId between snowflake JSON and transformed Encounter JSON
    def test_enclocationid(self):
        if dataSnwEncInput['locationId'] == dataTransformerEnc['location']['location']['reference'].split('/')[1]:
            print('locationId Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwEncInput['locationId'],dataTransformerEnc['location']['location']['reference'].split('/')[1],"locationId not Matched")        
    
    #Validation of locationId between snowflake JSON and transformed Encounter JSON
    def test_encfacilityname(self):
        if dataSnwEncInput['FacilityName'] == dataTransformerEnc['serviceProvider']['display']:
            print('FacilityName Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwEncInput['FacilityName'],dataTransformerEnc['serviceProvider']['display'],"FacilityName not Matched")        
     
    #Validation of encId between snowflake JSON and transformed Encounter JSON
    def test_encId(self):
        if dataSnwEncInput['encId'] == dataTransformerEnc['partOf']['display']:
            print('encId Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwEncInput['encId'],dataTransformerEnc['partOf']['display'],"encId not Matched")        
     

if __name__ == '__main__':
    unittest.main()