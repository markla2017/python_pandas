import pandas as pd

# Wczytaj plik excel
df_sales = pd.read_excel('files\supermarket_sales.xlsx')
print(df_sales)

# pivot table, aggregate function for two columns
print(df_sales.pivot_table(index="Gender", 
                           values=["Quantity", "Total"],
                           aggfunc="sum"))

# pivot table, that says how much male and female spend in each 
print(df_sales.pivot_table(index="Gender", 
                           columns="Product line",
                           values="Total",
                           aggfunc="sum"))