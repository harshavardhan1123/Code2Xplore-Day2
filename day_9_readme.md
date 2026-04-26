# Multi-Level Data Replication & Integrity Analyzer

## Overview
This project simulates data replication in a cloud system and analyzes how improper copying methods cause data inconsistency. It demonstrates the difference between assignment, shallow copy, and deep copy using nested data structures in Python.

## Features
- Uses lists, dictionaries, and sets  
- Implements assignment, shallow copy, and deep copy  
- Applies personalized modification based on register number  
- Detects data leakage and integrity issues  
- Finds overlapping data using sets  

## Concepts Used
Lists, Dictionaries, Sets, Functions, Loops, Conditional Statements, Shallow Copy, Deep Copy

## How It Works
The program creates user data, replicates it using different copying techniques, modifies the copied data, and compares results to identify unintended changes and data corruption.

## Data Corruption Definition
Data corruption occurs when original data is unintentionally modified due to shared references in shallow copy or assignment.

## How to Run
python day9.py

## Output
- Before and After comparison  
- Memory reference check  
- Integrity report (leakage_count, safe_count, overlap_count)  
