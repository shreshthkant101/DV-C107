import pandas as pd
import plotly.graph_objects as gob
import csv


file = pd.read_csv("data.csv")

student = file.loc[file['student_id'] == "TRL_zet"]


f = gob.Figure(gob.Bar(
    x= ["Level 1","Level 2","Level 3","Level 4"],
    y= student.groupby("level")["attempt"].mean(),
    orientation="v"
))


f.show()


"""
ids= pd.unique(file['student_id'])

count = pd.value_counts(ids)



"""