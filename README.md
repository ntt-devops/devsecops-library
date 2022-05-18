# devsecops-library

Welcome to Gravitee.io UI Components

Overview
This library shares workflows, secrets and runners which can be reused in all the projects.  

Features
1.) Sonarcloud and Trivy container scan workflows are available to reuse. This will avoid duplication and make your workflow easier to maintain

User guide
To call the Trivy container scan workflow in your project, just add new job in your workflow:

jobs:
  call-workflow:
    uses: ntt-devops/devsecops-library/.github/workflows/trivy-container-scan.yml@main
    with:
      imagename: <<image name>>
    secrets:
      awskeyid: ${{ secrets.awskeyid }}
      awskeysecret: ${{ secrets.awskeysecret }}    

Reference : https://docs.github.com/en/actions/using-workflows/sharing-workflows-secrets-and-runners-with-your-organization
