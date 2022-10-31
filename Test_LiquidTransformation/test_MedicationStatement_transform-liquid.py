import unittest
import json

#Copy the dictionaries as strings into variables inorder to identify and validate snowflake JSON Keys presence in newly created strings.
trans_medstat_resource = '"resourceType": "MedicationStatement","id": "{{msg.id}}","text": {"status": "generated","div": "{{msg.text.div | escape_special_chars}}"'
trans_contained = '"contained": [{"resourceType": "Medication","id": "{{msg.contained.id}}","code": {"coding": [{"system": "http://hl7.org/fhir/sid/ndc","code": "{{msg.NDC_CODE}}","display": "{{msg.NDC_DESCRIPTION}}"},]},"form": {"coding": [{% for c in msg.form.coding-%}{"system": "{{c.system}}","code": "{{c.code}}","display": "{{c.display}}"},{% endfor -%}]},"ingredient": [{% for i in msg.ingredient -%}{"itemCodeableConcept": {{% for icc in i.itemCodeableConcept -%}"coding": [{% for c in icc.coding-%}{"system": "{{c.system}}","code": "{{c.code}}","display": "{{c.display}}"},{% endfor -%}],{% endfor -%}},"strength": {{% for s in i.strength -%}"numerator": {"value": {{s.numerator.value}},"system": "{{s.numerator.system}}","code": "{{s.numerator.code}}"},"denominator": {"value": {{s.denominator.value}},"system": "{{s.denominator.system}}",            "code": "{{s.denominator.code}}"},{% endfor -%}}},{"itemCodeableConcept": {"coding": [{% for c in icc.coding-%}{"system": "{{c.system}}","code": "{{c.code}}","display": "{{c.display}}"}{% endfor -%}]},"strength": {{% for s in i.strength -%}"numerator": {"value": {{s.numerator.value}},"system": "{{s.numerator.system}},"code": "{{s.numerator.code}}"},"denominator": {"value": {{s.denominator.value}},"system": "{{s.denominator.system}}","code": "T{{s.denominator.code}}"},{% endfor -%},},},{% endfor -%}],"batch": {"lotNumber": "{{msg.batch.lotNumber}}","expirationDate": "{{msg.expirationDate | date: "yyyy-MM-dd"}}"}}],'
trans_identifier = '"identifier": [{"use": "{{msg.identifier.use}}","system": "{{msg.identifier.system}}","value": "{{msg.identifier.value}}"}],'
trans_basedon = '"basedOn": [{"reference": "MedicationRequest/{{msg.basedOn.reference}}"}],'
trans_partof = '"partOf": [{"reference": "MedicationDispense/{{msg.partOf.reference}}"}],'
trans_status = '"status": "active","statusReason":{"coding": [{% for c in msg.coding-%}{"system": "http://hl7.org/fhir/ValueSet/reason-medication-status-codes","code": "{{c.code}}","display": "{{c.display}}"},{% endfor -%}]},'
trans_category = '"category": {"coding": [{% for c in msg.category.coding -%}{"system": "http://hl7.org/fhir/ValueSet/medication-statement-category","code": "{{c.code}}","display": "{{c.display}}"},{% endfor -%}]},'
trans_medcodeconcept = '"medicationCodeableConcept": {"coding": [{% for c in msg.coding-%}{"system": "http://hl7.org/fhir/ValueSet/reason-medication-status-codes","code": "{{c.code}}","display": "{{c.display}}"},{% endfor -%}],"text": "{{msg.text}}"},'
trans_medicationresponse = '"medicationReference": {"reference": "Medication/{{msg.medicationReference.reference}}"},'
trans_subject = '"subject": {"reference": "Patient/{{msg.subject.reference}}","display": "{{msg.FIRSTNAME}} {{msg.MIDDLENAME}} {{msg.LASTNAME}}"},'
trans_context = '"context": {"reference": "Encounter/{{msg.context.reference}}","display": "{{msg.context.display}}"},'
trans_effdate = '{% if msg.effectiveDateTime -%}"effectiveDateTime": "{{msg.effectiveDateTime | date: "yyyy-MM-dd"}}",{% endif -%},{% if msg.effectivePeriod -%}"effectiveDateTime": "{{msg.msg.effectivePeriod}}",{% endif -%},"dateAsserted": "{{msg.dateAsserted | date: "yyyy-MM-dd"}}",'
trans_infosource = '"informationSource": {"reference": "Patient/{{msg.informationSource.reference}}","display": "{{msg.informationSource.display}}"},'
trans_derivedfrom = ' "derivedFrom": [{"reference": "Medication/{{msg.derivedFrom.reference}}"}],'
trans_reasoncode = '"reasonCode": [{"coding": [{% for c in msg.coding -%}{"system": "http://hl7.org/fhir/ValueSet/condition-code","code": "{{c.code}}","display": "{{c.display}}"},{% endfor -%}]}],"reasonReference": {"reference": "Condition/{{msg.reasonReference.reference}}","display": "{{msg.reasonReference.display}}"},"note": [{"text": "{{msg.note.text}}"}],'
trans_dosage = '"dosage": [{% for d in msg.dosage -%}{"sequence": {{d.sequence}},"text": "{{d.text}}","additionalInstruction": [{"text": "{{d.additionalInstruction.text}}"}],"timing": {{% for t in d.timing -%}"repeat": {"frequency": {{t.repeat.frequency}},"period": {{t.repeat.period}},"periodUnit": "{{t.repeat.periodUnit}}"}{% endfor -%}},"asNeededCodeableConcept": {{% for ncc in d.asNeededCodeableConcept -%}"coding": [{"system": "{{ncc.coding.system}}","code": "{{ncc.coding.code}}","display": "{{ncc.coding.display}}"}],{% endfor -%}},"route": {{% for r in d.route -%}"coding": [{"system": "{{r.coding.system}}","code": "{{r.coding.code}}","display": "{{r.coding.display}}"}],   {% endfor -%}},"doseAndRate": [{"type": {{% for t in d.doseAndRate.type -%}"coding": [{"system": "{{t.coding.system}}","code": "{{t.coding.code}}","display": "{{t.coding.display}}"}], {% endfor -%}},"doseRange": {{% for dr in d.doseAndRate.doseRange -%}"low": {"value": {{dr.low.value}},"unit": "{{dr.low.unit}}","system": "{{dr.low.system}}","code": "{{dr.low.code}}" },"high": { "value": {{dr.high.value}},"unit": "{{dr.high.unit}}","system": "{{dr.high.system}}","code": "{{dr.high.code}}"},{% endfor -%}}}]},{% endfor -%}]'


#Write class to run unit tests. These are created to retrieve the validate the snowflake Keys presence in liquid FHIR template that has been
#created for patient resource
#if statements are written to display message in vs code for all passed tests 

class TestliqTransform (unittest.TestCase):
     
    #Validating key resourceType in liquid template
    def test_liqmedstatrestype(self):
        if ("resourceType" in trans_medstat_resource) == True:
            print("resourceType presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("resourceType" in trans_medstat_resource,True,"resourceType not present in liquid template")
    #Validating key NDC_CODE in liquid template
    def test_liqmedstatndccode(self):
        if ("NDC_CODE" in trans_contained) == True:
            print("NDC_CODE presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("NDC_CODE" in trans_contained,True,"NDC_CODE not present in liquid template")
    #Validating key NDC_DESCRIPTION in liquid template
    def test_liqmedstatndcdesc(self):
        if ("NDC_DESCRIPTION" in trans_contained) == True:
            print("NDC_DESCRIPTION presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("NDC_DESCRIPTION" in trans_contained,True,"NDC_DESCRIPTION not present in liquid template")
    #Validating key identifier in liquid template
    def test_liqmedstatid(self):
        if ("identifier" in trans_identifier) == True:
            print ("identifier presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("identifier" in trans_identifier,True,"identifier not present in liquid template")
    #Validating key basedOn in liquid template
    def test_liqmedstatbasedon(self):
        if ("basedOn" in trans_basedon) == True:
            print ("basedOn presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("basedOn" in trans_basedon,True,"basedOn not present in liquid template")
    #Validating key partOf in liquid template
    def test_liqmedstatpartof(self):
        if ("partOf" in trans_partof) == True:
            print ("partOf presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("partOf" in trans_partof,True,"partOf not present in liquid template")
    #Validating key status in liquid template
    def test_liqmedstatstatus(self):
        if ("status" in trans_status) == True:
            print ("status presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("status" in trans_status,True,"status not present in liquid template")    
    #Validating key statusReason in liquid template
    def test_liqmedstatreason(self):
        if ("statusReason" in trans_status) == True:
            print ("statusReason presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("statusReason" in trans_status,True,"statusReason not present in liquid template")
    #Validating key category in liquid template
    def test_liqmedstatcat(self):
        if ("category" in trans_category) == True:
            print ("category presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("category" in trans_category,True,"category not present in liquid template")
    #Validating key medicationCodeableConcept in liquid template
    def test_liqmedstatcodeconcept(self):
        if ("medicationCodeableConcept" in trans_medcodeconcept) == True:
            print ("medicationCodeableConcept presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("medicationCodeableConcept" in trans_medcodeconcept,True,"medicationCodeableConcept not present in liquid template")    
    #Validating key medicationReference in liquid template
    def test_liqmedstatmedref(self):
        if ("medicationReference" in trans_medicationresponse) == True:
            print ("medicationReference presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("medicationReference" in trans_medicationresponse,True,"medicationReference not present in liquid template")
    #Validating key subject in liquid template
    def test_liqmedstatsub(self):
        if ("subject" in trans_subject) == True:
            print ("subject presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("subject" in trans_subject,True,"subject not present in liquid template")
    #Validating key FIRSTNAME in liquid template
    def test_liqmedstatfname(self):
        if ("FIRSTNAME" in trans_subject) == True:
            print ("FIRSTNAME presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("FIRSTNAME" in trans_subject,True,"FIRSTNAME not present in liquid template")
    #Validating key MIDDLENAME in liquid template
    def test_liqmedstatmname(self):
        if ("MIDDLENAME" in trans_subject) == True:
            print ("MIDDLENAME presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MIDDLENAME" in trans_subject,True,"MIDDLENAME not present in liquid template")
    #Validating key LASTNAME in liquid template
    def test_liqmedstatlname(self):
        if ("LASTNAME" in trans_subject) == True:
            print ("LASTNAME presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("LASTNAME" in trans_subject,True,"LASTNAME not present in liquid template")
    #Validating key context in liquid template
    def test_liqmedstatcontext(self):
        if ("context" in trans_context) == True:
            print ("context presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("context" in trans_context,True,"context not present in liquid template")
    #Validating key effectiveDateTime in liquid template
    def test_liqmedstateffdt(self):
        if ("effectiveDateTime" in trans_effdate) == True:
            print ("effectiveDateTime presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("effectiveDateTime" in trans_effdate,True,"effectiveDateTime not present in liquid template")
    #Validating key effectivePeriod in liquid template
    def test_liqmedstateffperiod(self):
        if ("effectivePeriod" in trans_effdate) == True:
            print ("effectivePeriod presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("effectivePeriod" in trans_effdate,True,"effectivePeriod not present in liquid template")
    #Validating key dateAsserted in liquid template
    def test_liqmedstatdtassert(self):
        if ("dateAsserted" in trans_effdate) == True:
            print ("dateAsserted presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("dateAsserted" in trans_effdate,True,"dateAsserted not present in liquid template")
    #Validating key informationSource in liquid template
    def test_liqmedstatinfosrc(self):
        if ("informationSource" in trans_infosource) == True:
            print ("informationSource presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("informationSource" in trans_infosource,True,"informationSource not present in liquid template")
    #Validating key derivedFrom in liquid template
    def test_liqmedstatderfrm(self):
        if ("derivedFrom" in trans_derivedfrom) == True:
            print ("derivedFrom presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("derivedFrom" in trans_derivedfrom,True,"derivedFrom not present in liquid template")
    #Validating key reasonCode in liquid template
    def test_liqmedstatrsncode(self):
        if ("reasonCode" in trans_reasoncode) == True:
            print ("reasonCode presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("reasonCode" in trans_reasoncode,True,"reasonCode not present in liquid template")
    #Validating key reasonReference in liquid template
    def test_liqmedstatrsnref(self):
        if ("reasonReference" in trans_reasoncode) == True:
            print ("reasonReference presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("reasonReference" in trans_reasoncode,True,"reasonReference not present in liquid template")
    #Validating key note in liquid template
    def test_liqmedstatnote(self):
        if ("note" in trans_reasoncode) == True:
            print ("note presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("note" in trans_reasoncode,True,"note not present in liquid template")
    #Validating key dosage in liquid template
    def test_liqmedstatdosage(self):
        if ("dosage" in trans_dosage) == True:
            print ("dosage presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("dosage" in trans_dosage,True,"dosage not present in liquid template")

if __name__ == '__main__':
    unittest.main()