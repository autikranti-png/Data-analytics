import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

INPUT = Path("data/raw_sales_data.csv")
OUTPUT = Path("data/cleaned_sales_data.csv")
CHART_DIR = Path("charts")
CHART_DIR.mkdir(exist_ok=True)

def clean_data(df):
    df = df.copy()
    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce", dayfirst=True)
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
    df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")

    df["Customer_Name"] = df["Customer_Name"].fillna("Unknown Customer")
    df["Region"] = df["Region"].fillna("Unknown").astype(str).str.strip().str.title()

    valid_qty = df.loc[df["Quantity"] > 0, "Quantity"]
    df.loc[df["Quantity"] <= 0, "Quantity"] = np.nan
    df["Quantity"] = df["Quantity"].fillna(valid_qty.median()).round().astype(int)

    df["Sales"] = df["Sales"].mask(df["Sales"] < 0)
    df["Sales"] = df["Sales"].fillna(df.groupby("Category")["Sales"].transform("median"))
    df["Sales"] = df["Sales"].fillna(df["Sales"].median())

    df["Profit"] = df["Profit"].mask(df["Profit"] < 0)
    df["Profit"] = df["Profit"].fillna(df.groupby("Category")["Profit"].transform("median"))
    df["Profit"] = df["Profit"].fillna(df["Profit"].median())

    df = df.drop_duplicates()
    df["Order_Date"] = df["Order_Date"].fillna(df["Order_Date"].median())
    df["Sales"] = df["Sales"].round(2)
    df["Profit"] = df["Profit"].round(2)
    return df.sort_values("Order_Date").reset_index(drop=True)

def generate_report(df):
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_orders = df["Order_ID"].nunique()
    total_quantity = df["Quantity"].sum()
    aov = total_sales / total_orders

    print("\nAUTOMATED SALES REPORT")
    print("-" * 30)
    print(f"Total Sales       : ₹{total_sales:,.2f}")
    print(f"Total Profit      : ₹{total_profit:,.2f}")
    print(f"Total Orders      : {total_orders:,}")
    print(f"Total Quantity    : {total_quantity:,}")
    print(f"Average Order     : ₹{aov:,.2f}")
    print(f"Rows in dataset   : {len(df):,}")

if __name__ == "__main__":
    raw = pd.read_csv(INPUT)
    cleaned = clean_data(raw)
    cleaned.to_csv(OUTPUT, index=False)
    generate_report(cleaned)
    print(f"\nCleaned file saved to: {OUTPUT}")
