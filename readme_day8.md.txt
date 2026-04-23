# Autonomous Smart City Data Intelligence System

## Overview

This project simulates a smart city environment where multiple zones are monitored based on traffic density, air quality index, and energy consumption. The system generates random data, analyzes it, and identifies high-risk zones to determine the overall condition of the city.

## Features

* Random data generation for 15–20 zones
* Zone classification (High Risk, Energy Critical, Safe)
* Custom risk score calculation with transformation
* Data analysis using NumPy and Pandas
* Identification of top 3 risky zones
* Final decision on city status (Stable to Critical)

## Technologies Used

* Python
* NumPy
* Pandas
* Math module
* Random module

## Personalization

The system includes personalization by using the student’s name length in the risk score formula to introduce variation. The register number is used to control data handling—since the register number is even, the dataset is shuffled; if it were odd, the data would be sorted based on traffic values.

## How It Works

1. Random data is generated for each zone
2. Data is processed based on personalization rules
3. Risk scores are calculated and transformed
4. Zones are categorized based on conditions
5. Data is analyzed using Pandas and NumPy
6. Top risky zones are identified
7. Final city status is determined

## Output

The program displays:

* DataFrame of all zones
* Categorized zones
* Top 3 risky zones
* Risk summary (max, average, min)
* Final system decision

## Insight

Air quality has a stronger influence on overall risk compared to traffic and energy, indicating that pollution control is a key factor in maintaining a smart and stable city.

## Conclusion

The system demonstrates how multi-factor data analysis can be used to monitor urban conditions and support decision-making in smart city environments.
