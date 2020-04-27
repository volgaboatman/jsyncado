set RESOURCE_GROUP=adointegration_test
set FUNC_APP_NAME=jsyncado
set FUNC_APP_STORAGE=jsyncado
set LOCATION=northeurope

set ADO_URL=https://dev.azure.com/KonigLabsCompany
set ADO_PROJECT=ADO_integration_test
set ADO_PAT=<YOUR_PAT>

call az group create --name %RESOURCE_GROUP% --location %LOCATION%

call az storage account create --name %FUNC_APP_STORAGE% --location %LOCATION% --resource-group %RESOURCE_GROUP% --sku Standard_LRS
call az functionapp create --resource-group %RESOURCE_GROUP% --os-type Linux --consumption-plan-location %LOCATION% --runtime python --runtime-version 3.7 --functions-version 3 --name %FUNC_APP_NAME% --storage-account %FUNC_APP_STORAGE%

call az functionapp config appsettings set --name %FUNC_APP_NAME% --resource-group %RESOURCE_GROUP% --settings ADO_CREDENTIAL=%ADO_PAT%
call az functionapp config appsettings set --name %FUNC_APP_NAME% --resource-group %RESOURCE_GROUP% --settings ADO_PROJECT_NAME=%ADO_PROJECT%
call az functionapp config appsettings set --name %FUNC_APP_NAME% --resource-group %RESOURCE_GROUP% --settings ADO_BASE_URL=%ADO_URL

call func azure functionapp publish %FUNC_APP_NAME%
