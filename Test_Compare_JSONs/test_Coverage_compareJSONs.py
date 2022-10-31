import unittest
import json

#Procedure to import file from different folder using sys, path, append
import sys
sys.path.append(".")
from Read_JSON import dataSnwCovInput,dataTransformerCov,input_covsubid

#Write class to run unit tests. These are created to retrieve the values from Snowflake and transformed JSONs and perform comparison 
#between them to ensure that the snowflake JSON transformation is successful when created using liquid FHIR template

class TestTransform (unittest.TestCase):    
    
    # if statements are written to display message in vs code for all passed tests   
    
    #Coverage Tests start here
    #Validation of PLAN_NUMBER between snowflake JSON and transformed Coverage JSON
    def test_covplnnbr(self):
        if dataSnwCovInput['PLAN_NUMBER'] == dataTransformerCov['identifier'][0]['value']:
            print('PLAN_NUMBER Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['PLAN_NUMBER'],dataTransformerCov['identifier'][0]['value'],"PLAN_NUMBER not Matched")

    #Validation of HICN between snowflake JSON and transformed Coverage JSON
    def test_covHICN(self):
        if dataSnwCovInput['HICN'] == dataTransformerCov['identifier'][1]['value']:
            print('HICN Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['HICN'],dataTransformerCov['identifier'][1]['value'],"HICN not Matched")

    #Validation of COVERAGE_STATUS between snowflake JSON and transformed Coverage JSON
    def test_covstatus(self):
        if dataSnwCovInput['COVERAGE_STATUS'] == dataTransformerCov['status']:
            print('COVERAGE_STATUS Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['COVERAGE_STATUS'],dataTransformerCov['status'],"COVERAGE_STATUS not Matched")

    #Validation of COVERAGE_TYPE between snowflake JSON and transformed Coverage JSON
    def test_covtype(self):
        if dataSnwCovInput['COVERAGE_TYPE'] == dataTransformerCov['type']['coding'][0]['code']:
            print('COVERAGE_TYPE Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['COVERAGE_TYPE'],dataTransformerCov['type']['coding'][0]['code'],"COVERAGE_TYPE not Matched") 

    #Validation of COVERAGE_TYPE_DESC between snowflake JSON and transformed Coverage JSON
    def test_covtypedesc(self):
        if dataSnwCovInput['COVERAGE_TYPE_DESC'] == dataTransformerCov['type']['coding'][0]['display']:
            print('COVERAGE_TYPE_DESC Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['COVERAGE_TYPE_DESC'],dataTransformerCov['type']['coding'][0]['display'],"COVERAGE_TYPE_DESC not Matched") 
    
    
    #Validation of POLICY_HOLDER between snowflake JSON and transformed Coverage JSON
    def test_covplcyhldr(self):
        if dataSnwCovInput['POLICY_HOLDER'] == dataTransformerCov['policyHolder']['display']:
            print('POLICY_HOLDER Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['POLICY_HOLDER'],dataTransformerCov['policyHolder']['display'],"POLICY_HOLDER not Matched")

    #Validation of SUBSCRIBER between snowflake JSON and transformed Coverage JSON
    def test_covsubscriber(self):
        if dataSnwCovInput['SUBSCRIBER'] == dataTransformerCov['subscriber']['display']:
            print('SUBSCRIBER Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['SUBSCRIBER'],dataTransformerCov['subscriber']['display'],"SUBSCRIBER not Matched") 

    #Validation of SubscriberID between snowflake JSON and transformed Coverage JSON
    def test_covcmsidhicnmbr(self):
        if input_covsubid == dataTransformerCov['subscriberId']:
            print('SUBSCRIBERID Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(input_covsubid,dataTransformerCov['subscriberId'],"SUBSCRIBERID not Matched") 

    #Validation of BENEFICIARY between snowflake JSON and transformed Coverage JSON
    def test_covbeneficary(self):
        if dataSnwCovInput['BENEFICIARY'] == dataTransformerCov['beneficiary']['display']:
            print('BENEFICIARY Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['BENEFICIARY'],dataTransformerCov['beneficiary']['display'],"BENEFICIARY not Matched") 

    #Validation of DEPENDENT between snowflake JSON and transformed Coverage JSON
    def test_covdependent(self):
        if dataSnwCovInput['DEPENDENT'] == dataTransformerCov['dependent']:
            print('DEPENDENT Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['DEPENDENT'],dataTransformerCov['dependent'],"DEPENDENT not Matched") 

    #Validation of RELATIONSHIP between snowflake JSON and transformed Coverage JSON
    def test_covrelationship(self):
        if dataSnwCovInput['RELATIONSHIP'] == dataTransformerCov['relationship']['coding'][0]['code']:
            print('RELATIONSHIP Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['RELATIONSHIP'],dataTransformerCov['relationship']['coding'][0]['code'],"RELATIONSHIP not Matched")
    
    #Validation of COVERAGE_START_DATE between snowflake JSON and transformed Coverage JSON
    def test_covstrtdt(self):
        if dataSnwCovInput['COVERAGE_START_DATE'] == dataTransformerCov['period']['start']:
            print('COVERAGE_START_DATE Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['COVERAGE_START_DATE'],dataTransformerCov['period']['start'],"COVERAGE_START_DATE not Matched")
    
    #Validation of COVERAGE_STOP_DATE between snowflake JSON and transformed Coverage JSON
    def test_covstopdt(self):
        if dataSnwCovInput['COVERAGE_STOP_DATE'] == dataTransformerCov['period']['end']:
            print('COVERAGE_STOP_DATE Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['COVERAGE_STOP_DATE'],dataTransformerCov['period']['end'],"COVERAGE_STOP_DATE not Matched")

    #Validation of PAYOR between snowflake JSON and transformed Coverage JSON
    def test_covpayor(self):
        if dataSnwCovInput['PAYOR'] == dataTransformerCov['payor'][0]['display']:
            print('PAYOR Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['PAYOR'],dataTransformerCov['payor'][0]['display'],"PAYOR not Matched")

    #Validation of PLAN_TYPE between snowflake JSON and transformed Coverage JSON
    def test_covplntype(self):
        if dataSnwCovInput['PLAN_TYPE'] == dataTransformerCov['class'][0]['type']['coding'][0]['code']:
            print('PLAN_TYPE Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['PLAN_TYPE'],dataTransformerCov['class'][0]['type']['coding'][0]['code'],"PLAN_TYPE not Matched")

    #Validation of PLAN_VALUE between snowflake JSON and transformed Coverage JSON
    def test_covplnvalue(self):
        if dataSnwCovInput['PLAN_VALUE'] == dataTransformerCov['class'][0]['value']:
            print('PLAN_VALUE Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['PLAN_VALUE'],dataTransformerCov['class'][0]['value'],"PLAN_VALUE not Matched")

    #Validation of PLAN_DESCRIPTION between snowflake JSON and transformed Coverage JSON
    def test_covplndesc(self):
        if dataSnwCovInput['PLAN_DESCRIPTION'] == dataTransformerCov['class'][0]['name']:
            print('PLAN_DESCRIPTION Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['PLAN_DESCRIPTION'],dataTransformerCov['class'][0]['name'],"PLAN_DESCRIPTION not Matched")

    #Validation of ORDER between snowflake JSON and transformed Coverage JSON
    def test_covplnordr(self):
        if dataSnwCovInput['ORDER'] == dataTransformerCov['order']:
            print('ORDER Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['ORDER'],dataTransformerCov['order'],"ORDER not Matched")

    #Validation of NETWORK between snowflake JSON and transformed Coverage JSON
    def test_covnetwork(self):
        if dataSnwCovInput['NETWORK'] == dataTransformerCov['network']:
            print('NETWORK Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['NETWORK'],dataTransformerCov['network'],"NETWORK not Matched")

    #Validation of COST_TO_BENEFICIARY_TYPE between snowflake JSON and transformed Coverage JSON
    def test_covcsttoBen(self):
        if dataSnwCovInput['COST_TO_BENEFICIARY_TYPE'] == dataTransformerCov['costToBeneficiary'][0]['type']['coding'][0]['code']:
            print('COST_TO_BENEFICIARY_TYPE Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['COST_TO_BENEFICIARY_TYPE'],dataTransformerCov['costToBeneficiary'][0]['type']['coding'][0]['code'],"COST_TO_BENEFICIARY_TYPE not Matched")
    
    #Validation of COST_TO_BENEFICIARY_TYPE_DESC between snowflake JSON and transformed Coverage JSON
    def test_covcsttoBendesc(self):
        if dataSnwCovInput['COST_TO_BENEFICIARY_TYPE_DESC'] == dataTransformerCov['costToBeneficiary'][0]['type']['coding'][0]['display']:
            print('COST_TO_BENEFICIARY_TYPE_DESC Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['COST_TO_BENEFICIARY_TYPE_DESC'],dataTransformerCov['costToBeneficiary'][0]['type']['coding'][0]['display'],"COST_TO_BENEFICIARY_TYPE_DESC not Matched")
    
    #Validation of COST_QUANTITY_CURRENCY between snowflake JSON and transformed Coverage JSON
    def test_covcstvalmoney(self):
        if dataSnwCovInput['COST_QUANTITY_CURRENCY'] == dataTransformerCov['costToBeneficiary'][0]['valueQuantity']['code']:
            print('COST_QUANTITY_CURRENCY Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['COST_QUANTITY_CURRENCY'],dataTransformerCov['costToBeneficiary'][0]['valueQuantity']['code'],"COST_QUANTITY_CURRENCY not Matched")
    
    #Validation of COST_QUANTITY_VALUE between snowflake JSON and transformed Coverage JSON
    def test_covcstvalmoneycur(self):
        if str(dataSnwCovInput['COST_QUANTITY_VALUE']) == dataTransformerCov['costToBeneficiary'][0]['valueQuantity']['value']:
            print('COST_QUANTITY_VALUE Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(str(dataSnwCovInput['COST_QUANTITY_VALUE']),dataTransformerCov['costToBeneficiary'][0]['valueQuantity']['value'],"COST_QUANTITY_VALUE not Matched")
    
    #Validation of BENEFICIARY_EXCEPTION_TYPE between snowflake JSON and transformed Coverage JSON
    def test_covbenexcptype(self):
        if dataSnwCovInput['BENEFICIARY_EXCEPTION_TYPE'] == dataTransformerCov['costToBeneficiary'][0]['exception'][0]['type']['coding'][0]['code']:
            print('BENEFICIARY_EXCEPTION_TYPE Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['BENEFICIARY_EXCEPTION_TYPE'],dataTransformerCov['costToBeneficiary'][0]['exception'][0]['type']['coding'][0]['code'],"BENEFICIARY_EXCEPTION_TYPE not Matched")
    
    #Validation of BENEFICIARY_EXCEPTION_PERIOD_START between snowflake JSON and transformed Coverage JSON
    def test_covbenexcperstart(self):
        if dataSnwCovInput['BENEFICIARY_EXCEPTION_PERIOD_START'] == dataTransformerCov['costToBeneficiary'][0]['exception'][0]['period']['start']:
            print('BENEFICIARY_EXCEPTION_PERIOD_START Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['BENEFICIARY_EXCEPTION_PERIOD_START'],dataTransformerCov['costToBeneficiary'][0]['exception'][0]['period']['start'],"BENEFICIARY_EXCEPTION_PERIOD_START not Matched")
    
    #Validation of BENEFICIARY_EXCEPTION_PERIOD_END between snowflake JSON and transformed Coverage JSON
    def test_covbenexcperend(self):
        if dataSnwCovInput['BENEFICIARY_EXCEPTION_PERIOD_END'] == dataTransformerCov['costToBeneficiary'][0]['exception'][0]['period']['end']:
            print('BENEFICIARY_EXCEPTION_PERIOD_END Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['BENEFICIARY_EXCEPTION_PERIOD_END'],dataTransformerCov['costToBeneficiary'][0]['exception'][0]['period']['end'],"BENEFICIARY_EXCEPTION_PERIOD_END not Matched")
    
    #Validation of SUBROGATION between snowflake JSON and transformed Coverage JSON
    def test_covsubrogation(self):
        if dataSnwCovInput['SUBROGATION'] == dataTransformerCov['subrogation']:
            print('SUBROGATION Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['SUBROGATION'],dataTransformerCov['subrogation'],"SUBROGATION not Matched")
    
    #Validation of CONTRACT between snowflake JSON and transformed Coverage JSON
    def test_covcontract(self):
        if dataSnwCovInput['CONTRACT'] == dataTransformerCov['contract'][0]['display']:
            print('CONTRACT Matched')
        #Prints message if the test fails for comparison
        self.assertEqual(dataSnwCovInput['CONTRACT'],dataTransformerCov['contract'][0]['display'],"CONTRACT not Matched")
    

if __name__ == '__main__':
    unittest.main()