import pandas as pd
import csv

# list of countries not eligible for the whitelisting process
countries = ['United States of America', 'United States', 'USA', 'America', 'Cuba', 'North Korea', 'Timor-Leste', 'Timor Leste' 'Cambodia', 'Laos', 'Tanzania', 'Serbia', 'Tunisia', 'Uganda', 'Mali', 'Pakistan', 'Afghanistan', 'Somalia', 'Zimbabwe', 'Congo', 'Democratic Republic of Congo', 'Democratic Republic of the Congo', 'Malawi', 'Mozambique', 'Crimea', 'Kyrgyzstan', 'Uzbekistan', 'Turkmenistan', 'Burundi', 'Darfur', 'South Sudan', 'Sudan (Darfur)', 'Darfur', 'Republic of the Sudan', 'Sudan', 'Guinea-Bissau', 'Guinea Bissau', 'Kosovo', 'Iran', 'Iraq', 'Libya', 'Syria', 'Ethiopia', 'Yemen', 'Sri Lanka', 'Belarus', 'Venezuela']

# loading the dataset
dir = './Data/' # change this to the directory where the data is kept
df = pd.read_csv(dir + 'Dfyn WhiteList Form 1 Responses.csv') 

# dropping all entries from any of the aforementioned countries
for ind in df.index:
    country = df['Country'][ind]
    if country.lower() in (name.lower() for name in countries):
        df.drop(ind, inplace=True)
        
# dropping duplicate wallet addresses (keeping the first instance of each duplicate)
df.drop_duplicates(subset=['ERC20 Wallet Address'], keep='first', inplace=True)

df.to_csv(dir + 'Level 0 Filtered.csv')