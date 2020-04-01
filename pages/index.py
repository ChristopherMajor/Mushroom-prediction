# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Poisonous or Edible?

            This app can help predict whether a mushroom from the Agaricus or Lepiota family is poisonous or edible.\n
            Input your mushrooms attributes or check out the "Insights" tab to learn more about how to determine your attributes.
            
            """
        ),
        dcc.Link(dbc.Button('Classify your mushroom', color='primary'), href='/predictions')
    ],
    md=4,
)

# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        html.Img(src='/assets/1200px-Amanita_muscaria_(fly_agaric).jpg', style ={'height': 600, 'width':400},
         className='img-fluid'),
    ]
)

layout = dbc.Row([column1, column2])