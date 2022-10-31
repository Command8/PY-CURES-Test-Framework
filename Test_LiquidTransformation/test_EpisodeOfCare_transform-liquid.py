import unittest
import json

#Copy the dictionaries as strings into variables inorder to identify and validate snowflake JSON Keys presence in newly created strings.
trans_epi_resource = '"resourceType": "EpisodeOfCare","identifier" : [{"use": "official","value": "{{msg.CENSEOID}}","assigner":{"display":"Signify Health CenseoID"}}],'
trans_status ='"status": "{{msg.STATUS_CODE}}"'
trans_statusHistory ='"statusHistory" : [{{% if msg.STATUS_CODE == "" -%}"status": "inactive",{% else -%}"status": "active",{% endif -%},"period" : {"start": "{{msg.DATE_OF_SERVICE | date: "yyyy-MM-dd"}}",}}],'
trans_type = '"type": [{"coding": [{"system": "http://hl7.org/fhir/ValueSet/episodeofcare-type","code": "{{msg.type.coding.code}}","display": "{{msg.type.coding.display}}"}],"text": "{{msg.type.text}}"}],'
trans_diagnosis = '"diagnosis" : [{"condition" : {"reference": "Condition/{{msg.condition.reference}}",},"role":{"coding": [{"system": "http://http://hl7.org/fhir/ValueSet/diagnosis-role","code": "{{msg.role.coding.code}}","display": "{{msg.role.coding.display}}"}],"text": "{{msg.role.text}}"},{% if msg.DX_1 == "" -%}"rank": "0",{% else -%}"rank": "1",{% endif -%}}]'
trans_patient = '"patient": {"reference": "Patient/{{msg.patient.reference}}","display": "{{msg.MEMBER_NAME}}"},'
trans_managingOrg ='"managingOrganization": {"reference": "Organization/{{msg.managingOrganization.reference}}","display": "{{msg.managingOrganization.reference}}"},'
trans_period = '"period" : {"start": "{{ msg.DATE_OF_SERVICE | date: "yyyy-MM-dd"}}"},'
trans_refreq = '"referralRequest": [{"reference": "ServiceRequest/{{msg.referralRequest.reference}}","display": "{{msg.referralRequest.reference}}"}],'
trans_caremgr = '"careManager":{"reference": "Practitioner/{{msg.careManager.reference}}","display": "{{msg.careManager.reference}}"},'
trans_team = '"team": [{"reference": "CareTeam/{{msg.team.reference}}","display": "{{msg.team.reference}}"}],'
trans_account = '"account": [{"reference": "Account/{{msg.accountt.reference}}","display": "{{msg.accountt.reference}}"}],'


#Write class to run unit tests. These are created to retrieve the validate the snowflake Keys presence in liquid FHIR template that has been
#created for patient resource
# if statements are written to display message in vs code for all passed tests 

class TestliqTransform (unittest.TestCase):

     
    #Validating key CENSEOID in liquid template
    def test_liqEpicenid(self):
        if ("CENSEOID" in trans_epi_resource) == True:
            print("CENSEOID presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("CENSEOID" in trans_epi_resource,True,"CENSEOID not present in liquid template")
    #Validating key STATUS_CODE in liquid template
    def test_liqEpiKeystatus(self):
        if ("STATUS_CODE" in trans_status) == True:
            print ("STATUS_CODE presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("STATUS_CODE" in trans_status,True,"STATUS_CODE not present in liquid template")
    #Validating key DATE_OF_SERVICE in liquid template
    def test_liqEpidtofsrvc(self):
        if ("DATE_OF_SERVICE" in trans_statusHistory) == True:
            print ("DATE_OF_SERVICE presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("DATE_OF_SERVICE" in trans_statusHistory,True,"DATE_OF_SERVICE not present in liquid template")
    #Validating key RANK(DX_1) in liquid template
    def test_liqEpiDX1(self):
        if ("DX_1" in trans_diagnosis) == True:
            print ("RANK(DX_1) presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("DX_1" in trans_diagnosis,True,"RANK(DX_1) not present in liquid template")
    #Validating key MEMBER_NAME in liquid template
    def test_liqEpiMemName(self):
        if ("MEMBER_NAME" in trans_patient) == True:
            print ("MEMBER_NAME presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_NAME" in trans_patient,True,"MEMBER_NAME not present in liquid template")    
    
if __name__ == '__main__':
    unittest.main()