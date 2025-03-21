import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
df = sns.load_dataset('titanic')

# Display basic info about the dataset
print("Dataset Overview:\n")
print(df.info())
print("\nFirst 5 Rows:\n", df.head())

# Data Cleaning
print("\nHandling Missing Values:")
print(df.isnull().sum())

# Fill missing values for 'age' with median
df['age'].fillna(df['age'].median(), inplace=True)

# Fill missing values for 'embark_town' with mode
df['embark_town'].fillna(df['embark_town'].mode()[0], inplace=True)

# Drop 'deck' column due to excessive missing values
df.drop(columns=['deck'], inplace=True)

# Remove duplicate entries if any
df.drop_duplicates(inplace=True)

# Detect and handle outliers using IQR
Q1 = df['fare'].quantile(0.25)
Q3 = df['fare'].quantile(0.75)
IQR = Q3 - Q1
outlier_condition = (df['fare'] < (Q1 - 1.5 * IQR)) | (df['fare'] > (Q3 + 1.5 * IQR))
df = df[~outlier_condition]

# Exploratory Data Analysis (EDA)
print("\nSummary Statistics:\n", df.describe())

# Univariate Analysis
plt.figure(figsize=(8,5))
sns.histplot(df['age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.show()

# Bivariate Analysis
plt.figure(figsize=(8,5))
sns.boxplot(x='sex', y='age', data=df)
plt.title('Age Distribution by Gender')
plt.show()

# Multivariate Analysis
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.show()

# Final Cleaned Dataset Preview
print("\nFinal Dataset Shape:", df.shape)
print(df.head())
