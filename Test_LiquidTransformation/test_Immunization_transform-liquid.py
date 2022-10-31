import unittest
import json

trans_resourceType = '{"resourceType" : "Immunization","identifier" : [{"use": "official","value": "{{msg.CENSEOID}}","assigner":{"display":"Signify Health CenseoID"}}],'
trans_status = '{% if msg.ANSWERTEXT == "Yes"-%} "status" : "completed", {% else %}"status" : "not-done", {% endif %}'
trans_statusReason = '{% if msg.statusReason != null -%}"statusReason" : { "coding": [{"system": "http://snomed.info/sct","code": "{{msg.statusReason.coding.code}}","display": "{{msg.statusReason.coding.display}}"},],"text": "{{msg.statusReason.text}}"}, {% endif %}'
trans_vaccineCode = '"vaccineCode" : {{% if msg.vaccineCode != null -%}"coding": [{"system": "http://hl7.org/fhir/sid/cvx","code": "{{msg.vaccineCode.coding.code}}","display": "{{msg.vaccineCode.coding.display}}"},],{% endif %}"text": "{{msg.QUESTIONTEXT}} {{msg.ANSWERTEXT}}" },'
trans_patient = '"patient": {"reference": "Patient/{{msg.PATIENT_FHIR_ID}}","display": "{{msg.MEMBER_NAME}}","type": "{{msg.patient.type}}","identifier": "{{msg.patient.identifier}}"},{% if msg.encounterDate != null -%}'
trans_encounter = '"encounter": {"reference": "Encounter/{{msg.encounter.reference}}","display": "{{msg.encounter.display}}","type": "{{msg.encounter.type}}","identifier": "{{msg.encounter.identifier}}"},{% endif -%}'
trans_occurrenceDataTime = '"occurrenceDateTime" : "{{msg.occurrenceDateTime | date:"yyyy-MM-dd"}}",'
trans_occurrenceString = '"occurrenceString" : "unknown",'
trans_recorded = '"recorded" : "{{msg.recorded}}", "primarySource" : "{{msg.primarySource}}", {% if msg.reportOrigin != null -%}'
trans_reportOrigin = '"reportOrigin" : { "coding": [{"system": "http://terminology.hl7.org/CodeSystem/immunization-origin","code": "{{msg.reportOrigin.coding.code}}","display": "{{msg.reportOrigin.coding.display}}"},],"text": "{{msg.reportOrigin.text}}" }, {% endif -%}'
trans_location = '"location" : { "reference": "{{msg.location.reference}}","display": "{{msg.location.display}}","type": "{{msg.location.type}}","identifier": "{{msg.location.identifier}}"},'
trans_manufacturer = '"manufacturer" : { "reference": "{{msg.manufacturer.reference}}","display": "{{msg.manufacturer.display}}","type": "{{msg.manufacturer.type}}","identifier": "{{msg.manufacturer.identifier}}"}, '
trans_lotNumber = '"lotNumber" : "{{msg.lotNumber}}",'
trans_expirationDate = '"expirationDate" : "{{msg.expiredDate | date:"yyyy-MM-dd"}}",' 
trans_site = '{% if msg.site != null -%}"site" : { "coding": [{"system": "http://terminology.hl7.org/CodeSystem/v3-ActSite","code": "{{msg.site.coding.code}}","display": "{{msg.site.coding.display}}"},],"text": "{{msg.site.text}}"}, {% endif -%}'
trans_route = '{% if msg.route != null -%}"route" : { "coding": [{"system": "http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration","code": "{{msg.route.coding.code}}","display": "{{msg.route.coding.display}}"},],"text": "{{msg.route.text}}"  }, {% endif -%}'
trans_doseQuantity = '"doseQuantity" : { "value": "{{msg.doseQuantity.value}}"},'
trans_performer = '"performer":[{   {% if msg.function != null -%}"function" : { "coding": [{"system": "http://terminology.hl7.org/CodeSystem/v2-0443","code": "{{msg.performer.function.coding.code}}","display": "{{msg.performer.function.coding.display}}"}],"text": "{{msg.performer.function.text}}" }, {% endif -%}  "actor" : {"reference": "{{msg.performer.actor.reference}}","display": "{{msg.performer.actor.display}}","type": "{{msg.performer.actor.type}}","identifier": "{{msg.performer.actor.identifier}}" }}],'
trans_note = '"note" : [{"authorReference": {"reference": "{{msg.note.authorReference.reference}}","display": "{{msg.note.authorReference.display}}"},"authorString": "{{msg.note.authorString}}","time": "{{msg.DATEOFSERVICE | add_hyphens_date}}","text": "{{msg.SECTIONDISPLAYTEXT}} {{msg.QUESTIONTEXT2}} {{msg.ANSWERTEXT}}"}],'
trans_reasonCode = '{% if msg.reasonCode != null -%}"reasonCode" : [{ "coding": [{"system": "http://snomed.info/sct","code": "{{msg.reasonCode.coding.code}}","display": "{{msg.reasonCode.coding.display}}"},],"text": "{{msg.reasonCode.text}}"}], {% endif -%} '
trans_reasonReference = '"reasonReference" : [{"reference": "{{msg.reasonReference.reference}}","display": "{{msg.reasonReference.display}}","type": "{{msg.reasonReference.type}}","identifier": "{{msg.reasonReference.identifier}}"},{"reference": "{{msg.reasonReference.reference}}","display": "{{msg.reasonReference.display}}","type": "{{msg.reasonReference.type}}","identifier": "{{msg.reasonReference.identifier}}"} ], '
trans_isSubpotent = '"isSubpotent" : "{{msg.isSubpotent}}", {% if msg.subpotentReason != null -%}'
trans_subpotentReason = '"subpotentReason" : [{ "coding": [{"system": "http://terminology.hl7.org/CodeSystem/immunization-subpotent-reason","code": "{{msg.subpotentReason.coding.code}}","display": "{{msg.subpotentReason.coding.display}}"},],"text": "{{msg.subpotentReason.text}}"  }, {% endif -%}'
trans_education = '"education" : [{ "documentType" : "{{msg.education.documentType}}", "reference" : "{{msg.education.reference}}", "publicationDate" : "{{msg.education.publicationDate | date: "yyyy-MM-dd"}}","presentationDate" : "{{msg.education.presentationDate | date: "yyyy-MM-dd"}}" }],'
trans_programEligibility = '{% if msg.programEligibility != null -%}"programEligibility" : [{ "coding": [{"system": "http://terminology.hl7.org/CodeSystem/immunization-program-eligibility","code": "{{msg.programEligibility.coding.code}}","display": "{{msg.programEligibility.coding.display}}"},],"text": "{{msg.programEligibility.text}}"  }], {% endif -%} '
trans_fundingSource = '{% if msg.fundingSource != null -%}"fundingSource" : { "coding": [{"system": "http://terminology.hl7.org/CodeSystem/immunization-funding-source","code": "{{msg.fundingSource.coding.code}}","display": "{{msg.fundingSource.coding.display}}"},],"text": "{{msg.fundingSource.text}}"  }, {% endif -%} '
trans_reaction = '"reaction" : [{ "date" : "{{msg.reaction.date | date: "yyyy-MM-dd"}}","detail" : { "reference": "{{msg.reaction.detail.reference}}","display": "{{msg.reaction.detail.display}}","type": "{{msg.reaction.detail.type}}","identifier": "{{msg.reaction.detail.identifier}}"}, "reported" : "{{msg.reaction.reported}}"}],'
trans_protocolApplied = '"protocolApplied" : [{ "series" : "{{msg.protocolApplied.series}}","authority" : { "reference": "{{msg.protocolApplied.authority.reference}}","display": "{{msg.protocolApplied.authority.display}}","type": "{{msg.protocolApplied.authority.type}}","identifier": "{{msg.protocolApplied.authority.identifier}}"}, {% if msg.targetDisease != null -%}"targetDisease" : [{ "coding": [{"system": "http://snomed.info/sct","code": "{{msg.protocolApplied.targetDisease.coding.code}}","display": "{{msg.protocolApplied.fundingSource.coding.display}}"},],"text": "{{msg.protocolApplied.targetDisease.text}}"}], {% endif -%} '
trans_dosenumber = '"doseNumberPositiveInt" : "{{msg.doseNumberPositiveInt}}","doseNumberString" : "{{msg.doseNumberString}}",'
trans_seriesDoses = '"seriesDosesPositiveInt" : "{{msg.seriesDosesPositiveInt}}",'
trans_seriesDosesString = '"seriesDosesString" : "{{msg.seriesDosesString}}"}]}'


class TestliqTransform (unittest.TestCase):

    #Validating key resourceType Immunization in Immunization liquid template
    def test_immunresourceType(self):
        if ("Immunization" in trans_resourceType) == True:
            print("Immunization presence is validated in Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("Immunization" in trans_resourceType,True,"Immunization not present in Immunization liquid template")

    #Validating key ANSWERTEXT in Immunization liquid template
    def test_immunstatus(self):
        if ("ANSWERTEXT" in trans_status) == True:
            print("ANSWERTEXT presence is validated in Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("ANSWERTEXT" in trans_status,True,"ANSWERTEXT not present in Immunization liquid template")

    #Validating key statusReason.coding.code  in Immunization liquid template
    def test_immunstatusreasoncode(self):
        if ("statusReason.coding.code" in trans_statusReason) == True:
            print("statusReason.coding.code presence is validated in Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("statusReason.coding.code" in trans_statusReason,True,"statusReason.coding.code not present in Immunization liquid template")

    #Validating key statusReason.coding.display in Immunization liquid template
    def test_immunstatusreasondisplay(self):
        if ("statusReason.coding.display" in trans_statusReason) == True:
            print("statusReason.coding.display presence is validated in Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("statusReason.coding.display" in trans_statusReason,True,"Immunization not present in liquid template")

    #Validating key statusReason.text  in Immunization liquid template
    def test_immunstatusreasontext(self):
        if ("statusReason.text" in trans_statusReason) == True:
            print("statusReason.text presence is validated in Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("statusReason.text" in trans_statusReason,True,"Immunization not present in liquid template")

    #Validating key vaccineCode.coding.code  in Immunization liquid template
    def test_immunvaccinecode(self):
        if ("vaccineCode.coding.code" in trans_vaccineCode) == True:
            print("vaccineCode.coding.code presence is validated in Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("vaccineCode.coding.code" in trans_vaccineCode,True,"Immunization not present in liquid template")

    #Validating key vaccineCode.coding.display  in Immunization liquid template
    def test_immunvaccinedisplay(self):
        if ("vaccineCode.coding.display" in trans_vaccineCode) == True:
            print("vaccineCode.coding.display presence is validated in Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("vaccineCode.coding.display" in trans_vaccineCode,True,"vaccineCode.coding.display not present in Immunization liquid template")

    #Validating key QUESTIONTEXT  in Immunization liquid template
    def test_immunvaccinetextquestion(self):
        if ("QUESTIONTEXT" in trans_vaccineCode) == True:
            print("QUESTIONTEXT presence is validated in vaccineCode.text Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("QUESTIONTEXT" in trans_vaccineCode,True,"QUESTIONTEXT not present in vaccineCode.text Immunization liquid template")

    #Validating key ANSWERTEXT  in Immunization liquid template
    def test_immunvaccinetextanswer(self):
        if ("ANSWERTEXT" in trans_vaccineCode) == True:
            print("ANSWERTEXT presence is validated in vaccineCode.text Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("ANSWERTEXT" in trans_vaccineCode,True,"ANSWERTEXT vaccineCode.text not present in Immunization liquid template")

    #Validating key PATIENT_FHIR_ID  in Immunization liquid template
    def test_immunpatientref(self):
        if ("PATIENT_FHIR_ID" in trans_patient) == True:
            print("PATIENT_FHIR_ID presence is validated in patient.reference Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PATIENT_FHIR_ID" in trans_patient,True,"PATIENT_FHIR_ID patient.reference not present in Immunization liquid template")

    #Validating key MEMBER_NAME  in Immunization liquid template
    def test_immunpatientdisplay(self):
        if ("MEMBER_NAME" in trans_patient) == True:
            print("MEMBER_NAME presence is validated in patient.display Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_NAME" in trans_patient,True,"MEMBER_NAME patient.display not present in Immunization liquid template")

    #Validating key patient.type  in Immunization liquid template
    def test_immunpatienttype(self):
        if ("patient.type" in trans_patient) == True:
            print("patient.type presence is validated in patient.type Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("patient.type" in trans_patient,True,"patient.type not present in Immunization liquid template")

    #Validating key encounter.reference  in Immunization liquid template
    def test_immunencounterref (self):
        if ("encounter.reference" in trans_encounter) == True:
            print("encounter.reference  presence is validated in encounter.reference  Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("encounter.reference" in trans_encounter,True,"encounter.reference  not present in Immunization liquid template")

    #Validating key encounter.display  in Immunization liquid template
    def test_immunencounterdis (self):
        if ("encounter.display" in trans_encounter) == True:
            print("encounter.display  presence is validated in encounter.display  Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("encounter.display" in trans_encounter,True,"encounter.display  not present in Immunization liquid template")

    #Validating key encounter.type  in Immunization liquid template
    def test_immunencountertype (self):
        if ("encounter.type" in trans_encounter) == True:
            print("encounter.type  presence is validated in encounter.type  Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("encounter.type" in trans_encounter,True,"encounter.type  not present in Immunization liquid template")

    #Validating key encounter.identifier  in Immunization liquid template
    def test_immunencounterid (self):
        if ("encounter.identifier" in trans_encounter) == True:
            print("encounter.identifier presence is validated in encounter.identifier  Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("encounter.identifier" in trans_encounter,True,"encounter.identifier  not present in Immunization liquid template")

    #Validating key occurrenceDateTime  in Immunization liquid template
    def test_immunoccurrencedatetime (self):
        if ("occurrenceDateTime" in trans_occurrenceDataTime) == True:
            print("occurrenceDateTime presence is validated in occurrenceDateTime Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("occurrenceDateTime" in trans_occurrenceDataTime,True,"occurrenceDateTime not present in Immunization liquid template")

    #Validating key occurrenceString  in Immunization liquid template
    def test_immunoccurrencestring (self):
        if ("occurrenceString" in trans_occurrenceString) == True:
            print("occurrenceString presence is validated in occurrenceString Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("occurrenceString" in trans_occurrenceString,True,"occurrenceString not present in Immunization liquid template")

   #Validating key recorded  in Immunization liquid template
    def test_immunrecorded (self):
        if ("recorded" in trans_recorded) == True:
            print("recorded presence is validated in recorded Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("recorded" in trans_recorded,True,"recorded not present in Immunization liquid template")

   #Validating key primarySource  in Immunization liquid template
    def test_immunprimarysource (self):
        if ("primarySource" in trans_recorded) == True:
            print("primarySource presence is validated in primarySource Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("primarySource" in trans_recorded,True,"primarySource not present in Immunization liquid template")

   #Validating key reportOrigin.coding.code  in Immunization liquid template
    def test_immunreportorigincode (self):
        if ("reportOrigin.coding.code" in trans_reportOrigin) == True:
            print("reportOrigin.coding.code presence is validated in reportOrigin.coding.code Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("reportOrigin.coding.code" in trans_reportOrigin,True,"reportOrigin.coding.code not present in Immunization liquid template")

   #Validating key reportOrigin.coding.display  in Immunization liquid template
    def test_immunreportorigindisplay (self):
        if ("reportOrigin.coding.display" in trans_reportOrigin) == True:
            print("reportOrigin.coding.display presence is validated in reportOrigin.coding.display Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("reportOrigin.coding.display" in trans_reportOrigin,True,"reportOrigin.coding.display not present in Immunization liquid template")

   #Validating key reportOrigin.text  in Immunization liquid template
    def test_immunreportorigintext (self):
        if ("reportOrigin.text" in trans_reportOrigin) == True:
            print("reportOrigin.text presence is validated in reportOrigin.text Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("reportOrigin.text" in trans_reportOrigin,True,"reportOrigin.text not present in Immunization liquid template") 

  
   #Validating key location.reference  in Immunization liquid template
    def test_immunlocationref (self):
        if ("location.reference" in trans_location) == True:
            print("location.reference presence is validated in location.reference Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("location.reference" in trans_location,True,"location.reference not present in Immunization liquid template") 

   #Validating key location.display  in Immunization liquid template
    def test_immunlocationdisplay (self):
        if ("location.display" in trans_location) == True:
            print("location.display presence is validated in location.display Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("location.display" in trans_location,True,"location.display not present in Immunization liquid template") 

   #Validating key location.type  in Immunization liquid template
    def test_immunlocationtype (self):
        if ("location.type" in trans_location) == True:
            print("location.type presence is validated in location.type Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("location.type" in trans_location,True,"location.type not present in Immunization liquid template") 

   #Validating key location.identifier  in Immunization liquid template
    def test_immunlocationidentifier (self):
        if ("location.identifier" in trans_location) == True:
            print("location.identifier presence is validated in location.identifier Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("location.identifier" in trans_location,True,"location.identifier not present in Immunization liquid template") 

   #Validating key manufacturer.reference  in Immunization liquid template
    def test_immunmanufacturerref (self):
        if ("manufacturer.reference" in trans_manufacturer) == True:
            print("location.reference presence is validated in location.reference Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("manufacturer.reference" in trans_manufacturer,True,"manufacturer.reference not present in Immunization liquid template") 

   #Validating key manufacturer.display  in Immunization liquid template
    def test_immunmanufacturerdisplay (self):
        if ("manufacturer.display" in trans_manufacturer) == True:
            print("manufacturer.display presence is validated in manufacturer.display Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("manufacturer.display" in trans_manufacturer,True,"manufacturer.display not present in Immunization liquid template") 

   #Validating key manufacturer.type  in Immunization liquid template
    def test_immunmanufacturertype (self):
        if ("manufacturer.type" in trans_manufacturer) == True:
            print("manufacturer.type presence is validated in manufacturer.type Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("manufacturer.type" in trans_manufacturer,True,"manufacturer.type not present in Immunization liquid template") 

   #Validating key manufacturer.identifier  in Immunization liquid template
    def test_immunmanufactureridentifier (self):
        if ("manufacturer.identifier" in trans_manufacturer) == True:
            print("manufacturer.identifier presence is validated in manufacturer.identifier Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("manufacturer.identifier" in trans_manufacturer,True,"manufacturer.identifier not present in Immunization liquid template") 

   #Validating key lotNumber  in Immunization liquid template
    def test_immunlotnumber (self):
        if ("lotNumber" in trans_lotNumber) == True:
            print("lotNumber presence is validated in lotNumber Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("lotNumber" in trans_lotNumber,True,"lotNumber not present in Immunization liquid template") 

   #Validating key expirationDate  in Immunization liquid template
    def test_immunexpirationDate (self):
        if ("expirationDate" in trans_expirationDate) == True:
            print("expirationDate presence is validated in expirationDate Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("expirationDate" in trans_expirationDate,True,"expirationDate not present in Immunization liquid template") 


   #Validating key site.coding.code  in Immunization liquid template
    def test_immunsitecode (self):
        if ("site.coding.code" in trans_site) == True:
            print("site.coding.code presence is validated in site.coding.code Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("site.coding.code" in trans_site,True,"site.coding.code not present in Immunization liquid template") 

   #Validating key site.coding.display  in Immunization liquid template
    def test_immunsitedisplay (self):
        if ("site.coding.display" in trans_site) == True:
            print("site.coding.display presence is validated in site.coding.display Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("site.coding.display" in trans_site,True,"site.coding.display not present in Immunization liquid template") 

   #Validating key site.text  in Immunization liquid template
    def test_immunsitetext (self):
        if ("site.text" in trans_site) == True:
            print("site.text presence is validated in site.text Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("site.text" in trans_site,True,"site.text not present in Immunization liquid template") 

   #Validating key route.coding.code  in Immunization liquid template
    def test_immunroutecode (self):
        if ("route.coding.code" in trans_route) == True:
            print("route.coding.code presence is validated in route.coding.code Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("route.coding.code" in trans_route,True,"route.coding.code not present in Immunization liquid template") 

   #Validating key route.coding.display  in Immunization liquid template
    def test_immunroutedisplay (self):
        if ("route.coding.display" in trans_route) == True:
            print("route.coding.display presence is validated in route.coding.display Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("route.coding.display" in trans_route,True,"route.coding.display not present in Immunization liquid template") 

   #Validating key route.text  in Immunization liquid template
    def test_immunroutetext (self):
        if ("route.text" in trans_route) == True:
            print("route.text presence is validated in route.route Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("route.text" in trans_route,True,"route.text not present in Immunization liquid template") 

   #Validating key doseQuantity.value  in Immunization liquid template
    def test_immundosequantityvalue (self):
        if ("doseQuantity.value" in trans_doseQuantity) == True:
            print("doseQuantity.value  presence is validated in doseQuantity.value  Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("doseQuantity.value" in trans_doseQuantity,True,"doseQuantity.value  not present in Immunization liquid template") 

    #Validating key performer.function.coding.code  in Immunization liquid template
    def test_immunperformerfunctioncode (self):
        if ("performer.function.coding.code" in trans_performer) == True:
            print("performer.function.coding.code presence is validated in performer.function.coding.code Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("performer.function.coding.code" in trans_performer,True,"performer.function.coding.code not present in Immunization liquid template") 

    #Validating key performer.function.coding.display  in Immunization liquid template
    def test_immunperformerfunctiondisplay (self):
        if ("performer.function.coding.display" in trans_performer) == True:
            print("performer.function.coding.display presence is validated in performer.function.coding.display Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("performer.function.coding.display" in trans_performer,True,"performer.function.coding.display not present in Immunization liquid template")

    #Validating key performer.function.text  in Immunization liquid template
    def test_immunperformerfunctiontext (self):
        if ("performer.function.text" in trans_performer) == True:
            print("performer.function.text presence is validated in performer.function.text Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("performer.function.text" in trans_performer,True,"performer.function.text not present in Immunization liquid template")  

    #Validating key performer.actor.reference  in Immunization liquid template
    def test_immunperformeractorcode (self):
        if ("performer.actor.reference" in trans_performer) == True:
            print("performer.actor.reference presence is validated in performer.actor.code Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("performer.actor.reference" in trans_performer,True,"performer.actor.reference not present in Immunization liquid template") 

    #Validating key performer.actor.display  in Immunization liquid template
    def test_immunperformeractordisplay (self):
        if ("performer.actor.display" in trans_performer) == True:
            print("performer.actor.display presence is validated in performer.actor.display Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("performer.actor.display" in trans_performer,True,"performer.actor.display not present in Immunization liquid template") 

  #Validating key performer.actor.type  in Immunization liquid template
    def test_immunperformeractortype (self):
        if ("performer.actor.type" in trans_performer) == True:
            print("performer.actor.type presence is validated in performer.actor.type Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("performer.actor.type" in trans_performer,True,"performer.actor.type not present in Immunization liquid template") 

   #Validating key performer.actor.identifier  in Immunization liquid template
    def test_immunperformeractoridentifier (self):
        if ("performer.actor.identifier" in trans_performer) == True:
            print("performer.actor.identifier  presence is validated in performer.actor.identifier Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("performer.actor.identifier" in trans_performer,True,"performer.actor.identifier not present in Immunization liquid template") 

   #Validating key note.authorReference.reference  in Immunization liquid template
    def test_immunnoteauthorref (self):
        if ("note.authorReference.reference" in trans_note) == True:
            print("note.authorReference.reference  presence is validated in note.authorReference.reference Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("note.authorReference.reference" in trans_note,True,"note.authorReference.reference not present in Immunization liquid template") 

   #Validating key note.authorReference.reference  in Immunization liquid template
    def test_immunnoteauthorref (self):
        if ("note.authorReference.reference" in trans_note) == True:
            print("note.authorReference.reference  presence is validated in note.authorReference.reference Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("note.authorReference.reference" in trans_note,True,"note.authorReference.reference not present in Immunization liquid template") 

   #Validating key note.authorReference.display  in Immunization liquid template
    def test_immunnoteauthordisplay (self):
        if ("note.authorReference.display" in trans_note) == True:
            print("note.authorReference.display  presence is validated in note.authorReference.display Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("note.authorReference.display" in trans_note,True,"note.authorReference.display not present in Immunization liquid template")

   #Validating key note.authorString  in Immunization liquid template
    def test_immunauthorstring (self):
        if ("note.authorString" in trans_note) == True:
            print("note.authorString  presence is validated in note.authorString Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("note.authorString" in trans_note,True,"authorString not present in Immunization liquid template")

   #Validating key DATEOFSERVICE note.time  in Immunization liquid template
    def test_immunnotetime (self):
        if ("DATEOFSERVICE" in trans_note) == True:
            print("DATEOFSERVICE  presence is validated in note.time Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("DATEOFSERVICE" in trans_note,True,"time not present in Immunization liquid template")

    #Validating key SECTIONDISPLAYTEXT note.text  in Immunization liquid template
    def test_immunnotetext (self):
        if ("SECTIONDISPLAYTEXT" in trans_note) == True:
            print("SECTIONDISPLAYTEXT  presence is validated in note.text Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("SECTIONDISPLAYTEXT" in trans_note,True,"note.text not present in Immunization liquid template")

    #Validating key reasonCode.coding.code  in Immunization liquid template
    def test_immunreasoncode (self):
        if ("reasonCode.coding.code" in trans_reasonCode) == True:
            print("reasonCode.coding.code  presence is validated in reasonCode.coding.code Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("reasonCode.coding.code" in trans_reasonCode,True,"reasonCode.coding.code not present in Immunization liquid template")

    #Validating key reasonCode.coding.display  in Immunization liquid template
    def test_immunreasondisplay (self):
        if ("reasonCode.coding.display" in trans_reasonCode) == True:
            print("reasonCode.coding.display  presence is validated in reasonCode.coding.display Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("reasonCode.coding.display" in trans_reasonCode,True,"reasonCode.coding.display not present in Immunization liquid template")

    #Validating key reasonCode.text  in Immunization liquid template
    def test_immunreasontext (self):
        if ("reasonCode.text" in trans_reasonCode) == True:
            print("reasonCode.text   presence is validated in reasonCode.text Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("reasonCode.text" in trans_reasonCode,True,"reasonCode.text  not present in Immunization liquid template")

    #Validating key reasonReference.reference  in Immunization liquid template
    def test_immunreasonreferenceref (self):
        if ("reasonReference.reference" in trans_reasonReference) == True:
            print("reasonReference.reference presence is validated in reasonReference.reference Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("reasonReference.reference" in trans_reasonReference,True,"reasonReference.reference not present in Immunization liquid template")

    #Validating key reasonReference.display  in Immunization liquid template
    def test_immunreasonreferencedisplay (self):
        if ("" in trans_reasonReference) == True:
            print("reasonReference.display   presence is validated in reasonReference.display Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("reasonReference.display" in trans_reasonReference,True,"reasonReference.display not present in Immunization liquid template")

    #Validating key reasonReference.type  in Immunization liquid template
    def test_immunreasonreferencetype (self):
        if ("" in trans_reasonReference) == True:
            print("reasonReference.type   presence is validated in reasonReference.type Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("reasonReference.type" in trans_reasonReference,True,"reasonReference.type not present in Immunization liquid template")

    #Validating key reasonReference.identifier  in Immunization liquid template
    def test_immunreasonreferenceid (self):
        if ("" in trans_reasonReference) == True:
            print("reasonReference.identifier   presence is validated in reasonReference.identifier Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("reasonReference.identifier" in trans_reasonReference,True,"reasonReference.identifier not present in Immunization liquid template")

    #Validating key isSubpotent in Immunization liquid template
    def test_immunisSubpotent (self):
        if ("isSubpotent" in trans_isSubpotent) == True:
            print("isSubpotent  presence is validated in isSubpotent Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("isSubpotent" in trans_isSubpotent,True,"isSubpotent not present in Immunization liquid template")

    #Validating key subpotentReason.coding.code in Immunization liquid template
    def test_immunsubpotentreasoncode (self):
        if ("subpotentReason.coding.code" in trans_subpotentReason) == True:
            print("subpotentReason.coding.code  presence is validated in subpotentReason.coding.code Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("subpotentReason.coding.code" in trans_subpotentReason,True,"subpotentReason.coding.code not present in Immunization liquid template")

    #Validating key subpotentReason.coding.display in Immunization liquid template
    def test_immunsubpotentreasondisplay (self):
        if ("subpotentReason.coding.display" in trans_subpotentReason) == True:
            print("subpotentReason.coding.display  presence is validated in subpotentReason.coding.display Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("subpotentReason.coding.display" in trans_subpotentReason,True,"subpotentReason.coding.display not present in Immunization liquid template")

    #Validating key subpotentReason.text in Immunization liquid template
    def test_immunsubpotentreasontext (self):
        if ("subpotentReason.text" in trans_subpotentReason) == True:
            print("subpotentReason.text  presence is validated in subpotentReason.text Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("subpotentReason.text" in trans_subpotentReason,True,"subpotentReason.text not present in Immunization liquid template")

    #Validating key education.documentType in Immunization liquid template
    def test_immuneducationdoctype (self):
        if ("education.documentType" in trans_education) == True:
            print("education.documentType  presence is validated in education.documentType Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("education.documentType" in trans_education,True,"education.documentType not present in Immunization liquid template")

    #Validating key education.reference in Immunization liquid template
    def test_immuneducationref (self):
        if ("education.reference" in trans_education) == True:
            print("education.reference presence is validated in education.reference Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("education.reference" in trans_education,True,"education.reference not present in Immunization liquid template")

    #Validating key education.publicationDatein Immunization liquid template
    def test_immuneducationpubdate (self):
        if ("education.publicationDate" in trans_education) == True:
            print("education.publicationDate presence is validated in education.publicationDate Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("education.publicationDate" in trans_education,True,"education.publicationDate not present in Immunization liquid template")

    #Validating key education.presentationDate in Immunization liquid template
    def test_immuneducationpresentdate (self):
        if ("education.presentationDate" in trans_education) == True:
            print("education.presentationDate presence is validated in education.presentationDate Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("education.presentationDate" in trans_education,True,"education.presentationDate not present in Immunization liquid template")

    #Validating key programEligibility.coding.code in Immunization liquid template
    def test_immunprogramEligibilitycode (self):
        if ("programEligibility.coding.code" in trans_programEligibility) == True:
            print("programEligibility.coding.code presence is validated in programEligibility.coding.code Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("programEligibility.coding.code" in trans_programEligibility,True,"programEligibility.coding.code not present in Immunization liquid template")

    #Validating key programEligibility.coding.display in Immunization liquid template
    def test_immunprogramEligibilitydisplay (self):
        if ("programEligibility.coding.display" in trans_programEligibility) == True:
            print("programEligibility.coding.display presence is validated in programEligibility.coding.display Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("programEligibility.coding.display" in trans_programEligibility,True,"programEligibility.coding.display not present in Immunization liquid template")

    #Validating key programEligibility.text in Immunization liquid template
    def test_immunprogramEligibilitytext (self):
        if ("programEligibility.text" in trans_programEligibility) == True:
            print("programEligibility.text presence is validated in programEligibility.text Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("programEligibility.text" in trans_programEligibility,True,"programEligibility.text not present in Immunization liquid template")

    #Validating key reaction.date  in Immunization liquid template
    def test_immunreactiondate  (self):
        if ("reaction.date" in trans_reaction) == True:
            print("reaction.date  presence is validated in reaction.date Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("reaction.date" in trans_reaction,True,"reaction.date not present in Immunization liquid template")

    #Validating key reaction.detail.reference  in Immunization liquid template
    def test_immunreactionref  (self):
        if ("reaction.detail.reference" in trans_reaction) == True:
            print("reaction.detail.reference presence is validated in reaction.detail.reference Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("reaction.detail.reference" in trans_reaction,True,"reaction.detail.reference not present in Immunization liquid template")

    #Validating key reaction.detail.display  in Immunization liquid template
    def test_immunreactiondisplay  (self):
        if ("reaction.detail.display" in trans_reaction) == True:
            print("reaction.detail.display presence is validated in reaction.detail.display Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("reaction.detail.display" in trans_reaction,True,"reaction.detail.display not present in Immunization liquid template")

    #Validating key reaction.detail.type  in Immunization liquid template
    def test_immunreactiontype  (self):
        if ("reaction.detail.type" in trans_reaction) == True:
            print("reaction.detail.type presence is validated in reaction.detail.type Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("reaction.detail.type" in trans_reaction,True,"reaction.detail.type not present in Immunization liquid template")

   #Validating key reaction.detail.identifier  in Immunization liquid template
    def test_immunreactionid  (self):
        if ("reaction.detail.identifier" in trans_reaction) == True:
            print("reaction.detail.identifier presence is validated in reaction.detail.identifier Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("reaction.detail.identifier" in trans_reaction,True,"reaction.detail.identifier not present in Immunization liquid template")

   #Validating key reaction.detail.identifier  in Immunization liquid template
    def test_immunreactionid  (self):
        if ("reaction.detail.identifier" in trans_reaction) == True:
            print("reaction.detail.identifier presence is validated in reaction.detail.identifier Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("reaction.detail.identifier" in trans_reaction,True,"reaction.detail.identifier not present in Immunization liquid template")

   #Validating key reaction.reported  in Immunization liquid template
    def test_immunreactionreport  (self):
        if ("reaction.reported" in trans_reaction) == True:
            print("reaction.reported presence is validated in reaction.reported Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("reaction.reported" in trans_reaction,True,"reaction.reported not present in Immunization liquid template")

   #Validating key protocolApplied.series  in Immunization liquid template
    def test_immunprotocolappliedseries  (self):
        if ("protocolApplied.series" in trans_protocolApplied) == True:
            print("protocolApplied.series presence is validated in protocolApplied.series Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("protocolApplied.series" in trans_protocolApplied,True,"protocolApplied.series not present in Immunization liquid template")

   #Validating key protocolApplied.authority.reference  in Immunization liquid template
    def test_immunprotocolappliedref  (self):
        if ("protocolApplied.authority.reference" in trans_protocolApplied) == True:
            print("protocolApplied.authority.reference presence is validated in protocolApplied.authority.reference Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("protocolApplied.authority.reference" in trans_protocolApplied,True,"protocolApplied.authority.reference not present in Immunization liquid template")

   #Validating key protocolApplied.authority.display  in Immunization liquid template
    def test_immunprotocolapplieddisplay  (self):
        if ("protocolApplied.authority.display" in trans_protocolApplied) == True:
            print("protocolApplied.authority.display presence is validated in protocolApplied.authority.display Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("protocolApplied.authority.display" in trans_protocolApplied,True,"protocolApplied.authority.display not present in Immunization liquid template")

   #Validating key protocolApplied.authority.type  in Immunization liquid template
    def test_immunprotocolappliedtype  (self):
        if ("protocolApplied.authority.type" in trans_protocolApplied) == True:
            print("protocolApplied.authority.type presence is validated in protocolApplied.authority.type Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("protocolApplied.authority.type" in trans_protocolApplied,True,"protocolApplied.authority.type not present in Immunization liquid template")

   #Validating key protocolApplied.authority.identifier  in Immunization liquid template
    def test_immunprotocolappliedidentifier  (self):
        if ("protocolApplied.authority.identifier" in trans_protocolApplied) == True:
            print("protocolApplied.authority.identifier presence is validated in protocolApplied.authority.identifier Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("protocolApplied.authority.identifier" in trans_protocolApplied,True,"protocolApplied.authority.identifier not present in Immunization liquid template")

   #Validating key protocolApplied.targetDisease.coding.code in Immunization liquid template
    def test_immunprotocolappliedtargetcode  (self):
        if ("protocolApplied.targetDisease.coding.code" in trans_protocolApplied) == True:
            print("protocolApplied.targetDisease.coding.code presence is validated in protocolApplied.targetDisease.coding.code Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("protocolApplied.targetDisease.coding.code" in trans_protocolApplied,True,"protocolApplied.targetDisease.coding.code not present in Immunization liquid template")

   #Validating key protocolApplied.targetDisease.coding.display in Immunization liquid template
    def test_immunprotocolappliedtargetdisplay  (self):
        if ("protocolApplied.authority.display" in trans_protocolApplied) == True:
            print("protocolApplied.authority.display presence is validated in protocolApplied.authority.display Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("protocolApplied.authority.display" in trans_protocolApplied,True,"protocolApplied.authority.display not present in Immunization liquid template")


    #Validating key protocolApplied.targetDisease.text in Immunization liquid template
    def test_immunprotocolappliedtargettext  (self):
        if ("protocolApplied.targetDisease.text" in trans_protocolApplied) == True:
            print("protocolApplied.targetDisease.text presence is validated in protocolApplied.targetDisease.text Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("protocolApplied.targetDisease.text" in trans_protocolApplied,True,"protocolApplied.targetDisease.text not present in Immunization liquid template")

    #Validating key doseNumberPositiveInt in Immunization liquid template
    def test_immundosenumberpositiveint  (self):
        if ("doseNumberPositiveInt" in trans_dosenumber) == True:
            print("doseNumberPositiveInt presence is validated in doseNumberPositiveInt Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("doseNumberPositiveInt" in trans_dosenumber,True,"doseNumberPositiveInt not present in Immunization liquid template")

    #Validating key doseNumberString in Immunization liquid template
    def test_immundosenumberstring  (self):
        if ("doseNumberString" in trans_dosenumber) == True:
            print("doseNumberPositiveInt presence is validated in doseNumberPositiveInt Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("doseNumberPositiveInt" in trans_dosenumber,True,"doseNumberPositiveInt not present in Immunization liquid template")

    #Validating key seriesDosesString in Immunization liquid template
    def test_immunseriesdosesstring  (self):
        if ("seriesDosesString" in trans_seriesDosesString) == True:
            print("seriesDosesString presence is validated in seriesDosesString Immunization liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("seriesDosesString" in trans_seriesDosesString,True,"seriesDosesString not present in Immunization liquid template")



if __name__ == '__main__':
    unittest.main()