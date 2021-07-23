import pandas as pd
import plotly.graph_objects as gob
import csv


file = pd.read_csv("data.csv")

print(file.groupby("level")['attempt'].mean())

figure = gob.Figure(gob.Bar(
    x=file.groupby("level")['attempt'].mean(),
    y=["Level 1","Level 2","Level 3","Level 4"],
    orientation = "h"
))

figure.show()

