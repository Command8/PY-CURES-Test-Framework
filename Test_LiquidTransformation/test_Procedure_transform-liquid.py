import unittest
import json

trans_identifier = '"resourceType" : "Procedure","identifier" : [{"use": "official","value": "{{msg.CENSEOID}}","assigner":{"display":"Signify Health CenseoID"}},{"use": "usual","value": "{{msg.MEMBER_NUMBER}}","assigner":{"display":"Member Number"}},{"use": "usual","value": {{msg.HICN}},"assigner":{"display":"Medicare Identification Number"}}'
trans_instcanon = '"instantiatesCanonical" : ["http://hl7.org/fhir/StructureDefinition/Questionnaire"],'
trans_insturl = '"instantiatesUri": ["{{msg.instantiatesUri}}"],'
trans_basedon = '"basedOn": [{"reference": "CarePlan/{{msg.basedOn.reference}}"},{"reference": "ServiceRequest/{{msg.basedOn.reference}}"}],'
trans_partof = '"partOf" : [{"reference": "Observation/{{msg.partOf.reference}}"},{"reference": "Procedure/{{msg.partOf.reference}}"}], '
trans_status = '"status" : "unknown","statusReason" : {"coding": [{"system": "http://snomed.info/sct","code": "{{msg.statusReason.coding.code}}","display": "{{msg.statusReason.coding.display}}",}],"text": "{{msg.statusReason.text}}"},'
trans_Category = ' "category" : {"coding": [{"system": "http://snomed.info/sct","code": "{{msg.category.coding.code}}","display": "{{msg.category.coding.display}}",}],a"text": "{{msg.category.text}}"},'
trans_cptcode = '"code" : {"coding": [{"system": "http://snomed.info/sct","code": "{{msg.CPTCODE_PRIMARY}}","display": "{{msg.code.coding.display}}",},{"system": "http://snomed.info/sct","code": "{{msg.PROCEDURE_CODE_2}}","display": "{{msg.code.coding.display}}",}],"text": "{{msg.code.text}}"},'
trans_subject = '"subject" : {"reference": "Patient/{{msg.subject.reference}}"},'
trans_encounter = '"encounter" : {"reference": "Encounter/{{msg.encounter.reference}}"},'
trans_Performed  = '"performedDateTime" : "{{msg.DATE_OF_SERVICE | date: "yyyy-MM-dd"}}","performedPeriod" : {"start": "{{msg.DATE_OF_SERVICE | date: "yyyy-MM-dd"}}","end": "{{msg.effectivePeriod.end | date: "yyyy-MM-dd"}}"},"performedString" : "{{msg.performedString}}","performedAge" : "{{msg.performedAge}}","performedRange" :{"low": {"value": "{{msg.performedRange.low.value}}","unit": "{{msg.performedRange.low.unit}}","system": "{{msg.performedRange.low.system}}",   "code": "{{msg.performedRange.low.code}}"},"high": {"value": "{{msg.performedRangee.high.value}}","unit": "{{msg.performedRange.high.unit}}","system": "{{msg.performedRange.high.system}}","code": "{{msg.performedRange.high.code}}"}},'
trans_recorder = '"recorder" : {"reference": "Practitioner/{{msg.recorder.reference}}"}, '              
trans_asserter = '"asserter" : {"reference": "Practitioner/{{msg.asserter.reference}}"}, '
trans_performer = '"performer" : [{"function" : {"coding": [{"system": "http://snomed.info/sct","code": "{{msg.SPECIALTY_CODE}}","display": "{{msg.SPECIALTY_NAME}}",}],},"actor" : { "reference": "Practitioner/{{msg.performer.actor.reference}}"},"onBehalfOf" : {"reference": "Organization/{{msg.performer.onBehalfOf.reference}}"}}],'
trans_location = '"location" : {"reference": "Location/{{msg.location.reference}}"},'
trans_DxCodes = '"reasonCode": [{"coding": [{% if msg.DX_1 != ""-%}{ "system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_1}}","display": "{{reasonCode.coding.display}}"},{% else %}"",{% endif -%}{% if msg.DX_2 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_2}}","display": "{{reasonCode.coding.display}}"},{% else %}"",{% endif -%}{% if msg.DX_3 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_3}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_4 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_4}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_5 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_5}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_6 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_6}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_7 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_7}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_8 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_8}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_9 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_9}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_10 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_10}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_11 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_11}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_12 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_12}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_13 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_13}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_14 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_14}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_15 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_15}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_16 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_16}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_17 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_17}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_18 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_18}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_19 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_19}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_20 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_20}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_21 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_21}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_22 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_22}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_23 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_23}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_24 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_24}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_25 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_25}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_26 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_26}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_27 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_27}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_28 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_28}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_29 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_29}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}{% if msg.DX_30 != ""-%}{"system": "http://hl7.org/fhir/ValueSet/icd-10","code": "{{msg.DX_30}}","display": "{{reasonCode.coding.display}}"{% else %}"",{% endif -%}]}],'
trans_rsnref = '"reasonReference" : [{"reference": "Observation/{{msg.reasonReference.reference}}"},{"reference": "Procedure/{{msg.reasonReference.reference}}"}],'
trans_bodysuite = ' "bodySite" : [{"coding": [{"system": "http://snomed.info/sct","code": "{{msg.bodySite.coding.code}}","display": "{{msg.bodySite.coding.display}}"}],"text": "{{msg.bodySite.coding.code.text}}"}], '
trans_outcome = '"outcome" : {"coding": [{"system": "http://snomed.info/sct","code": "{{msg.outcome.coding.code}}","display": "{{msg.outcome.coding.display}}"}],"text": "{{msg.outcome.code.text}}"}, '
trans_report = '"report" : [{"reference": "Composition/{{msg.report.reference}}"},{"reference": "DiagnosticReport/{{msg.report.reference}}"},{"reference": "DocumentReference/{{msg.report.reference}}"}],'
trans_complication = '  "complication" : [{"coding": [{"system": "http://snomed.info/sct","code": "{{msg.complication.coding.code}}","display": "{{msg.complication.coding.display}}"}],"text": "{{msg.complication.code.text}}"}],"complicationDetail" : [{"reference": "Condition/{{msg.complicationDetail.reference}}"},], '
trans_followup = '"followUp" : [{ "coding": [{"system": "http://snomed.info/sct","code": "{{msg.followUp.coding.code}}","display": "{{msg.followUp.coding.display}}"}],"text": "{{msg.followUp.code.text}}"}],'
trans_note = '"note" : [{"authorReference": {"reference": "Practitioner/{{msg.note.authorReference.reference}}","display": "{{msg.note.authorReference.display}}"},"authorString": "{{msg.note.authorString}}","time": "{{msg.note.time | date: "yyyy-MM-dd"}}","text": "{{msg.note.text}}"}],'
trans_focaldevice = '"focalDevice" : [{"action" : {"coding": [{"system": "http://snomed.info/sct","code": "{{msg.focalDevice.action.coding.code}}","display": "{{msg.focalDevice.action.coding.display}}"}], "text": "{{msg.focalDevice.action.code.text}}"},"manipulated" : {"reference": "Device/{{msg.manipulated.reference}}"}}],'
trans_usedref = '"usedReference" : [{"reference": "Device/{{msg.usedReference.reference}}"},{"reference": "Medication/{{msg.usedReference.reference}}"}],'
trans_usecode = '"usedCode" : [{"coding": [{"system": "http://snomed.info/sct","code": "{{msg.usedCode.coding.code}}","display": "{{msg.usedCode.coding.display}}"}],"text": "{{msg.usedCode.text}}"}]}'


#Write class to run unit tests. These are created to retrieve the validate the snowflake Keys presence in liquid FHIR template that has been
#created for patient resource
# if statements are written to display message in vs code for all passed tests 

class TestliqTransform (unittest.TestCase):

     
    #Validating key CPTCODE_PRIMARY in liquid template
    def test_liqProccptprim(self):
        if ("CPTCODE_PRIMARY" in trans_cptcode) == True:
            print("CPTCODE_PRIMARY presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("CPTCODE_PRIMARY" in trans_cptcode,True,"CPTCODE_PRIMARY not present in liquid template")
    #Validating key PROCEDURE_CODE_2 in liquid template
    def test_liqProccode2(self):
        if ("PROCEDURE_CODE_2" in trans_cptcode) == True:
            print ("PROCEDURE_CODE_2 presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROCEDURE_CODE_2" in trans_cptcode,True,"PROCEDURE_CODE_2 not present in liquid template")
    #Validating key #Validating key DATE_OF_SERVICE in liquid template
    def test_liqProcdos(self):
        if ("DATE_OF_SERVICE" in trans_Performed) == True:
            print ("DATE_OF_SERVICE presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("DATE_OF_SERVICE" in trans_Performed,True,"DATE_OF_SERVICE not present in liquid template") 
    #Validating key #Validating key CENSEOID in liquid template
    def test_liqProccensid(self):
        if ("CENSEOID" in trans_identifier) == True:
            print ("CENSEOID presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("CENSEOID" in trans_identifier,True,"CENSEOID not present in liquid template")
    #Validating key #Validating key MEMBER_NUMBER in liquid template
    def test_liqProcmemnbr(self):
        if ("MEMBER_NUMBER" in trans_identifier) == True:
            print ("MEMBER_NUMBER presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_NUMBER" in trans_identifier,True,"MEMBER_NUMBER not present in liquid template")
    #Validating key #Validating key HICN in liquid template
    def test_liqProchicn(self):
        if ("HICN" in trans_identifier) == True:
            print ("HICN presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("HICN" in trans_identifier,True,"HICN not present in liquid template")

    #Validating key #Validating keys for 30 DX Codes in liquid template
    def test_liqProcDXCodes(self):
        #Loop runs from 0 till 30; hence increment the variable by 1
        for y in range(30):
            if (str('DX_'+ str(y+1)) in trans_DxCodes) == True:
                print ("DX_" + str(y+1) + " presence is validated in liquid template")
            #Prints message if the test fails for comparison
            self.assertEqual(str('DX_'+str(y+1)) in trans_DxCodes,True,"DX_" + str(y+1) + " not present in liquid template")

if __name__ == '__main__':
    unittest.main()