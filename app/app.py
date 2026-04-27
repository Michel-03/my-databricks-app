import os

env = os.getenv("ENV", "dev")

print(f"🚀 Running Databricks App to check in {env} environment")    