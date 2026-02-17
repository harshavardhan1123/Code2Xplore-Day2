Weight Load Classification System

Project Description
This Python program classifies weight entries into different load categories and modifies the final plan based on a calculated Plan Load Index derived from the user’s name.

Program Logic

Step 1 Name Analysis
The user enters a full name.
Spaces are ignored while counting characters.
Total characters are stored as L.
Plan Load Index is calculated using the formula:

PLI equals L modulus 3.

Step 2 Weight Classification
The user enters weights separated by spaces.
Each weight is classified as follows:

If weight is less than zero it is treated as an invalid entry.
If weight is between 0 and 5 it is Very Light.
If weight is between 6 and 25 it is Normal Load.
If weight is between 26 and 60 it is Heavy Load.
If weight is greater than 60 it is Overload.

Step 3 Plan Modification Rules

If PLI equals 0
All overload weights are moved to invalid entries.

If PLI equals 1
All very light weights are removed from the plan.

If PLI equals 2
Both very light and overload weights are removed.

The number of affected entries is calculated.

Program Output

The program displays
Final category lists
Invalid entries
Valid weight count
Affected entries count
Calculated L value
Calculated PLI value

How to Run the Program

Install Python version 3 or above.
Save the program file as day5.py.
Open terminal or command prompt.
Run the command:

python day5.py

Enter the full name and weights when prompted.

Example Input

Full name Rahul Kumar
Weights 2 10 45 70 minus 5

Technologies Used

Python 3
Loops
Conditional statements
Lists
String handling

Repository Structure

day5.py
README.md

Purpose of the Project

This project is created for academic learning.
It demonstrates input processing, data classification, and conditional plan modification using Python.
