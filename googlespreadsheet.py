import pandas as pd
import numpy as np

gsheetid = "1u89hD0d3ZJY73v00CipKPdcrOaPMQ1u0KUa0DUZhEQc"
sheet_name = "journal"
gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)

df = pd.read_csv(gsheet_url)
data = df.loc[:,'date entered':'buying power effect']
data = data.fillna("")
#data = df.style.set_properties(**{'text-align': 'right'})
"""
data = df.style.format({"quoted price": "${:20,.0f}", 
                          "curr price": "${:20,.0f}", 
                          "max profit": "${:20,.0f}",
                          "max loss":"${:20,.0f}"})\
                .hide_index()
"""
#print(df)