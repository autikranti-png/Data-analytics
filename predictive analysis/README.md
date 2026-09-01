# 📊 Predictive Analytics Using Historical Data

> A machine learning project that analyzes historical sales data, identifies trends and seasonal patterns, evaluates predictive models, and forecasts future sales.

---

## 📌 Project Overview

**Predictive Analytics Using Historical Data** is an end-to-end data science and machine learning project developed to demonstrate how historical business data can be transformed into meaningful insights and future predictions.

The project uses a dataset containing **10,000 historical daily sales records**. The data is cleaned, explored, transformed, and used to build predictive regression models.

Two machine learning approaches are implemented:

- **Linear Regression**
- **Random Forest Regression**

The models are evaluated using standard regression metrics such as **MAE, MSE, RMSE, and R² Score**.

Finally, the selected model is used to generate a **90-day future sales forecast**.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Analyze historical sales data.
- Perform data cleaning and preprocessing.
- Handle missing values and duplicate records.
- Explore sales trends and patterns.
- Analyze monthly and yearly sales behavior.
- Identify seasonal patterns.
- Perform feature engineering.
- Build machine learning regression models.
- Evaluate and compare model performance.
- Generate future sales predictions.
- Visualize historical, predicted, and forecasted sales.
- Save the trained model using Pickle.
- Provide business-oriented insights from the analysis.

---

## 🧩 Problem Statement

Businesses collect large amounts of sales data every day. However, historical data becomes significantly more valuable when it can be used to predict future demand.

The problem addressed in this project is:

> **How can historical sales data be analyzed and used to build a predictive model capable of forecasting future sales?**

The solution involves data preprocessing, exploratory data analysis, feature engineering, machine learning, model evaluation, and future forecasting.

---

# 🔄 Project Workflow

```text
                 ┌─────────────────────┐
                 │ Historical Sales    │
                 │ Data - 10,000 Rows  │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │ Data Loading        │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │ Data Cleaning       │
                 │ & Preprocessing     │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │ Exploratory Data    │
                 │ Analysis            │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │ Feature Engineering │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │ Train-Test Split    │
                 │     80% / 20%       │
                 └──────────┬──────────┘
                            ↓
              ┌─────────────┴─────────────┐
              ↓                           ↓
     ┌─────────────────┐        ┌──────────────────┐
     │ Linear          │        │ Random Forest    │
     │ Regression      │        │ Regression       │
     └────────┬────────┘        └─────────┬────────┘
              ↓                           ↓
              └─────────────┬─────────────┘
                            ↓
                 ┌─────────────────────┐
                 │ Model Evaluation    │
                 │ MAE / MSE / RMSE/R²│
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │ Model Comparison    │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │ Future Sales        │
                 │ Forecast - 90 Days  │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │ Insights &          │
                 │ Visualization       │
                 └─────────────────────┘
