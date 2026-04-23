import random
import math
import numpy as np
import pandas as pd

n = "harshavardhanreddy"
l = len(n)
rno = 54

def build_data():
    z = random.randint(15, 20)
    a = []
    for i in range(z):
        a.append({
            "zone": i+1,
            "traffic": random.randint(0, 100),
            "air_quality": random.randint(0, 300),
            "energy": random.randint(0, 500)
        })
    return a

def group_zones(a):
    d = {"high": [], "energy_critical": [], "safe": []}
    for i in a:
        if i["air_quality"] > 200 or i["traffic"] > 80:
            d["high"].append(i["zone"])
        elif i["energy"] > 400:
            d["energy_critical"].append(i["zone"])
        elif i["traffic"] < 30 and i["air_quality"] < 100:
            d["safe"].append(i["zone"])
    return d

def order_by_traffic(a):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i]["traffic"] > a[j]["traffic"]:
                a[i], a[j] = a[j], a[i]
    return a

def compute_score(a):
    for i in a:
        t = i["traffic"]
        q = i["air_quality"]
        e = i["energy"]
        score = (t*0.35 + q*0.45 + e*0.2 + (l % 5))
        if score <= 0:
            score = 1
        i["risk_score"] = round(score, 2)
        i["log_score"] = round(math.log(score + 1), 2)
    return a

def analyze_data(a):
    df = pd.DataFrame(a)
    arr = np.array(df[["traffic", "air_quality", "energy"]])
    m = np.mean(arr, axis=0)

    b = a[:]
    for i in range(len(b)):
        for j in range(i+1, len(b)):
            if b[i]["risk_score"] < b[j]["risk_score"]:
                b[i], b[j] = b[j], b[i]

    top = b[:3]

    s = [i["risk_score"] for i in a]
    t = (max(s), round(sum(s)/len(s), 2), min(s))

    return df, m, top, t

def final_decision(x):
    if x < 100:
        return "City Stable"
    elif x < 200:
        return "Moderate Risk"
    elif x < 300:
        return "High Alert"
    else:
        return "Critical Emergency"

a = build_data()

if rno % 2 == 0:
    random.shuffle(a)
else:
    a = order_by_traffic(a)

a = compute_score(a)
c = group_zones(a)
df, m, top, t = analyze_data(a)
res = final_decision(t[1])

print("\n==== Smart City Report ====\n")

print("Zone Data Snapshot:")
print(df.head())

print("\nCategory Summary:")
print("High Risk Zones:", c["high"])
print("Energy Critical Zones:", c["energy_critical"])
print("Safe Zones:", c["safe"])

print("\nTop Risk Zones:")
for i in top:
    print(f"Zone {i['zone']} -> Score {i['risk_score']}")

print("\nRisk Summary (Max, Avg, Min):", t)

if l % 2 == 0:
    print("\nNote: System observed more high-risk zones today.")
else:
    print("\nNote: Several zones are maintaining safe conditions.")

print("\nFinal Status:", res)

print("\nInsight: Air quality plays a dominant role in determining overall city risk compared to other factors.")