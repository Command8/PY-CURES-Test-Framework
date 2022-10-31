provider "azurerm" {
  features {}
}

module "resource_group" {
  source = "app.terraform.io/sgfy/resource_group/azure"
  name   = "fhir"
  tags = {
    description = "Resources used by TEKSystems for FHIR integration."
    owner       = "cyclops"
    contact     = "netops@signifyhealth.com"
    system      = "na"
  }
}
