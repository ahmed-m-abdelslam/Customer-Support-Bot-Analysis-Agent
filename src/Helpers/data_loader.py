import json
from functools import lru_cache

@lru_cache
def load_data():
    with open("Data/CustomerSupportSample.json", encoding="utf-8") as f:
        return json.load(f)
