import sqlite3
import pandas as pd
import logging
from ingestion_db import ingest_db

logging.basicConfig(
    filename = "logs/get_vendor_summary.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    filemode = "a"
)

def create_vendor_summary(conn):
    '''this function will merge the different tables to get the overall vendor summary and adding new columns in the resultant data'''
    vendor_sales_summary = pd.read_sql_query("""WITH FreightSummary AS 
        (SELECT 
                VendorNumber,
                SUM(Freight) as FreightCost
                FROM vendor_invoice
                GROUP BY VendorNumber),
                                         
        PurchaseSummary AS
                (SELECT
                        p.VendorNumber,
                        p.VendorName,
                        p.Brand,
                        p.Description,                                 
                        p.PurchasePrice,
                        pp.Volume,
                        pp.Price as ActualPrice,
                        SUM(p.Quantity) as TotalPurchaseQuantity,
                        SUM(p.Dollars) as TotalPurchaseDollars
                FROM purchases p
                JOIN purchase_prices pp
                ON p.Brand = pp.Brand
                        WHERE p.PurchasePrice > 0
                        GROUP BY p.VendorNumber, p.VendorName, p.Brand, p.Description, p.PurchasePrice, pp.Volume),

        SalesSummary AS
                (SELECT
                        VendorNo,
                        Brand,
                        SUM(SalesDollars) as TotalSalesDollars,
                        SUM(SalesPrice) as TotalSalesPrice,
                        SUM(SalesQuantity) as TotalSalesQuantity,
                        SUM(ExciseTax) as TotalExciseTax
                FROM sales
                GROUP BY VendorNo, Brand)

        SELECT
            ps.VendorNumber,
            ps.VendorName,
            ps.Brand,
            ps.Description,
            ps.PurchasePrice,                                     
            ps.ActualPrice,
            ps.Volume,
            ps.TotalPurchaseQuantity,
            ps.TotalPurchaseDollars,                                                                                                                                                    
            ss.TotalSalesQuantity,
            ss.TotalSalesDollars,
            ss.TotalSalesPrice,
            ss.TotalExciseTax,
            fs.FreightCost                                                                                                                                                    
        FROM PurchaseSummary as ps
        LEFT JOIN SalesSummary as ss
            ON ps.VendorNumber = ss.VendorNo                                         
            AND ps.Brand = ss.Brand
        LEFT JOIN FreightSummary as fs 
            ON ps.VendorNumber = fs.VendorNumber
        ORDER BY ps.TotalPurchaseDollars DESC""",conn)
    
    return vendor_sales_summary

def clean_data(df):
    '''this function will clean the data'''
    # changing the data type in float
    df['Volume'] = df['Volume'].astype('float')

    # treating the null values
    df.fillna(0, inplace=True)

    # removing spaces from categorical columns
    df['VendorName'] = df['VendorName'].str.strip()
    df['Description'] = df['Description'].str.strip()
    
    # creating new columns for better analysis
    df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']
    df['ProfitMargin'] = (df['GrossProfit']/df['TotalSalesDollars'])*100
    df['StockTurnover'] = df['TotalSalesQuantity']/df['TotalPurchaseQuantity']
    df['SalestoPurchaseRatio'] = df['TotalSalesDollars']/df['TotalPurchaseDollars']

    return df

if __name__ == "__main__" : 
   # creating a database connection 
   conn = sqlite3.connect('inventory.db')

   logging.info('Creating vendor summary table...........')
   summary_df = create_vendor_summary(conn)
   logging.info(summary_df.head())

   logging.info('Cleaning Data ........')
   clean_df = clean_data(summary_df)
   logging.info(clean_df.head())

   logging.info('Ingesting Data......')
   ingest_db(clean_df, 'vendor_sales_summary', conn)
   logging.info('Ingestion Completed')





