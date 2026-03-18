reg_last_digit = int(input("Enter last digit of register number: "))

if reg_last_digit % 2 == 0:

    energy_readings = []

    n = int(input("Enter number of readings: "))
    for i in range(n):
        val = int(input(f"Enter reading {i+1}: "))
        energy_readings.append(val)

    categorized={
        "efficient":[],
        "moderate":[],
        "high":[],
        "invalid":[]
    }

    for e in energy_readings:
        if e<0:
            categorized["invalid"].append(e)
        elif  0 <= e <= 50:
            categorized["efficient"].append(e)
        elif 51<=e<=150:
            categorized["moderate"].append(e)
        else:
            categorized["high"].append(e)

    valid_readings=[e for e in energy_readings if e>=0]

    summary=(
        len(energy_readings),
        sum(valid_readings),
        len(categorized["efficient"]),
        len(categorized["moderate"]),
        len(categorized["high"]),
        len(categorized["invalid"]),
    )

    result=[]

    if len(categorized["high"])>3:
        result.append("Overconsumption")

    if len(categorized["efficient"])-len(categorized["moderate"])<=1:
        result.append("Balanced Usage")

    if  sum(valid_readings)>600:
        result.append("Energy waste Detected")

    print("Display:")

    print("\nCategorized Readings:")
    for key in categorized:
        print(f"{key.capitalize()}: {categorized[key]}")

    print(f"\nTotal Consumption: {summary[0]}")
    print(f"Number of Buildings: {summary[1]}")

    print("\nEfficiency Result:")
    if result:
        for res in result:
            print(res)
    else:
        print("Efficient Campus")

else:
    print("Program will not run because last digit is odd.")