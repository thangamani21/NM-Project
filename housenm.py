import pandas as pd

# Load the CSV file using a raw string to handle backslashes
df = pd.read_csv(r"C:\Users\Jacophine Susmi\Downloads\Housing.csv")

# Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Summary information
print("\nDataset Info:")
print(df.info())

# Basic statistics
print("\nStatistical Summary:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())
