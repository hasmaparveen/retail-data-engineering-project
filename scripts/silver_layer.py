import pandas as pd

DATA_PATH = "data"

def load_data():
    customers = pd.read_csv(f"{DATA_PATH}/customers.csv")
    products = pd.read_csv(f"{DATA_PATH}/products.csv")
    orders = pd.read_csv(f"{DATA_PATH}/orders.csv")
    return customers, products, orders

def clean_customers(customers):
    customers = customers.drop_duplicates()
    customers["signup_date"] = pd.to_datetime(customers["signup_date"])
    customers = customers.dropna(subset=["customer_id"])
    return customers

def clean_products(products):
    products = products.drop_duplicates()
    products["price"] = products["price"].astype(float)
    return products

def clean_orders(orders, customers, products):
    orders = orders.drop_duplicates()
    orders["order_date"] = pd.to_datetime(orders["order_date"])

    # Validate foreign keys
    orders = orders[
        orders["customer_id"].isin(customers["customer_id"]) &
        orders["product_id"].isin(products["product_id"])
    ]

    return orders

if __name__ == "__main__":
    customers, products, orders = load_data()

    customers_clean = clean_customers(customers)
    products_clean = clean_products(products)
    orders_clean = clean_orders(orders, customers_clean, products_clean)

    print("✅ Silver Layer Cleaning Completed\n")
    print(f"Customers: {customers_clean.shape}")
    print(f"Products: {products_clean.shape}")
    print(f"Orders: {orders_clean.shape}")
