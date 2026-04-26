import random
import copy
import math
import numpy as np
import pandas as pd

def create_data(n):
    data = []
    for i in range(n):
        data.append({
            "zone": i + 1,
            "metrics": {
                "traffic": random.randint(10, 100),
                "pollution": random.randint(20, 150),
                "energy": random.randint(50, 200)
            },
            "history": [random.randint(10, 100) for _ in range(5)]
        })
    return data

def make_copies(data):
    ref = data
    shallow = data[:]
    deep = copy.deepcopy(data)
    return ref, shallow, deep

def risk_calc(t, p, e):
    return math.log(t + p + e)

def update_data(data):
    for item in data:
        item["metrics"]["traffic"] += random.randint(1, 15)
        item["history"].append(random.randint(40, 120))

        t = item["metrics"]["traffic"]
        p = item["metrics"]["pollution"]
        e = item["metrics"]["energy"]

        item["risk"] = risk_calc(t, p, e)

def apply_personalization(data, roll):
    if roll % 2 == 0:
        data.reverse()
    else:
        data[:] = data[3:] + data[:3]

def convert_df(data):
    rows = []
    for d in data:
        rows.append([
            d["zone"],
            d["metrics"]["traffic"],
            d["metrics"]["pollution"],
            d["metrics"]["energy"],
            d.get("risk", 0)
        ])
    return pd.DataFrame(rows, columns=["zone", "traffic", "pollution", "energy", "risk"])

def manual_corr(x, y):
    x = np.array(x)
    y = np.array(y)
    mx = np.mean(x)
    my = np.mean(y)

    num = np.sum((x - mx) * (y - my))
    den = math.sqrt(np.sum((x - mx) ** 2) * np.sum((y - my) ** 2))

    return num / den if den != 0 else 0

def analyze(df):
    risks = df["risk"].values
    mean = np.mean(risks)
    var = np.var(risks)
    std = np.std(risks)

    anomalies = df[df["risk"] > mean + std]["zone"].tolist()
    corr_val = manual_corr(df["traffic"], df["pollution"])

    return mean, var, anomalies, corr_val

def detect(before, after, df):
    corrupted = before != after

    risks = df["risk"].values
    max_r = np.max(risks)
    min_r = np.min(risks)

    stability = 1 / (np.var(risks) + 1e-5)

    if corrupted and max_r > 5:
        decision = "Critical Failure"
    elif corrupted:
        decision = "High Corruption Risk"
    elif max_r > 5:
        decision = "Moderate Risk"
    else:
        decision = "System Stable"

    return (max_r, min_r, stability), decision

def main():
    roll_number = 54

    data = create_data(15)
    before = copy.deepcopy(data)

    print("BEFORE:\n", data)

    ref, shallow, deep = make_copies(data)

    update_data(shallow)
    apply_personalization(shallow, roll_number)

    df = convert_df(shallow)

    mean, var, anomalies, corr = analyze(df)
    result, decision = detect(before, data, df)

    print("\nDATAFRAME:\n", df)
    print("\nORIGINAL AFTER:", data)
    print("\nDEEP COPY:", deep)
    print("\nANOMALY ZONES:", anomalies)
    print("\nTUPLE:", result)
    print("\nDECISION:", decision)

main()