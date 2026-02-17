name = input("Enter full name: ")

# Calculate L (without spaces)
L = 0
for ch in name:
    if ch != " ":
        L += 1

PLI = L % 3

print("L:", L)
print("PLI:", PLI)

# Input weights
data = input("Enter weights: ")

weights = []
num = ""

for ch in data:
    if ch != " ":
        num += ch
    else:
        if num != "":
            weights.append(int(num))
            num = ""
if num != "":
    weights.append(int(num))

very_light = []
normal_load = []
heavy_load = []
overload = []
invalid_entries = []

valid_count = 0

for w in weights:

    if w < 0:
        invalid_entries.append(w)

    elif w <= 5:
        very_light.append(w)
        valid_count += 1

    elif w <= 25:
        normal_load.append(w)
        valid_count += 1

    elif w <= 60:
        heavy_load.append(w)
        valid_count += 1

    else:
        overload.append(w)
        valid_count += 1


affected = 0

# Apply PLI
if PLI == 0:
    for x in overload:
        invalid_entries.append(x)
        affected += 1
    overload = []

elif PLI == 1:
    affected = len(very_light)
    very_light = []

else:   # PLI == 2
    affected = len(very_light) + len(overload)
    very_light = []
    overload = []


print("\nFinal Plan")
print("Very Light:", very_light)
print("Normal:", normal_load)
print("Heavy:", heavy_load)
print("Overload:", overload)
print("Invalid:", invalid_entries)

print("Valid Count:", valid_count)
print("Affected:", affected)