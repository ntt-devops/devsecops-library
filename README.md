# Welcome to DevSecOps Library

Overview

This library shares workflows, secrets and runners which can be reused in all the projects.  

Features

1.) Sonarcloud Analysis, Checkov Terraform Scan and Trivy Container Scan workflows are available to reuse. This will avoid duplication and make your workflow easier to maintain

User guide

To call the Trivy container scan workflow in your project, just add new job in your workflow:

  trivy-scan:
  
    uses: ntt-devops/devsecops-library/.github/workflows/trivy-container-scan.yml@main
    
    needs: [job name]
    
    with:
    
      imagename: <<image name>>
      
    secrets:
    
      awskeyid: ${{ secrets.awskeyid }}
      
      awskeysecret: ${{ secrets.awskeysecret }}    
      
      
To call the Sonarcloud Analysis workflow in your project, just add new job in your workflow:   
   
   sonarcloud-analysis:
   
    uses: ntt-devops/devsecops-library/.github/workflows/sonarcloud-analysis.yml@main
    
    with:
    
      projectdir: <<project directory>>
      
    secrets:
    
      sonartoken: <<Sonar Token>>   
      

To call the Checkov Terraform Scan workflow in your project, just add new job in your workflow:   

  checkov-terraform-scan-workflow:
  
    uses: ntt-devops/devsecops-library/.github/workflows/checkov-terraform-scan.yml@main
    
    with:
    
      projectdir: << Directory Name >>
      
      softfail: << true or false >>
      

Reference : https://docs.github.com/en/actions/using-workflows/sharing-workflows-secrets-and-runners-with-your-organization
