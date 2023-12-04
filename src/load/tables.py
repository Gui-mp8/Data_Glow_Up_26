import pandas as pd
import httpx

df = pd.read_csv("data/olist/olist_customers_dataset.csv", delimiter=",")

# for index, row in df.iterrows():
payload = {
    "customer_id": "06b8999e2fba1a1fbc88172c00ba8bc7",
    "customer_unique_id": "861eff4711a542e4b93843c6dd7febb0",
    "customer_zip_code_prefix": "14409",
    "customer_city": "franca",
    "customer_state": "SP",
}

url = "http://127.0.0.1:8000/customers"
# Make a POST request using httpx
with httpx.Client() as client:
    response = client.post(url, json=payload)

# Check the response status
if response.status_code == 200:
    print(f"Successfully added customer")
else:
    print(f"Failed to add customer. Status code: {response.status_code}")
