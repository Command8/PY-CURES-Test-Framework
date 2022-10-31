import unittest
import json

#Copy the dictionaries as strings into variables inorder to identify and validate snowflake JSON Keys presence in newly created strings.
trans_pat_resource = '"resourceType": "Patient","id": "{{ msg.PatientId | to_json_string | generate_uuid }}","identifier": [{"use": "usual","type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v2-0203","code": "MR"},"value": "{{ msg.CENSEOID }}"}{"use": "usual","type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v2-0203","code": "PI"}]},"value": "{{ msg.Member_Number }}"},{"use": "usual","type": {"coding": [}"system": "http://terminology.hl7.org/CodeSystem/v2-0203","code": "SS"}"value": "{{ msg.MEMBER_SSN }}"}],"active": true,"name": [{"family": "{{ msg.MEMBER_LAST_NAME }}","given": ["{{ msg.MEMBER_FIRST_NAME }}",{{ msg.MEMBER_MIDDLE_NAME }}""],"suffix": ["{{ msg.SUFFIX }}"],}],'
trans_telecom = '"telecom": [{"system": "phone","use": "home","value": "{{msg.MEMBER_TELEPHONE}}",},{"system": "sms","use": "mobile","value": "{{msg.MEMBER_CELL}}",},{"system": "other","use": "temp","value": "{{msg.SECONDARYPHONE}}",},{"system": "email","use": "home","value": "{{msg.MEMBER_EMAIL}}",},]'
trans_gender = '"gender":{% if msg.MEMBER_GENDER == "M" -%} "male",{% elsif msg.MEMBER_GENDER == "F" -%}"female",{% elsif msg.MEMBER_GENDER == "U" -%}"unknown",{% elsif code -%}"other",{% else %}"",{% endif -%}'
trans_dob = '"birthDate": "{{ msg.MEMBER_DATE_OF_BIRTH | split:" " | first }}'
trans_deceased = '"deceasedBoolean": "{{msg.DeceasedBoolean}}","deceasedDateTime" : "{{msg.DeceasedDateTime}}"'
trans_address = '"address": [{"use": "home","type": "postal","line": "{{msg.MEMBER_ADDRESS1}}, {{msg.MEMBER_ADDRESS2}}","city": "{{msg.MEMBER_CITY}}","state":"{{msg.MEMBER_STATE}}","postalCode": "{{msg.MEMBER_ZIP}}", "district": "{{msg.MEMBER_COUNTY}}","country": "USA",},{"use": "billing","type": "physical","line": "{{msg.MEMBER_MAIL_ADDRESS1}}, {{msg.MEMBER_MAIL_ADDRESS2}}","city": "{{msg.MEMBER_MAIL_CITY}}","state":"{{msg.MEMBER_MAIL_STATE}}","postalCode": "{{msg.MEMBER_MAIL_ZIP}}",},],'
trans_maritalStatus =  '"maritalStatus" : {"coding":[{"system" : "{{msg.MARITALSTATUSSYSTEM}}","code" : "{{msg.MARITALSTATUSCODE}}", "display" : "{{msg.MEMBER_MARITALSTATUS}}",}],"text": "{{msg.MEMBER_MARITALSTATUS}}",},'
trans_multibirth = '"multipleBirthBoolean": "{{msg.MultipleBirth}}","multipleBirthInteger": "{{msg.MultipleBirthInteger}}"'
trans_contact = '"contact": [{"relationship" : {"coding":[{"system" : "http://hl7.org/fhir/ValueSet/patient-contactrelationship","code" : "{{msg.RELATIONSHIPCODE}}", "display" : "{{msg.RELATIONSHIP}}",}],"text": "{{msg.RELATIONSHIP}}",},"name": {"family": "{{ msg.lastname }}","given": ["{{ msg.firstname }}"]},"gender": "{{msg.kinGender}}","organization": {"reference": "Organization/{{msg.contOrgId}}","display": "{{msg.organization}}"},"period":{"start": "{{ msg.startDate | add_hyphens_date }}","end": "{{ msg.endDate | add_hyphens_date }}",},"telecom": [{{"system": "phone",	"use" : "home","value": "{{msg.MEMBER_SECONDARY_CONTACT_PHONE}}",}],"address":{"use": "home","type": "postal","line": "{{msg.MEMBER_SECONDARY_CONTACT}}","city": "{{msg.KinAddress.City}}","postalCode": "{{msg.ZipCode}}",},}],'
trans_mangOrg = '"managingOrganization": {"reference": "Organization/{{msg.CLIENTID}}","display": "{{msg.CLIENTNAME}}"},'
trans_pcp = '"generalPractitioner": [{"reference": "Practioner/{{msg.PCP_ID}}","display": "{{msg.PCP_FIRSTNAME}} {{msg.PCP_LASTNAME}}"},],"extension":[{"url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity","extension": [{"url": "text","valueString":"{{msg.ETHNICITY}}"}]}'
trans_comm = '"communication":[{"language":{"valueCodeableConcept":{"coding":[{"system":"http://hl7.org/fhir/ValueSet/languages","code": "en","display":"{{msg.PREFERREDSPOKENLANGUAGE}}",}],"text": "{{msg.PREFERREDSPOKENLANGUAGE}}"}}],'

#Write class to run unit tests. These are created to retrieve the validate the snowflake Keys presence in liquid FHIR template that has been
#created for patient resource
# if statements are written to display message in vs code for all passed tests 

class TestliqTransform (unittest.TestCase):

    print("resource_type")     
    #Validating key CENSEOID in liquid template
    def test_liqpatcenseoid(self):
        if ("CENSEOID" in trans_pat_resource) == True:
            print("CENSEOID presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("CENSEOID" in trans_pat_resource,True,"CENSEOID not present in liquid template")
    #Validating key Member_Number in liquid template
    def test_liqpatmemnbr(self):
        if ("Member_Number" in trans_pat_resource) == True:
            print ("Member_Number presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("Member_Number" in trans_pat_resource,True,"Member_Number not present in liquid template")
    #Validating key MEMBER_SSN in liquid template
    def test_liqpatmemssn(self):
        if ("MEMBER_SSN" in trans_pat_resource) == True:
            print ("MEMBER_SSN presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_SSN" in trans_pat_resource,True,"MEMBER_SSN not present in liquid template")
    #Validating key MEMBER_LAST_NAME in liquid template
    def test_liqpatmemlname(self):
        if ("MEMBER_LAST_NAME" in trans_pat_resource) == True:
            print ("MEMBER_LAST_NAME presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_LAST_NAME" in trans_pat_resource,True,"MEMBER_LAST_NAME not present in liquid template")
    #Validating key MEMBER_FIRST_NAME in liquid template
    def test_liqpatmemfname(self):
        if ("MEMBER_FIRST_NAME" in trans_pat_resource) == True:
            print ("MEMBER_FIRST_NAME presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_FIRST_NAME" in trans_pat_resource,True,"MEMBER_FIRST_NAME not present in liquid template")
    #Validating key MEMBER_MIDDLE_NAME in liquid template
    def test_liqpatmemmname(self):
        if ("MEMBER_MIDDLE_NAME" in trans_pat_resource) == True:
            print ("MEMBER_MIDDLE_NAME presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_MIDDLE_NAME" in trans_pat_resource,True,"MEMBER_MIDDLE_NAME not present in liquid template")
    #Validating key SUFFIX in liquid template
    def test_liqpatsuffix(self):
        if ("SUFFIX" in trans_pat_resource) == True:
            print ("SUFFIX presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("SUFFIX" in trans_pat_resource,True,"SUFFIX not present in liquid template")


    print("telecom")
    #Validating key MEMBER_CELL in liquid template
    def test_liqpatmemtel(self):
        if ("MEMBER_TELEPHONE" in trans_telecom) == True:
            print ("MEMBER_TELEPHONE presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_TELEPHONE" in trans_telecom,True,"MEMBER_TELEPHONE not present in liquid template")
    #Validating key MEMBER_CELL in liquid template
    def test_liqpatmemcell(self):
        if ("MEMBER_CELL" in trans_telecom) == True:
            print ("MEMBER_CELL presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_CELL" in trans_telecom,True,"MEMBER_CELL not present in liquid template")
    #Validating key SECONDARYPHONE in liquid template
    def test_liqpatsecph(self):
        if ("SECONDARYPHONE" in trans_telecom) == True:
            print ("SECONDARYPHONE presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("SECONDARYPHONE" in trans_telecom,True,"SECONDARYPHONE not present in liquid template")
    #Validating key MEMBER_EMAIL in liquid template
    def test_liqpatmememail(self):
        if ("MEMBER_EMAIL" in trans_telecom) == True:
            print ("MEMBER_EMAIL presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_EMAIL" in trans_telecom,True,"MEMBER_EMAIL not present in liquid template")


    print("gender")
    #Validating key MEMBER_GENDER in liquid template
    def test_liqpatmgenderlogic(self):
        if ('MEMBER_GENDER == "M"' in trans_gender) == True:
            print ("MEMBER_GENDER code logic for male is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual('MEMBER_GENDER == "M"' in trans_gender,True,"MEMBER_GENDER code logic for male not present in liquid template")
    def test_liqpatfmgenderlogic(self):
        if ('MEMBER_GENDER == "F"' in trans_gender) == True:
            print ("MEMBER_GENDER code logic for female is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual('MEMBER_GENDER == "F"' in trans_gender,True,"MEMBER_GENDER code logic for female not present in liquid template")
    def test_liqpatugenderlogic(self):
        if ('MEMBER_GENDER == "U"' in trans_gender) == True:
            print ("MEMBER_GENDER code logic for unknown is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual('MEMBER_GENDER == "U"' in trans_gender,True,"MEMBER_GENDER code logic for unknown not present in liquid template")


    print("dob")
    #Validating key MEMBER_DATE_OF_BIRTH in liquid template
    def test_liqpatdob(self):
        if ("MEMBER_DATE_OF_BIRTH" in trans_dob) == True:
            print ("MEMBER_DATE_OF_BIRTH presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_DATE_OF_BIRTH" in trans_dob,True,"MEMBER_DATE_OF_BIRTH not present in liquid template")


    print("deceasedBoolean")
    def test_liqdeceasedboolean(self):
    #Validating key DeceasedBoolean in liquid template
        if ("DeceasedBoolean" in trans_deceased) == True:
            print ("DeceasedBoolean presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("DeceasedBoolean" in trans_deceased,True,"DeceasedBoolean not present in liquid template")
    def test_liqdeceasedDateTime(self):
    #Validating key deceasedDateTime in liquid template
        if ("deceasedDateTime" in trans_deceased) == True:
            print ("deceasedDateTime presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("deceasedDateTime" in trans_deceased,True,"deceasedDateTime not present in liquid template")


    print("address")
    #Validating key MEMBER_ADDRESS1 in liquid template
    def test_liqpatmemaddress1(self):
        if ("MEMBER_ADDRESS1" in trans_address) == True:
            print ("MEMBER_ADDRESS1 presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_ADDRESS1" in trans_address,True,"MEMBER_ADDRESS1 not present in liquid template")
    #Validating key MEMBER_ADDRESS2 in liquid template
    def test_liqpatmemaddress2(self):
        if ("MEMBER_ADDRESS2" in trans_address) == True:
            print ("MEMBER_ADDRESS2 presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_ADDRESS2" in trans_address,True,"MEMBER_ADDRESS2 not present in liquid template")
    #Validating key MEMBER_CITY in liquid template
    def test_liqpatmemcity(self):
        if ("MEMBER_CITY" in trans_address) == True:
            print ("MEMBER_CITY presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_CITY" in trans_address,True,"MEMBER_CITY not present in liquid template")
    #Validating key MEMBER_COUNTY in liquid template
    def test_liqpatmemcounty(self):
        if ("MEMBER_COUNTY" in trans_address) == True:
            print ("MEMBER_COUNTY presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_COUNTY" in trans_address,True,"MEMBER_COUNTY not present in liquid template")
    #Validating key MEMBER_STATE in liquid template
    def test_liqpatmemstate(self):
        if ("MEMBER_STATE" in trans_address) == True:
            print ("MEMBER_STATE presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_STATE" in trans_address,True,"MEMBER_STATE not present in liquid template")
    #Validating key MEMBER_ZIP in liquid template
    def test_liqpatmemzip(self):
        if ("MEMBER_ZIP" in trans_address) == True:
            print ("MEMBER_ZIP presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_ZIP" in trans_address,True,"MEMBER_ZIP not present in liquid template")
    #Validating key country in liquid template
    def test_liqpatcountry(self):
        if ("country" in trans_address) == True:
            print ("country presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("country" in trans_address,True,"country not present in liquid template")
    #Validating key MEMBER_MAIL_ADDRESS1 in liquid template
    def test_liqpatmailaddress1(self):
        if ("MEMBER_MAIL_ADDRESS1" in trans_address) == True:
            print ("MEMBER_MAIL_ADDRESS1 presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_MAIL_ADDRESS1" in trans_address,True,"MEMBER_MAIL_ADDRESS1 not present in liquid template")
    #Validating key MEMBER_MAIL_ADDRESS2 in liquid template
    def test_liqpatmailaddress2(self):
        if ("MEMBER_MAIL_ADDRESS2" in trans_address) == True:
            print ("MEMBER_MAIL_ADDRESS2 presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_MAIL_ADDRESS2" in trans_address,True,"MEMBER_MAIL_ADDRESS2 not present in liquid template")
    #Validating key MEMBER_MAIL_CITY in liquid template
    def test_liqpatmailcity(self):
        if ("MEMBER_MAIL_CITY" in trans_address) == True:
            print ("MEMBER_MAIL_CITY presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_MAIL_CITY" in trans_address,True,"MEMBER_MAIL_CITY not present in liquid template")
    #Validating key MEMBER_MAIL_STATE in liquid template
    def test_liqpatmailstate(self):
        if ("MEMBER_MAIL_STATE" in trans_address) == True:
            print ("MEMBER_MAIL_STATE presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_MAIL_STATE" in trans_address,True,"MEMBER_MAIL_STATE not present in liquid template")
    #Validating key MEMBER_MAIL_ZIP in liquid template
    def test_liqpatmailzip(self):
        if ("MEMBER_MAIL_ZIP" in trans_address) == True:
            print ("MEMBER_MAIL_ZIP presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_MAIL_ZIP" in trans_address,True,"MEMBER_MAIL_ZIP not present in liquid template")


    #no snowflake reference
    print("MaritalStatus")
    def test_liqpatmaritalstatussys(self):
    #Validating key MaritalStatusCode in liquid template
        if ("MARITALSTATUSSYSTEM" in trans_maritalStatus) == True:
            print ("MARITALSTATUSSYSTEM presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MARITALSTATUSSYSTEM" in trans_maritalStatus,True,"MARITALSTATUSSYSTEM not present in liquid template")
    #Validating key MaritalStatus in liquid template
    def test_liqpatmaritalstatuscode(self):
        if ("MARITALSTATUSCODE" in trans_maritalStatus) == True:
            print ("MARITALSTATUSCODE presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MARITALSTATUSCODE" in trans_maritalStatus,True,"MARITALSTATUSCODE not present in liquid template")
    #Validating key MaritalStatus in liquid template
    def test_liqpatmemmaritalstatus(self):
        if ("MEMBER_MARITALSTATUS" in trans_maritalStatus) == True:
            print ("MEMBER_MARITALSTATUS presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_MARITALSTATUS" in trans_maritalStatus,True,"MEMBER_MARITALSTATUS not present in liquid template")
    #Validating key MaritalStatus in liquid template
    def test_liqpatmemmaritalstatus(self):
        if ("MEMBER_MARITALSTATUS" in trans_maritalStatus) == True:
            print ("MEMBER_MARITALSTATUS presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_MARITALSTATUS" in trans_maritalStatus,True,"MEMBER_MARITALSTATUS not present in liquid template")


    #no snowflake reference
    print("multipleBirthBoolean")
    #Validating key MultipleBirth in liquid template
    def test_liqpatMultipleBirth(self):
        if ("MultipleBirth" in trans_multibirth) == True:
            print ("MultipleBirth presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MultipleBirth" in trans_multibirth,True,"MultipleBirth not present in liquid template")
    #Validating key MultipleBirthInteger in liquid template
    def test_liqpatMultipleBirthIgr(self):
        if ("MultipleBirthInteger" in trans_multibirth) == True:
            print ("MultipleBirthInteger presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MultipleBirthInteger" in trans_multibirth,True,"MultipleBirthInteger not present in liquid template")


    
    
    print("contact")
    #Validating key MEMBER_SECONDARY_CONTACT_PHONE in liquid template
    def test_liqpatmemsecphone(self):
        if ("MEMBER_SECONDARY_CONTACT_PHONE" in trans_contact) == True:
            print ("MEMBER_SECONDARY_CONTACT_PHONE presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_SECONDARY_CONTACT_PHONE" in trans_contact,True,"MEMBER_SECONDARY_CONTACT_PHONE not present in liquid template")
    #Validating key MEMBER_SECONDARY_CONTACT_PHONE in liquid template
    def test_liqpatmemseccnt(self):
        if ("MEMBER_SECONDARY_CONTACT" in trans_contact) == True:
            print ("MEMBER_SECONDARY_CONTACT presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_SECONDARY_CONTACT" in trans_contact,True,"MEMBER_SECONDARY_CONTACT not present in liquid template")


    print("managingOrganization")
    #Validating key CLIENTID in liquid template
    def test_liqpatclientid(self):
        if ("CLIENTID" in trans_mangOrg) == True:
            print ("CLIENTID presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("CLIENTID" in trans_mangOrg,True,"CLIENTID not present in liquid template")
    #Validating key CLIENTNAME in liquid template
    def test_liqpatclientname(self):
        if ("CLIENTNAME" in trans_mangOrg) == True:
            print ("CLIENTNAME presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("CLIENTNAME" in trans_mangOrg,True,"CLIENTNAME not present in liquid template")


    print("generalPractitioner")
    #Validating key PCP_ID in liquid template
    def test_liqpatpcpid(self):
        if ("PCP_ID" in trans_pcp) == True:
            print ("PCP_ID presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PCP_ID" in trans_pcp,True,"PCP_ID not present in liquid template")
    #Validating key PCP_FIRSTNAME in liquid template
    def test_liqpatpcpfname(self):
        if ("PCP_FIRSTNAME" in trans_pcp) == True:
            print ("PCP_FIRSTNAME presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PCP_FIRSTNAME" in trans_pcp,True,"PCP_FIRSTNAME not present in liquid template")
    #Validating key PCP_LASTNAME in liquid template
    def test_liqpatpcpfname(self):
        if ("PCP_LASTNAME" in trans_pcp) == True:
            print ("PCP_LASTNAME presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PCP_LASTNAME" in trans_pcp,True,"PCP_LASTNAME not present in liquid template")
    #Validating key ETHNICITY in liquid template
    def test_liqpatethnicity(self):
        if ("ETHNICITY" in trans_pcp) == True:
            print ("ETHNICITY presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("ETHNICITY" in trans_pcp,True,"ETHNICITY not present in liquid template")


    print("communications")
    #Validating key PREFERREDSPOKENLANGUAGE in liquid template
    def test_liqpatpfrdspknlang(self):
        if ("PREFERREDSPOKENLANGUAGE" in trans_comm) == True:
            print ("PREFERREDSPOKENLANGUAGE presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PREFERREDSPOKENLANGUAGE" in trans_comm,True,"PREFERREDSPOKENLANGUAGE not present in liquid template")

if __name__ == '__main__':
    unittest.main()