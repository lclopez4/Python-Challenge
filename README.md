python-challenge
Module 3 challenge - create python scripts to analyze financial records for a company and to modernize a vote-counting process ChatGPT corrected Code for PyBank:

In handling the Greatest Increase and Decrease in Profits, the initial values were incorrectly set to "date," which was a string, rather than integers. This led to an incorrect calculation. To correct this, the values were properly initialized as follows:
greatest_increase = float('-inf')
greatest_decrease = float('inf')
For Tracking Net Total Profit and Loss, the original variables were not being utilized effectively. ChatGPT provided recommendations to improve clarity by making variable names more descriptive and ensuring they were correctly referenced throughout the script.
This ensured that numerical operations could be performed correctly.

Regarding String Formatting in Print and Write Statements, corrections were made to enhance readability and accuracy. Additionally, the variables greatest_increase_month and greatest_decrease_month were originally assigned to " = date", which was incorrect. The correct approach was:
greatest_increase_month = ""
greatest_decrease_month = ""
To improve the formatting of the output file, a new line was added to the txt_file.write function by including (\n), ensuring better readability of the saved results.
I received helped from ChatGPT and classmates. 

