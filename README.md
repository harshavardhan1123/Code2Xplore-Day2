I made this program to check how energy is being used in different buildings. The idea is simple, we take some energy readings and see whether the usage is low, normal, or too high. Based on that, I grouped the readings into efficient, moderate, high, and invalid.

To do this, I first took the input values from the user using a loop and stored them in a list. Then I went through each value one by one and used conditions to decide where it belongs. I used a dictionary to keep all these categories so it’s easy to track. After that, I removed the invalid values and calculated the total energy usage. I also used a tuple just to store some summary values.

Then I checked a few conditions like whether there are too many high readings, whether the usage looks balanced, or if the total consumption is too much. Based on these, the program prints the final result along with all the categorized readings.

I also added a small personalization where the program runs only if the last digit of my register number is even. If it’s odd, the program just stops.

I tried the program with different types of inputs like normal values, high values, and even invalid ones to make sure it works in all cases.

From this, I got a better idea of how to use loops and conditions properly and how to handle data in a structured way instead of just writing random code.
