import pandas as pd

DATA_PATH = "data"

def load_clean_data():
    customers = pd.read_csv(f"{DATA_PATH}/customers.csv")
    products = pd.read_csv(f"{DATA_PATH}/products.csv")
    orders = pd.read_csv(f"{DATA_PATH}/orders.csv")

    customers["signup_date"] = pd.to_datetime(customers["signup_date"])
    orders["order_date"] = pd.to_datetime(orders["order_date"])

    return customers, products, orders

def create_fact_table(customers, products, orders):
    # Join orders with products
    fact_sales = orders.merge(products, on="product_id", how="left")

    # Join with customers
    fact_sales = fact_sales.merge(customers, on="customer_id", how="left")

    # Business logic: calculate total revenue
    fact_sales["total_amount"] = fact_sales["quantity"] * fact_sales["price"]

    return fact_sales

if __name__ == "__main__":
    customers, products, orders = load_clean_data()

    fact_sales = create_fact_table(customers, products, orders)

    print("✅ Gold Layer Created Successfully\n")
    print(f"Fact table shape: {fact_sales.shape}")
    print("\nSample Data:")
    print(fact_sales.head())
