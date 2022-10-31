import unittest
import json

trans_claims_resource = '"resourceType" : "Claim","identifier" : {"use": "official","value": "{{msg.ClaimNumber}}",},'
trans_claims_status = '"status" : "active",' #required
trans_claims_type = '"type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/claim-type","code": "institutional"//Should this be institutional or professional}]},'
#trans_claims_subtype = More granular claim type
trans_claims_use = '"use" : "claim", ' #required
trans_claims_patient =   '"patient" : {"reference": "Patient/{{msg.CenseoID}}"'
trans_claims_billablePeriod = '"billablePeriod": {"start": "{{msg.ServiceFromDate_Date_of_Service | date: "yyyy-MM-dd"}}","end": "{{msg.ServiceThruDate | date: "yyyy-MM-dd"}}"},'
trans_claims_created = '"created" : "{{msg.ClaimEntryDate | date: "yyyy-MM-dd"}}", '
trans_claims_enterer = '"enterer" : {"reference": "Practitioner/{{msg.Provider_ID}}"'
#trans_claims_insurer = Target
trans_claims_provider = '"provider" : {"reference": "Practitioner/{{msg.Provider_ID}}"},'
trans_claims_priority = '"priority" : { "coding": [{"code": "normal"]},'
trans_claims_prescription = '"prescription" : { "reference": "MedicationRequest/{{msg.MedicationID}}"},"payee" : { "type": {"coding":[{"code": "provider","display": "{{msg.RenderingProviderNPI}}""}]}},'
#trans_claims_originalPrescription = 
trans_claims_payee = '"payee" : { "type": {"coding":[{"code": "provider","display": "{{msg.RenderingProviderNPI}}""}]}},'
#trans_claims_referral = Treatment referral
trans_claims_facility = '"facility" : {"identifier":{"value": "{{msg.PlaceOfService}}"}'
trans_claims_careTeam = '"careTeam": [{"sequence": 1,"provider": {"reference": "Practitioner/{{msg.Provider_ID}}"}}],'
trans_claims_diagnosis = '"diagnosis" : [{ "sequence" : 1, "diagnosisCodeableConcept" : { "coding": [{"code": "{{msg.DX_1}}"}]}},{ "sequence" : 2, "diagnosisCodeableConcept" : { "coding": [{"code": "{{msg.DX_2}}"}]}},{ "sequence" : 3, "diagnosisCodeableConcept" : { "coding": [{"code": "{{msg.DX_3}}"}]}}],'
trans_claim_procedure = '"procedure": [{"sequence": 1,"type": [{"coding": [{"code": "primary"}]}],"date": "{{msg.ServiceFromDate /Date_of_Service | date: "yyyy-MM-dd"}}","procedureCodeableConcept": {"coding": [{"code": "{{msg.ProcedureCode /CPTCode_Primary}}"}]}},{"sequence": 2,"type": [{"coding": [{"code": "secondary"}]}],"date": "{{msg.ServiceFromDate /Date_of_Service | date: "yyyy-MM-dd"}}","procedureCodeableConcept": {"coding": [{"code": "{{msg.ProcedureCode2}}"}]}}],  '
trans_claims_insure =   '"insurance" : [{ /"sequence" : 1, "focal" : true, "coverage" : {"reference" : "Coverage/{{msg.CoverageID}}"} }],'
trans_claims_total = '"total" :{"value": "{{msg.BillAmount}}" }'

class TestliqTransform (unittest.TestCase):
    def test_liqclmsnum(self):
        print("identifier.value = ClaimNumber exists:")
        #Validating key ClaimNumber in liquid template
        if ("ClaimNumber" in trans_claims_resource) == True:
            print ("ClaimNumber exists in liquid template")
        #Prints message if the test fails for comparison    
        self.assertEqual("ClaimNumber" in trans_claims_resource,True,"ClaimNumber not present in liquid template") 

    def test_liqclmsstatus(self):
        print("status = active exists:")
        #Validating key claim in liquid template
        if "active" in trans_claims_status:
            print ("active exists in liquid template")
        #Prints message if the test fails for comparison    
        self.assertEqual("active" in trans_claims_status,True,"active not present in liquid template") 

    def test_liqclmsuse(self):
        print("use = claim exists:")
        #Validating key claim in liquid template
        if "claim" in trans_claims_use:
            print ("claim exists in liquid template")
        #Prints message if the test fails for comparison    
        self.assertEqual("claim" in trans_claims_use,True,"claim not present in liquid template") 

    def test_liqclmspatientid(self):
        print("patient.reference = CenseoID exists:")
        #Validating key CenseoID in liquid template
        if "CenseoID" in trans_claims_patient:
            print ("CenseoID exists in liquid template")
        #Prints message if the test fails for comparison    
        self.assertEqual("CenseoID" in trans_claims_patient,True,"CenseoID not present in liquid template") 


    def test_liqclmsbp1(self):
        print("billablePeriod.start = ServiceFromDate_Date_of_Service exists:")
        #Validating key ServiceFromDate_Date_of_Service in liquid template
        if "ServiceFromDate_Date_of_Service" in trans_claims_billablePeriod:
            print ("ServiceFromDate_Date_of_Service exists in liquid template")
        #Prints message if the test fails for comparison    
        self.assertEqual("ServiceFromDate_Date_of_Service" in trans_claims_billablePeriod,True,"ServiceFromDate_Date_of_Service not present in liquid template") 

    def test_liqclmsbp2(self):
        print("billablePeriod.end = ServiceThruDate exists:")
        #Validating key ServiceThruDate in liquid template
        if ("ServiceThruDate" in trans_claims_billablePeriod) == True:
            print ("ServiceThruDate exists in liquid template")
        #Prints message if the test fails for comparison    
        self.assertEqual("ServiceThruDate" in trans_claims_billablePeriod,True,"ServiceThruDate not present in liquid template") 

    def test_liqclmscreated(self):
        print("created = ClaimEntryDate exists:")
        #Validating key ClaimEntryDate in liquid template
        if ("ClaimEntryDate" in trans_claims_created) == True:
            print ("ClaimEntryDate exists in liquid template" in trans_claims_created)
        #Prints message if the test fails for comparison    
        self.assertEqual("ClaimEntryDate" in trans_claims_created,True,"ClaimEntryDate not present in liquid template") 

    def test_liqclmenterer(self):
        print("enterer.reference = Provider_ID exists:")
        #Validating key Provider_ID in liquid template
        if ("Provider_ID" in trans_claims_enterer) == True:
            print ("Provider_ID exists in liquid template")
        #Prints message if the test fails for comparison    
        self.assertEqual("Provider_ID" in trans_claims_enterer,True,"Provider_ID not present in liquid template") 

    def test_liqclmsprvdr(self):
        print("provider.reference = Provider_ID exists:")
        #Validating key Provider_ID in liquid template
        if "Provider_ID" in trans_claims_provider:
            print ("Provider_ID" in trans_claims_provider)
        #Prints message if the test fails for comparison    
        self.assertEqual("Provider_ID" in trans_claims_provider,True,"Provider_ID not present in liquid template")             

    def test_liqclmspriority(self):
        print("priority.coding.code = normal exists:")
        #Validating key normal in liquid template
        if "normal" in trans_claims_priority:
            print ("normal" in trans_claims_priority)
        #Prints message if the test fails for comparison    
        self.assertEqual("normal" in trans_claims_priority,True,"normal not present in liquid template") 

    def test_liqclmsprscrpt(self):
        print("prescription.reference = MedicationID exists:")
        #Validating key MedicationID in liquid template
        if "MedicationID" in trans_claims_prescription:
            print ("MedicationID" in trans_claims_prescription)
        #Prints message if the test fails for comparison    
        self.assertEqual("MedicationID" in trans_claims_prescription,True,"MedicationID not present in liquid template") 

    def test_liqclmspayee1(self):
        print("payee.type.coding.code = provider exists:")
        #Validating key provider in liquid template
        if "provider" in trans_claims_payee:
            print ("provider" in trans_claims_payee)
        #Prints message if the test fails for comparison    
        self.assertEqual("provider" in trans_claims_payee,True,"provider not present in liquid template") 

    def test_liqclmspayee2(self):
        print("payee.type.coding.display = RenderingProviderNPI exists:")
        #Validating key RenderingProviderNPI in liquid template
        if "RenderingProviderNPI" in trans_claims_payee:
            print ("RenderingProviderNPI" in trans_claims_payee)
        #Prints message if the test fails for comparison    
        self.assertEqual("RenderingProviderNPI" in trans_claims_payee,True,"RenderingProviderNPI not present in liquid template") 

    def test_liqclmsfacility(self):
        print("facility.identifier.value = PlaceOfService exists:")
        #Validating key PlaceOfService in liquid template
        if "PlaceOfService" in trans_claims_facility:
            print ("PlaceOfService" in trans_claims_facility)
        #Prints message if the test fails for comparison    
        self.assertEqual("PlaceOfService" in trans_claims_facility,True,"PlaceOfService not present in liquid template") 

    
    def test_liqclmscareteam(self):
        print("careTeam.sequence.provider.reference = Provider_ID exists:")
        #Validating key Provider_ID in liquid template
        if "Provider_ID" in trans_claims_careTeam:
            print ("Provider_ID" in trans_claims_careTeam)
        #Prints message if the test fails for comparison    
        self.assertEqual("Provider_ID" in trans_claims_careTeam,True,"Provider_ID not present in liquid template") 

    def test_liqclmsdiagnosis1(self):
        print("diagnosis.sequence.diagnosisCodeableConcept.coding.code = DX_1 exists:")
        #Validating key DX_1 in liquid template
        if "DX_1" in trans_claims_diagnosis:
            print ("DX_1" in trans_claims_diagnosis)
        #Prints message if the test fails for comparison    
        self.assertEqual("DX_1" in trans_claims_diagnosis,True,"DX_1 not present in liquid template") 

    def test_liqclmsdiagnosis2(self):
        print("diagnosis.sequence.diagnosisCodeableConcept.coding.code = DX_2 exists:")
        #Validating key DX_2 in liquid template
        if "DX_2" in trans_claims_diagnosis:
            print ("DX_2" in trans_claims_diagnosis)
        #Prints message if the test fails for comparison    
        self.assertEqual("DX_2" in trans_claims_diagnosis,True,"DX_2 not present in liquid template") 

    def test_liqclmsdiagnosis3(self):
        print("diagnosis.sequence.diagnosisCodeableConcept.coding.code = DX_3 exists:")
        #Validating key DX_2 in liquid template
        if "DX_3" in trans_claims_diagnosis:
            print ("DX_3" in trans_claims_diagnosis)
        #Prints message if the test fails for comparison    
        self.assertEqual("DX_3" in trans_claims_diagnosis,True,"DX_2 not present in liquid template") 

    def test_liqclmsprocedure1(self):
        print("procedure.sequence.type.coding.code = primary exists:")
        #Validating key primary in liquid template
        if "primary" in trans_claim_procedure:
            print ("primary" in trans_claim_procedure)
        #Prints message if the test fails for comparison    
        self.assertEqual("primary" in trans_claim_procedure,True,"primary not present in liquid template") 

    def test_liqclmsprocedure2(self):
        print("procedure.date = ServiceFromDate exists:")
        #Validating key ServiceFromDate in liquid template
        if "ServiceFromDate" in trans_claim_procedure:
            print ("ServiceFromDate" in trans_claim_procedure)
        #Prints message if the test fails for comparison    
        self.assertEqual("ServiceFromDate" in trans_claim_procedure,True,"ServiceFromDate not present in liquid template")

    def test_liqclmsprocedure3(self):
        print("procedure.procedureCodeableConcept.coding.code = ProcedureCode exists:")
        #Validating key ProcedureCode in liquid template
        if "ProcedureCode" in trans_claim_procedure:
            print ("ProcedureCode" in trans_claim_procedure)
        #Prints message if the test fails for comparison    
        self.assertEqual("ProcedureCode" in trans_claim_procedure,True,"ProcedureCode not present in liquid template")

    def test_liqclmsprocedure4(self):
        print("procedure.sequence.type.coding.code = secondary exists:")
        #Validating key secondary in liquid template
        if "secondary" in trans_claim_procedure:
            print ("secondary" in trans_claim_procedure)
        #Prints message if the test fails for comparison    
        self.assertEqual("secondary" in trans_claim_procedure,True,"secondary not present in liquid template") 

    def test_liqclmsprocedure5(self):
        print("procedure.date = ServiceFromDate exists:")
        #Validating key ServiceFromDate in liquid template
        if "ServiceFromDate" in trans_claim_procedure:
            print ("ServiceFromDate" in trans_claim_procedure)
        #Prints message if the test fails for comparison    
        self.assertEqual("ServiceFromDate" in trans_claim_procedure,True,"ServiceFromDate not present in liquid template")
    
    def test_liqclmsprocedure6(self):
        print("procedure.procedureCodeableConcept.coding.code = ProcedureCode2 exists:")
        #Validating key ProcedureCode2 in liquid template
        if "ProcedureCode2" in trans_claim_procedure:
            print ("ProcedureCode2" in trans_claim_procedure)
        #Prints message if the test fails for comparison    
        self.assertEqual("ProcedureCode2" in trans_claim_procedure,True,"ProcedureCode2 not present in liquid template")

    def test_liqclmsinsurance1(self):
        print("insurance.sequence = 1 exists:")
        #Validating key 1 in liquid template
        if "1" in trans_claims_insure:
            print ("1" in trans_claims_insure)
        #Prints message if the test fails for comparison    
        self.assertEqual("1" in trans_claims_insure,True,"1 not present in liquid template")

    def test_liqclmsinsurance2(self):
        print("insurance.focal = true exists:")
        #Validating key true in liquid template
        if "true" in trans_claims_insure:
            print ("true" in trans_claims_insure)
        #Prints message if the test fails for comparison    
        self.assertEqual("true" in trans_claims_insure,True,"true not present in liquid template")

    def test_liqclmsinsurance3(self):
        print("insurance.coverage.reference = CoverageID exists:")
        #Validating key CoverageID in liquid template
        if "CoverageID" in trans_claims_insure:
            print ("CoverageID" in trans_claims_insure)
        #Prints message if the test fails for comparison    
        self.assertEqual("CoverageID" in trans_claims_insure,True,"CoverageID not present in liquid template")

    def test_liqclmstotal(self):
        print("insurance.total.value = BillAmount exists:")
        #Validating key BillAmount in liquid template
        if "BillAmount" in trans_claims_total:
            print ("BillAmount" in trans_claims_total)
        #Prints message if the test fails for comparison    
        self.assertEqual("BillAmount" in trans_claims_total,True,"BillAmount not present in liquid template")       

if __name__ == '__main__':
    unittest.main()