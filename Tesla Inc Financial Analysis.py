import pandas as pd
import numpy as np
from openpyxl import Workbook

# Data from HTML document (key metrics for 2012-2020)
data = {
    'Year': [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
    'Revenue ($M)': [413, 2013, 3200, 4046, 7000, 11759, 21461, 24578, 31536],
    'Net Income ($M)': [-396, -74, -294, -889, -675, -1962, -976, -862, 690],
    'R&D Expenses ($M)': [274, 232, 465, 718, 834, 1378, 1460, 1343, 1491],
    'PP&E ($M)': [552, 738, 1829, 3403, 5983, 10028, 11330, 20199, 23375],
    'Vehicle Production': [3100, 22500, 35000, 51095, 83922, 100757, 254530, 365232, 509737],
    'Vehicle Deliveries': [2650, 22477, 31655, 50580, 76295, 103097, 245240, 367550, 499550]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate Revenue CAGR (2012-2020)
initial_revenue = df['Revenue ($M)'][0]
final_revenue = df['Revenue ($M)'][8]
years = 2020 - 2012
cagr = (final_revenue / initial_revenue) ** (1 / years) - 1
cagr_percent = cagr * 100

# Add calculated metrics
df['Revenue Growth (%)'] = df['Revenue ($M)'].pct_change() * 100
df['Gross Margin (%)'] = [None, None, 27.6, 22.8, 22.8, 18.9, 18.8, 16.6, 21.0]  # From HTML context
df['R&D as % of Revenue'] = df['R&D Expenses ($M)'] / df['Revenue ($M)'] * 100

# Summary statistics
summary = {
    'Metric': ['Revenue CAGR (2012-2020)', '2020 Net Income ($M)', '2020 Regulatory Credits ($M)', 
              '2020 Automotive Gross Margin (%)', '2020 PP&E ($M)', '2020 Vehicle Deliveries'],
    'Value': [f'{cagr_percent:.2f}%', 690, 1600, 26, 23375, 499550]
}
summary_df = pd.DataFrame(summary)

# Export to Excel
with pd.ExcelWriter('Tesla_Financial_Analysis_2012_2020.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Financial_Operational_Data', index=False)
    summary_df.to_excel(writer, sheet_name='Summary_Stats', index=False)

print("Excel file 'Tesla_Financial_Analysis_2012_2020.xlsx' created successfully.")
print(f"Revenue CAGR (2012-2020): {cagr_percent:.2f}%")