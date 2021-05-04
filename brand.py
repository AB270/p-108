import plotly.figure_factory as ff
import csv
import pandas as pd

df = pd.read_csv("data.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"])
fig.show()