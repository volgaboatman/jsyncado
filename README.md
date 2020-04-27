# Setup instructions

## Configure your local environment

Before you begin, you must have the following:

- [Azure Functions Core Tools](https://docs.microsoft.com/ru-ru/azure/azure-functions/functions-run-local#v2) version 3.x.

- [The Azure CLI](https://docs.microsoft.com/ru-ru/cli/azure/install-azure-cli?view=azure-cli-latest) version 2.0.76 or later.

Prerequisite check

- In a terminal or command window, run func --version to check that the Azure Functions Core Tools are version 2.7.1846 or later.

- Run az --version to check that the Azure CLI version is 2.0.76 or later.

- Run az login to sign in to Azure and verify an active subscription.

## Create Personal Access Token for access to Azure DevOps

[How to genarate PAT](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=preview-page)

## Edit azure.cmd

Edit azure.cmd and set variables

```
set RESOURCE_GROUP=adointegration_test
set FUNC_APP_NAME=jsyncado
set FUNC_APP_STORAGE=jsyncado
set LOCATION=northeurope

set ADO_URL=https://<your company>.visualstudio.com/
set ADO_PROJECT=<yor project>
set ADO_PAT=<PAT for azure devops>
```

## Run azure.cmd

Run azure.cmd. This script creates a resource group and all necessary resources inside. A successful result should look like this

```
... many lines ...
Uploading built content /home/site/deployments/functionappartifact.squashfs for linux consumption function app...
Resetting all workers for jsyncado.azurewebsites.net
Deployment successful.
Remote build succeeded!
Syncing triggers...
Functions in jsyncado:
    Receiver - [httpTrigger]
        Invoke url: https://jsyncado.azurewebsites.net/api/receiver?code=GuXoMRhXwKNbVTeaXJavRbCMqwt8S2REq6drz5fGMHWtGcWiGvlXuQ==

    logger - [httpTrigger]
        Invoke url: https://jsyncado.azurewebsites.net/api/logger?code=PXDjxdCnciZ05FiRT7HuEXiREDg8yGoMgUPEyKz3ziYGDfFG8UmKfQ==

    sender_ado - [httpTrigger]
        Invoke url: https://jsyncado.azurewebsites.net/api/sender_ado?code=/bw6jfzz2W4XRl5ZHP7ff3CzFqfmt5ywnLwjZVztzgflqKpb1NZWig==
```

Save invoke url for Receiver and sender_ado.

## Configure Jira

Open Jira project settings and set webhook to: "<receiver invoke url>&user_id=1&profile_id=3"

## Consfigure write back

Send sender_ado url to me to configure our services.

## Check together that all works fine

Do a conference to check that all works fine!
