import unittest
import json

#Copy the dictionaries as strings into variables inorder to identify and validate snowflake JSON Keys presence in newly created strings.
trans_prac_resource = '"resourceType": "Practitioner","id": "example","text": {"status": "generated","div": "{{msg.text.div | escape_special_chars }}"},"identifier": [{"use": "official","value": "{{msg.PCP_ID }}"},{"use": "official", "type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v2-0203","code": "NPI","display" : "National provider identifier"}]},"value": "{{ msg.PROVIDER_NPI }}"},{"type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v2-0203","code": "UPIN","display" : "PHYSICIAN IDENTIFICATION NUMBER"}]},"value": "{{ msg.PROVIDER_PIN }}"},{"use": "official","type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v2-0203","code": "TAX"}]},"value": "{{ msg.PROVIDER_TAXID}}"},{"use": "official","value": "{{msg.IPA }}"},{"use": "official","value": "{{msg.IPA_IDENTIFIER }}"},{"use": "official","value": "{{msg.LPO }}"},{"use": "official","value": "{{ msg.LPO_IDENTIFIER }}"},{"use": "official","type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v2-0203","code": "SN","display" : "SUBSCIBER identifier"}]},"value": "{{ msg.SUBSCRIBER_ID }}"},{"use": "official","value": "{{ msg.PCP_PROVIDER_ID }}"},{"use": "official","value": "{{ msg.PROVIDER_ID }}"},{"use": "official", "type": {"coding": [{"system": "http://hl7.org/fhir/ValueSet/provider-taxonomy","code": "103G00000X","display" : "PROVIDER_TAXONOMY_CODE ",}]},"value": "{{msg.PROVIDER_TAXONOMY_CODE }}"},{"use": "official","type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v2-0203","code": "BSNR","display" : "PROVIDER_LOCATION_ID"}]},"value": "{{msg.PROVIDER_LOCATION_ID }}"}],"active": true,"name": [{"family": "{{ msg.PROVIDER_LASTNAME }}","given": ["{{ msg.PROVIDER_FIRSTNAME }}","{{ msg.PROVIDER_MIDDLE_INITIAL}}"],"prefix": ["{{ msg.PROVIDER_PREFIX}}"],"text": "{{ msg.OFFICE_CONTACT_NAME}}"}]'
trans_telecom = '[{"system": "phone","value": "{{msg.PROVIDER_PHONE}}","use": "work"},"system": "fax","value": "{{msg.PROVIDER_FAX}}","use": "work"},{"system": "email","value": "{{msg.PROVIDER_EMAIL}}","use": "work"}]'
trans_gender = '"gender": {% if msg.PROVIDER_GENDER == "M" -%} "male", {% elsif msg.PROVIDER_GENDER == "F" -%} "female",{% elsif msg.PROVIDER_GENDER == "O" -%}"other", {% elsif code -%}."unknown",{% else %}"",{% endif -%}'
trans_dob = '"birthDate": "{{ msg.PROVIDER_DOB| split:" " | first}}""'
trans_address = '[{"use": "billing","type": "physical","line": "{{msg.PROVIDER_ADDRESS1}}, {{msg.PROVIDER_ADDRESS2}},{{msg.PROVIDER_ADDRESS3}}","city": "{{msg.PROVIDER_CITY}}","state":"{{msg.PROVIDER_STATE}}","district": "{{msg.PROVIDER_COUNTY}}","postalCode": "{{msg.PROVIDER_ZIPCode}}"},]'
trans_comm = '"communication": [{"coding":[{"system":"http://hl7.org/fhir/ValueSet/languages","code": "en",}],"text": "{{msg.PROVIDER_LANGUAGE}}"},],' 
trans_qualifications = '"qualification": [ {"identifier": [{"use": "official","type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v2-0360","code": "MD","display" : "Doctor of Medicine"}]},"value": "{{ msg.PROVIDER_QUALIFICATION}}"},],}],} '

#Write class to run unit tests. These are created to retrieve the validate the snowflake Keys presence in liquid FHIR template that has been
#created for patient resource
# if statements are written to display message in vs code for all passed tests 

class TestliqTransform (unittest.TestCase):

    print("resource_type")     
    #Validating key PROVIDER_ID in liquid template
    def test_liqpracid(self):
        if ("PROVIDER_ID" in trans_prac_resource) == True:
            print("PROVIDER_ID presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_ID" in trans_prac_resource,True,"PROVIDER_ID not present in liquid template")
    #Validating key PROVIDER_NPI in liquid template
    def test_liqpracnpi(self):
        if ("PROVIDER_NPI" in trans_prac_resource) == True:
            print ("PROVIDER_NPI presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_NPI" in trans_prac_resource,True,"PROVIDER_NPI not present in liquid template")
    #Validating key PROVIDER_FIRSTNAME in liquid template
    def test_liqpraclname(self):
        if ("PROVIDER_FIRSTNAME" in trans_prac_resource) == True:
            print ("PROVIDER_FIRSTNAME presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_FIRSTNAME" in trans_prac_resource,True,"PROVIDER_FIRSTNAME not present in liquid template")
    #Validating key PROVIDER_LASTNAME in liquid template
    def test_liqpracfname(self):
        if ("PROVIDER_LASTNAME" in trans_prac_resource) == True:
            print ("PROVIDER_LASTNAME presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_LASTNAME" in trans_prac_resource,True,"PROVIDER_LASTNAME not present in liquid template")
    #Validating key PROVIDER_MIDDLE_INITIAL in liquid template
    def test_liqpracmi(self):
        if ("PROVIDER_MIDDLE_INITIAL" in trans_prac_resource) == True:
            print ("PROVIDER_MIDDLE_INITIAL presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_MIDDLE_INITIAL" in trans_prac_resource,True,"PROVIDER_MIDDLE_INITIAL not present in liquid template")
    #Validating key PROVIDER_PIN in liquid template
    def test_liqpracpin(self):
        if ("PROVIDER_PIN" in trans_prac_resource) == True:
            print ("PROVIDER_PIN presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_PIN" in trans_prac_resource,True,"PROVIDER_PIN not present in liquid template")
    #Validating key IPA in liquid template
    def test_liqpracipa(self):
        if ("IPA" in trans_prac_resource) == True:
            print ("IPA presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("IPA" in trans_prac_resource,True,"IPA not present in liquid template")
    #Validating key IPA_IDENTIFIER in liquid template
    def test_liqpracipaid(self):
        if ("IPA_IDENTIFIER" in trans_prac_resource) == True:
            print ("IPA_IDENTIFIER presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("IPA_IDENTIFIER" in trans_prac_resource,True,"IPA_IDENTIFIER not present in liquid template")
    #Validating key LPO in liquid template
    def test_liqpraclpo(self):
        if ("LPO" in trans_prac_resource) == True:
            print ("LPO presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("LPO" in trans_prac_resource,True,"LPO not present in liquid template")
    #Validating key PROVIDER_TAXID in liquid template
    def test_liqpraclpo(self):
        if ("PROVIDER_TAXID" in trans_prac_resource) == True:
            print ("PROVIDER_TAXID presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_TAXID" in trans_prac_resource,True,"PROVIDER_TAXID not present in liquid template")
    #Validating key LPO_IDENTIFIER in liquid template
    def test_liqpraclpoid(self):
        if ("LPO_IDENTIFIER" in trans_prac_resource) == True:
            print ("LPO_IDENTIFIER presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("LPO_IDENTIFIER" in trans_prac_resource,True,"LPO_IDENTIFIER not present in liquid template")
    #Validating key SUBSCRIBER_ID in liquid template
    def test_liqpracsbid(self):
        if ("SUBSCRIBER_ID" in trans_prac_resource) == True:
            print ("SUBSCRIBER_ID presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("SUBSCRIBER_ID" in trans_prac_resource,True,"SUBSCRIBER_ID not present in liquid template")
    #Validating key PCP_ID in liquid template
    def test_liqpracgrpid(self):
        if ("PCP_ID" in trans_prac_resource) == True:
            print ("PCP_ID presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PCP_ID" in trans_prac_resource,True,"PCP_ID not present in liquid template")
    #Validating key PROVIDER_TAXONOMY_CODE in liquid template
    def test_liqpractxcd(self):
        if ("PROVIDER_TAXONOMY_CODE" in trans_prac_resource) == True:
            print ("PROVIDER_TAXONOMY_CODE presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_TAXONOMY_CODE" in trans_prac_resource,True,"PROVIDER_TAXONOMY_CODE not present in liquid template")
    #Validating key PCP_PROVIDER_ID in liquid template
    def test_liqpractpcppvid(self):
        if ("PCP_PROVIDER_ID" in trans_prac_resource) == True:
            print ("PCP_PROVIDER_ID presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PCP_PROVIDER_ID" in trans_prac_resource,True,"PCP_PROVIDER_ID not present in liquid template")
    #Validating key PROVIDER_LOCATION_ID in liquid template
    def test_liqpractlcid(self):
        if ("PROVIDER_LOCATION_ID" in trans_prac_resource) == True:
            print ("PROVIDER_LOCATION_ID presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_LOCATION_ID" in trans_prac_resource,True,"PROVIDER_LOCATION_ID not present in liquid template")
    #Validating key PROVIDER_PREFIX in liquid template
    def test_liqpracpfx(self):
        if ("PROVIDER_PREFIX" in trans_prac_resource) == True:
            print ("PROVIDER_PREFIX presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_PREFIX" in trans_prac_resource,True,"PROVIDER_PREFIX not present in liquid template")
    #Validating key OFFICE_CONTACT_NAME in liquid template
    def test_liqpracofcctnm(self):
        if ("OFFICE_CONTACT_NAME" in trans_prac_resource) == True:
            print ("OFFICE_CONTACT_NAME presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("OFFICE_CONTACT_NAME" in trans_prac_resource,True,"OFFICE_CONTACT_NAME not present in liquid template")


    print("telecom")
    #Validating key PROVIDER_PHONE in liquid template
    def test_liqpracprmy(self):
        if ("PROVIDER_PHONE" in trans_telecom) == True:
            print ("PROVIDER_PHONE presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_PHONE" in trans_telecom,True,"PROVIDER_PHONE not present in liquid template")
    #Validating key PROVIDER_FAX in liquid template
    def test_liqpracfax(self):
        if ("PROVIDER_FAX" in trans_telecom) == True:
            print ("PROVIDER_FAX presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_FAX" in trans_telecom,True,"PROVIDER_FAX not present in liquid template")
    #Validating key PROVIDER_EMAIL in liquid template
    def test_liqpracemail(self):
        if ("PROVIDER_EMAIL" in trans_telecom) == True:
            print ("PROVIDER_EMAIL presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_EMAIL" in trans_telecom,True,"PROVIDER_EMAIL not present in liquid template")    


    
    print("dob")
    #Validating key PROVIDER_DOB in liquid template
    def test_liqpracdob(self):
        if ("PROVIDER_DOB" in trans_dob) == True:
            print ("PROVIDER_DOB presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_DOB" in trans_dob,True,"PROVIDER_DOB not present in liquid template")


    print("address")
    #Validating key PROVIDER_ADDRESS1 in liquid template
    def test_liqpracaddress1(self):
        if ("PROVIDER_ADDRESS1" in trans_address) == True:
            print ("PROVIDER_ADDRESS1 presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_ADDRESS1" in trans_address,True,"PROVIDER_ADDRESS1 not present in liquid template")
    #Validating key PROVIDER_ADDRESS2 in liquid template
    def test_liqpracaddress2(self):
        if ("PROVIDER_ADDRESS2" in trans_address) == True:
            print ("PROVIDER_ADDRESS2 presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_ADDRESS2" in trans_address,True,"PROVIDER_ADDRESS2 not present in liquid template")
    #Validating key PROVIDER_ADDRESS3 in liquid template
    def test_liqpracaddress3(self):
        if ("PROVIDER_ADDRESS3" in trans_address) == True:
            print ("PROVIDER_ADDRESS3 presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_ADDRESS3" in trans_address,True,"PROVIDER_ADDRESS3 not present in liquid template")
    #Validating key PROVIDER_CITY in liquid template
    def test_liqpraccity(self):
        if ("PROVIDER_CITY" in trans_address) == True:
            print ("PROVIDER_CITY presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_CITY" in trans_address,True,"PROVIDER_CITY not present in liquid template")
    #Validating key PROVIDER_STATE in liquid template
    def test_liqpracstate(self):
        if ("PROVIDER_STATE" in trans_address) == True:
            print ("PROVIDER_STATE presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_STATE" in trans_address,True,"PROVIDER_STATE not present in liquid template")
    #Validating key PROVIDER_COUNTY in liquid template
    def test_liqpraccounty(self):
        if ("PROVIDER_COUNTY" in trans_address) == True:
            print ("PROVIDER_COUNTY presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_COUNTY" in trans_address,True,"PROVIDER_COUNTY not present in liquid template")
    #Validating key PROVIDER_ZIPCode in liquid template
    def test_liqpraczip(self):
        if ("PROVIDER_ZIPCode" in trans_address) == True:
            print ("PROVIDER_ZIPCode presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_ZIPCode" in trans_address,True,"PROVIDER_ZIPCode not present in liquid template")
    

    print("gender")
    #Validating key PROVIDER_GENDER in liquid template
    def test_liqpracmgenderlogic(self):
        if ('PROVIDER_GENDER == "M"' in trans_gender) == True:
            print ("PROVIDER_GENDER code logic for male is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual('PROVIDER_GENDER == "M"' in trans_gender,True,"PROVIDER_GENDER code logic for male not present in liquid template")
    def test_liqpracfmgenderlogic(self):
        if ('PROVIDER_GENDER == "F"' in trans_gender) == True:
            print ("PROVIDER_GENDER code logic for female is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual('PROVIDER_GENDER == "F"' in trans_gender,True,"PROVIDER_GENDER code logic for female not present in liquid template")
    def test_liqpracugenderlogic(self):
        if ('PROVIDER_GENDER == "O"' in trans_gender) == True:
            print ("PROVIDER_GENDER code logic for unknown is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual('PROVIDER_GENDER == "O"' in trans_gender,True,"PROVIDER_GENDER code logic for unknown not present in liquid template")

    
    print("communications")
    #Validating key PROVIDER_LANGUAGE in liquid template
    def test_liqpraclang(self):
        if ("PROVIDER_LANGUAGE" in trans_comm) == True:
            print ("PROVIDER_LANGUAGE presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_LANGUAGE" in trans_comm,True,"PROVIDER_LANGUAGE not present in liquid template")
    
    print("Qualification")
    #Validating key PROVIDER_QUALIFICATION in liquid template
    def test_liqpracqfn(self):
        if ("PROVIDER_QUALIFICATION" in trans_qualifications) == True:
            print ("PROVIDER_QUALIFICATION presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PROVIDER_QUALIFICATION" in trans_qualifications,True,"PROVIDER_QUALIFICATION not present in liquid template")

if __name__ == '__main__':
    unittest.main()