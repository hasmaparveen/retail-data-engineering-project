import pandas as pd
import random
from faker import Faker
import os

fake = Faker()

DATA_PATH = "data"
os.makedirs(DATA_PATH, exist_ok=True)

def generate_customers(n=1000):
    customers = []
    for i in range(n):
        customers.append({
            "customer_id": i + 1,
            "name": fake.name(),
            "email": fake.email(),
            "city": fake.city(),
            "signup_date": fake.date_between(start_date='-2y', end_date='today')
        })
    return pd.DataFrame(customers)

def generate_products(n=100):
    categories = ["Electronics", "Clothing", "Home", "Sports"]
    products = []
    for i in range(n):
        products.append({
            "product_id": i + 1,
            "product_name": fake.word(),
            "category": random.choice(categories),
            "price": round(random.uniform(10, 500), 2)
        })
    return pd.DataFrame(products)

def generate_orders(n=5000):
    orders = []
    for i in range(n):
        orders.append({
            "order_id": i + 1,
            "customer_id": random.randint(1, 1000),
            "product_id": random.randint(1, 100),
            "quantity": random.randint(1, 5),
            "order_date": fake.date_between(start_date='-1y', end_date='today')
        })
    return pd.DataFrame(orders)

if __name__ == "__main__":
    customers_df = generate_customers()
    products_df = generate_products()
    orders_df = generate_orders()

    customers_df.to_csv(f"{DATA_PATH}/customers.csv", index=False)
    products_df.to_csv(f"{DATA_PATH}/products.csv", index=False)
    orders_df.to_csv(f"{DATA_PATH}/orders.csv", index=False)

    print("✅ Data generation completed successfully.")
