# DATA CLEANING & REPORTING AUTOMATION
## Automated Sales Data Cleaning, Analysis and Reporting

### 1. Introduction
Data quality is critical for reliable business analysis. Real-world datasets commonly contain missing values, duplicate records, inconsistent text, invalid numerical values and inconsistent date formats. This project develops an automated workflow to clean such data and transform it into an analysis-ready format.

### 2. Problem Statement
Manual data cleaning and reporting are time-consuming and error-prone. The objective is to automate preprocessing and generate repeatable reports and visual summaries from a raw sales dataset.

### 3. Objectives
- Identify data-quality issues.
- Handle missing values.
- Remove duplicate records.
- Standardize inconsistent values.
- Correct data types and invalid values.
- Validate cleaned data.
- Calculate business KPIs.
- Generate charts automatically.
- Prepare data for Power BI reporting.

### 4. Dataset
The project uses a synthetic sales dataset containing 10,000 original records plus intentionally introduced quality issues and duplicate rows.

Main columns:
- Order_ID
- Order_Date
- Customer_Name
- Product
- Category
- Quantity
- Sales
- Profit
- Region

### 5. Tools and Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Power BI

### 6. Data Quality Issues
The raw dataset contains:
- Missing Customer_Name, Quantity, Region and Sales values.
- Duplicate records.
- Inconsistent region capitalization and whitespace.
- Multiple date formats.
- Zero and negative quantities.
- Negative sales anomalies.

### 7. Data Cleaning Methodology
**Step 1 — Data loading:** Read the raw CSV using Pandas.

**Step 2 — Profiling:** Check dimensions, data types, missing values, duplicate rows and descriptive statistics.

**Step 3 — Data type conversion:** Convert dates and numerical columns into appropriate formats.

**Step 4 — Missing values:** Replace missing customer names and regions with suitable labels. Numeric missing values are handled using valid medians/category-level medians.

**Step 5 — Standardization:** Normalize region names using trimming and title casing.

**Step 6 — Invalid values:** Replace non-positive quantities and negative sales/profit anomalies.

**Step 7 — Duplicate removal:** Remove repeated records.

**Step 8 — Validation:** Confirm there are no remaining missing values, duplicates or invalid numerical values.

### 8. Automation
The cleaning logic is implemented as a reusable `clean_data()` function. The Python script reads the raw CSV, performs the cleaning process, exports the cleaned CSV and prints an automated KPI report. This makes the process repeatable whenever a new dataset is received.

### 9. KPI Reporting
The automated report calculates:
- Total Sales: ₹413,044,735.48
- Total Profit: ₹57,515,119.49
- Total Orders: 10,000
- Total Quantity: 45,481
- Average Order Value: ₹41,304.47

### 10. Visualizations
The project generates:
1. Monthly Sales Trend
2. Sales by Category
3. Profit by Region
4. Top 10 Products by Sales

### 11. Power BI Dashboard
The cleaned dataset can be imported into Power BI. Recommended dashboard components are KPI cards, monthly sales trend, category sales, regional profit, top products and slicers for date, region and category.

### 12. Results
The workflow successfully transforms inconsistent raw data into a clean dataset suitable for analysis. The automation reduces repetitive manual preprocessing and creates consistent outputs for reporting.

### 13. Benefits
- Faster data preparation
- Reduced manual errors
- Repeatable cleaning process
- Improved data quality
- Better reporting efficiency
- Easy integration with Power BI

### 14. Future Scope
- Automated email report delivery
- Scheduled execution
- Database integration
- Cloud-based data pipeline
- Power BI Service refresh
- Advanced anomaly detection
- Machine-learning-based data-quality monitoring

### 15. Conclusion
The Data Cleaning & Reporting Automation project demonstrates an end-to-end process for transforming messy sales data into reliable business information. Python automates preprocessing and KPI generation, while Power BI can provide interactive reporting and decision-support dashboards.
