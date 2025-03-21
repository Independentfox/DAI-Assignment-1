# DAI-Assignment-1
Titanic Dataset Analysis Report

Introduction

The Titanic dataset provides information about passengers aboard the Titanic, including demographics, ticket details, and survival status. This analysis focuses on data cleaning and exploratory data analysis (EDA) to uncover insights into passenger attributes and relationships.

Data Cleaning

1. Handling Missing Values

The age column had missing values, which were filled with the median age.

The embark_town column had missing values, which were replaced with the mode (most frequent value).

The deck column had excessive missing values and was removed.

2. Removing Duplicates

Duplicate records were checked and removed to ensure data integrity.

3. Detecting and Handling Outliers

The fare column had extreme outliers, which were identified using the Interquartile Range (IQR) method and removed.

Exploratory Data Analysis (EDA)

1. Univariate Analysis

Age Distribution: A histogram showed that the majority of passengers were between 20-40 years old, with a peak around 30.

Fare Distribution: Most passengers paid fares below 100, with a few outliers paying significantly more.

Survival Rate: About 38% of passengers survived.

2. Bivariate Analysis

Age vs. Gender: A boxplot showed that the median age of male and female passengers was similar, but males had a wider age distribution.

Survival by Gender: A higher proportion of females survived compared to males.

3. Multivariate Analysis

Correlation Heatmap:

Fare had a positive correlation with survival, indicating higher-class passengers had better survival chances.

Pclass (passenger class) had a negative correlation with survival, suggesting first-class passengers were more likely to survive.

Conclusion

This analysis cleaned the dataset by addressing missing values, removing duplicates, and handling outliers. EDA revealed significant trends, such as a higher survival rate among females and first-class passengers. The findings suggest that socio-economic factors played a crucial role in survival probabilities during the Titanic disaster.

Next Steps

Perform predictive modeling to classify survival chances based on passenger attributes.

Further explore interactions between multiple variables, such as age, class, and fare, using machine learning techniques.
