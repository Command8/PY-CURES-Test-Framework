import unittest
import json

trans_medreq_resourceType = '{"resourceType": "MedicationRequest","id": "{{msg.id}}","text": {"status": "generated","div": "{{ msg.text.div | escape_special_chars }}"},"contained": [{"resourceType": "Medication","id": "{{msg.contained.id}}","code": {"coding": [{"system": "{{msg.code.coding.system}}","code": "{{msg.code.coding.code}}","display": "{{msg.code.coding.display}}"}]}],'
trans_medreq_identifier = '"identifier": [{"use": "{{msg.identifier.use}}","type": "{{msg.identifier.type}}","system": "{{msg.identifier.system}}","value": "{{msg.CENSEOID}}","period": "{{msg.identifier.period}}","assigner": {"display": "SignifyHealth"},}],{% if msg.DATE_OF_SERVICE == "" -%}"status": "inactive",{% else -%}"status": "active",{% endif -%},'
trans_medreq_statusReason = '"statusReason":{"coding": ["system": "http://hl7.org/fhir/ValueSet/medicationrequest-status-reason","code": "{{msg.statusReason.coding.code}}","display": "{{msg.statusReason.coding.display}}"},],},'
trans_medreq_intent = '"intent": "order",'
trans_medreq_category = '"category":[{"coding": [{"system": "http://hl7.org/fhir/ValueSet/medicationrequest-category","code": "{{msg.category.coding.code}}","display": "{{msg.category.coding.display}}"},],}],'
trans_medreq_priority = '"priority": "{{msg.priority}}",'
trans_medreq_doNotPerform = '"doNotPerform": "{{msg.doNotPerform}}",'
trans_medreq_reportedBoolean =  '"reportedBoolean": "{{msg.reportedBoolean}}",'
trans_medreq_reportReference =   '"reportedReference":{"reference": "Practitioner/{{msg.reportedReference.reference}}","display": "{{msg.reportedReference.display}}"},'
trans_medreq_medicationCodableConcept = '"medicationCodeableConcept": {"coding": [{% for code in msg.NDC_CODE -%}{% for desc in msg.NDC_DESCRIPTION -%}{"system": "http://hl7.org/fhir/sid/ndc","code": "{{code}}","display": "{{desc}}"},{% endfor -%}{% endfor -%}],},'
trans_medreq_medicationReference ="medicationReference"': {"reference": "Medication/{{msg.medicationReference.reference}}","display": "{{msg.medicationReference.display}}"},'
trans_medreq_subject = '"subject": {"reference": "Patient/{{msg.subject.reference}}","display": "{{msg.subject.display}}"},'
trans_medreq_encounter = '"encounter": {"reference": "Encounter/{{msg.encounter.reference}}","display": "{{msg.encounter.display}}"},'
trans_medreq_supportingInfo = '"supportingInformation": {"reference": "Resource/{{msg.supportingInformation.reference}}","display": "{{msg.supportingInformation.display}}"},'
trans_medreq_authoredOn = '"authoredOn": "{{msg.DATE_OF_SERVICE | date: "yyyy-MM-dd"}}","requester": {"reference": "Practitioner/{{msg.requester.reference}}","display": "{{msg.requester.display}}"},'
trans_medreq_performer = '"performer": {"reference": "Practitioner/{{msg.performer.reference}}","display": "{{msg.performer.display}}"},'
trans_medreq_performerType = '"performerType": {"coding": ["system": "http://hl7.org/fhir/ValueSet/performer-role","code": "{{msg.performerType.coding.code}}","display": "{{msg.performerType.coding.display}}"},],},'
trans_medreq_recorder =  '"recorder": {"reference": "Practitioner/{{msg.recorder.reference}}","display": "{{msg.recorder.display}}"},'
trans_medreq_reasonCode = '"reasonCode": [{"coding": [{"system": "http://hl7.org/fhir/ValueSet/condition-code","code": "{{msg.reasonCode.coding.code}}","display": "{{msg.reasonCode.coding.display}}"},],}],'
trans_medreq_reasonReference = '"reasonReference": {"reference": "Condition/{{msg.reasonReference.reference}}","display": "{{msg.reasonReference.display}}"},'
trans_medreq_instantiatesCanonical = '"instantiatesCanonical":[{"value": "{{msg.instantiatesCanonical.value}}"}],'
trans_medreq_instantiatesUrl = '"instantiatesUri":[    {"uri": "{{msg.instantiatesUri.uri}}"}],'
trans_medreq_basedOn = '"basedOn": [{"reference": "MedicationRequest/{{msg.basedOn.reference}}"}],'
trans_medreq_groupIndentifier = '"groupIdentifier": {"use": "{{msg.groupIdentifier.use}}","system": "{{msg.groupIdentifier.system}}","value": "{{msg.groupIdentifier.value}}"},'
trans_medreq_courseOfTherapyType =  '"courseOfTherapyType": {"coding": [{"system": "http://hl7.org/fhir/ValueSet/medicationrequest-course-of-therapy","code": "{{msg.courseOfTherapyType.coding.code}}","display": "{{msg.courseOfTherapyType.coding.display}}"}],},'
trans_medreq_insurance = '"insurance": [{"reference": "Coverage/{{msg.insurance.reference}}"}],'
trans_medreq_note = '"note": [{"text": "{{msg.note.text}}"}],'
trans_medreq_dosageInstruction = '"dosageInstruction": [{"sequence": 1,"text": "{{msg.dosageInstruction.text}}","timing": {"repeat": {"frequency": "{{msg.dosageInstruction.timing.repeat.frequency}}","period": "{{msg.dosageInstruction.timing.repeat.period}}","periodUnit": "{{msg.dosageInstruction.timing.repeat.periodUnit}}"},},"doseAndRate": [{"type": {"coding": [{"system": "{{msg.dosageInstruction.doseAndRate.type.coding.system}}","code": "{{msg.dosageInstruction.doseAndRate.type.coding.code}}","display": "{{msg.dosageInstruction.doseAndRate.type.coding.display}}"}],},"doseQuantity": {"value": {{msg.QUANTITY}},"unit": "{{msg.dosageInstruction.doseAndRate.doseQuantity.unit}}","system": "{{msg.dosageInstruction.doseAndRate.doseQuantity.system}}","code": "{{msg.dosageInstruction.doseAndRate.doseQuantity.code}}"}}]},],'
trans_medreq_dispenseRequest = '"dispenseRequest": {"initialFill": {"quantity": "{{msg.initialFill.quantity}}","duration": "{{msg.initialFill.duration}}"},'"dispenseInterval" "{{msg.dispenseInterval}}"",{% for dr in msg.dispenseRequest -%}validityPeriod"': {"start": "{{dr.validityPeriod.start | date: "yyyy-MM-dd"}}","end": "{{dr.validityPeriod.end | date: "yyyy-MM-dd"}}"},"numberOfRepeatsAllowed": {{dr.numberOfRepeatsAllowed}},"quantity": {"value": {{dr.quantity.value}},"unit": "{{dr.quantity.unit}}","system": "{{dr.quantity.system}}","code": "{{dr.quantity.code}}"},"expectedSupplyDuration": {"value": {{dr.expectedSupplyDuration.value}},"unit": "{{dr.expectedSupplyDuration.unit}}","system": "{{dr.expectedSupplyDuration.system}}","code": "{{dr.expectedSupplyDuration.code}}}{% endfor -%}},'
trans_medreq_substitution = '"substitution": {"allowedBoolean" : "{{msg.substitution}}","allowedCodeableConcept" : {"coding": [{"system": "http://terminology.hl7.org/ValueSet/v3-ActSubstanceAdminSubstitutionCode","code": "{{msg.substitution.allowableCodeableConcept.coding.code}}","display": "{{msg.substitution.allowableCodeableConcept.coding.display}}"}],},"reason": {"coding": [{"system": "http://terminology.hl7.org/ValueSet/v3-SubstanceAdminSubstitutionReason","code": "{{msg.reason.coding.code}}","display": "{{msg.reason.coding.display}}"}],}},'
trans_medreq_priorPrescription = '"priorPrescription": {"reference": "Condition/{{msg.priorPrescription.reference}}","display": "{{msg.priorPrescription.display}}"},'
trans_medreq_detectedIssue = '"detectedIssue": {"reference": "Condition/{{msg.detectedIssue.reference}}","display": "{{msg.detectedIssue.display}}"},'
trans_medreq_eventHistory = '"eventHistory": {"reference": "Provenance/{{msg.eventHistory.reference}}","display": "{{msg.eventHistory.display}}"},}'

class TestliqTransform (unittest.TestCase):
    def test_liqmedreqmedcodeconcept1(self):
        print("medicationCodeableConcept.coding.code = NDC_CODE exists:")
        #Validating key medicationCodeableConcept.coding.code in liquid template
        if ("NDC_CODE" in trans_medreq_medicationCodableConcept) == True:
            print ("NDC_CODE exists in liquid template")
        #Prints message if the test fails for comparison    
        self.assertEqual("NDC_CODE" in trans_medreq_medicationCodableConcept,True,"NDC_CODE not present in liquid template") 
        
    def test_liqmedreqmedcodeconcept2(self):
        print("medicationCodeableConcept.coding.display = NDC_DESCRIPTION exists:")
        #Validating key medicationCodeableConcept.coding.display in liquid template
        if ("NDC_DESCRIPTION" in trans_medreq_medicationCodableConcept) == True:
            print ("NDC_DESCRIPTION exists in liquid template")
        #Prints message if the test fails for comparison    
        self.assertEqual("NDC_DESCRIPTION" in trans_medreq_medicationCodableConcept,True,"NDC_DESCRIPTION not present in liquid template") 

    def test_liqmedreqauthoredon(self):
        print("authorOn = DATE_OF_SERVICE exists:")
        #Validating key authorOn in liquid template
        if ("DATE_OF_SERVICE" in trans_medreq_authoredOn) == True:
            print ("DATE_OF_SERVICE exists in liquid template")
        #Prints message if the test fails for comparison    
        self.assertEqual("DATE_OF_SERVICE" in trans_medreq_authoredOn,True,"DATE_OF_SERVICE not present in liquid template") 

    def test_liqmedreqdoseinstruct(self):
        print("dosageInstruction.doseQuantity.value = QUANTITY exists:")
        #Validating key QUANTITY in liquid template
        if ("QUANTITY" in trans_medreq_dosageInstruction) == True:
            print ("QUANTITY exists in liquid template")
        #Prints message if the test fails for comparison    
        self.assertEqual("QUANTITY" in trans_medreq_dosageInstruction,True,"QUANTITY not present in liquid template") 


    def test_liqmedreqidentifier(self):
        print("identifier.value = CENSEOID exists:")
        #Validating key CENSEOID in liquid template
        if ("CENSEOID" in trans_medreq_identifier) == True:
            print ("CENSEOID exists in liquid template")
        #Prints message if the test fails for comparison    
        self.assertEqual("CENSEOID" in trans_medreq_identifier,True,"CENSEOID not present in liquid template") 

    

if __name__ == '__main__':
    unittest.main()