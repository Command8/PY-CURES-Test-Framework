#------------------------------------------------------------------------------------------------------------
#  RESOURCE GROUP PERMISSIONS
#------------------------------------------------------------------------------------------------------------

data "azuread_user" "owners" {
  for_each            = var.rg_owners != null ? toset(var.rg_owners) : toset([])
  user_principal_name = each.key
}

data "azuread_user" "contributors" {
  for_each            = var.rg_contributors != null ? toset(var.rg_contributors) : toset([])
  user_principal_name = each.key
}

data "azuread_user" "readers" {
  for_each            = var.rg_readers != null ? toset(var.rg_readers) : toset([])
  user_principal_name = each.key
}

# Get other resource groups that need permissions set 
data "azurerm_resource_group" "default_rg" {
  name = "DefaultResourceGroup-CUS"
}

data "azurerm_resource_group" "aks_rg" {
  name = var.aks_rg
}

resource "azurerm_role_assignment" "owners" {
  for_each             = var.rg_owners != null ? toset(var.rg_owners) : toset([])
  scope                = module.resource_group.id
  role_definition_name = "Owner"
  principal_id         = data.azuread_user.owners[each.key].id

  depends_on = [
    data.azuread_user.owners
  ]
}

# Permissions for default resource group (DefaultResourceGroup-CUS)
resource "azurerm_role_assignment" "owners_default_rg" {
  for_each             = var.rg_owners != null ? toset(var.rg_owners) : toset([])
  scope                = data.azurerm_resource_group.default_rg.id
  role_definition_name = "Owner"
  principal_id         = data.azuread_user.owners[each.key].id

  depends_on = [
    data.azuread_user.owners
  ]
}

# Permissions for auto-generated AKS resource group
resource "azurerm_role_assignment" "owners_aks_rg" {
  for_each             = var.rg_owners != null ? toset(var.rg_owners) : toset([])
  scope                = data.azurerm_resource_group.aks_rg.id
  role_definition_name = "Owner"
  principal_id         = data.azuread_user.owners[each.key].id

  depends_on = [
    data.azuread_user.owners
  ]
}

resource "azurerm_role_assignment" "contributors" {
  for_each             = var.rg_contributors != null ? toset(var.rg_contributors) : toset([])
  scope                = module.resource_group.id
  role_definition_name = "Contributor"
  principal_id         = data.azuread_user.contributors[each.key].id

  depends_on = [
    data.azuread_user.contributors
  ]
}

resource "azurerm_role_assignment" "readers" {
  for_each             = var.rg_readers != null ? toset(var.rg_readers) : toset([])
  scope                = module.resource_group.id
  role_definition_name = "Reader"
  principal_id         = data.azuread_user.readers[each.key].id

  depends_on = [
    data.azuread_user.readers
  ]
}

resource "azurerm_role_assignment" "key_vault_contributors" {
  for_each             = var.rg_owners != null ? toset(var.rg_owners) : toset([])
  scope                = module.resource_group.id
  role_definition_name = "Key Vault Contributor"
  principal_id         = data.azuread_user.owners[each.key].id

  depends_on = [
    data.azuread_user.owners
  ]
}
