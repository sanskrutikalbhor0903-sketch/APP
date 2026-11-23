# ---------- 1. Import Libraries ----------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
sns.set_style("whitegrid")

# ---------- 2. Load Dataset ----------
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
print("Shape of dataset:", df.shape)
print("\nFirst 5 rows:\n", df.head())

# ---------- 3. Understand the Data ----------
print("\nDataset Info:")
df.info()

# 'TotalCharges' contains blank spaces, so convert it to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# ---------- 4. Descriptive Statistics ----------
num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']

print("\n--- Descriptive Statistics (Numerical) ---")
print(df[num_cols].describe())

print("\n--- Descriptive Statistics (Categorical) ---")
print(df.describe(include='object'))

print("\nSkewness:\n", df[num_cols].skew())
print("\nChurn Percentage:\n", df['Churn'].value_counts(normalize=True) * 100)

# ---------- 5. Handling Missing Data ----------
print("\n--- Missing Values (Before) ---")
print(df.isnull().sum())

plt.figure(figsize=(10, 4))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap (Before Cleaning)")
plt.show()

# Fill missing numerical values with median
df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())

# Remove duplicate rows (if any)
print("\nDuplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()

print("\n--- Missing Values (After) ---")
print(df.isnull().sum().sum(), "missing values remaining")

# ---------- 6. Visualization ----------
# 6.1 Univariate: Target variable
plt.figure(figsize=(5, 4))
sns.countplot(x='Churn', data=df, palette='Set2')
plt.title("Churn Distribution")
plt.show()

# 6.2 Univariate: Histograms of numerical features
df[num_cols].hist(bins=30, figsize=(12, 4), layout=(1, 3),
                  color='skyblue', edgecolor='black')
plt.suptitle("Histograms of Numerical Features")
plt.show()

# 6.3 Bivariate: Churn vs categorical features
fig, axes = plt.subplots(1, 3, figsize=(16, 4))
for ax, col in zip(axes, ['Contract', 'InternetService', 'gender']):
    sns.countplot(x=col, hue='Churn', data=df, ax=ax, palette='Set1')
    ax.set_title(f"Churn by {col}")
plt.tight_layout()
plt.show()

# 6.4 Bivariate: Churn vs numerical features
fig, axes = plt.subplots(1, 3, figsize=(16, 4))
for ax, col in zip(axes, num_cols):
    sns.boxplot(x='Churn', y=col, data=df, ax=ax, palette='Set3')
    ax.set_title(f"{col} vs Churn")
plt.tight_layout()
plt.show()

# 6.5 Multivariate: Correlation heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap")
plt.show()

# ---------- 7. Outlier Detection & Handling (IQR Method) ----------
# Boxplots before treatment
fig, axes = plt.subplots(1, 3, figsize=(14, 4))
for ax, col in zip(axes, num_cols):
    sns.boxplot(y=df[col], ax=ax, color='lightgreen')
    ax.set_title(f"{col} (Before)")
plt.tight_layout()
plt.show()

# Detect and cap outliers
print("\n--- Outlier Detection (IQR) ---")
for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    count = ((df[col] < lower) | (df[col] > upper)).sum()
    print(f"{col}: {count} outliers (Lower={lower:.2f}, Upper={upper:.2f})")

    # Capping (Winsorization)
    df[col] = np.where(df[col] < lower, lower,
              np.where(df[col] > upper, upper, df[col]))

# Boxplots after treatment
fig, axes = plt.subplots(1, 3, figsize=(14, 4))
for ax, col in zip(axes, num_cols):
    sns.boxplot(y=df[col], ax=ax, color='orange')
    ax.set_title(f"{col} (After)")
plt.tight_layout()
plt.show()

# ---------- 8. Save Cleaned Data ----------
df.drop('customerID', axis=1, inplace=True)
df.to_csv("cleaned_churn_data.csv", index=False)
print("\nCleaned dataset saved as 'cleaned_churn_data.csv'")

# ---------- 9. Key Observations ----------
print("""
OBSERVATIONS:
1. About 26-27% customers churned (imbalanced dataset).
2. Month-to-month contract customers churn the most.
3. Customers with low tenure are more likely to churn.
4. Higher monthly charges are linked with higher churn.
5. Tenure and TotalCharges are strongly positively correlated.
6. TotalCharges had 11 missing values, filled using median.
7. Outliers were checked using IQR and treated by capping.
""")
