
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# creat auxiliary files for plotting:
# paste ../data/lnumbers.txt ../data/getline_time.txt > ../data/getline.txt 
# paste ../data/lnumbers.txt ../data/getline_binsrch_time.txt > ../data/getline_binsrch.txt 

df = pd.read_table('../data/getline.txt', names=['line number', 'time'])
df_binsrch = pd.read_table('../data/getline_binsrch.txt', names=['line number', 'time'])

df = df.sort_values(by=['line number'])
df_binsrch = df_binsrch.sort_values(by=['line number'])

lin_nums = df.iloc[:,0]

trace1 = {'x': lin_nums, 
          'y': df.iloc[:,1],
          'type': 'scatter',
          'name': 'getLine',
          'mode': 'markers',
          'showlegend': True}

trace2 = {'x': lin_nums, 
          'y': df_binsrch.iloc[:,1],
          'type': 'scatter',
          'name': 'getLine_binarysearch',
          'mode': 'markers',
          'showlegend': True}

trend = px.scatter(df, x='line number', y='time', trendline='lowess')
nonlinfit = trend.data[1].y

trend = px.scatter(df_binsrch, x='line number', y='time', trendline='lowess')
nonlinfit_binsrch = trend.data[1].y

trace1fit = {'x': lin_nums, 
          'y': nonlinfit,
          'type': 'scatter',
          'name': 'getLine LOWESS fit',
          'mode': 'lines',
          'marker': {'color': 'midnightblue'},
          'showlegend': True}

trace2fit = {'x': lin_nums, 
          'y': nonlinfit_binsrch,
          'type': 'scatter',
          'name': 'getLine_binarysreach LOWESS fit',
          'mode': 'lines',
          'marker': {'color': 'crimson'},
          'showlegend': True}

layout = go.Layout({
          'xaxis': {'title': 'line number', 'rangemode': 'nonnegative'},
          'yaxis': {'title': 'time (s)', 'rangemode': 'nonnegative'}
         })

fig = go.Figure()

fig.add_trace(trace1)
fig.add_trace(trace2)
fig.add_trace(trace1fit)
fig.add_trace(trace2fit)
fig.update_layout(layout)

fig.show()

