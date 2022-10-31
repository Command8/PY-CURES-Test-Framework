import unittest
import json

#Copy the dictionaries as strings into variables inorder to identify and validate snowflake JSON Keys presence in newly created strings.
trans_enc_resource = '"resourceType": "Encounter","id": "{{msg.id}}","text": {"status": "generated","div": "{{msg.text.div | escape_special_chars}}"},'
trans_identifier = '"identifier": [{"use": "{{msg.identifier.use}}","system": "{{msg.identifier.system}}","value": "{{msg.identifier.value}}"}],'
trans_status = '"status" :{% if msg.Status == "planned" -%} "planned",{% elsif msg.Status == "arrived" -%}"arrived",{% elsif msg.Status == "triaged" -%}"triaged",{% elsif msg.Status == "in-progress" -%}"in-progress",{% elsif msg.Status == "onleave" -%}"onleave",{% elsif msg.Status == "finished" -%} "finished",{% elsif msg.Status == "cancelled" -%}"cancelled",{% elsif msg.Status == "other"" -%}"unknown",{% elsif code -%}{% else %} "",{% endif -%}'
trans_statushistory = ' "statusHistory": [{"status": "{{msg.statusHistory.status}}","period": {"start" : "{{msg.statusHistory.start}}",},}],'
trans_class = '"class": {"system": "http://terminology.hl7.org/CodeSystem/v3-ActCode","code": "IMP","display": "inpatient encounter"},'
trans_classhistory = '"classHistory": [{"status": "{{msg.classHistory.status}}","period": {"start" : "{{msg.classHistory.start}}",},}]'
trans_type = '"type": [{"coding": [{"system": "http://snomed.info/sct","code": "{{msg.EncounterType.code}}","display": "{{msg.EncounterType}}",}]}],'
trans_servicetype = '"serviceType": {"coding": [{ "system": "http://snomed.info/sct","code": "{{msg.serviceType.code}}","display": "{{msg.serviceType}}",}]},'
trans_priority = '"priority": {"coding": [{"system": "http://snomed.info/sct","code": "310361003","display": "Non-urgent cardiological admission"}]},'
trans_subject = '"subject": {"reference": "Patient/{{msg.PatientId}}","display": "{{msg.subject.display}}"}'
trans_episodeofCare = '"episodeOfCare": {"reference": "EpisodeOfCare/{{msg.EpisodeOfCareId}}","display": "{{msg.episodeOfCare.display}}"}'
trans_basedOn = '"basedOn": {"reference": "ServiceRequest/{{msg.basedOn}}","display": "{{msg.basedOn.display}}"}'
trans_participant = '"participant": [{"type": {"coding": [{"system": "http://snomed.info/sct","code": "{{msg.type.code}}","display": "{{msg.type}}",}]},"individual": {"reference": "Practitioner/{{msg.PCP_ID}}","display": "{{p.individual.display}}"},"period": {"start" : "{{msg.DateOfService}}",},}],'
trans_appointment = '"appointment": {"reference": "Appointment/{{msg.apptId}}","display": "{{msg.appointment.display}}"}'
trans_period = '"period": {"start" : "{{msg.AdmissionDate}}",}'
trans_length = '"length": {"value": "{{msg.length.value}}","unit": "min","system": "http://unitsofmeasure.org","code": "min"}'
trans_reasonCode ='"reasonCode": [{"coding": [{"system": "http://snomed.info/sct","code": "{{msg.ReasonCode.code}}","display": "{{msg.ReasonCode}}"}]}]'
trans_reasonReference ='"reasonReference": {"reference": "Condition/{{msg.reasonref}}","display": "{{msg.reasonRefernece}}"}'
trans_diagnosis = '"diagnosis":[{"condition": {"display": "Complications from Roel TPF chemotherapy on January 28th, 2013"},"use": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/diagnosis-role", "code": "{{msg.DiagnosisCode}}","display": "{{msg.AdmitDiag}}"}],"text": "{{msg.DiagnosisFullDiscription}}"},"rank": 1},],'
trans_account = '"account": {"reference": "Account/{{msg.account}}","display": "{{msg.accountName}}"},'
trans_hospitalization = '"hospitalization": {"preAdmissionIdentifier": {"use": "official","system": "http://www.amc.nl/zorgportal/identifiers/pre-admissions","value": "{{msg.preAdmissionIdentifier.value}}"},"origin": {"reference": "Location/{{msg.locationId}}","display": "{{msg.FacilityName}}"},"admitSource": {"coding": [{"system": "http://snomed.info/sct","code": "{{msg.admitSource.coding.code}}","display": "{{msg.AdmitSource}}"}]},"reAdmission": {"coding": [{"system": "http://snomed.info/sct","code": "{{msg.admitSource.coding.code}}","display": "{{msg.readmission}}"}]},"dietPreference": {"coding": [{"system": "http://snomed.info/sct","code": "{{msg.admitSource.coding.code}}","display": "{{msg.readmission}}"}]},"specialCourtesy": {"coding": [{"system": "http://snomed.info/sct","code": "{{msg.admitSource.coding.code}}","display": "{{msg.readmission}}"}]},"specialArrangement": {"coding": [{"system": "http://snomed.info/sct","code": "{{msg.admitSource.coding.code}}","display": "{{msg.readmission}}"}]},"destination": {"reference": "Location/{{msg.locationId}}","display": "{{msg.FacilityName}}"},"dischargeDisposition": {"coding": [{"system": "http://snomed.info/sct","code": "{{msg.dischargeDisposition.coding.code}}",      "display": "{{msg.dischargeDisposition.coding.display}}",}]}},'
trans_location = '"location": {"location": {"reference": "Location/{{msg.locationId}}","display": "{{msg.FacilityName}}"},"status":"planned","physicalType": {"coding": [{"system": "http://snomed.info/sct","code": "{{msg.dischargeDisposition.coding.code}}","display": "{{msg.dischargeDisposition.coding.display}}",}]},"period": {"start" : "{{msg.DateOfService}}",},},'
trans_facname ='"serviceProvider": {"reference": "Organization/{{msg.orgId}}","display": "{{msg.FacilityName}}"},'
trans_partof = '"partOf": {"reference": "Encounter/{{msg.encId}}","display": "{{msg.encId}}"},'


#Write class to run unit tests. These are created to retrieve the validate the snowflake Keys presence in liquid FHIR template that has been
#created for patient resource
# if statements are written to display message in vs code for all passed tests 

class TestliqTransform (unittest.TestCase):
    #Validating key Status in liquid template
    def test_liqencstatus(self):
        if ("Status" in trans_status) == True:
            print ("Status presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("Status" in trans_status,True,"Status not present in liquid template")
    #Validating key AdmissionDate in liquid template
    def test_liqencadmdt(self):
        if ("AdmissionDate" in trans_period) == True:
            print ("AdmissionDate presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("AdmissionDate" in trans_period,True,"AdmissionDate not present in liquid template")
    #Validating key AdmitSource in liquid template
    def test_liqencadmsrc(self):
        if ("AdmitSource" in trans_hospitalization) == True:
            print ("AdmitSource presence is validated in liquid template")
        #Prints message AdmitSource the test fails for comparison
        self.assertEqual("AdmitSource" in trans_hospitalization,True,"AdmitSource not present in liquid template")
    #Validating key AdmitDiag in liquid template
    def test_liqencadmdiag(self):
        if ("AdmitDiag" in trans_diagnosis) == True:
            print ("AdmitDiag presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("AdmitDiag" in trans_diagnosis,True,"AdmitDiag not present in liquid template")
    #Validating key PatientId in liquid template
    def test_liqencpatid(self):
        if ("PatientId" in trans_subject) == True:
            print ("PatientId presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PatientId" in trans_subject,True,"PatientId not present in liquid template")
    #Validating key EncounterType in liquid template
    def test_liqenctype(self):
        if ("EncounterType" in trans_type) == True:
            print ("EncounterType presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("EncounterType" in trans_type,True,"EncounterType not present in liquid template")
    #Validating key ReasonCode in liquid template
    def test_liqencrsncde(self):
        if ("ReasonCode" in trans_reasonCode) == True:
            print ("ReasonCode presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("ReasonCode" in trans_reasonCode,True,"ReasonCode not present in liquid template")
    #Validating key EpisodeOfCareId in liquid template
    def test_liqencepisodecareid(self):
        if ("EpisodeOfCareId" in trans_episodeofCare) == True:
            print ("EpisodeOfCareId presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("EpisodeOfCareId" in trans_episodeofCare,True,"EpisodeOfCareId not present in liquid template")
    #Validating key basedOn in liquid template
    def test_liqencbasedon(self):
        if ("basedOn" in trans_basedOn) == True:
            print ("basedOn presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("basedOn" in trans_basedOn,True,"basedOn not present in liquid template")
    #Validating key PCP_ID in liquid template
    def test_liqencpcpid(self):
        if ("PCP_ID" in trans_participant) == True:
            print ("PCP_ID presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PCP_ID" in trans_participant,True,"PCP_ID not present in liquid template")
    #Validating key apptId in liquid template
    def test_liqencapptid(self):
        if ("apptId" in trans_appointment) == True:
            print ("apptId presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("apptId" in trans_appointment,True,"apptId not present in liquid template")
    #Validating key reasonref in liquid template
    def test_liqencreasonref(self):
        if ("reasonref" in trans_reasonReference) == True:
            print ("reasonref presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("reasonref" in trans_reasonReference,True,"reasonref not present in liquid template")
    #Validating key locationId in liquid template
    def test_liqenclocationid(self):
        if ("locationId" in trans_location) == True:
            print ("locationId presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("locationId" in trans_location,True,"locationId not present in liquid template")
    #Validating key FacilityName in liquid template
    def test_liqencfacilityname(self):
        if ("FacilityName" in trans_facname) == True:
            print ("FacilityName presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("FacilityName" in trans_facname,True,"FacilityName not present in liquid template")
    #Validating key encId in liquid template
    def test_liqencencId(self):
        if ("encId" in trans_partof) == True:
            print ("encId presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("encId" in trans_partof,True,"encId not present in liquid template")
    #Validating key DiagnosisCode in liquid template
    def test_liqencdiagcode(self):
        if ("DiagnosisCode" in trans_diagnosis) == True:
            print ("DiagnosisCode presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("DiagnosisCode" in trans_diagnosis,True,"DiagnosisCode not present in liquid template")
    
if __name__ == '__main__':
    unittest.main()