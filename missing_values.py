# Check for Missing Values
missing_values = df.isnull().sum()
missing_percentage = (missing_values / len(df)) * 100

# Create a DataFrame for better visualization of missing values
missing_data = pd.DataFrame({
    'Missing Values': missing_values,
    'Percentage': missing_percentage
})

# Filter out columns with missing values
missing_data = missing_data[missing_data['Missing Values'] > 0]

# Display missing values information
print("Missing Values Overview:")
print(missing_data)

# Check for Duplicates
duplicate_count = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicate_count}")

# Data Types and Unique Values
data_types = df.dtypes
unique_values = df.nunique()

# Create a summary DataFrame for data types and unique values
data_quality = pd.DataFrame({
    'Data Type': data_types,
    'Unique Values': unique_values
})

print("\nData Types and Unique Values:")
print(data_quality)

# Basic Summary Statistics
summary_statistics = df.describe(include='all')
print("\nSummary Statistics:")
print(summary_statistics)
