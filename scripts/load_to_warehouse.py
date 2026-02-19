import pandas as pd
from sqlalchemy import create_engine

DATA_PATH = "data"

def load_data():
    customers = pd.read_csv(f"{DATA_PATH}/customers.csv")
    products = pd.read_csv(f"{DATA_PATH}/products.csv")
    orders = pd.read_csv(f"{DATA_PATH}/orders.csv")

    orders["order_date"] = pd.to_datetime(orders["order_date"])
    customers["signup_date"] = pd.to_datetime(customers["signup_date"])

    fact_sales = orders.merge(products, on="product_id", how="left")
    fact_sales = fact_sales.merge(customers, on="customer_id", how="left")
    fact_sales["total_amount"] = fact_sales["quantity"] * fact_sales["price"]

    return customers, products, fact_sales

def load_to_sqlite(customers, products, fact_sales):
    engine = create_engine("sqlite:///retail_warehouse.db")

    customers.to_sql("dim_customers", engine, if_exists="replace", index=False)
    products.to_sql("dim_products", engine, if_exists="replace", index=False)
    fact_sales.to_sql("fact_sales", engine, if_exists="replace", index=False)

    print("✅ Data successfully loaded into SQLite warehouse.")

if __name__ == "__main__":
    customers, products, fact_sales = load_data()
    load_to_sqlite(customers, products, fact_sales)
