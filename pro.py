import pandas as pd
import plotly.figure_factory as ff
import csv

df=pd.read_csv(r"data.csv")

fig=ff.create_distplot([df["Avg Rating"].tolist()],["average ratings"],show_hist=False)

fig.show()
