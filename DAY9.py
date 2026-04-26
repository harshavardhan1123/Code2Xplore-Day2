import copy

def create_users():
    users = []
    users.append({"id": 1, "data": {"files": ["a.txt", "b.txt"], "usage": 500}})
    users.append({"id": 2, "data": {"files": ["c.txt"], "usage": 300}})
    return users

def make_copies(data):
    ref_copy = data
    shallow_copy = data[:]
    deep_copy = copy.deepcopy(data)
    return ref_copy, shallow_copy, deep_copy

def update_users(data, reg_no):
    for i in range(len(data)):
        if reg_no % 2 == 0:
            data[i]["data"]["files"] += ["extra.txt"]
        else:
            if len(data[i]["data"]["files"]) > 0:
                data[i]["data"]["files"].remove(data[i]["data"]["files"][-1])

        data[i]["data"]["usage"] = data[i]["data"]["usage"] + 100

def analyze(before, after, shallow, deep):
    leak = 0
    safe = 0

    if before != after:
        leak = 1

    if deep == before:
        safe = 1

    files1 = set()
    files2 = set()

    for u in after:
        for f in u["data"]["files"]:
            files1.add(f)

    for u in shallow:
        for f in u["data"]["files"]:
            files2.add(f)

    common = files1 & files2

    print("\nAnalysis:")
    print("Shallow copy shares inner lists")
    print("Deep copy is independent")

    return (leak, safe, len(common))


def run():
    reg_no = 54

    data = create_users()
    before = copy.deepcopy(data)

    print("Before:")
    print(data)

    ref, sh, dp = make_copies(data)

    update_users(sh, reg_no)

    print("\nAfter:")
    print("Original:", data)
    print("Reference:", ref)
    print("Shallow:", sh)
    print("Deep:", dp)

    print("\nIDs:")
    print(id(data[0]["data"]["files"]))
    print(id(sh[0]["data"]["files"]))
    print(id(dp[0]["data"]["files"]))

    result = analyze(before, data, sh, dp)

    print("\nResult:", result)

run()