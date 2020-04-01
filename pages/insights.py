# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            # Insights
            ### How to determine your mushrooms attributes.
            #### Odor:
            ##### This one is quite simple... smell our mushroom! Some smells on the dropdown list you might not be familiar with are
            ##### anise, which is a black licorice type smell, and creosote, which is like fresh-paved asphalt. 

            #### Bruises:
            ##### Cut or pinch your mushroom. Does it change color after a few seconds? This is bruising. 

            #### Spore print color:
            ##### Cut the cap off your mushroom. Set it on a white piece of paper or foil and put a cup upsidedown over the cap.
            ##### Leave it for 2-24 hours depending on freshness of the cap. After waiting remove the cup and cap and you'll 
            ##### have a spore print left on the paper or foil. 

            #### Gill size:
            ##### This one is a little tricky. If the gills on the mushroom are about the thickness of a piece of paper they are narrow.
            ##### If the gills are thick like 2 credit cards stacked, then they are broad.

            


            """
        ),

    ],
)

layout = dbc.Row([column1])