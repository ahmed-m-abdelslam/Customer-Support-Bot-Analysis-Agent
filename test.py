import json

with open("src/Data/CustomerSupportSample.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# طباعة أول row
print(data[0])
