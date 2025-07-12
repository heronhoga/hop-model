import pandas as pd
import random

keywords = ["slot", "casino", "bola", "sbobet", "idnpoker", "food", "clothes"]
locations = ["Jakarta", "Surabaya", "Bandung", "Medan"]
devices = ["Android", "iOS", "Windows", "Linux"]

data = []
for _ in range(10000):
    keyword = random.choice(keywords)
    is_fraud = 1 if keyword in ["slot", "casino", "bola", "sbobet", "idnpoker"] else 0
    data.append({
        "amount": random.randint(10000, 500000),
        "transaction_type": random.choice(["purchase", "transfer"]),
        "merchant_category": "entertainment" if is_fraud else "others",
        "location": random.choice(locations),
        "device_used": random.choice(devices),
        "is_fraud": is_fraud,
        "time_since_last_transaction": random.randint(1, 600),
        "velocity_score": round(random.uniform(0.1, 1.0), 2),
        "geo_anomaly_score": round(random.uniform(0.1, 1.0), 2),
        "keyword_match": 1 if is_fraud else 0,
    })

df = pd.DataFrame(data)
df.to_csv("simulated_judi_dataset.csv", index=False)
