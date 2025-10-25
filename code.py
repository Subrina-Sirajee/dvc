import pandas as pd
import os

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
    }

df = pd.DataFrame(data)

new_row_loc = pd.DataFrame({'Name': ['Subrina'], 'Age': [25], 'City': ['Dhaka']})
df.loc[len(df)] = new_row_loc.loc[0]
data_dir='data'
os.makedirs(data_dir, exist_ok=True)
file_path=os.path.join(data_dir, 'sample_data.csv')
df.to_csv(file_path, index=False)
print(f"CSV file saved to {file_path}")