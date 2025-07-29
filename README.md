
# 🛠️ Vendor Data Analytics Project

A complete end-to-end data pipeline and analysis project focused on vendor, inventory, and sales data using **Python**, **Pandas**, **SQLite**, and **Jupyter Notebooks**.

---

# 🎯 Project Objective

The main goal of this project is to analyze inventory, purchase, and sales data from multiple vendors and generate a clean, unified summary that enables business decision-making. This involves:

- Cleaning and preprocessing raw CSV files using pandas to handle nulls, formats, and inconsistencies  
- Ingesting the cleaned datasets into a relational SQLite database  
- Performing exploratory data analysis (EDA) on the cleaned and joined data  
- Creating a comprehensive `vendor_sales_summary` table to support business insights  
- Addressing key business problems through data aggregation, transformation, and visualization  

📊 This project helps stakeholders understand:
- **Which vendors and products are performing best**
- **Inventory discrepancies**
- **Sales gaps** or **overstocking issues**

---

## 📂 Project Structure

```
├── Data_Exploration & final_table_creation.ipynb     # EDA on cleaned data, business problem-solving, visualizations
├── Database_Creation(Ingestion).py                   # Script to create SQLite DB and ingest cleaned datasets
├── vendor_sales_summary_creation.py                  # Script to create final summary table before visualization
├── /data                                             
│   └── (Raw CSVs → Cleaned using pandas before ingestion)
├── /db                                               # SQLite database generated from cleaned data
├── /logs                                             # Log files recording ingestion status and errors
```

---

## 📊 Vendor_Data_Relationship Diagram

<img width="3368" height="2604" alt="Vendor Data Relationship Diagram" src="https://github.com/user-attachments/assets/7ddcc20d-ff8b-4898-9494-12faa432a44b" />

### 📌 Note:
Out of the five available datasets, **four datasets** were utilized for analysis:

- `sales_info.csv`  
- `vendor_invoice.csv`  
- `purchase_prices.csv`  
- `purchase_details.csv`  

These datasets were integrated to analyze both **sales** and **purchases** in depth. By connecting the related tables, a consolidated summary table named **`vendor_sales_summary`** was created to better understand various business problems.

The analysis also supports insights into **inventory-related issues**, such as:
- Unsold stock
- Purchasing inefficiencies
- Sales gaps

The key common columns used to join these datasets were:
- `Brand`  
- `VendorNumber`  
- `PONumber`  

These were selected specifically to analyze **vendor performance** across multiple business dimensions.

---

## 📌 Key Business Problems Solved

This project answers several key business questions, including:

1. **Top-Selling Vendors & Brands**  
   Identify which vendors and product brands generate the highest total sales.

2. **Unsold Capital Analysis**  
   Determine how much inventory was purchased but not sold, tying up capital and storage space.

3. **Volume Sold Analysis**  
   Understand product volume trends by converting product sizes and aggregating total liters sold.

4. **Price Margin Insights**  
   Compare purchase prices and actual selling prices to analyze vendor profitability and pricing strategies.

5. **Sales vs Purchase Contribution**  
   Quantify vendor-wise contribution in both purchases and sales using percentage metrics.

6. **Cost Structure Understanding**  
   Measure the impact of excise tax and freight cost on total cost and profitability by vendor.

7. **Visual KPIs for Stakeholders**  
   Present insights using donut charts and data summaries for stakeholder visibility.

---

## 🧾 Why `vendor_sales_summary` Was Created

The `vendor_sales_summary` table is the **final analytical output table**, created by joining and aggregating data from:

- Vendor invoice details  
- Purchase details  
- Sales information  
- Pricing files  
- Inventory files  

It consolidates **vendor-wise**, **brand-wise**, and **product-level** information such as:

- Total Purchase Quantity & Purchase Dollars  
- Total Sales Quantity, Sales Price, and Revenue  
- Excise Tax and Freight Costs  
- Actual Selling Price vs Purchase Price  
- Product Volume & Size in mL  

This table serves as a **central dataset** to power:
- KPI dashboards  
- Retail performance reports  
- Data visualizations for business stakeholders  

---

## 📁 Datasets Used

> **Note:** Place all raw CSV files inside the `/data` folder.

- `begin_inventory.csv`  
- `end_inventory.csv`  
- `purchase_details.csv`  
- `purchase_prices.csv`  
- `sales_info.csv`  
- `vendor_invoice.csv`

---
