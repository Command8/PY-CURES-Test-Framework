from pickle import FALSE
import unittest
import json

#Procedure to import file from different folder using sys, path, append
import sys
sys.path.append(".")
from Read_JSON import prdataTransformer,dataPracRoleInput


class TestTransform (unittest.TestCase):  
    
 #Validation of PractitionerRole - PROVIDER_ROLE_ID value between input json and transformed PractitionerRole JSON    
    def test_providerroleid(self):
        if dataPracRoleInput['PROVIDER_ROLE_ID'] == prdataTransformer['identifier'][0]['value']:
            print(dataPracRoleInput['PROVIDER_ROLE_ID'])
        self.assertEqual(dataPracRoleInput['PROVIDER_ROLE_ID'],prdataTransformer['identifier'][0]['value'],"PROVIDER_ROLE_ID not present in liquid template") 

#Validation of PractitionerRole - PROVIDER_ACTIVE value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdactv(self):
        if dataPracRoleInput['PROVIDER_ACTIVE'] == prdataTransformer['active']:
            print(dataPracRoleInput['PROVIDER_ACTIVE'])
        self.assertEqual(dataPracRoleInput['PROVIDER_ACTIVE'],prdataTransformer['active'],"PROVIDER_ACTIVE not present in liquid template") 

#Validation of PractitionerRole - PROVIDER_ACTIVE_START value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdactvstr(self):
        if dataPracRoleInput['PROVIDER_ACTIVE_START'] == prdataTransformer['period'][0]['start']:
            print(dataPracRoleInput['PROVIDER_ACTIVE_START'])
        self.assertEqual(dataPracRoleInput['PROVIDER_ACTIVE_START'],prdataTransformer['period'][0]['start'],"PROVIDER_ACTIVE_START not present in liquid template") 

#Validation of PractitionerRole - PROVIDER_ACTIVE_END value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdactvend(self):
        if dataPracRoleInput['PROVIDER_ACTIVE_END'] == prdataTransformer['period'][0]['start']:
            print(dataPracRoleInput['PROVIDER_ACTIVE_START'])
        self.assertEqual(dataPracRoleInput['PROVIDER_ACTIVE_START'],prdataTransformer['period'][0]['start'],"PROVIDER_ACTIVE not present in liquid template") 

#Validation of PractitionerRole - PRACTITIONER value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdprctdis(self):
        if dataPracRoleInput['PRACTITIONER'] == print(prdataTransformer['practitioner'][0]['display']) :
            print(dataPracRoleInput['PRACTITIONER'])
        self.assertEqual(dataPracRoleInput['PRACTITIONER'], prdataTransformer['practitioner'][0]['display'] ,"PRACTITIONER not present in liquid template") 

#Validation of PractitionerRole - PROVIDER_ORGANIZATION value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdorg(self):
        if dataPracRoleInput['PROVIDER_ORGANIZATION'] == print(prdataTransformer['organization']['reference']) :
            print(dataPracRoleInput['PROVIDER_ORGANIZATION'])
        self.assertEqual(dataPracRoleInput['PROVIDER_ORGANIZATION'], prdataTransformer['organization']['reference'].split('/')[1].strip() ,"PROVIDER_ORGANIZATION not present in liquid template") 

#Validation of PractitionerRole - PROVIDER_ROLE_CODE value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdrlcode(self):
        if dataPracRoleInput['PROVIDER_ROLE_CODE'] == print(prdataTransformer['code'][0]['coding'][0]['code']) :
            print(dataPracRoleInput['PROVIDER_ROLE_CODE'])
        self.assertEqual(dataPracRoleInput['PROVIDER_ROLE_CODE'], prdataTransformer['code'][0]['coding'][0]['code'],"PROVIDER_ROLE_CODE not present in liquid template") 

#Validation of PractitionerRole - PROVIDER_ROLE_CODE_DESC value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdrlcodedesc(self):
        if dataPracRoleInput['PROVIDER_ROLE_CODE_DESC'] == print(prdataTransformer['code'][0]['text']) :
            print(dataPracRoleInput['PROVIDER_ROLE_CODE_DESC'])
        self.assertEqual(dataPracRoleInput['PROVIDER_ROLE_CODE_DESC'], prdataTransformer['code'][0]['text'],"PROVIDER_ROLE_CODE_DESC not present in liquid template") 

#Validation of PractitionerRole - PROVIDER_SPECIALITY_CODE value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdspcltycd(self):
        if dataPracRoleInput['PROVIDER_SPECIALITY_CODE'] == print(prdataTransformer['specialty'][0]['coding'][0]['code']) :
            print(dataPracRoleInput['PROVIDER_SPECIALITY_CODE'])
        self.assertEqual(dataPracRoleInput['PROVIDER_SPECIALITY_CODE'], prdataTransformer['specialty'][0]['coding'][0]['code'],"PROVIDER_SPECIALITY_CODE not present in liquid template") 

#Validation of PractitionerRole - PROVIDER_SPECIALITY_DESC value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdspcltycddesc(self):
        if dataPracRoleInput['PROVIDER_SPECIALITY_DESC'] == print(prdataTransformer['specialty'][0]['text']) :
            print(dataPracRoleInput['PROVIDER_SPECIALITY_DESC'])
        self.assertEqual(dataPracRoleInput['PROVIDER_SPECIALITY_DESC'], prdataTransformer['specialty'][0]['text'],"PROVIDER_SPECIALITY_DESC not present in liquid template") 

#Validation of PractitionerRole - PROVIDER_LOCATION value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdloc1(self):
        if dataPracRoleInput['PROVIDER_LOCATION'] == print(prdataTransformer['location']['reference']) :
            print(dataPracRoleInput['PROVIDER_LOCATION'])
        self.assertEqual(dataPracRoleInput['PROVIDER_LOCATION'], prdataTransformer['location']['reference'].split('/')[1].strip(),"PROVIDER_LOCATION not present in liquid template") 

#Validation of PractitionerRole - PROVIDER_LOCATION value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdloc2(self):
        if dataPracRoleInput['PROVIDER_LOCATION'] == print(prdataTransformer['location']['display']) :
            print(dataPracRoleInput['PROVIDER_LOCATION'])
        self.assertEqual(dataPracRoleInput['PROVIDER_LOCATION'],prdataTransformer['location']['display'],"PROVIDER_LOCATION not present in liquid template") 

#Validation of PractitionerRole - PROVIDER_HEALTHCARE_SERVICE value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdhcs(self):
        if dataPracRoleInput['PROVIDER_HEALTHCARE_SERVICE'] == print(prdataTransformer['healthcareService']['reference']) :
            print(dataPracRoleInput['PROVIDER_HEALTHCARE_SERVICE'])
        self.assertEqual(dataPracRoleInput['PROVIDER_HEALTHCARE_SERVICE'],prdataTransformer['healthcareService']['reference'].split('/')[1].strip(),"PROVIDER_HEALTHCARE_SERVICE not present in liquid template") 

#Validation of PractitionerRole - PROVIDER_HEALTHCARE_SERVICE display value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdhcsdsply(self):
        if dataPracRoleInput['PROVIDER_HEALTHCARE_SERVICE'] == print(prdataTransformer['healthcareService']['display']) :
            print(dataPracRoleInput['PROVIDER_HEALTHCARE_SERVICE'])
        self.assertEqual(dataPracRoleInput['PROVIDER_HEALTHCARE_SERVICE'],prdataTransformer['healthcareService']['display'],"PROVIDER_HEALTHCARE_SERVICE Display not present in liquid template") 


#Validation of PractitionerRole - PROVIDER_PHONEPRIMARY  value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdph1(self):
        if dataPracRoleInput['PROVIDER_PHONEPRIMARY'] == print(prdataTransformer['telecom'][0]['value']) :
            print(dataPracRoleInput['PROVIDER_PHONEPRIMARY'])
        self.assertEqual(dataPracRoleInput['PROVIDER_PHONEPRIMARY'],prdataTransformer['telecom'][0]['value'],"PROVIDER_PHONEPRIMARY not present in liquid template") 

#Validation of PractitionerRole - PROVIDER_PHONESECONDARY  value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdph2(self):
        if dataPracRoleInput['PROVIDER_PHONESECONDARY'] == print(prdataTransformer['telecom'][1]['value']) :
            print(dataPracRoleInput['PROVIDER_PHONESECONDARY'])
        self.assertEqual(dataPracRoleInput['PROVIDER_PHONESECONDARY'],prdataTransformer['telecom'][1]['value'],"PROVIDER_PHONESECONDARY not present in liquid template") 

#Validation of PractitionerRole - PROVIDER_CONTACT  value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdph3(self):
        if dataPracRoleInput['PROVIDER_CONTACT'] == print(prdataTransformer['telecom'][2]['value']) :
            print(dataPracRoleInput['PROVIDER_CONTACT'])
        self.assertEqual(dataPracRoleInput['PROVIDER_CONTACT'],prdataTransformer['telecom'][2]['value'],"PROVIDER_CONTACT not present in liquid template") 

#Validation of PractitionerRole - PROVIDER_FAX  value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdph4(self):
        if dataPracRoleInput['PROVIDER_FAX'] == print(prdataTransformer['telecom'][3]['value']) :
            print(dataPracRoleInput['PROVIDER_FAX'])
        self.assertEqual(dataPracRoleInput['PROVIDER_FAX'],prdataTransformer['telecom'][3]['value'],"PROVIDER_FAX not present in liquid template") 

#Validation of PractitionerRole - PROVIDER_AVAILABLE_STARTTIME  value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdavlstr(self):
        if dataPracRoleInput['PROVIDER_AVAILABLE_STARTTIME'] == print(prdataTransformer['availableTime'][0]['availableStartTime']) :
            print(dataPracRoleInput['PROVIDER_AVAILABLE_STARTTIME'])
        self.assertEqual(dataPracRoleInput['PROVIDER_AVAILABLE_STARTTIME'],prdataTransformer['availableTime'][0]['availableStartTime'],"PROVIDER_AVAILABLE_STARTTIME not present in liquid template") 

#Validation of PractitionerRole - PROVIDER_AVAILABLE_ENDTIME  value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdavlend(self):
        if dataPracRoleInput['PROVIDER_AVAILABLE_ENDTIME'] == print(prdataTransformer['availableTime'][0]['availableStartTime']) :
            print(dataPracRoleInput['PROVIDER_AVAILABLE_ENDTIME'])
        self.assertEqual(dataPracRoleInput['PROVIDER_AVAILABLE_ENDTIME'],prdataTransformer['availableTime'][0]['availableStartTime'],"PROVIDER_AVAILABLE_ENDTIME not present in liquid template") 

#Validation of PractitionerRole - PROVIDER_SERVICE_NOT_AVAILABLE_FROM  value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdavlend(self):
        if dataPracRoleInput['PROVIDER_SERVICE_NOT_AVAILABLE_FROM'] == print(prdataTransformer['notAvailable'][0]['during']['start']) :
            print(dataPracRoleInput['PROVIDER_SERVICE_NOT_AVAILABLE_FROM'])
        self.assertEqual(dataPracRoleInput['PROVIDER_SERVICE_NOT_AVAILABLE_FROM'],prdataTransformer['notAvailable'][0]['during']['start'],"PROVIDER_SERVICE_NOT_AVAILABLE_FROM not present in liquid template") 

#Validation of PractitionerRole - PROVIDER_SERVICE_NOT_AVAILABLE_TO  value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdavlend(self):
        if dataPracRoleInput['PROVIDER_SERVICE_NOT_AVAILABLE_TO'] == print(prdataTransformer['notAvailable'][0]['during']['end']) :
            print(dataPracRoleInput['PROVIDER_SERVICE_NOT_AVAILABLE_TO'])
        self.assertEqual(dataPracRoleInput['PROVIDER_SERVICE_NOT_AVAILABLE_TO'],prdataTransformer['notAvailable'][0]['during']['end'],"PROVIDER_SERVICE_NOT_AVAILABLE_TO not present in liquid template") 

#Validation of PractitionerRole - AVAILABILIY_EXCEPTION  value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdavlexcpt(self):
        if dataPracRoleInput['AVAILABILIY_EXCEPTION'] == print(prdataTransformer['availabilityExceptions']) :
            print(dataPracRoleInput['AVAILABILIY_EXCEPTION'])
        self.assertEqual(dataPracRoleInput['AVAILABILIY_EXCEPTION'],prdataTransformer['availabilityExceptions'],"AVAILABILIY_EXCEPTION not present in liquid template") 

#Validation of PractitionerRole - ENDPOINT_ACCESS reference  value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdavlend1(self):
        if dataPracRoleInput['ENDPOINT_ACCESS'] == print(prdataTransformer['endpoint'][0]['reference']) :
            print(dataPracRoleInput['ENDPOINT_ACCESS'])
        self.assertEqual(dataPracRoleInput['ENDPOINT_ACCESS'],prdataTransformer['endpoint'][0]['reference'].split('/')[1].strip(),"ENDPOINT_ACCESS reference not present in liquid template") 

#Validation of PractitionerRole - ENDPOINT_ACCESS display  value between input json and transformed PractitionerRole JSON    
    def test_providerroleprvdavlend2(self):
        if dataPracRoleInput['ENDPOINT_ACCESS'] == print(prdataTransformer['endpoint'][0]['display']) :
            print(dataPracRoleInput['ENDPOINT_ACCESS'])
        self.assertEqual(dataPracRoleInput['ENDPOINT_ACCESS'],prdataTransformer['endpoint'][0]['display'],"ENDPOINT_ACCESS reference not present in liquid template") 



if __name__ == '__main__':
    unittest.main()