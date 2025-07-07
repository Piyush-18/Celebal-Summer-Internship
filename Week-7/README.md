# ADF-CustomerMaster-ETL

This project implements an Azure Data Factory ETL pipeline that reads customer data from a CSV file in Azure Data Lake Storage and loads it into an Azure SQL Database.

## Components

- **Pipeline (`pl_CUST_MSTR_load`)**: Orchestrates the data movement.
- **Data Flow (`df_CUST_MSTR`)**: Contains logic to read from CSV and load to SQL.
- **Source Dataset (`DelimitedText1`)**: Points to a CSV in Azure Data Lake Storage.
- **Sink Datasets (`AzureSqlTable1`, `AzureSqlTable2`, `AzureSqlTable3`)**: Represent different destination SQL tables.

## Steps Followed

### A. Create Azure Resources
- Provisioned Azure Data Factory and Azure Data Lake.
- Uploaded `dummy.csv` to `celebald7/container`.

### B. Build Dataset with Parameters
- Added `folderPath` and `fileName` as parameters to `DelimitedText1`.
- Bound them in the Connection tab: 
  - File path: `@dataset().folderPath/@dataset().fileName`

### C. Build Data Flow
- Created `df_CUST_MSTR` with:
  - **Source**: `DelimitedText1`
  - **Sink**: `AzureSqlTable1`
- Enabled **Allow Schema Drift** in Source.
- Set sink table.

### D. Create Pipeline
- Created `pl_CUST_MSTR_load`.
- Added **Data Flow Activity** and linked to `df_CUST_MSTR`.
- Assigned values for parameters `folderPath = "celebald7/container"` and `fileName = "dummy.csv"`.

### E. Publish and Trigger
- Clicked “Publish All”.
- Debugged and tested the pipeline.

## Files

```
.
├── dummy.csv
├── pipeline
│   └── pl_CUST_MSTR_load.json
├── dataflow
│   └── df_CUST_MSTR.json
├── dataset
│   ├── DelimitedText1.json
│   ├── AzureSqlTable1.json
│   ├── AzureSqlTable2.json
│   └── AzureSqlTable3.json
└── README.md
```


