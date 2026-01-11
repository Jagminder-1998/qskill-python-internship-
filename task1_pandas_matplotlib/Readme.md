Task 1 – Pandas & Matplotlib Data Analysis
Objective-The objective of this task is to perform basic data analysis using the Pandas library and create visualizations using Matplotlib. The task involves loading a CSV file, analyzing the data, calculating averages, and visualizing insights through different plots.

Dataset Used-A sample employee dataset (employees.csv) containing the following columns:
Name – Employee name
Age – Age of the employee
Salary – Monthly salary
Experience – Years of work experience

Tools & Libraries Used-
Python
Pandas
Matplotlib
Seaborn

Steps Performed-
1. Data Loading-Loaded the CSV file using pandas.read_csv(), Stored data in a Pandas DataFrame

2. Basic Data Analysis-Checked dataset structure using df.info(), Generated statistical summary using df.describe()

3. Calculated-Average Salary, Average Age

4. Data Visualization-The following visualizations were created using Matplotlib and Seaborn:
Bar Chart – Salary of employees
Scatter Plot – Relationship between experience and salary
Heatmap – Correlation between age, salary, and experience
*All plots are saved inside the plots/ folder.

Insights & Observations-
The average salary of employees is ₹51,800.
Employees with higher experience tend to earn higher salaries.
There is a strong positive correlation between experience and salary, as shown in the scatter plot and heatmap.
Salary distribution varies significantly across employees, indicating experience-based growth.

Conclusion-
This task demonstrates the use of Pandas for data analysis and Matplotlib/Seaborn for visualization. It provides meaningful insights into employee salary trends based on experience and age.