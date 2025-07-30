import pandas as pd
from sqlalchemy import create_engine
import os
import time
import logging

os.makedirs(r"C:\Users\GURU PRAVEEN REDDY J\Projects\logs", exist_ok=True)

logging.basicConfig(
    filename=r"C:\Users\GURU PRAVEEN REDDY J\Projects\logs\get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s-%(levelname)s-%(message)s",
    filemode="a"
)

def create_vendor_summary(conn):
    Vendor_sales_summary=pd.read_sql('''
            WITH CTE_1 AS (
            SELECTimport pandas as pd
from sqlalchemy import create_engine
import os
import time
import logging

os.makedirs(r"C:\Users\GURU PRAVEEN REDDY J\Projects\logs", exist_ok=True)

logging.basicConfig(
    filename=r"C:\Users\GURU PRAVEEN REDDY J\Projects\logs\get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s-%(levelname)s-%(message)s",
    filemode="a"
)

def create_vendor_summary(conn):
    Vendor_sales_summary=pd.read_sql('''
            WITH CTE_1 AS (
            SELECT
                    p.VendorNumber,
                    p.VendorName,
                    p.Brand,
                    p.Description,
                    p.PurchasePrice,
                    pp.Price as ActualPrice,
                    pp.Volume,
                    SUM(Quantity) as TotalPurchaseQuantity,
                    SUM(Dollars) as TotalPurchaseDllars
                FROM purchase_details as p
                JOIN purchase_price_info as pp
                ON p.Brand=pp.Brand
                WHERE p.PurchasePrice>0
                GROUP BY p.VendorNumber,p.VendorName,p.Brand,p.Description,p.PurchasePrice
            ),
            
            CTE_2 AS (
                SELECT
                    VendorNO,
                    Brand,
                    AVG(SalesPrice) AS AvgSalesPrice,
                    SUM(SalesPrice) AS TotalSalesPrice,
                    SUM(SalesQuantity) AS TotalSalesQuantity,
                    SUM(SalesDollars) AS TotalSalesDollars,
                    SUM(ExciseTax) AS TotalExciseTax
                FROM sales_info
                GROUP BY VendorNO, Brand
            ),
            
            CTE_3 AS (
                SELECT 
                    VendorNumber,
                    SUM(Freight) AS TotalFreightCost
                FROM Vendor_invoice
                GROUP BY VendorNumber
            )
            
            SELECT 
                c1.VendorNumber,
                c1.VendorName,
                c1.Brand,
                c1.Description,
                c1.PurchasePrice,
                c1.ActualPrice,
                c1.Volume,
                c1.TotalPurchaseQuantity,
                c1.TotalPurchaseDllars,
                c2.TotalSalesQuantity,
                c2.TotalSalesPrice,
                c2.TotalSalesDollars,
                c2.TotalExciseTax,
                c3.TotalFreightCost,
                c2.TotalSalesDollars-c1.TotalPurchaseDllars as Gross_Profit,
                ROUND((CAST(c2.TotalSalesDollars AS FLOAT)-c1.TotalPurchaseDllars)*100/c2.TotalSalesDollars,2) AS Profit,
                ROUND(CAST(c2.TotalSalesQuantity AS FLOAT)/c1.TotalPurchaseQuantity,2) AS StockTurnOver,
                ROUND(CAST(c2.TotalSalesDollars AS FLOAT)/c1.TotalPurchaseDllars,2) AS SalesToPurchaseRatio
    
            FROM CTE_1 AS c1
            LEFT JOIN CTE_2 AS c2
                ON c1.VendorNumber = c2.VendorNO AND c1.Brand = c2.Brand
            LEFT JOIN CTE_3 AS c3
                ON c1.VendorNumber = c3.VendorNumber
            ORDER BY c1.TotalPurchaseDllars DESC;
            ''',conn)
    return Vendor_sales_summary
    
def to_clean_data(df):
    df.fillna(0,inplace=True)
    return df

def ingest_db(df,table_name,engine):
    df.to_sql(table_name,con=engine,if_exists="replace",index=False)

if __name__ == "__main__":
    conn=sqlite3.connect(r"db\inventory.db")
    logging.info("Creating Vendor Summary table")
    summary_df=create_vendor_summary(conn)
    logging.info(summary_df.head())

    logging.info("Cleaning data")
    clean_df=to_clean_data(summary_df)
    logging.info(clean_df.head())

    logging.info("Ingesting To DB")
    ingest_db(clean_df,'Vendor_sales_summary',conn)
    logging.info("completed")
    
                    p.VendorNumber,
                    p.VendorName,
                    p.Brand,
                    p.Description,
                    p.PurchasePrice,
                    pp.Price as ActualPrice,
                    pp.Volume,
                    SUM(Quantity) as TotalPurchaseQuantity,
                    SUM(Dollars) as TotalPurchaseDllars
                FROM purchase_details as p
                JOIN purchase_prices as pp
                ON p.Brand=pp.Brand
                WHERE p.PurchasePrice>0
                GROUP BY p.VendorNumber,p.VendorName,p.Brand,p.Description,p.PurchasePrice
            ),
            
            CTE_2 AS (
                SELECT
                    VendorNO,
                    Brand,
                    AVG(SalesPrice) AS AvgSalesPrice,
                    SUM(SalesPrice) AS TotalSalesPrice,
                    SUM(SalesQuantity) AS TotalSalesQuantity,
                    SUM(SalesDollars) AS TotalSalesDollars,
                    SUM(ExciseTax) AS TotalExciseTax
                FROM sales_info
                GROUP BY VendorNO, Brand
            ),
            
            CTE_3 AS (
                SELECT 
                    VendorNumber,
                    SUM(Freight) AS TotalFreightCost
                FROM Vendor_invoice
                GROUP BY VendorNumber
            )
            
            SELECT 
                c1.VendorNumber,
                c1.VendorName,
                c1.Brand,
                c1.Description,
                c1.PurchasePrice,
                c1.ActualPrice,
                c1.Volume,
                c1.TotalPurchaseQuantity,
                c1.TotalPurchaseDllars,
                c2.TotalSalesQuantity,
                c2.TotalSalesPrice,
                c2.TotalSalesDollars,
                c2.TotalExciseTax,
                c3.TotalFreightCost
            FROM CTE_1 AS c1
            LEFT JOIN CTE_2 AS c2
                ON c1.VendorNumber = c2.VendorNO AND c1.Brand = c2.Brand
            LEFT JOIN CTE_3 AS c3
                ON c1.VendorNumber = c3.VendorNumber
            ORDER BY c1.TotalPurchaseDllars DESC;
            ''',conn)
    return Vendor_sales_summary
    
def to_clean_data(df):
    df.fillna(0,inplace=True)

    df["VendorName"]=df["VendorName"].str.strip()

    df["Volume"]=df["Volume"].astype("float")

    df["Gross_Profit"]=df["TotalSalesDollars"]-df["TotalPurchaseDllars"]
    df["Profit"]=round(df["Gross_Profit"]*100/df["TotalSalesDollars"],2)
    df["StockTurnOver"]=round(df["TotalSalesQuantity"]/df["TotalPurchaseQuantity"],2)
    df["SalesTopurchaseRatio"]=round(df["TotalSalesDollars"]/df["TotalPurchaseDllars"],2)
    return df

def ingest_db(df,table_name,engine):
    df.to_sql(table_name,con=engine,if_exists="replace",index=False)

if __name__ == "__main__":
    conn=sqlite3.connect(r"db\inventory.db")
    logging.info("Creating Vendor Summary table")
    summary_df=create_vendor_summary(conn)
    logging.info(summary_df.head())

    logging.info("Cleaning data")
    clean_df=to_clean_data(summary_df)
    logging.info(clean_df.head())

    logging.info("Ingesting To DB")
    ingest_db(clean_df,'Vendor_sales_summary',conn)
    logging.info("completed")
    