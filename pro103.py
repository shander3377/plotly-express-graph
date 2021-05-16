import pandas as pd
import plotly.express as px

df = pd.read_csv(r"C:\Users\pankaj\Desktop\agrim\coding\c97\py\data1.csv")
fig = px.scatter(df, x="date",
 y="cases",
 color="country")
fig.show()
