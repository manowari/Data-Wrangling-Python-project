# Correlation Analysis
correlation_matrix = df.corr()
print(correlation_matrix)

# Visualize the correlation matrix
import seaborn as sns

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Unique Values in Each Column
for column in df.columns:
    unique_values = df[column].nunique()
    print(f'Unique values in {column}: {unique_values}')

# Value Counts for Categorical Variables
for column in df.select_dtypes(include=['object']).columns:
    print(df[column].value_counts())

# Check for Outliers using Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df['numerical_column'])
plt.title('Boxplot of Numerical Column')
plt.show()

# Distribution of a Specific Numerical Column
plt.figure(figsize=(10, 6))
sns.histplot(df['numerical_column'], bins=30, kde=True)
plt.title('Distribution of Numerical Column')
plt.xlabel('Numerical Column')
plt.ylabel('Frequency')
plt.show()

# Grouped Bar Plot for Categorical Data
grouped_data = df.groupby('categorical_column')['numerical_column'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='categorical_column', y='numerical_column', data=grouped_data)
plt.title('Mean of Numerical Column by Categorical Column')
plt.xticks(rotation=45)
plt.show()

# Time Series Analysis: Plotting the Trend
df['numerical_column'].plot(figsize=(12, 6))
plt.title('Trend of Numerical Column Over Time')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()

# Summary Statistics by Group
group_summary = df.groupby('categorical_column').agg(['mean', 'median', 'std'])
print(group_summary)
