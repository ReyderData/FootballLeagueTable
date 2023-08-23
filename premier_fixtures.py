import pandas as pd
import requests

from openpyxl import load_workbook
from openpyxl import Workbook


x = 1
y = str(x)

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

tabla_sorted = []
tabla_sorted = pd.DataFrame(tabla_sorted)

while x <= 38:
  url = f'https://www.worldfootball.net/schedule/eng-premier-league-2023-2024-spieltag/{y}/'
  r = requests.get(url, headers=header)
  dfs = pd.read_html(r.text)
  df = dfs[1]
  sort_cols = df[[0,1,2,5,4]]
  sort_cols = pd.DataFrame(sort_cols)
  tabla_sorted = pd.concat([tabla_sorted, sort_cols])
  x = x + 1
  y = str(x)

tabla_sorted.columns = ["Date", "Hour", "Local", "Result", "Away"]

tabla_sorted = tabla_sorted.fillna(axis=0, method='ffill').fillna(0)

#print(tabla_sorted)
#print(tabla_sorted.shape)
#print(tabla_sorted.ndim)

#tabla_sorted[["Local Result", "Away Result"]] = tabla_sorted["Result"].str.split(' ', 3, expand=True)
tabla_sorted["Result"]= tabla_sorted["Result"].str.slice_replace(3, repl="")
tabla_sorted.loc[tabla_sorted['Result'] == "res", 'Result'] = "-:-"
#tabla_sorted
tabla_sorted[["Local Result", "Away Result"]] = tabla_sorted["Result"].str.split(':', expand=True)
tabla_sorted.loc[tabla_sorted['Local Result'] == "-", 'Local Result'] = ""
tabla_sorted.loc[tabla_sorted['Away Result'] == "-", 'Away Result'] = ""
#tabla_sorted

'''
for resultado in tabla_sorted["Result"]:
    if any(c.isdigit() for c in resultado):
        tabla_sorted[["Local Result", "Away Result"]] = tabla_sorted["Result"].str.split(':', expand=True).astype(int)
    else:
        tabla_sorted[["Local Result", "Away Result"]] = tabla_sorted["Result"]

for resultado in tabla_sorted["Result"]:
tabla_sorted[["Local Result", "Away Result"]] = tabla_sorted["Result"].str.split(':', expand=True).astype(int)

'''


tabla_sorted.to_csv('fixtures23_24.csv')
#tabla_sorted.to_excel('fixturesTEST.xlsx', sheet_name='Fixtures')

writer = pd.ExcelWriter('D:\IGNACI_STUFF\FOOTBALL\Football Results To League Table\PremierLeague_23_24.xlsx', engine='openpyxl',
                    mode='a', if_sheet_exists='overlay')

tabla_sorted.to_excel(writer, sheet_name='Pruebas',index=False, header=True)

writer.save()

