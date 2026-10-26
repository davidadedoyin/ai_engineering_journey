import os

expected_key = os.getenv("APP_SECRET", "demo-secret")
print("Expected secret length:", len(expected_key))
