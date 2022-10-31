terraform {
  backend "remote" {
    hostname     = "app.terraform.io"
    organization = "sgfy"

    workspaces {
      prefix = "az-fhir"
    }
  }
}
