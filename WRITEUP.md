# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

_For **both** a VM or App Service solution for the CMS app:_

- _Analyze costs, scalability, availability, and workflow_
  | | VM | App Service |
  |--------------|--------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
  | **Cost** | Billing based on VM size, storage (OS, data, backups), licensing, networking, and other services | Billing based on service plan, number of instances, storage, network bandwidth, and additional services |
  | **Scalability** | Scale Sets can increase/decrease the number of virtual machines or automatically change as needed | Automatically scale (add instances) or scale up (increase capacity) based on criteria such as CPU, memory, or number of requests |
  | **Availability** | Guaranteed uptime of 99.9% when using Availability Set and up to 99.99% when using Availability Zones | Guaranteed 99.95% uptime for applications from Standard Tier and above |
  | **Deployment** | Requires manual installation of operating systems, software, and environment configuration or using tools such as ARM templates, PowerShell, or Terraform | Deploy easily using tools like Azure Portal, CLI, Visual Studio, or through CI/CD pipelines |

- _Choose the appropriate solution (VM or App Service) for deploying the app_
- _Justify your choice_

From my opinion and appropriate solution, both VM and App Service are good for our application, but I choose App Service for some reasons:

- _This is fully manage platform_
- _This is rapid deployment, support CI/CD_
- _This is simplifies deploying applications across multiple regions for geo-redundancy and disaster recovery_
- _And this is an ideal for modern application architectures, including microservices and serverless computing_

### Assess app changes that would change your decision.

_Detail how the app and any other needs would have to change for you to change your decision in the last section._

| VM                                                                                           | App Service                                                       |
| -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Control over environment like OS, software, configurations that are required for application | Modern App deployment (microservices, serverless,...) management. |
