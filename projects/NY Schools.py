import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Analyzing Test Scores Across NYC Public Schools
#This project used data manipulation and summary statistics techniques to analyze and 
#visualize the distribution of test scores across different schools in New York City. 
#The data was cleaned, key metrics were calculated, 
#and insights into performance trends across school districts were provided. 
#The analysis helped in understanding how different factors 
#affect school performance across various neighborhoods.




# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# Start coding here...
# Add as many cells as you like...

import pandas as pd

# Step 1: Filter schools with average_math >= 640
best_math_schools = schools[schools['average_math'] >= 640]

# Step 2: Select only the necessary columns (school_name, average_math)
best_math_schools = best_math_schools[['school_name', 'average_math']]

# Step 3: Sort the DataFrame by average_math in descending order
best_math_schools = best_math_schools.sort_values(by='average_math', ascending=False)

# Display the result
print("ANS FOR TASK1")
print(best_math_schools)
print("----------------------------------------------------------------------")
print("ANS FOR TASK2")
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]
top_10_schools = schools[["school_name", "total_SAT"]]
top_10_schools = top_10_schools.sort_values(by='total_SAT',ascending=False )
top_10_schools = top_10_schools.head(10)

print(top_10_schools)
print("----------------------------------------------------------------------")
print("ANS FOR TASK3")

schools["average_SAT"] = schools.groupby("borough")["total_SAT"].transform("mean")
schools["std_SAT"] = schools.groupby("borough")["total_SAT"].transform("std")
schools["num_schools"] = schools.groupby("borough")["total_SAT"].transform("count")


largest_std_dev = schools[["borough", "num_schools", "average_SAT", "std_SAT"]].drop_duplicates(subset="borough")
largest_std_dev = largest_std_dev.sort_values(by='std_SAT',ascending=False).head(1)
# Round numeric values to two decimal places
largest_std_dev[["average_SAT", "std_SAT", "num_schools"]] = largest_std_dev[["average_SAT", "std_SAT", "num_schools"]].round(2)

print(largest_std_dev)
# Assuming your DataFrame is 'schools' and you have the 'total_SAT' column
plt.figure(figsize=(10,6))

# Using seaborn for a cleaner visualization
sns.histplot(schools['total_SAT'], bins=20, kde=True)  # kde=True adds a smoothed line to the histogram

# Set labels and title
plt.title('Distribution of Total SAT Scores', fontsize=16)
plt.xlabel('Total SAT Score', fontsize=14)
plt.ylabel('Number of Schools', fontsize=14)

# Show the plot
plt.show()
