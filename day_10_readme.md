# Multi-Level Data Replication & Risk Analysis System

## Overview
This project simulates a large-scale data replication system where improper copying techniques can cause hidden data corruption. It combines Python internals with data science concepts to analyze data integrity and predict system risks.

## Features
- Generates random multi-level nested data for 15 zones  
- Implements assignment, shallow copy, and deep copy  
- Applies custom risk calculation using logarithmic transformation  
- Converts data into a Pandas DataFrame  
- Uses NumPy for mean, variance, and anomaly detection  
- Manual correlation calculation (without using .corr())  
- Detects data corruption, risk patterns, and system stability  

## Technologies Used
- Python  
- NumPy  
- Pandas  
- math module  
- random module  

## How It Works
1. Random data is generated for multiple zones  
2. Data is replicated using assignment, shallow copy, and deep copy  
3. Modifications are applied to copied data  
4. Risk score is calculated using log transformation  
5. Data is analyzed using NumPy and Pandas  
6. Corruption and anomalies are detected  
7. Final system decision is generated  

## Data Corruption Definition
Data corruption occurs when original data is unintentionally modified due to shared references in shallow copy or assignment.

## Personalization
The program applies a rule based on the register number:
- Even → dataset is reversed  
- Odd → dataset is rotated by 3 positions  

## Output
- DataFrame of processed data  
- Comparison of original and copied data  
- Anomaly detection results  
- Tuple (max_risk, min_risk, stability_index)  
- Final system status (Stable / Risk / Failure)  

## How to Run
python your_file_name.py

## Learning Outcome
This project helped in understanding Python memory handling, especially shallow vs deep copy, and applying data science techniques like NumPy and Pandas for analysis and prediction.

## Author
Your Name  
SRM University-AP  
CSE205 – Hands-on Python