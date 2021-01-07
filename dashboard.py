import pandas as pd
import numpy as np
import plotly.io as pio
import plotly.graph_objs as go
import plotly.express as px
import plotly
import plotly.offline as py
import json
from flask import Flask, render_template
from flask_cors import CORS

py.init_notebook_mode(connected=False) #True
pio.renderers.default = "browser"

app = Flask(__name__,template_folder='templates')
CORS(app)

df = pd.read_csv("covid_data.csv")
worldometer = pd.read_csv('worldometer_data.csv')

def create_plot_chart():
    df['Country,\nOther'].replace('', np.nan, inplace=True)
    df['Total\nCases'].replace('', np.nan, inplace=True)
    df.dropna(subset=['Country,\nOther'], inplace=True)
    df.dropna(subset=['Total\nCases'], inplace=True)

    trace1 = go.Bar(x=df["Country,\nOther"][0:50].dropna(), y=df["Total\nCases"],textposition='auto')
    layout = go.Layout(title="Total number of cases per country", xaxis=dict(title="Country"),
                       yaxis=dict(title="Total confirmed cases"), )
    data = [trace1]
    fig = go.Figure(data=data, layout=layout)
    fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                      marker_line_width=1.5, opacity=0.6)
    fig.update_layout(barmode='stack', yaxis={'categoryorder': 'total descending'})
    return fig
fig1 = create_plot_chart()


def create_plot_pie():
    df['Country,\nOther'].replace('', np.nan, inplace=True)
    df['Total\nCases'].replace('', np.nan, inplace=True)
    df.dropna(subset=['Country,\nOther'], inplace=True)
    df.dropna(subset=['Total\nCases'], inplace=True)
    fig_2 = go.Figure(data=[go.Pie(labels=df['Country,\nOther'][:20].dropna(), values=df['New\nDeaths'][0:20].dropna(), hole=.3)])
    fig_2.update_layout(title='Sunburst Chart')
    return fig_2
fig2 = create_plot_pie()


def create_plot_chart_2():
    df['Country,\nOther'].replace('', np.nan, inplace=True)
    df['Total\nCases'].replace('', np.nan, inplace=True)
    df.dropna(subset=['Country,\nOther'], inplace=True)
    df.dropna(subset=['Total\nCases'], inplace=True)

    trace1 = go.Bar(x=df["Country,\nOther"][0:50].dropna(), y=df["Total\nDeaths"],textposition='auto')
    layout = go.Layout(title="Total number of deaths per country", xaxis=dict(title="Country"),
                       yaxis=dict(title="Total death cases"), )
    data = [trace1]

    fig = go.Figure(data=data, layout=layout)
    fig.update_traces(marker_color='lightsalmon')

    fig.update_layout(barmode='stack', yaxis={'categoryorder': 'total descending'})
    return fig
fig3 = create_plot_chart_2()


def create_plot_4():
    df['Tests/\n1M pop'].replace('', np.nan, inplace=True)
    df['Deaths/\n1M pop'].replace('', np.nan, inplace=True)
    df.dropna(subset=['Tests/\n1M pop'], inplace=True)
    df.dropna(subset=['Deaths/\n1M pop'], inplace=True)

    data = [go.Scatter(x=df["Tests/\n1M pop"], y=df["Deaths/\n1M pop"], mode='markers')]
    layout = go.Layout(title='Correlation between N° Tests & Deaths', xaxis=dict(title='Tests/\n1M pop'),
                       yaxis=dict(title='Deaths/\n1M pop'))
    fig = go.Figure(data=data, layout=layout)
    fig.update_layout( xaxis={'categoryorder': 'total descending'},yaxis={'categoryorder': 'total descending'})
    return fig
fig4 = create_plot_4()

def create_plot_5():
    df['Country,\nOther'].replace('', np.nan, inplace=True)
    df['Tests/\n1M pop'].replace('', np.nan, inplace=True)
    df.dropna(subset=['Country,\nOther'], inplace=True)
    df.dropna(subset=['Tests/\n1M pop'], inplace=True)

    trace1 = go.Bar(x=df["Country,\nOther"][0:50].dropna(), y=df["Tests/\n1M pop"], textposition='auto')
    layout = go.Layout(title="Total number of tests/1M pop per country", xaxis=dict(title="Country"),
                       yaxis=dict(title="Number of tests/1M pop"), )
    data = [trace1]
    fig = go.Figure(data=data, layout=layout)
    fig.update_traces(marker_color='greenyellow')
    fig.update_layout(barmode='stack', yaxis={'categoryorder': 'total descending'})
    return fig
fig5 = create_plot_5()


def create_plot_6():
    df['text'] = df.apply(lambda r: "Deaths: " + str(r['Total\nDeaths']) + " Suspected: " + " " + str(r['New\nCases']), axis=1)
    country_code = pd.read_csv("countrycode.csv")
    # Convert the dataframe to dictionary
    country_code.set_index('COUNTRY', inplace=True)
    dict_country_code = country_code.to_dict()
    REPLACE_LIST = dict_country_code['CODE']
    # Replace Country with Codes
    df.replace(REPLACE_LIST, inplace=True)

    data = dict(
        type='choropleth',
        colorscale='ylorrd',
        locations=df['Country,\nOther'].values,
        z=df['Total\nCases'],
        text=df['text'],
        colorbar={'title': 'Corona Total Cases'},
    )
    layout = dict(
        title='Global Corona stats',
        geo=dict(
            showframe=False,
            projection={'type': 'natural earth'}
        )
    )
    fig = go.Figure(data=[data], layout=layout)
    return fig
fig6 = create_plot_6()


def create_plot_7():
    fig = px.pie(df, values='Total\nRecovered', names='Country,\nOther',
                 title='Percentage of Total Recovered in 20 Most Affected Countries')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    #graph1Plot = plotly.offline.plot(fig)
    return fig
fig7 = create_plot_7()

def create_plot_8():
    # Sunburst Chart using Plotly
    fig = px.sunburst(worldometer.head(50), path=['Continent', 'Country/Region', 'WHO Region'], values='Population',
                      color='ActiveCases',
                      color_continuous_scale='RdBu',
                      color_continuous_midpoint=np.average(worldometer.head(50)['Serious,Critical'],
                                                           weights=worldometer.head(50)['Population']))
    fig.update_layout(title='Sunburst Chart')
    return fig
fig8 = create_plot_8()

def create_plot_9():
    fig = px.scatter(worldometer.head(50), x="TotalCases", y="TotalDeaths", size='Population',
                     color="Continent",
                     hover_name="Country/Region", log_x=True, size_max=60)
    fig.update_layout(title='Bubble Plot for Total Cases v Total Deaths of 50 Most Affected Countries',
                      xaxis_title='Cases', yaxis_title='Deaths')
    return fig
fig9 = create_plot_9()

def create_plot_10():
    fig = px.scatter_3d(worldometer.head(20), x='TotalCases', y='TotalDeaths', z='TotalRecovered',
                        color='Country/Region')
    fig.update_layout(title='3D Plot of Total Cases, Total Deaths and Total Recovered of Top 20 Affected Countries')
    return fig
fig10 = create_plot_10()

def create_plot_11():
    fig = px.bar(worldometer.head(10), y='Tests/1M pop', x='Country/Region', color='WHO Region', height=400)
    fig.update_layout(title='Comparison of Tests/Million of 10 Most Affected Countries', xaxis_title='Country',
                      yaxis_title='Tests/Million', template="plotly_dark")
    return fig
fig11 = create_plot_11()



@app.route("/")
def index():
    figures = []
    figures.append(fig1)
    figures.append(fig2)
    figures.append(fig3)
    figures.append(fig4)
    figures.append(fig5)
    figures.append(fig6)
    figures.append(fig7)
    figures.append(fig8)
    figures.append(fig9)
    figures.append(fig10)
    figures.append(fig11)
    #figures.append(fig12)
    ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]
    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html',ids=ids,figuresJSON=figuresJSON)


if __name__ == "__main__":
    print(df)
    app.run(debug=True,  port=5000)