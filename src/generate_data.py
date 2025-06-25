
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
num_samples = 500
original_df = pd.DataFrame({
    "Category1": np.random.choice(["A", "B", "C", "D", "E"], num_samples, p=[0.2, 0.4, 0.2, 0.1, 0.1]),
    "Value1": np.random.normal(10, 2, num_samples), # Continuous variable
    "Value2": np.random.normal(20, 6, num_samples), # Continuous variable
})
original_df.to_csv("dataset.csv", sep=";")

print("Original Dataset Summary:")
print(original_df.describe(include='all'))

# Code for new dataset generation based on characteristics of the original dataset
np.random.seed(42)
num_samples_new = 1000 

category_proportions = original_df['Category1'].value_counts(normalize=True)

value1_mean, value1_std = original_df['Value1'].mean(), original_df['Value1'].std()
value2_mean, value2_std = original_df['Value2'].mean(), original_df['Value2'].std()

new_df = pd.DataFrame({
    "Category1": np.random.choice(category_proportions.index, num_samples_new, p=category_proportions.values),
    "Value1": np.random.normal(value1_mean, value1_std, num_samples_new),
    "Value2": np.random.normal(value2_mean, value2_std, num_samples_new),
})

new_df.to_csv("new_dataset.csv", sep=";")

# Code for Verification of similarity between original and new datasets
print("\nNew Dataset Summary:")
print(new_df.describe(include='all'))

# Statistical comparison
print("\nStatistical Comparison:")
print("Original Category Proportions:")
print(category_proportions)
print("\nNew Category Proportions:")
print(new_df['Category1'].value_counts(normalize=True))

print("\nOriginal Value1 Mean and Std:")
print(value1_mean, value1_std)
print("\nNew Value1 Mean and Std:")
print(new_df['Value1'].mean(), new_df['Value1'].std())

print("\nOriginal Value2 Mean and Std:")
print(value2_mean, value2_std)
print("\nNew Value2 Mean and Std:")
print(new_df['Value2'].mean(), new_df['Value2'].std())

# Visual comparison
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
sns.histplot(original_df['Value1'], kde=True, color='blue', label='Original Value1')
sns.histplot(new_df['Value1'], kde=True, color='green', label='New Value1')
plt.legend()

plt.subplot(2, 2, 2)
sns.histplot(original_df['Value2'], kde=True, color='blue', label='Original Value2')
sns.histplot(new_df['Value2'], kde=True, color='red', label='New Value2')
plt.legend()

plt.subplot(2, 2, 3)
sns.countplot(x=original_df['Category1'], order=['A','B', 'C', 'D', 'E'],color='blue', label='Original Category1')
plt.legend()

plt.subplot(2, 2, 4)
sns.countplot(x=new_df['Category1'], order=['A','B', 'C', 'D', 'E'], color='green', label='New Category1')
plt.legend()

plt.tight_layout()
plt.savefig("comparison.png")
plt.show()