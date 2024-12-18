import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df2 = pd.read_csv(r"Cancer_Data.csv")
print(df2.columns)

# Encoding the diagnosis column to be numeric
df2['diagnosis_num'] = df2['diagnosis'].map({'M': 1, 'B': 0})

#Dropping cols we won't use
df = df2[['radius_mean', 'area_mean', 'compactness_mean', 'concavity_mean', 
          'concave points_mean', 'symmetry_mean', 'texture_mean', 'diagnosis', 'diagnosis_num', "id"]].copy()

total_count = df["id"].shape[0]

total_count_M = df[df["diagnosis_num"] == 1].shape[0]
total_count_B = df[df["diagnosis_num"] == 0].shape[0]

perc_of_cancer = total_count_M / total_count *100 #Printing % of canceours tumors.

dfM= df[df["diagnosis_num"] == 1] 
dfB= df[df["diagnosis_num"] == 0]

sns.countplot(x="diagnosis", data=df, palette="viridis")
plt.suptitle("The count of Benign vs Malignant tumors")
plt.show()

radius_mean_avgM = dfM["radius_mean"].mean()
area_mean_avgM = dfM["area_mean"].mean()
compactness_mean_avgM = dfM["compactness_mean"].mean()
concavity_mean_avgM = dfM["concavity_mean"].mean()
concave_points_mean_avgM = dfM["concave points_mean"].mean()
symmetry_mean_avgM = dfM["symmetry_mean"].mean()
texture_mean_avgM = dfM["texture_mean"].mean()

radius_mean_avgB = dfB["radius_mean"].mean()
area_mean_avgB = dfB["area_mean"].mean()
compactness_mean_avgB = dfB["compactness_mean"].mean()
concavity_mean_avgB = dfB["concavity_mean"].mean()
concave_points_mean_avgB = dfB["concave points_mean"].mean()
symmetry_mean_avgB = dfB["symmetry_mean"].mean()
texture_mean_avgB = dfB["texture_mean"].mean()


print(radius_mean_avgM)
print(area_mean_avgM)
print(compactness_mean_avgM)
print(concave_points_mean_avgM)
print(symmetry_mean_avgM)
print(texture_mean_avgM)

print(radius_mean_avgB)
print(area_mean_avgB)
print(compactness_mean_avgB)
print(concave_points_mean_avgB)
print(symmetry_mean_avgB)
print(texture_mean_avgB)


data_to_plot = {
    'Feature': ['radius_mean', 'area_mean', 'compactness_mean', 'concave_points_mean', 
                'symmetry_mean', 'texture_mean'],
    'Avg_M': [radius_mean_avgM, area_mean_avgM, compactness_mean_avgM, 
              concave_points_mean_avgM, symmetry_mean_avgM, texture_mean_avgM],
    'Avg_B': [radius_mean_avgB, area_mean_avgB, compactness_mean_avgB, 
              concave_points_mean_avgB, symmetry_mean_avgB, texture_mean_avgB]
}

# Create dataframe
data2 = pd.DataFrame(data_to_plot)

# Reshape the dataframe
data2 = pd.melt(data2, id_vars=['Feature'], value_vars=['Avg_M', 'Avg_B'], 
                var_name='Diagnosis', value_name='Average')

# Create subplots, one for each feature
fig, axes = plt.subplots(2, 3, figsize=(15, 10))  # 2 rows, 3 columns
axes = axes.flatten()  # Flatten the 2D array of axes for easier indexing

# Loop through each feature and plot it in the corresponding subplot
for i, feature in enumerate(data_to_plot['Feature']):
    # Filter data for the current feature
    feature_data = data2[data2['Feature'] == feature]
    
    # Plot on the corresponding subplot
    sns.barplot(x='Diagnosis', y='Average', data=feature_data, ax=axes[i], palette="viridis")
    
    # Set titles and labels with adjusted font size
    axes[i].set_title(f'{feature} Comparison', fontsize=12)  # Smaller title font size
    axes[i].set_xlabel('Diagnosis', fontsize=12)
    axes[i].set_ylabel('Average Value', fontsize=12)

# Adjust layout to avoid overlap
plt.tight_layout()
plt.show()

df_DROPPED = df.drop(columns=['diagnosis', "id"])

sns.heatmap(df_DROPPED.corr(), annot=True)
plt.show()

print(perc_of_cancer)

