import pandas as pd
import random

keywords = ["slot", "casino", "bola", "sbobet", "idnpoker", "food", "clothes", "gadget", "ticket"]
locations = ["Jakarta", "Surabaya", "Bandung", "Medan"]
devices = ["Android", "iOS", "Windows", "Linux"]
merchant_categories = ["entertainment", "shopping", "gaming", "others", "travel", "fashion"]

def generate_merchant_category(is_fraud):
    if is_fraud:
        return random.choices(
            ["entertainment", "gaming", "shopping", "others"],
            weights=[0.4, 0.3, 0.2, 0.1]
        )[0]
    else:
        return random.choices(
            ["shopping", "others", "entertainment", "gaming"],
            weights=[0.4, 0.3, 0.2, 0.1]
        )[0]

data = []
for _ in range(10000):
    keyword = random.choice(keywords)

    is_fraud = 1 if keyword in ["slot", "casino", "bola", "sbobet", "idnpoker"] and random.random() < 0.7 else 0

    data.append({
        "amount": random.randint(10000, 500000),
        "transaction_type": random.choice(["purchase", "transfer"]),
        "merchant_category": generate_merchant_category(is_fraud),
        "location": random.choice(locations),
        "device_used": random.choice(devices),
        "is_fraud": is_fraud,
        "time_since_last_transaction": random.randint(1, 600),
        "velocity_score": round(random.uniform(0.1, 1.0), 2),
        "geo_anomaly_score": round(random.uniform(0.1, 1.0), 2),
        "keyword_match": 1 if keyword in ["slot", "casino", "bola", "sbobet", "idnpoker"] else 0,
    })

df = pd.DataFrame(data)
df.to_csv("simulated_judi_dataset.csv", index=False)
