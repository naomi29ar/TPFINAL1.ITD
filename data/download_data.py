import requests
import os

RESOURCE_ID = "814b7b54-477a-4c25-b3bf-6be05412069d"
API_URL = f"https://data.iadb.org/api/3/action/resource_show?id={RESOURCE_ID}"

os.makedirs("data/raw", exist_ok=True)

meta = requests.get(API_URL).json()
download_url = meta["result"]["url"]

response = requests.get(download_url)
response.raise_for_status()

output_path = "data/raw/idb_projects_dataset.csv"
with open(output_path, "wb") as f:
    f.write(response.content)

print(f"Dataset descargado en: {output_path}")
