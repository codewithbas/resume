param name string
param location string = resourceGroup().location
param customDomains array

param skuName string = 'Free'
param skuTier string = 'Free'

param repositoryUrl string

@secure()
param repositoryToken string

param branch string
param skipActionGeneration bool

resource staticWebApp 'Microsoft.Web/staticSites@2021-02-01' = {
  name: name
  location: location
  sku: {
    name: skuName
    tier: skuTier
  }
  properties: {
    repositoryUrl: repositoryUrl
    repositoryToken: repositoryToken
    branch: branch
    buildProperties: {
      skipGithubActionWorkflowGeneration: skipActionGeneration
    }
  }
  resource domains 'customDomains' = [for domain in customDomains: {
    name: domain
    properties: {
      validationMethod: 'dns-txt-token'
    }
  }]
}

// output deployment_token string = listSecrets(staticWebApp.id, staticWebApp.apiVersion).properties.apiKey
