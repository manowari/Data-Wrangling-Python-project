import pandas as pd
import matplotlib.pyplot as plt

# Load a CSV file into a DataFrame
df = pd.read_csv('your_file.csv')

# Explore the Data
print(df.head())
print(df.info())
print(df.describe())

# Clean the Data
# Check for missing values
print(df.isnull().sum())

# Drop rows with any missing values
df_cleaned = df.dropna()

# Fill missing values with a specific value
df_filled = df.fillna(value={'column_name': 'default_value'})

# Rename columns
df.rename(columns={'old_name': 'new_name'}, inplace=True)

# Drop unnecessary columns
df.drop(columns=['unnecessary_column'], inplace=True)

# Filter data based on a condition
filtered_df = df[df['column_name'] > value]

# Group by a column and calculate the mean
grouped_df = df.groupby('column_name').mean()

# Create a new column based on existing columns
df['new_column'] = df['column1'] + df['column2']

# Sort DataFrame by a column
sorted_df = df.sort_values(by='column_name', ascending=True)

# Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv('cleaned_file.csv', index=False)

# Merge two DataFrames
merged_df = pd.merge(df1, df2, on='key_column', how='inner')

# Create a pivot table
pivot_table = df.pivot_table(values='value_column', index='index_column', columns='column_to_pivot', aggfunc='sum')

# Time Series Handling
# Convert a column to datetime
df['date_column'] = pd.to_datetime(df['date_column'])

# Set the datetime column as index
df.set_index('date_column', inplace=True)

# Resample the data to monthly mean
resampled_df = df.resample('M').mean()

# Data Visualization
df['column_name'].plot()
plt.title('Column Name over Time')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()
