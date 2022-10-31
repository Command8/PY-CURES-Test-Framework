from fileinput import filename
import json

fileName = ''   # Variable for Input JSON file
fhirResource = '' # variable for Resourcefile
fhirResourceType = '' # variable for ResourceType

#Function for passing Input JSON as parameter
def getResourceFile (fileName):
    with open(fileName,'r') as (fhirResourceFile):
        fhirResource = json.load(fhirResourceFile)       
        values = (fhirResource)
        return values

#Function for passing Input JSON, field value as parameters
def getResourceType (fileName,fhirResourceType):
    with open((fileName),'r') as (fhirResourceFile):
        fhirResource = json.load(fhirResourceFile)       
        
        fhirResourceType = fhirResource['resourceType']
        print (fhirResourceType)
        values = (fhirResource,fhirResourceType)
        return values       