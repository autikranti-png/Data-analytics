# Data Cleaning & Reporting Automation

## 📌 Project Overview
This project demonstrates an automated workflow for cleaning, validating, analyzing, and reporting sales data. The workflow uses Python and Pandas for preprocessing and visualization, with the cleaned dataset ready for Power BI reporting.

## 🎯 Objectives
- Handle missing values
- Remove duplicate records
- Standardize inconsistent text and dates
- Correct invalid numeric values
- Validate data quality
- Calculate business KPIs
- Generate automated visual summaries
- Prepare cleaned data for Power BI

## 🛠️ Tools & Technologies
- Python 3
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Power BI

## 📂 Project Structure
```text
Data_Cleaning_Reporting_Automation/
├── data/
│   ├── raw_sales_data.csv
│   └── cleaned_sales_data.csv
├── notebooks/
│   └── Data_Cleaning_Reporting_Automation.ipynb
├── src/
│   └── data_cleaning_automation.py
├── charts/
│   ├── monthly_sales_trend.png
│   ├── sales_by_category.png
│   ├── profit_by_region.png
│   └── top_10_products.png
├── reports/
└── README.md
```

## 🔄 Workflow
```text
Raw Dataset
   ↓
Data Profiling
   ↓
Missing Value Handling
   ↓
Duplicate Removal
   ↓
Data Type Correction
   ↓
Text Standardization
   ↓
Invalid Value Correction
   ↓
Data Validation
   ↓
KPI Calculation
   ↓
Charts & Visual Reporting
   ↓
Power BI Dashboard
```

## 🧹 Data Cleaning Performed
1. Converted Order_Date to datetime.
2. Converted Quantity, Sales and Profit to numeric types.
3. Filled missing customer names.
4. Standardized region names using strip/title.
5. Replaced invalid/non-positive quantities with a valid median.
6. Replaced negative/missing Sales and Profit values using category medians and overall medians.
7. Removed duplicate rows.
8. Validated the final dataset for missing values and invalid records.

## 📊 Main KPIs
- Total Sales
- Total Profit
- Total Orders
- Total Quantity
- Average Order Value

## 📈 Visualizations
- Monthly Sales Trend
- Sales by Category
- Profit by Region
- Top 10 Products by Sales

## 📊 Power BI Dashboard
Import `data/cleaned_sales_data.csv` into Power BI and create:
- KPI cards for Sales, Profit, Orders, Quantity and AOV
- Monthly Sales line chart
- Category Sales bar chart
- Region Profit chart
- Top Products chart
- Slicers for Date, Region and Category

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install pandas numpy matplotlib jupyter
```

### 2. Open the project
```bash
cd Data_Cleaning_Reporting_Automation
```

### 3. Run the automation script
```bash
python src/data_cleaning_automation.py
```

### 4. Run the notebook
```bash
jupyter notebook
```
Open:
`notebooks/Data_Cleaning_Reporting_Automation.ipynb`

## 📌 Dataset Summary
- Raw records: 10,120
- Cleaned records: 10,048
- Duplicate records removed: 72
- Missing values after cleaning: 0
- Invalid quantities after cleaning: 0
- Negative sales after cleaning: 0

## 📄 Expected Outcome
The project provides an end-to-end example of data preprocessing, automation and reporting efficiency. It converts inconsistent raw data into a clean, analysis-ready dataset and produces business-ready visual summaries.

## 👩‍💻 Author
**Kranti Auti**

## ⭐ Project Status
Completed — ready for academic submission and Power BI dashboard development.
