import os

env = os.getenv("ENV", "dev")

print(f"🚀 Running Databricks App in {env} environment")    