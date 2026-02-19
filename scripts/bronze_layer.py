import pandas as pd
import os

DATA_PATH = "data"

def load_raw_data():
    try:
        customers = pd.read_csv(f"{DATA_PATH}/customers.csv")
        products = pd.read_csv(f"{DATA_PATH}/products.csv")
        orders = pd.read_csv(f"{DATA_PATH}/orders.csv")

        print("✅ Bronze Layer Loaded Successfully\n")
        print(f"Customers rows: {customers.shape[0]}")
        print(f"Products rows: {products.shape[0]}")
        print(f"Orders rows: {orders.shape[0]}")

        return customers, products, orders

    except Exception as e:
        print("❌ Error in Bronze Layer:", str(e))

if __name__ == "__main__":
    load_raw_data()
