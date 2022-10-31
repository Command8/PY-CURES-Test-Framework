import unittest
import json

trans_resourceType = '{"resourceType" : "Observation",'
trans_identifier = '"identifier" : [{"use": "official","value": {{msg.CENSEOID}},"assigner":{"display":"Signify Health CenseoID"}},{"use": "usual","value": {{msg.HICN}},"assigner":{"display":"Medicare Identification Number"}}],'
trans_basedOn = '"basedOn" : [{ "reference": "CarePlan/{{msg.basedOn.reference}}","display": "{{msg.basedOn.display}}"},{"reference": "MedicationRequest/{{msg.basedOn.reference}}","display": "{{msg.basedOn.display}}"}],'
trans_partOf = '"partOf" : [{"reference": "Immunization/{{msg.partOf.reference}}","display": "{{msg.partOf.display}}"},{"reference": "MedicationDispense/{{msg.partOf.reference}}","display": "{{msg.partOf.display}}"},{"reference": "MedicationStatement/{{msg.partOf.reference}}","display": "{{msg.partOf.display}}"},{"reference": "Procedure/{{msg.partOf.reference}}","display": "{{msg.partOf.display}}"}],'
trans_status = '"status" : "final",' 
trans_category =  '"category" : [{{% if msg.LABTESTID != "" -%}"coding": [{"system": "http://terminology.hl7.org/CodeSystem/observation-category","code": "laboratory","display": "Laboratory",}],{% endif -%}"text": "{{msg.category.text}}"}], '
trans_code =   '"code" : { "coding": [{"system": "http://loinc.org","code": "{{msg.LOINC}}","display": "{{msg.code.coding.display}}"}],"text": "{{msg.LABTESTNAME}}"},'
trans_subject = '"subject" : { "reference": "Patient/{{msg.PATIENT_FHIR_ID}}","display": "{{msg.MEMBER_NAME}}"},'
trans_focus =   '"focus" : [{ "reference": "Procedure/{{msg.focus.reference}}","display": "{{msg.focus.display}}"}],'
trans_encounter = '"encounter" : {"reference": "Encounter/{{msg.encounter.reference}}","display": "{{msg.encounter.display}}"},'
trans_effectiveDateTime = '"effectiveDateTime" : "{{msg.LABRESULTSDATECOLLECTED | date: "yyyy-MM-dd"}}",'
trans_effictivePeriod = '"effectivePeriod" : {"start": "{{msg.effectivePeriod.start | date: "yyyy-MM-dd"}}","end": "{{msg.effectivePeriod.end | date: "yyyy-MM-dd"}}"},'
trans_effectiveTime = '"effectiveTiming" : {"event":"{{msg.effectiveTiming.event}}"},'
trans_effectiveInstant = '"effectiveInstant" : "{{msg.effectiveInstant | date: "yyyy-MM-dd"}}",'
trans_issued =  '"issued" : "{{msg.LABRESULTSDATERELEASED | date: "yyyy-MM-dd"}}",'
trans_performer = '"performer" : [{"reference": "Practitioner/{{msg.performer.reference}}","display": "{{msg.performer.display}}"}],'
trans_valueQuantity = '"valueQuantity" : { "value": "{{msg.LABRESULTVALUE}}","unit": "{{msg.RESULTSUNITS}}","system": "http://unitsofmeasure.org","code": "{{msg.valueQuantity.code}}"},'
trans_valueCodeableConcept = '"valueCodeableConcept" : { "coding": [{"system": "{{msg.valueCodeableConcept.coding.system}}","code": "{{msg.valueCodeableConcept.coding.code}}","display": "{{msg.valueCodeableConcept.coding.display}}"}],"text": "{{msg.valueCodeableConcept.text}}"},'
trans_valueString = '"valueString" : "{{msg.valueString}}",'
trans_valueBoolean = '"valueBoolean" : "{{msg.valueBoolean}}",'
trans_valueInteger = '"valueInteger" : "{{msg.valueInteger}}",'
trans_valueRange = '"valueRange" : {"low":{"value":"{{msg.valueRange.low.value}}","unit": "{{msg.valueRange.low.unit}}","system": "{{msg.valueRange.low.system}}","code": "{{msg.valueRange.low.code}}",},"high":{"value":"{{msg.valueRange.high.value}}","unit": "{{msg.valueRange.high.unit}}","system":"{{msg.valueRange.high.system}}","code": "{{msg.valueRange.high.code}}"},'
trans_valueRatio = '"valueRatio" : {"numerator": {"value": "{{msg.valueRatio.numerator.value}}"},"denominator": {"value": "{{msg.valueRatio.denominator.value}}"}},'
trans_valueSampleData = '"valueSampledData" : {"origin": "{{msg.valueSampledData.origin}}","period": "{{msg.valueSampledData.period}}","factor": "{{msg.valueSampledData.factor}}","lowerLimit":"{{msg.valueSampledData.lowerLimit}}","upperLimit": "{{msg.valueSampledData.upperLimit}}","dimensions": "{{msg.valueSampledData.dimensions}}","data": "{{msg.valueSampledData.data}}"},'
trans_valueTime = '"valueTime" : "{{msg.valueTime | date: "hh:mm:ss"}}",'
trans_valueDateTime = '"valueDateTime" : "{{msg.valueDateTime | date: "yyyy-MM-dd"}}",'
trans_valuePeriod = '"valuePeriod" : { "start": "{{msg.valuePeriod.start | date: "yyyy-MM-dd"}}","end": "{{msg.valuePeriod.end | date: "yyyy-MM-dd"}}"},'
trans_dataAbsentReason = '"dataAbsentReason" : {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/data-absent-reason","code": "{{msg.dataAbsentReason.coding.code}}","display": "{{msg.dataAbsentReason.coding.display}}"],"text": "{{msg.dataAbsentReason.text}}"}, '
trans_interpretation = '"interpretation" : [{ "coding": [{"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation","code": "{{msg.ABNORMALINDICATOR}}",{% assign display = "display": "{{msg.interpretation.coding.display}}" %}{% case {{msg.ABNORMALINDICATOR}} %}{%when N %}"display": "Normal"{%when A %}"display": "Abnormal"{%when H %}"display": "High"{%when L %}"display": "Low"{% else %}"display": "{{msg.interpretation.coding.display}}"{% endcase %}}],"text": "{{msg.interpretation.text}}"  }],'
trans_note = '"note" : [{ "text": "{{msg.LABRESULTSCOMMENT}}"}],'
trans_bodySite = '"bodySite" : {"coding": [{"system": "http://snomed.info/sct","code": "{{msg.bodySite.coding.code}}","display": "{{msg.bodySite.coding.display}}"}],"text": "{{msg.bodySite.text}}"},'
trans_method = '"method" : {"coding": [{"system": "http://snomed.info/sct","code": "{{msg.method.coding.code}}","display": "{{msg.method.coding.display}}"}],"text": "{{msg.method.text}}"}, '
trans_specimen = '"specimen" : { "reference": "Specimen/{{msg.specimen.reference}}","display": "{{msg.specimen.display}}"},'
trans_device = '"device" : {"reference": "Device/{{msg.device.reference}}","display": "{{msg.device.display}}"},'
trans_referenceRange = '"referenceRange" : [{"low" : {"value":"{{msg.NORMALSLOW}}","unit": "{{msg.RESULTSUNITS}}","system": "http://unitsofmeasure.org","code": ""{{msg.referenceRange.low.code}}"}, "high" : { "value":"{{msg.NORMALSHIGH}}","unit": "{{msg.RESULTSUNITS}}","system": "http://unitsofmeasure.org","code": "{{msg.referenceRange.high.code}}"},"type" : {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/referencerange-meaning","code": "{{msg.referenceRange.type.coding.code}}","display": "{{msg.referenceRange.type.coding.display}}"}], "text": "{{msg.referenceRange.type.text}}" }, "appliesTo" : { "coding": [{"system": "http://snomed.info/sct","code": "{{msg.referenceRange.appliesTo.coding.code}}","display": "{{msg.referenceRange.appliesTo.coding.display}}"}],"text": "{{msg.appliesTo.text}}", "coding": [{"system": "http://terminology.hl7.org/ValueSet/v3-Race","code": "{{msg.referenceRange.appliesTo.coding.code}}","display": "{{msg.referenceRange.appliesTo.coding.display}}"}],"text": "{{msg.appliesTo.text}}" }], "age" : { "low":{"value":"{{msg.referenceRange.low.value}}"},"high":{"value":"{{msg.referenceRange.low.value}}"}}, "text" : "{{msg.text}}" }],'
trans_hasMember = '"hasMember" : [{"reference": "Observation/{{msg.hasMember.reference}}","display": "{{msg.hasMember.display}}"},{"reference": "QuestionnaireResponse/{{msg.hasMember.reference}}","display": "{{msg.hasMember.display}}"}],'
trans_derivedFrom = '"derivedFrom" : [{"reference": "Observation/{{msg.derivedFrom.reference}}","display": "{{msg.derivedFrom.display}}"},{"reference": "QuestionnaireResponse/{{msg.derivedFrom.reference}}","display": "{{msg.derivedFrom.display}}"}],'
trans_component = '"component" : [{ "code" : { "coding": [{"system": "http://loinc.org","code": "{{msg.component.code.coding.code}}","display": "{{msg.component.code.coding.display}}"}],"text": "{{msg.component.code.text}}"}, '
trans_valueQuantity2 = '"valueQuantity" : {"value": "{{msg.valueQuantity.value}}","unit": "{{msg.valueQuantity.unit}}","system": "http://unitsofmeasure.org","code": "{{msg.valueQuantity.code}}"},'
trans_valueCodeableConcept2 = '"valueCodeableConcept" : { "coding": [{"system": "{{msg.valueCodeableConcept.system.code}}","code": "{{msg.valueCodeableConcept.coding.code}}","display": "{{msg.valueCodeableConcept.coding.display}}"}],"text": "{{msg.valueCodeableConcept.text}}"},'
trans_valueString2 = '"valueString" : "{{msg.component.valueString}}",'
trans_valueBoolean2 = '"valueBoolean" : "{{msg.component.valueBoolean}}",'
trans_valueInteger2 = '"valueInteger" : "{{msg.component.valueInteger}}", '    
trans_valueRange2 = '"valueRange" : {"low":{"value":"{{msg.component.valueRange.low.value}}"},"high":{"value":"{{msg.component.valueRange.high.value}}"}},'
trans_valueRatio2 = '"valueRatio" : { "numerator": {"value": "{{msg.component.valueRatio.numerator.value}}"},"denominator": {"value": "{{msg.component.valueRatio.denominator.value}}"}},'
trans_valueSampleData2 = '"valueSampledData" : {"origin": "{{msg.valueSampledData.origin}}","period": "{{msg.valueSampledData.period}}","factor": "{{msg.valueSampledData.factor}}","lowerLimit":"{{msg.valueSampledData.lowerLimit}}","upperLimit": "{{msg.valueSampledData.upperLimit}}","dimensions": "{{msg.valueSampledData.dimensions}}","data": "{{msg.valueSampledData.data}}"},'
trans_valueTime2 = '"valueTime" : "{{msg.valueTime | date: "hh:mm:ss"}}",'
trans_valueDateTime2 = '"valueDateTime" : "{{msg.valueDateTime | date: "yyyy-MM-dd"}}",'
trans_valuePeriod2 = '"valuePeriod" : { "start": "{{msg.valuePeriod.start | date: "yyyy-MM-dd"}}","end": "{{msg.valuePeriod.end | date: "yyyy-MM-dd"}}"},'
trans_dataAbsentReason2 = '"dataAbsentReason" : {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/data-absent-reason","code": "{{msg.dataAbsentReason.coding.code}}","display": "{{msg.dataAbsentReason.coding.display}}"}],"text": "{{msg.dataAbsentReason.text}}"},'
trans_interpretation2 = '"interpretation" : [{"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation","code": "{{msg.interpretation.coding.code}}","display": "{{msg.interpretation.coding.display}}"}],"text": "{{msg.interpretation.text}}"}], '
trans_referenceRange2 = '"referenceRange" : [{"low": {"value": "{{msg.referenceRange.low.value}}","unit": "{{msg.referenceRange.low.unit}}","system": "http://unitsofmeasure.org","code": "{{msg.referenceRange.low.code}}"},"high": {"value": "{{msg.referenceRange.high.value}}","unit": "{{msg.referenceRange.high.unit}}","system": "http://unitsofmeasure.org","code": "{{msg.referenceRange.high.code}}"}}]}]}'


class TestliqTransform (unittest.TestCase):


    #Validating key resourceType in liquid template
    def test_observresourceType(self):
        if ("Observation" in trans_resourceType) == True:
            print("Observation presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("Observation" in trans_resourceType,True,"id not present in liquid template")


    #Validating key CENSEOID in liquid template
    def test_observidentifier(self):
        if ("CENSEOID" in trans_identifier) == True:
            print("CENSEOID presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("CENSEOID" in trans_identifier,True,"CENSEOID not present in liquid template")


    #Validating key trans_basedOn in liquid template
    def test_observbasedOn(self):
        if ("basedOn.reference" in trans_basedOn) == True:
            print("basedOn.reference presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("basedOn.reference" in trans_basedOn,True,"basedOn.reference not present in liquid template")

    #Validating key trans_basedOn in liquid template
    def test_observpartof(self):
        if ("partOf.reference" in trans_partOf) == True:
            print("partOf.reference presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("partOf.reference" in trans_partOf,True,"partOf.reference not present in liquid template")


    #Validating key trans_basedOn in liquid template
    def test_observstatus (self):
        if ("final" in trans_status) == True:
            print("final presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("final" in trans_status,True,"final not present in liquid template")


   #Validating key trans_category in liquid template
    def test_observcategory (self):
        if ("LABTESTID" in trans_category) == True:
            print("LABTESTID presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("LABTESTID" in trans_category,True,"LABTESTID not present in liquid template")


    #Validating key trans_category in liquid template
    def test_observcategory (self):
        if ("LABTESTID" in trans_category) == True:
            print("LABTESTID presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("LABTESTID" in trans_category,True,"LABTESTID not present in liquid template")


   #Validating key trans_code in liquid template
    def test_observcode (self):
        if ("LOINC" in trans_code) == True:
            print("LOINC presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("LOINC" in trans_code,True,"LOINC not present in liquid template")


   #Validating key trans_subject in liquid template
    def test_observsubject (self):
        if ("PATIENT_FHIR_ID" in trans_subject) == True:
            print("PATIENT_FHIR_ID presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PATIENT_FHIR_ID" in trans_subject,True,"PATIENT_FHIR_ID not present in liquid template")

   #Validating key trans_focus in liquid template
    def test_observfocus (self):
        if ("focus.reference" in trans_focus) == True:
            print("focus.reference presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("focus.reference" in trans_focus,True,"focus.reference not present in liquid template")

   #Validating key trans_encounter in liquid template
    def test_observencounter (self):
        if ("encounter.reference" in trans_encounter) == True:
            print("encounter.reference presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("encounter.reference" in trans_encounter,True,"encounter.reference not present in liquid template")

   #Validating key trans_effictivePeriod in liquid template
    def test_observeffectperiod (self):
        if ("effectivePeriod.start" in trans_effictivePeriod) == True:
            print("effectivePeriod.start presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("effectivePeriod.start" in trans_effictivePeriod,True,"effectivePeriod.start not present in liquid template")

   #Validating key trans_effectiveTime in liquid template
    def test_observeffecttime (self):
        if ("effectiveTiming.event" in trans_effectiveTime) == True:
            print("effectiveTiming.event presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("effectiveTiming.event" in trans_effectiveTime,True,"effectiveTiming.event not present in liquid template")

    #Validating key trans_effectiveInstant in liquid template
    def test_observeffectinstant (self):
        if ("effectiveInstant" in trans_effectiveInstant) == True:
            print("effectiveInstant presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("effectiveInstant" in trans_effectiveInstant,True,"effectiveInstant not present in liquid template")

    #Validating key trans_issued in liquid template
    def test_observissued (self):
        if ("LABRESULTSDATERELEASED" in trans_issued) == True:
            print("LABRESULTSDATERELEASED presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("LABRESULTSDATERELEASED" in trans_issued,True,"LABRESULTSDATERELEASED not present in liquid template")

    #Validating key trans_performer in liquid template
    def test_observissued (self):
        if ("performer.reference" in trans_performer) == True:
            print("performer.reference presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("performer.reference" in trans_performer,True,"performer.reference not present in liquid template")

    #Validating key trans_valueQuantity in liquid template
    def test_observvaluequantity1 (self):
        if ("LABRESULTVALUE" in trans_valueQuantity) == True:
            print("LABRESULTVALUE presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("LABRESULTVALUE" in trans_valueQuantity,True,"LABRESULTVALUE not present in liquid template")

    #Validating key trans_valueQuantity in liquid template
    def test_observvaluequantity2 (self):
        if ("RESULTSUNITS" in trans_valueQuantity) == True:
            print("RESULTSUNITS presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("RESULTSUNITS" in trans_valueQuantity,True,"RESULTSUNITS not present in liquid template")

    #Validating key trans_valueCodeableConcept in liquid template
    def test_observvaluecodesystem (self):
        if ("valueCodeableConcept.coding.system" in trans_valueCodeableConcept) == True:
            print("valueCodeableConcept.coding.system presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueCodeableConcept.coding.system" in trans_valueCodeableConcept,True,"valueCodeableConcept.coding.system not present in liquid template")

    #Validating key trans_valueCodeableConcept in liquid template
    def test_observvaluecodedisplay (self):
        if ("valueCodeableConcept.coding.display" in trans_valueCodeableConcept) == True:
            print("valueCodeableConcept.coding.display presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueCodeableConcept.coding.display" in trans_valueCodeableConcept,True,"valueCodeableConcept.coding.display not present in liquid template")

    #Validating key trans_valueCodeableConcept in liquid template
    def test_observvaluecodetext (self):
        if ("valueCodeableConcept.text" in trans_valueCodeableConcept) == True:
            print("valueCodeableConcept.text presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueCodeableConcept.text" in trans_valueCodeableConcept,True,"valueCodeableConcept.text not present in liquid template")


    #Validating key trans_valueString in liquid template
    def test_observvaluestring (self):
        if ("valueString" in trans_valueString) == True:
            print("valueString presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueString" in trans_valueString,True,"valueString not present in liquid template")

    #Validating key trans_valueBoolean in liquid template
    def test_observvalueboolean (self):
        if ("valueBoolean" in trans_valueBoolean) == True:
            print("valueBoolean presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueBoolean" in trans_valueBoolean,True,"valueBoolean not present in liquid template")

    #Validating key trans_valueInteger in liquid template
    def test_observvalueinteger (self):
        if ("valueInteger" in trans_valueInteger) == True:
            print("valueInteger presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueInteger" in trans_valueInteger,True,"valueInteger not present in liquid template")

    #Validating key trans_valueRange in liquid template
    def test_observvaluerange (self):
        if ("valueRange" in trans_valueRange) == True:
            print("valueRange presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueRange" in trans_valueRange,True,"valueRange not present in liquid template")

    #Validating key trans_valueRatio  in liquid template
    def test_observvalueratio (self):
        if ("valueRatio" in trans_valueRatio ) == True:
            print("valueRatio presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueRatio" in trans_valueRatio ,True,"valueRatio not present in liquid template")

    #Validating key trans_valueRatio  in liquid template
    def test_observvaluerationum (self):
        if ("valueRatio.numerator.value" in trans_valueRatio ) == True:
            print("valueRatio.numerator.value presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueRatio.numerator.value" in trans_valueRatio ,True,"valueRatio.numerator.value not present in liquid template")

    #Validating key trans_valueRatio  in liquid template
    def test_observvalueratioden (self):
        if ("valueRatio.denominator.value" in trans_valueRatio) == True:
            print("valueRatio.denominator.value presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueRatio.denominator.value" in trans_valueRatio,True,"valueRatio.denominator.value not present in liquid template")

    #Validating key trans_valueSampleData   in liquid template
    def test_observsampledataorigin (self):
        if ("valueSampledData.origin" in trans_valueSampleData) == True:
            print("valueSampledData.origin presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueSampledData.origin" in trans_valueSampleData,True,"valueSampledData.origin not present in liquid template")

    #Validating key trans_valueSampleData   in liquid template
    def test_observsampledataperiod (self):
        if ("valueSampledData.period" in trans_valueSampleData) == True:
            print("valueSampledData.period presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueSampledData.period" in trans_valueSampleData,True,"valueSampledData.period not present in liquid template")

    #Validating key trans_valueTime    in liquid template
    def test_observvaluetime (self):
        if ("valueTime" in trans_valueTime) == True:
            print("valueTime presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueTime" in trans_valueTime,True,"valueTime not present in liquid template")

    #Validating key trans_valueDateTime in liquid template
    def test_observvaluedatetime (self):
        if ("valueDateTime" in trans_valueDateTime) == True:
            print("valueDateTime presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueDateTime" in trans_valueDateTime,True,"valueDateTime not present in liquid template")

    #Validating key trans_valuePeriod  in liquid template
    def test_observvalueperiodstart (self):
        if ("valuePeriod.start" in trans_valuePeriod) == True:
            print("valuePeriod.start presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valuePeriod.start" in trans_valuePeriod,True,"valuePeriod.start not present in liquid template")

    #Validating key trans_valuePeriod  in liquid template
    def test_observvalueperiodend (self):
        if ("valuePeriod.end" in trans_valuePeriod) == True:
            print("valuePeriod.end presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valuePeriod.end" in trans_valuePeriod,True,"valuePeriod.end not present in liquid template")

        #Validating key trans_dataAbsentReason   in liquid template
    def test_observabsentreasoncode (self):
        if ("dataAbsentReason.coding.code" in trans_dataAbsentReason ) == True:
            print("dataAbsentReason.coding.code presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("dataAbsentReason.coding.code" in trans_dataAbsentReason ,True,"dataAbsentReason.coding.code not present in liquid template")

    #Validating key trans_dataAbsentReason   in liquid template
    def test_observabsentreasoncode (self):
        if ("dataAbsentReason.coding.code" in trans_dataAbsentReason ) == True:
            print("dataAbsentReason.coding.code presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("dataAbsentReason.coding.code" in trans_dataAbsentReason ,True,"dataAbsentReason.coding.code not present in liquid template")

    #Validating key trans_dataAbsentReason   in liquid template
    def test_observabsentreasondisplay (self):
        if ("dataAbsentReason.coding.display" in trans_dataAbsentReason ) == True:
            print("dataAbsentReason.coding.display presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("dataAbsentReason.coding.display" in trans_dataAbsentReason ,True,"dataAbsentReason.coding.display not present in liquid template")

    #Validating key trans_dataAbsentReason   in liquid template
    def test_observabsentreasontext (self):
        if ("dataAbsentReason.text" in trans_dataAbsentReason ) == True:
            print("dataAbsentReason.text presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("dataAbsentReason.text" in trans_dataAbsentReason ,True,"dataAbsentReason.text not present in liquid template")

    #Validating key trans_interpretation    in liquid template
    def test_observinterpretation (self):
        if ("ABNORMALINDICATOR" in trans_interpretation) == True:
            print("ABNORMALINDICATOR presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("ABNORMALINDICATOR" in trans_interpretation,True,"ABNORMALINDICATOR not present in liquid template")

    #Validating key trans_interpretation    in liquid template
    def test_observinterpretationdisplay (self):
        if ("interpretation.coding.display" in trans_interpretation) == True:
            print("interpretation.coding.display presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("interpretation.coding.display" in trans_interpretation,True,"interpretation.coding.display not present in liquid template")

    #Validating key trans_interpretation    in liquid template
    def test_observinterpretationtext (self):
        if ("interpretation.text" in trans_interpretation) == True:
            print("interpretation.text presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("interpretation.text" in trans_interpretation,True,"interpretation.text not present in liquid template")

    #Validating key trans_note  in liquid template
    def test_observnote (self):
        if ("LABRESULTSCOMMENT" in trans_note) == True:
            print("LABRESULTSCOMMENT presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("LABRESULTSCOMMENT" in trans_note,True,"LABRESULTSCOMMENT not present in liquid template")

    #Validating key trans_bodySite   in liquid template
    def test_observbodySitecode (self):
        if ("bodySite.coding.code" in trans_bodySite ) == True:
            print("bodySite.coding.code presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("bodySite.coding.code" in trans_bodySite,True,"bodySite.coding.code not present in liquid template")

    #Validating key trans_bodySite   in liquid template
    def test_observbodySitedisplay (self):
        if ("bodySite.coding.display" in trans_bodySite ) == True:
            print("bodySite.coding.display presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("bodySite.coding.display" in trans_bodySite,True,"bodySite.coding.display not present in liquid template")

    #Validating key trans_bodySite   in liquid template
    def test_observbodySitetext (self):
        if ("bodySite.text" in trans_bodySite ) == True:
            print("bodySite.text presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("bodySite.text" in trans_bodySite,True,"bodySite.text not present in liquid template")

    #Validating key trans_method    in liquid template
    def test_observmethodcode (self):
        if ("method.coding.code" in trans_method  ) == True:
            print("method.coding.code presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("method.coding.code" in trans_method ,True,"method.coding.code not present in liquid template")

    #Validating key trans_method    in liquid template
    def test_observmethoddisplay (self):
        if ("method.coding.display" in trans_method  ) == True:
            print("method.coding.display presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("method.coding.display" in trans_method ,True,"method.coding.display not present in liquid template")

    #Validating key trans_method    in liquid template
    def test_observmethodtext (self):
        if ("method.text" in trans_method) == True:
            print("method.text presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("method.text" in trans_method ,True,"method.text not present in liquid template")

    #Validating key trans_specimen     in liquid template
    def test_observspecimenreference (self):
        if ("specimen.reference" in trans_specimen) == True:
            print("specimen.reference presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("specimen.reference" in trans_specimen,True,"specimen.reference not present in liquid template")

    #Validating key trans_specimen     in liquid template
    def test_observspecimendisplay (self):
        if ("specimen.display" in trans_specimen) == True:
            print("specimen.display presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("specimen.display" in trans_specimen,True,"specimen.display not present in liquid template")

    #Validating key trans_device      in liquid template
    def test_observdevicedisplay (self):
        if ("device.display" in trans_device ) == True:
            print("device.display presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("device.display" in trans_device ,True,"device.display not present in liquid template")

    #Validating key trans_device      in liquid template
    def test_observdevicereference (self):
        if ("device.reference" in trans_device ) == True:
            print("device.reference presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("device.reference" in trans_device ,True,"device.reference not present in liquid template")

    #Validating key trans_referenceRange       in liquid template
    def test_observreferencerangenormalslow (self):
        if ("NORMALSLOW" in trans_referenceRange) == True:
            print("NORMALSLOW presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("NORMALSLOW" in trans_referenceRange,True,"NORMALSLOW not present in liquid template")

    #Validating key trans_referenceRange       in liquid template
    def test_observreferencerangeresultsunits1 (self):
        if ("RESULTSUNITS" in trans_referenceRange) == True:
            print("RESULTSUNITS presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("RESULTSUNITS" in trans_referenceRange,True,"RESULTSUNITS not present in liquid template")

    #Validating key trans_referenceRange       in liquid template
    def test_observreferencerangenormalshigh (self):
        if ("NORMALSHIGH" in trans_referenceRange) == True:
            print("NORMALSHIGH presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("NORMALSHIGH" in trans_referenceRange,True,"NORMALSHIGH not present in liquid template")

    #Validating key trans_referenceRange       in liquid template
    def test_observreferencerangeresultsunits2 (self):
        if ("RESULTSUNITS" in trans_referenceRange) == True:
            print("RESULTSUNITS presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("RESULTSUNITS" in trans_referenceRange,True,"RESULTSUNITS not present in liquid template")

    #Validating key trans_hasMember in liquid template
    def test_observhasmemberreference (self):
        if ("hasMember.reference" in trans_hasMember ) == True:
            print("hasMember.reference presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("hasMember.reference" in trans_hasMember,True,"hasMember.reference not present in liquid template")

    #Validating key trans_hasMember in liquid template
    def test_observhasmemberdisplay (self):
        if ("hasMember.display" in trans_hasMember ) == True:
            print("hasMember.display presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("hasMember.display" in trans_hasMember,True,"hasMember.display not present in liquid template")

    #Validating key trans_derivedFrom in liquid template
    def test_observderivedfromreference (self):
        if ("derivedFrom.reference" in trans_derivedFrom) == True:
            print("derivedFrom.reference presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("derivedFrom.reference" in trans_derivedFrom ,True,"derivedFrom.reference not present in liquid template")

    #Validating key trans_derivedFrom in liquid template
    def test_observderivedfromdisplay (self):
        if ("derivedFrom.display" in trans_derivedFrom) == True:
            print("derivedFrom.display presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("derivedFrom.display" in trans_derivedFrom ,True,"derivedFrom.display not present in liquid template")

    #Validating key trans_component  in liquid template
    def test_observcomponentdisplay (self):
        if ("component.code.coding.display" in trans_component ) == True:
            print("component.code.coding.display presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("component.code.coding.display" in trans_component  ,True,"component.code.coding.display not present in liquid template")

    #Validating key trans_component  in liquid template
    def test_observcomponentcode (self):
        if ("component.code.coding.code" in trans_component ) == True:
            print("component.code.coding.code presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("component.code.coding.code" in trans_component  ,True,"component.code.coding.code not present in liquid template")    

    #Validating key trans_component  in liquid template
    def test_observcomponenttext (self):
        if ("ccomponent.code.text" in trans_component) == True:
            print("component.code.text presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("component.code.text" in trans_component  ,True,"component.code.text not present in liquid template") 

    #Validating key trans_valueQuantity2   in liquid template
    def test_observvaluequantityunit2 (self):
        if ("valueQuantity.unit" in trans_valueQuantity2) == True:
            print("valueQuantity.unit presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueQuantity.unit" in trans_valueQuantity2,True,"valueQuantity.unit not present in liquid template") 

    #Validating key trans_valueQuantity2   in liquid template
    def test_observvaluequantityvalue2 (self):
        if ("valueQuantity.value" in trans_valueQuantity2) == True:
            print("valueQuantity.value presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueQuantity.value" in trans_valueQuantity2,True,"valueQuantity.value not present in liquid template") 

    #Validating key trans_valueQuantity2   in liquid template
    def test_observvaluequantitycode2 (self):
        if ("valueQuantity.code" in trans_valueQuantity2) == True:
            print("valueQuantity.code presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueQuantity.code" in trans_valueQuantity2,True,"valueQuantity.code not present in liquid template") 

    #Validating key trans_valueCodeableConcept2    in liquid template
    def test_observvaluecodeableconceptcode2 (self):
        if ("valueCodeableConcept.coding.code" in trans_valueCodeableConcept2 ) == True:
            print("valueCodeableConcept.coding.code presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueCodeableConcept.coding.code" in trans_valueCodeableConcept2,True,"valueCodeableConcept.coding.code not present in liquid template") 

    #Validating key trans_valueCodeableConcept2    in liquid template
    def test_observvaluecodeableconceptdisplay2(self):
        if ("valueCodeableConcept.coding.display" in trans_valueCodeableConcept2 ) == True:
            print("valueCodeableConcept.coding.display presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueCodeableConcept.coding.display" in trans_valueCodeableConcept2,True,"valueCodeableConcept.coding.display not present in liquid template") 

    #Validating key trans_valueCodeableConcept2    in liquid template
    def test_observvaluecodeableconcepttext2(self):
        if ("valueCodeableConcept.text" in trans_valueCodeableConcept2 ) == True:
            print("valueCodeableConcept.text presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueCodeableConcept.text" in trans_valueCodeableConcept2,True,"valueCodeableConcept.text not present in liquid template") 

    #Validating key trans_valueString2     in liquid template
    def test_observvaluestring2(self):
        if ("component.valueString" in trans_valueString2  ) == True:
            print("component.valueString presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("component.valueString" in trans_valueString2 ,True,"component.valueString not present in liquid template") 

    #Validating key trans_valueBoolean2     in liquid template
    def test_observvalueboolean2(self):
        if ("component.valueBoolean" in trans_valueBoolean2  ) == True:
            print("component.valueBoolean presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("component.valueBoolean" in trans_valueBoolean2 ,True,"component.valueBoolean not present in liquid template") 

    #Validating key trans_valueInteger2  in liquid template
    def test_observvalueboolean2(self):
        if ("component.valueInteger" in trans_valueInteger2   ) == True:
            print("component.valueInteger presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("component.valueInteger" in trans_valueInteger2  ,True,"component.valueInteger not present in liquid template") 

    #Validating key trans_valueRange2   in liquid template
    def test_observvaluerangelow2(self):
        if ("component.valueRange.low.value" in trans_valueRange2    ) == True:
            print("component.valueRange.low.value presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("component.valueRange.low.value" in trans_valueRange2,True,"component.valueRange.low.value not present in liquid template") 

    #Validating key trans_valueRange2   in liquid template
    def test_observvaluerangehigh2(self):
        if ("component.valueRange.high.value" in trans_valueRange2    ) == True:
            print("component.valueRange.high.value presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("component.valueRange.high.value" in trans_valueRange2,True,"component.valueRange.high.value not present in liquid template") 

    #Validating key trans_valueRatio2   in liquid template
    def test_observvaluerationum2(self):
        if ("valueRatio.numerator.value" in trans_valueRatio2    ) == True:
            print("valueRatio.numerator.value presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueRatio.numerator.value" in trans_valueRatio2,True,"valueRatio.numerator.value not present in liquid template") 

    #Validating key trans_valueRatio2   in liquid template
    def test_observvalueratioden2(self):
        if ("valueRatio.denominator.value" in trans_valueRatio2    ) == True:
            print("valueRatio.denominator.value presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueRatio.denominator.value" in trans_valueRatio2,True,"valueRatio.denominator.value not present in liquid template") 

    #Validating key trans_valueSampleData2    in liquid template
    def test_observvaluesampledataorigin2(self):
        if ("valueSampledData.origin" in trans_valueSampleData2) == True:
            print("valueSampledData.origin presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueSampledData.origin" in trans_valueSampleData2,True,"valueSampledData.origin not present in liquid template") 


    #Validating key trans_valueSampleData2    in liquid template
    def test_observvaluesampledataperiod2(self):
        if ("valueSampledData.period" in trans_valueSampleData2) == True:
            print("valueSampledData.period presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueSampledData.period" in trans_valueSampleData2,True,"valueSampledData.period not present in liquid template") 


    #Validating key trans_valueSampleData2    in liquid template
    def test_observvaluesampledatafactor2(self):
        if ("valueSampledData.factor" in trans_valueSampleData2) == True:
            print("valueSampledData.factor presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueSampledData.factor" in trans_valueSampleData2,True,"valueSampledData.factor not present in liquid template") 

    #Validating key trans_valueSampleData2    in liquid template
    def test_observvaluesampledatalowlimit2(self):
        if ("valueSampledData.lowerLimit" in trans_valueSampleData2) == True:
            print("valueSampledData.lowerLimit presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueSampledData.lowerLimit" in trans_valueSampleData2,True,"valueSampledData.lowerLimit not present in liquid template") 

    #Validating key trans_valueSampleData2    in liquid template
    def test_observvaluesampledataupperlimit2(self):
        if ("valueSampledData.upperLimit" in trans_valueSampleData2) == True:
            print("valueSampledData.upperLimit presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueSampledData.upperLimit" in trans_valueSampleData2,True,"valueSampledData.upperLimit not present in liquid template")

    #Validating key trans_valueSampleData2    in liquid template
    def test_observvaluesampledatdimensions2(self):
        if ("valueSampledData.dimensions" in trans_valueSampleData2) == True:
            print("valueSampledData.dimensions presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueSampledData.dimensions" in trans_valueSampleData2,True,"valueSampledData.dimensions not present in liquid template")        

    #Validating key trans_valueSampleData2    in liquid template
    def test_observvaluesampledatadata2(self):
        if ("valueSampledData.data" in trans_valueSampleData2) == True:
            print("valueSampledData.data presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueSampledData.data" in trans_valueSampleData2,True,"valueSampledData.data not present in liquid template") 

    #Validating key trans_valueTime2     in liquid template
    def test_observvaluetime2(self):
        if ("valueTime" in trans_valueTime2 ) == True:
            print("valueTime presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueTime" in trans_valueTime2 ,True,"valueTime not present in liquid template")  

    #Validating key trans_valueDateTime2      in liquid template
    def test_observvaluedatetime2(self):
        if ("valueDateTime" in trans_valueDateTime2  ) == True:
            print("valueDateTime presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valueDateTime" in trans_valueDateTime2  ,True,"valueDateTime not present in liquid template") 

    #Validating key trans_valuePeriod2       in liquid template
    def test_observvalueperiodstart2(self):
        if ("valuePeriod.start" in trans_valuePeriod2) == True:
            print("valuePeriod.start presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valuePeriod.start" in trans_valuePeriod2   ,True,"valuePeriod.start not present in liquid template") 

    #Validating key trans_valuePeriod2       in liquid template
    def test_observvalueperiodend2(self):
        if ("valuePeriod.end" in trans_valuePeriod2) == True:
            print("valuePeriod.end presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("valuePeriod.end" in trans_valuePeriod2   ,True,"valuePeriod.end not present in liquid template") 

    #Validating key trans_dataAbsentReason2        in liquid template
    def test_observdataabsentreasoncode2(self):
        if ("dataAbsentReason.coding.code" in trans_dataAbsentReason2) == True:
            print("dataAbsentReason.coding.code presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("dataAbsentReason.coding.code" in trans_dataAbsentReason2,True,"dataAbsentReason.coding.code not present in liquid template") 

    #Validating key trans_dataAbsentReason2        in liquid template
    def test_observdataabsentreasondisplay2(self):
        if ("dataAbsentReason.coding.display" in trans_dataAbsentReason2) == True:
            print("dataAbsentReason.coding.display presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("dataAbsentReason.coding.display" in trans_dataAbsentReason2,True,"dataAbsentReason.coding.display not present in liquid template") 

    #Validating key trans_dataAbsentReason2        in liquid template
    def test_observdataabsentreasontext2(self):
        if ("dataAbsentReason.text" in trans_dataAbsentReason2) == True:
            print("dataAbsentReason.text presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("dataAbsentReason.text" in trans_dataAbsentReason2,True,"dataAbsentReason.text not present in liquid template") 

    #Validating key trans_interpretation2         in liquid template
    def test_observinterpretationcode2(self):
        if ("interpretation.coding.code" in trans_interpretation2 ) == True:
            print("interpretation.coding.code presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("interpretation.coding.code" in trans_interpretation2 ,True,"interpretation.coding.code not present in liquid template") 

    #Validating key trans_interpretation2         in liquid template
    def test_observinterpretationdisplay2(self):
        if ("interpretation.coding.display" in trans_interpretation2 ) == True:
            print("interpretation.coding.display presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("interpretation.coding.display" in trans_interpretation2 ,True,"interpretation.coding.display not present in liquid template") 

    #Validating key trans_interpretation2         in liquid template
    def test_observinterpretationtext2(self):
        if ("interpretation.text" in trans_interpretation2 ) == True:
            print("interpretation.text presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("interpretation.text" in trans_interpretation2 ,True,"interpretation.text not present in liquid template") 

    #Validating key trans_referenceRange2          in liquid template
    def test_observreferencerangelowvalue2(self):
        if ("referenceRange.low.value" in trans_referenceRange2  ) == True:
            print("referenceRange.low.value presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("referenceRange.low.value" in trans_referenceRange2  ,True,"referenceRange.low.value not present in liquid template") 

    #Validating key trans_referenceRange2          in liquid template
    def test_observreferencerangelowunit2(self):
        if ("referenceRange.low.unit" in trans_referenceRange2  ) == True:
            print("referenceRange.low.unit presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("referenceRange.low.unit" in trans_referenceRange2  ,True,"referenceRange.low.unit not present in liquid template") 

    #Validating key trans_referenceRange2          in liquid template
    def test_observreferencerangelowcode2(self):
        if ("referenceRange.low.code" in trans_referenceRange2  ) == True:
            print("referenceRange.low.code presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("referenceRange.low.code" in trans_referenceRange2  ,True,"referenceRange.low.code not present in liquid template") 

    #Validating key trans_referenceRange2          in liquid template
    def test_observreferencerangehighvalue2(self):
        if ("referenceRange.high.value" in trans_referenceRange2  ) == True:
            print("referenceRange.high.value presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("referenceRange.high.value" in trans_referenceRange2  ,True,"referenceRange.high.value not present in liquid template") 

    #Validating key trans_referenceRange2          in liquid template
    def test_observreferencerangehighunit2(self):
        if ("referenceRange.high.unit" in trans_referenceRange2  ) == True:
            print("referenceRange.high.unit presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("referenceRange.high.unit" in trans_referenceRange2  ,True,"referenceRange.high.unit not present in liquid template") 

    #Validating key trans_referenceRange2          in liquid template
    def test_observreferencerangehighcode2(self):
        if ("referenceRange.high.code" in trans_referenceRange2  ) == True:
            print("referenceRange.high.code presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("referenceRange.high.code" in trans_referenceRange2  ,True,"referenceRange.high.code not present in liquid template") 

if __name__ == '__main__':
    unittest.main()