import pandas as pd

def Partition(input_df, dim, start_row, end_row, dataCount):
    # Get the subset of the dataframe based on the specified rows and columns
    subset_df = input_df.iloc[start_row:end_row + 1, dim:]

    # Sort the subset dataframe by its values
    sorted_df = subset_df.sort_values(by=list(subset_df.columns))

    # Update the original dataframe with the sorted values
    input_df.iloc[start_row:end_row + 1, dim:] = sorted_df.values

    # Count the number of rows for each distinct value in the dim column of input_df
    counts = sorted_df.iloc[:, 0].value_counts().sort_index().tolist()
    dataCount.extend(counts)

# Example usage:
# Create a sample DataFrame
data = {'A': [3, 1, 2], 'B': [3, 3, 4], 'C': [9, 7, 8]}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Call the Partition function to sort a portion of the DataFrame and count values
dataCount = []
Partition(df, 1, 0, 2, dataCount)

print("\nSorted DataFrame:")
print(df)

print("\nCounts:")
print(dataCount)

print(df.iloc[0, 2])
