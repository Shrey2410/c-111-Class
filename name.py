import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("Mean of the population is: ", mean)
print("Standard deviation of the population: ", std_deviation)

fig = ff.create_distplot([data],["Math Scores"], show_hist = False)
fig.show()