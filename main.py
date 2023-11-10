import pandas as pd

# Wczytaj plik csv
df_gdp = pd.read_csv('files\gdp.csv')

print(df_gdp.pivot(index="year", columns="country", values="gdppc"))

