import unittest
import json

#Copy the dictionaries as strings into variables inorder to identify and validate snowflake JSON Keys presence in newly created strings.
trans_cov_resource = '"resourceType": "Coverage","id": "{{msg.id}}","text": {"status": "generated","div": "{{msg.text.div | escape_special_chars }}"},'
trans_identifier = '"identifier": [{"use": "official", "value": "{{msg.PLAN_NUMBER }}"},{"use": "official","value": "{{msg.HICN }}"}],'
trans_status = '"status": "{{msg.COVERAGE_STATUS}}"'
trans_type ='"type": {"coding": [{"system": "https://terminology.hl7.org/3.1.0/ValueSet-v3-ActCoverageTypeCode.html","code": "{{msg.COVERAGE_TYPE }}","display": "{{msg.COVERAGE_TYPE_DESC }}"}]},'
trans_policyholder ='"policyHolder": {"reference": "Oraganization/","display": "{{msg.POLICY_HOLDER}}"},'
trans_subscriber= '"subscriber": {"reference": "Patient/","display""display": "{{msg.SUBSCRIBER}}": {% if msg.CENSEOID -%}"{{msg.CENSEOID}}",{% elseif msg.CMSID_HIC_NUMBER -%}"{{msg.CMSID_HIC_NUMBER}}",{% elsif msg.MEMBER_NUMBER -%}"{{msg.MEMBER_NUMBER}}",{% elsif msg.MEMBERID -%}"{{msg.MEMBERID}}",{% elsif msg.HICN -%}"{{msg.HICN}}",{% else %}{% endif %}'
trans_beneficiary = '"beneficiary": {"reference": "Patient/","display": "{{msg.BENEFICIARY}}"},"dependent": "{{msg.DEPENDENT}}","relationship": {"coding": [{"system": "http://hl7.org/fhir/ValueSet/subscriber-relationship","code": "{{ msg.RELATIONSHIP }}"}]},'
trans_period = '"period": {"start": "{{ msg.COVERAGE_START_DATE }}","end": "{{ msg.COVERAGE_STOP_DATE }}"},'
trans_payor= '"payor": [{"reference": "Organization/","display": "{{msg.PAYOR}}"}],'
trans_class = '"class": [{"type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/coverage-class","code": "{{ msg.PLAN_TYPE}}"}]},"value": "{{ msg.PLAN_VALUE}}","name": "{{ msg.PLAN_DESCRIPTION }}"}],'
trans_order = '"order": "{{ msg.ORDER }}"'
trans_network = '"network": "{{ msg.NETWORK }}"'
trans_costtobeneficiary = '"costToBeneficiary": [{"type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/coverage-copay-type","code": "{{ msg.COST_TO_BENEFICIARY_TYPE }}","display": "{{msg.COST_TO_BENEFICIARY_TYPE_DESC}}"}]},"valueQuantity": {"value": "{{msg.COST_QUANTITY_VALUE}}","code": "{{msg.COST_QUANTITY_CURRENCY}}"},"valueMoney": {"value": "{{ msg.COST_MONEY_VALUE}}","currency": "{{ msg.COST_MONEY_CURRENCY }}"},"exception": [{"type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/ex-coverage-financial-exception","code": "{{ msg.BENEFICIARY_EXCEPTION_TYPE }}"}],"period": {"start": "{{ msg.BENEFICIARY_EXCEPTION_PERIOD_START }}","end": "{{ msg.BENEFICIARY_EXCEPTION_PERIOD_END }}"}}]}],'
trans_subrogation = '"subrogation" : "{{ msg.SUBROGATION}}"'
trans_contract = '"contract" : [{"reference": "Contract/","display": "{{ msg.CONTRACT}}"}]'

#Write class to run unit tests. These are created to retrieve the validate the snowflake Keys presence in liquid FHIR template that has been
#created for patient resource
# if statements are written to display message in vs code for all passed tests 

class TestliqTransform (unittest.TestCase):

     
    #Validating key PLAN_NUMBER in liquid template
    def test_liqcovplnnmbr(self):
        if ("PLAN_NUMBER" in trans_identifier) == True:
            print("PLAN_NUMBER presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PLAN_NUMBER" in trans_identifier,True,"PLAN_NUMBER not present in liquid template")
    #Validating key HICN in liquid template
    def test_liqcovhicn(self):
        if ("HICN" in trans_identifier) == True:
            print ("HICN presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("HICN" in trans_identifier,True,"HICN not present in liquid template")
    #Validating key COVERAGE_STATUS in liquid template
    def test_liqcovstatus(self):
        if ("COVERAGE_STATUS" in trans_status) == True:
            print ("COVERAGE_STATUS presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("COVERAGE_STATUS" in trans_status,True,"COVERAGE_STATUS not present in liquid template")
    #Validating key COVERAGE_TYPE in liquid template
    def test_liqcovtype(self):
        if ("COVERAGE_TYPE" in trans_type) == True:
            print ("COVERAGE_TYPE presence is validated in liquid template")
        #Prints message AdmitSource the test fails for comparison
        self.assertEqual("COVERAGE_TYPE" in trans_type,True,"COVERAGE_TYPE not present in liquid template")
    #Validating key COVERAGE_TYPE_DESC in liquid template
    def test_liqcovtypedesc(self):
        if ("COVERAGE_TYPE_DESC" in trans_type) == True:
            print ("COVERAGE_TYPE_DESC presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("COVERAGE_TYPE_DESC" in trans_type,True,"COVERAGE_TYPE_DESC not present in liquid template")    
    #Validating key POLICY_HOLDER in liquid template
    def test_liqcovplcyhldr(self):
        if ("POLICY_HOLDER" in trans_policyholder) == True:
            print ("POLICY_HOLDER presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("POLICY_HOLDER" in trans_policyholder,True,"POLICY_HOLDER not present in liquid template")
    #Validating key SUBSCRIBER in liquid template
    def test_liqcovsbscr(self):
        if ("SUBSCRIBER" in trans_subscriber) == True:
            print ("SUBSCRIBER presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("SUBSCRIBER" in trans_subscriber,True,"SUBSCRIBER not present in liquid template")
    #Validating key CENSEOID in liquid template
    def test_liqcovcenseoid(self):
        if ("CENSEOID" in trans_subscriber) == True:
            print ("CENSEOID presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("CENSEOID" in trans_subscriber,True,"CENSEOID not present in liquid template")    
    #Validating key CMSID_HIC_NUMBER in liquid template
    def test_liqcovcmsid(self):
        if ("CMSID_HIC_NUMBER" in trans_subscriber) == True:
            print ("CMSID_HIC_NUMBER presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("CMSID_HIC_NUMBER" in trans_subscriber,True,"CMSID_HIC_NUMBER not present in liquid template")
    #Validating key MEMBER_NUMBER in liquid template
    def test_liqcovmemnum(self):
        if ("MEMBER_NUMBER" in trans_subscriber) == True:
            print ("MEMBER_NUMBER presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBER_NUMBER" in trans_subscriber,True,"MEMBER_NUMBER not present in liquid template")
    #Validating key MEMBERID in liquid template
    def test_liqcovmemid(self):
        if ("MEMBERID" in trans_subscriber) == True:
            print ("MEMBERID presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("MEMBERID" in trans_subscriber,True,"MEMBERID not present in liquid template")
    #Validating key HICN in liquid template
    def test_liqcovhicn(self):
        if ("HICN" in trans_subscriber) == True:
            print ("HICN presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("HICN" in trans_subscriber,True,"HICN not present in liquid template")
    #Validating key BENEFICIARY in liquid template
    def test_liqcovben(self):
        if ("BENEFICIARY" in trans_beneficiary) == True:
            print ("BENEFICIARY presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("BENEFICIARY" in trans_beneficiary,True,"BENEFICIARY not present in liquid template")
    #Validating key DEPENDENT in liquid template
    def test_liqcovdep(self):
        if ("DEPENDENT" in trans_beneficiary) == True:
            print ("DEPENDENT presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("DEPENDENT" in trans_beneficiary,True,"DEPENDENT not present in liquid template")
    #Validating key RELATIONSHIP in liquid template
    def test_liqcovrel(self):
        if ("RELATIONSHIP" in trans_beneficiary) == True:
            print ("RELATIONSHIP presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("RELATIONSHIP" in trans_beneficiary,True,"RELATIONSHIP not present in liquid template")
    #Validating key COVERAGE_START_DATE in liquid template
    def test_liqcovstrtdt(self):
        if ("COVERAGE_START_DATE" in trans_period) == True:
            print ("COVERAGE_START_DATE presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("COVERAGE_START_DATE" in trans_period,True,"COVERAGE_START_DATE not present in liquid template")
    #Validating key COVERAGE_STOP_DATE in liquid template
    def test_liqcovstopdt(self):
        if ("COVERAGE_STOP_DATE" in trans_period) == True:
            print ("COVERAGE_STOP_DATE presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("COVERAGE_STOP_DATE" in trans_period,True,"COVERAGE_STOP_DATE not present in liquid template")
    #Validating key PAYOR in liquid template
    def test_liqcovpayor(self):
        if ("PAYOR" in trans_payor) == True:
            print ("PAYOR presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PAYOR" in trans_payor,True,"PAYOR not present in liquid template")
    #Validating key PLAN_TYPE in liquid template
    def test_liqcovplntype(self):
        if ("PLAN_TYPE" in trans_class) == True:
            print ("PLAN_TYPE presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PLAN_TYPE" in trans_class,True,"PLAN_TYPE not present in liquid template")
    #Validating key PLAN_VALUE in liquid template
    def test_liqcovplnvalue(self):
        if ("PLAN_VALUE" in trans_class) == True:
            print ("PLAN_VALUE presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PLAN_VALUE" in trans_class,True,"PLAN_VALUE not present in liquid template")
    #Validating key PLAN_DESCRIPTION in liquid template
    def test_liqcovplndesc(self):
        if ("PLAN_DESCRIPTION" in trans_class) == True:
            print ("PLAN_DESCRIPTION presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("PLAN_DESCRIPTION" in trans_class,True,"PLAN_DESCRIPTION not present in liquid template")
    #Validating key ORDER in liquid template
    def test_liqcovorder(self):
        if ("ORDER" in trans_order) == True:
            print ("ORDER presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("ORDER" in trans_order,True,"ORDER not present in liquid template")
    #Validating key NETWORK in liquid template
    def test_liqcovnetwork(self):
        if ("NETWORK" in trans_network) == True:
            print ("NETWORK presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("NETWORK" in trans_network,True,"NETWORK not present in liquid template")
    #Validating key COST_TO_BENEFICIARY_TYPE in liquid template
    def test_liqcovbentype(self):
        if ("COST_TO_BENEFICIARY_TYPE" in trans_costtobeneficiary) == True:
            print ("COST_TO_BENEFICIARY_TYPE presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("COST_TO_BENEFICIARY_TYPE" in trans_costtobeneficiary,True,"COST_TO_BENEFICIARY_TYPE not present in liquid template")
    #Validating key COST_TO_BENEFICIARY_TYPE_DESC in liquid template
    def test_liqcovbentypedesc(self):
        if ("COST_TO_BENEFICIARY_TYPE_DESC" in trans_costtobeneficiary) == True:
            print ("COST_TO_BENEFICIARY_TYPE_DESC presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("COST_TO_BENEFICIARY_TYPE_DESC" in trans_costtobeneficiary,True,"COST_TO_BENEFICIARY_TYPE_DESC not present in liquid template")
    #Validating key COST_QUANTITY_VALUE in liquid template
    def test_liqcovcostqntyval(self):
        if ("COST_QUANTITY_VALUE" in trans_costtobeneficiary) == True:
            print ("COST_QUANTITY_VALUE presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("COST_QUANTITY_VALUE" in trans_costtobeneficiary,True,"COST_QUANTITY_VALUE not present in liquid template")
    #Validating key COST_QUANTITY_CURRENCY in liquid template
    def test_liqcovcostqntycur(self):
        if ("COST_QUANTITY_CURRENCY" in trans_costtobeneficiary) == True:
            print ("COST_QUANTITY_CURRENCY presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("COST_QUANTITY_CURRENCY" in trans_costtobeneficiary,True,"COST_QUANTITY_CURRENCY not present in liquid template")
    #Validating key COST_MONEY_VALUE in liquid template
    def test_liqcovcostmoneyval(self):
        if ("COST_MONEY_VALUE" in trans_costtobeneficiary) == True:
            print ("COST_MONEY_VALUE presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("COST_MONEY_VALUE" in trans_costtobeneficiary,True,"COST_MONEY_VALUE not present in liquid template")
    #Validating key COST_MONEY_CURRENCY in liquid template
    def test_liqcovcostmoneycur(self):
        if ("COST_MONEY_CURRENCY" in trans_costtobeneficiary) == True:
            print ("COST_MONEY_CURRENCY presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("COST_MONEY_CURRENCY" in trans_costtobeneficiary,True,"COST_MONEY_CURRENCY not present in liquid template")
    #Validating key BENEFICIARY_EXCEPTION_TYPE in liquid template
    def test_liqcovbenexcptype(self):
        if ("BENEFICIARY_EXCEPTION_TYPE" in trans_costtobeneficiary) == True:
            print ("BENEFICIARY_EXCEPTION_TYPE presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("BENEFICIARY_EXCEPTION_TYPE" in trans_costtobeneficiary,True,"BENEFICIARY_EXCEPTION_TYPE not present in liquid template")
    #Validating key BENEFICIARY_EXCEPTION_PERIOD_START in liquid template
    def test_liqcovbenexcpstrt(self):
        if ("BENEFICIARY_EXCEPTION_PERIOD_START" in trans_costtobeneficiary) == True:
            print ("BENEFICIARY_EXCEPTION_PERIOD_START presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("BENEFICIARY_EXCEPTION_PERIOD_START" in trans_costtobeneficiary,True,"BENEFICIARY_EXCEPTION_PERIOD_START not present in liquid template")
    #Validating key BENEFICIARY_EXCEPTION_PERIOD_END in liquid template
    def test_liqcovbenexcpend(self):
        if ("BENEFICIARY_EXCEPTION_PERIOD_END" in trans_costtobeneficiary) == True:
            print ("BENEFICIARY_EXCEPTION_PERIOD_END presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("BENEFICIARY_EXCEPTION_PERIOD_END" in trans_costtobeneficiary,True,"BENEFICIARY_EXCEPTION_PERIOD_END not present in liquid template")
    #Validating key SUBROGATION in liquid template
    def test_liqcovsubrogation(self):
        if ("SUBROGATION" in trans_subrogation) == True:
            print ("SUBROGATION presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("SUBROGATION" in trans_subrogation,True,"SUBROGATION not present in liquid template")
    #Validating key CONTRACT in liquid template
    def test_liqcovcontract(self):
        if ("CONTRACT" in trans_contract) == True:
            print ("CONTRACT presence is validated in liquid template")
        #Prints message if the test fails for comparison
        self.assertEqual("CONTRACT" in trans_contract,True,"CONTRACT not present in liquid template")





if __name__ == '__main__':
    unittest.main()