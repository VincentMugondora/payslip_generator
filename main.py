import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)

# Corrected engine name
df.to_excel("output.xlsx", index=False, engine='openpyxl')

print("Data exported to output.xlsx successfully.")
