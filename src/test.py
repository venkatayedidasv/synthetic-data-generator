
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set random seed for reproducibility of the original dataset
np.random.seed(42)
# A seed is an initial value used by a random number generator (RNG) to start its sequence of pseudo-random numbers.

# Generate the original dataset

num_samples = 500
df_original = pd.DataFrame({
    "Category1": np.random.choice(["A", "B", "C", "D", "E"], num_samples, p=[0.2, 0.4, 0.2, 0.1, 0.1]),
    "Value1": np.random.normal(10, 2, num_samples),
    "Value2": np.random.normal(20, 6, num_samples),
})
df_original.to_csv("dataset.csv", sep=";")

# Load the original dataset
df_original = pd.read_csv("dataset.csv", sep=";")

# Estimate parameters from the original dataset
# For Category1: calculate probabilities
category_counts = df_original["Category1"].value_counts(normalize=True)
categories = ["A", "B", "C", "D", "E"]
probs = category_counts.reindex(categories, fill_value=0).values

# For Value1: calculate mean and std
mean1 = df_original["Value1"].mean()
std1 = df_original["Value1"].std()

# For Value2: calculate mean and std
mean2 = df_original["Value2"].mean()
std2 = df_original["Value2"].std()

# Set random seed for new samples
np.random.seed(43)

# Define number of new samples (larger than original)
num_new_samples = 1000

# Generate new samples
new_Category1 = np.random.choice(categories, size=num_new_samples, p=probs)
new_Value1 = np.random.normal(mean1, std1, num_new_samples)
new_Value2 = np.random.normal(mean2, std2, num_new_samples)

# Create new DataFrame
df_new = pd.DataFrame({
    "Category1": new_Category1,
    "Value1": new_Value1,
    "Value2": new_Value2
})

# Save new dataset to CSV
df_new.to_csv("new_dataset.csv", sep=";", index=False)

# Verification
# Print summary statistics
print("Original Category1 frequencies:")
print(df_original["Category1"].value_counts(normalize=True).reindex(categories, fill_value=0))
print("\nNew Category1 frequencies:")
print(df_new["Category1"].value_counts(normalize=True).reindex(categories, fill_value=0))
print("\nOriginal Value1 mean and std:", df_original["Value1"].mean(), df_original["Value1"].std())
print("New Value1 mean and std:", df_new["Value1"].mean(), df_new["Value1"].std())
print("\nOriginal Value2 mean and std:", df_original["Value2"].mean(), df_original["Value2"].std())
print("New Value2 mean and std:", df_new["Value2"].mean(), df_new["Value2"].std())

# Plot bar chart for Category1
fig, ax = plt.subplots()
original_counts = df_original["Category1"].value_counts(normalize=True).reindex(categories, fill_value=0)
new_counts = df_new["Category1"].value_counts(normalize=True).reindex(categories, fill_value=0)
bar_width = 0.35
index = np.arange(len(categories))
ax.bar(index, original_counts, bar_width, label="Original")
ax.bar(index + bar_width, new_counts, bar_width, label="New")
ax.set_xlabel("Category")
ax.set_ylabel("Proportion")
ax.set_title("Category1 Distribution")
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(categories)
ax.legend()
plt.show()

# Plot histograms for Value1 and Value2
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].hist(df_original["Value1"], bins=20, alpha=0.5, label="Original")
axes[0].hist(df_new["Value1"], bins=20, alpha=0.5, label="New")
axes[0].set_title("Value1 Distribution")
axes[0].legend()
axes[1].hist(df_original["Value2"], bins=20, alpha=0.5, label="Original")
axes[1].hist(df_new["Value2"], bins=20, alpha=0.5, label="New")
axes[1].set_title("Value2 Distribution")
axes[1].legend()
plt.show()
