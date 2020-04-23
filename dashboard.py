# Importing libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas
import plotly.graph_objs as go

# initializing the dash class
app = dash.Dash()

# import data
df = pandas.read_csv('insurance.csv')
print(df)

app.layout = html.Div([
    dcc.Graph(
        id='bmi-vs-charges',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['region'] == i]['bmi'],
                    y=df[df['region'] == i]['charges'],
                    text=[df['region'] == i],
                    mode='markers',
                    opacity=0.8,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.region.unique()
            ],
            'layout': go.Layout(
                xaxis={'title': 'BMI'},
                yaxis={'title': 'Charges'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    ),
    dcc.Graph(
        id='children-vs-charges',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['region'] == i]['children'],
                    y=df[df['region'] == i]['charges'],
                    text=[df['region'] == i],
                    mode='markers',
                    opacity=0.8,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.region.unique()
            ],
            'layout': go.Layout(
                xaxis={'title': 'Children'},
                yaxis={'title': 'Charges'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    ),
    dcc.Graph(
        id='age-vs-charges',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['region'] == i]['age'],
                    y=df[df['region'] == i]['charges'],
                    text=[df['region'] == i],
                    mode='markers',
                    opacity=0.8,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.region.unique()
            ],
            'layout': go.Layout(
                xaxis={'title': 'Age'},
                yaxis={'title': 'Charges'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
