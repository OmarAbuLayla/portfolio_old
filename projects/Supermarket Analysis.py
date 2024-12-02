import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv(r"supermarket_sales - Sheet1.csv")


product_line_income = df.groupby("Product line")["gross income"].sum().reset_index()
sns.catplot(x="Product line", y="gross income", data=product_line_income, kind="bar", palette="viridis")
plt.title("Total Gross Income by Product Line")
plt.xlabel("Gross Income in USD")
plt.ylabel("Product Line")
plt.xticks(rotation=75)
plt.tight_layout()

sorted_productsLOW = product_line_income.sort_values(by="gross income", ascending= True)
sorted_productsHIGH = product_line_income.sort_values(by="gross income", ascending=False)

least_preforming = sorted_productsLOW.iloc[0]["Product line"]
least_preforming_income = sorted_productsLOW.iloc[0]["gross income"]
print(f"The least prefoming line is is the {least_preforming} and it controbuted to a total of {least_preforming_income} of revenue.")

most_preforming = sorted_productsHIGH.iloc[0]["Product line"]
most_preforming_income = sorted_productsHIGH.iloc[0]["gross income"]
print(f"The most prefoming line is is the {most_preforming} and it controbuted to a total of {most_preforming_income} of revenue.")

print("######################################################################################################################################")

customer_mem = df[df["Customer type"] == "Member"]
customer_non = df[df["Customer type"] == "Normal"]

total_for_members = customer_mem["Total"].sum()
total_for_non = customer_non["Total"].sum()

if total_for_members > total_for_non:
    print(f"Members tend to buy more than non members, loyalty program is working well. Total spendings for members is {total_for_members}")
else:
    print("Non members tend to buy more than members, hence there is a problem with the loyalty program")

print("######################################################################################################################################")
rating_for_mem = customer_mem["Rating"].mean()
rating_for_non = customer_non["Rating"].mean()

if rating_for_mem > rating_for_non:
    print(f"The average rating given by members is {rating_for_mem} and its higher than ratings for non members which is {rating_for_non}.")

else:
    print(f"The average rating given by non members is {rating_for_non} and its higher than ratings for members which is {rating_for_mem}.")

print("######################################################################################################################################")

branchA = df[df["Branch"] == "A"]
branchB = df[df["Branch"] == "B"]
branchC = df[df["Branch"] == "C"]

total_for_A = branchA["Total"].sum()
total_for_B = branchB["Total"].sum()
total_for_C = branchC["Total"].sum()



if total_for_A > total_for_B and total_for_A > total_for_B:
    print(f"Branch A is the most selling branch! Total selling is: {total_for_A} USD.")

elif total_for_B > total_for_A and total_for_B > total_for_C:
    print("Branch B is the highest selling branch!")

else:
    print("Branch C is the highest selling branch!")
print("######################################################################################################################################")

branch_totals = {
    "Branch" : ["A", "B", "C"],
    "Total Sales (USD)": [total_for_A, total_for_B, total_for_C]
}

branch_df = pd.DataFrame(branch_totals)

sns.catplot(x="Branch", y="Total Sales (USD)", data= branch_df, palette= "viridis", kind="bar")
plt.title("Total Sales by Branch")
plt.xlabel("Branch")
plt.ylabel("Total Sales (USD)")
plt.tight_layout()


rating_avg_for_a = branchA["Rating"].mean()
rating_avg_for_b = branchB["Rating"].mean()
rating_avg_for_c = branchC["Rating"].mean()

if rating_avg_for_a > rating_avg_for_b and rating_avg_for_a > rating_avg_for_c:
    print("Branch A has the heighst ratings.")

elif rating_avg_for_b > rating_avg_for_a and  rating_avg_for_b > rating_avg_for_c:
    print("Branch B has the heighst ratings.")

else: 
    print("Branch C has the heighst ratings.")
print("######################################################################################################################################")

paymentCash = df[df["Payment"] == "Cash"].shape[0]
paymentCC = df[df["Payment"] == "Credit card"].shape[0]
payment_EWallet = df[df["Payment"] == "Ewallet"].shape[0]

paymentDF = {
    "Payment" : ["Cash", "CC", "EWallet"],
    "Count": [paymentCash, paymentCC, payment_EWallet]
}

paymentDF = pd.DataFrame(paymentDF)

sns.catplot(x="Payment", y="Count", data=paymentDF, palette="viridis", kind="bar")
plt.title("Payment methods vs Count")
plt.xlabel("Payment methods")
plt.ylabel("Count")
plt.tight_layout()


if paymentCash > paymentCC and paymentCash > payment_EWallet:
    print("Payment by Cash is the most common.")

elif paymentCC > paymentCash and  paymentCC > payment_EWallet:
    print("Payment by Credit Card is the most common.")

else: 
    print("Branch C has the heighst ratings.")

print("######################################################################################################################################")

avg_ratings = df.groupby("Product line")["Rating"].mean().reset_index()
highest_rated = avg_ratings.loc[avg_ratings["Rating"].idxmax()]
lowest_rated = avg_ratings.loc[avg_ratings["Rating"].idxmin()]


print(f"The highest-rated product line is '{highest_rated['Product line']}' with an average rating of {highest_rated['Rating']:.2f}.")
print(f"The lowest-rated product line is '{lowest_rated['Product line']}' with an average rating of {lowest_rated['Rating']:.2f}.")
print("######################################################################################################################################")

sns.catplot(x="Rating", y="Product line", data=df, palette="viridis", kind="bar")
plt.title("Customer Ratings Across Product Lines")
plt.xlabel("Rating")
plt.ylabel("Product Line")
plt.tight_layout()

# Show the plot
plt.show()

