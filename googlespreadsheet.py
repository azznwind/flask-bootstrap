import pandas as pd

gsheetid = "1u89hD0d3ZJY73v00CipKPdcrOaPMQ1u0KUa0DUZhEQc"
sheet_name = "journal"
gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)
df = pd.read_csv(gsheet_url)
#print(df)