
# Azure Data Factory Incremental Load Project

This project demonstrates a complete end-to-end data integration and automation flow using Azure Data Factory (ADF). It includes:

## ✅ Key Components

- **Linked Services**
  - `MySQL_Local_OnPrem`: Connects to local MySQL server
  - `AzureSQL_HR_DataWarehouse`: Connects to Azure SQL Database

- **Datasets**
  - `MySQL_Employees_Staging`: Source dataset from MySQL
  - `AzureSQL_Employees_Prod`: Sink dataset in Azure SQL DB

- **Pipelines**
  - `Initial_Employee_DataLoad`: Full load from MySQL to Azure
  - `Incremental_Employee_DataSync`: Loads only updated data using LastModified timestamp

- **Triggers**
  - `Daily_Incremental_Trigger`: Runs every day to sync incremental changes
  - `Monthly_LastSaturday_Trigger`: Runs only on the last Saturday of every month

## 📂 Directory Structure

```
ADF-Incremental-Load-Project/
├── linkedServices/
│   ├── MySqlLinkedService.json
│   └── AzureSqlDatabase.json
├── datasets/
│   ├── MySqlEmployees.json
│   └── AzureSqlEmployees.json
├── pipelines/
│   ├── InitialLoadPipeline.json
│   └── IncrementalLoadPipeline.json
├── triggers/
│   ├── Daily_Incremental_Trigger.json
│   └── Monthly_LastSaturday_Trigger.json
└── README.md
```

## 🚀 Usage

Import these JSON files into Azure Data Factory using "Manage Hub" > "Import ARM Template" or manually recreate them based on the provided logic.

