#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from chart_studio import plotly as py
from haversine import haversine, Unit, inverse_haversine
import plotly.graph_objects as go
import plotly.express as px
import urllib.parse
import requests, math, random
import streamlit as st
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from sqlalchemy import create_engine



## PART 1 - Intro

st.write('''
# Let us help you find your next apartment!
Did you get a new job? Are you considering moving closer to work? Will paying more for an apartment closer to work to reduce your commute time actually make sense financially? Let us help you answer that question!
In the fields below, enter an address for your new job location and we will locate apartments in that area categorized by commute time. Be sure to spell everything correctly! The form is case-insensitive.

Note, this version is a proof-of-concept using a combination of real and randomly generated rental listings for the Arlington, VA area. The final version will use actual listings from a real estate website like [apartments.com](https://www.apartments.com) for any area.
''')


# PART 2 - Get user's target location, speed, hourly wage

st.write(
'''
## Enter your workplace location in the fields below.

''')

with st.form(key='user_info'):
    street = st.text_input('Street', max_chars=100, value='932 N Kenmore St')
    city = st.text_input('City', max_chars=100, value='Arlington')
    state = st.text_input('State', max_chars=2, value='VA')
    zipcode = st.text_input('Zip', max_chars=5, value='22201')

    address = street + ' ' + city + ' ' + state + ' ' + zipcode

    st.write(
    '''
    ## Enter your hourly wage ($ per hour)
    This will let us determine how much your time spent commuting is worth to you. The more time you spend commuting, the higher your effective rent will be.
    ''')

    hourly_income = st.number_input('Hourly wage', value=40)

    # st.write('''
    # ## Enter your anticipated average commuting speed
    # The default is 40 mph.
    # ''')

    # speed = st.number_input('Speed', min_value=1, max_value=70, value=40)

    mode = st.radio('How will you get to work?', ('Drive', 'Bike', 'Walk'))
    mode = mode.replace('Drive', 'driving').replace('Walk', 'walking').replace('Bike', 'cycling')

    st.write('''
    ## Select your desired range of rents
    The search will increase the rent based on the time required to commute to your set job location.
    ''')

    rental_range = st.slider('Range of rents', value=[1500, 3500], min_value=1400, max_value = 4000)

    apt_types = st.multiselect('Select the types of apartments to search for.', ['Studio', 'One bedroom', 'Two bedrooms'], ['Studio', 'One bedroom', 'Two bedrooms'])
    apt_types = [apt.replace('Studio', 'studio').replace('One bedroom', '1_br').replace('Two bedrooms', '2_br') for apt in apt_types]  
    
    st.write('''
        Note, you must click "Submit" to create/update the map if you make a change to the search parameters above.
    ''')

    with open('mapbox_key.txt') as f:
        mapbox_access_token = f.read().rstrip()

    submit_button = st.form_submit_button(label='Submit')

if submit_button:
# PART 3 - Generate random apartment listings. This will be replaced with real listings in the actual deployment.    
    # st.write(apt_types)
    # def generate_map_data(workplace, distance, num_points=5000):
    #     def rent_gen(kind):
    #         studio_low = 1500
    #         one_br_low = 1700
    #         two_br_low = 2200
    #         high = 1000
    #         if kind == 'studio':
    #          return np.random.randint(studio_low, studio_low + high + 1)
    #         elif kind == '1_br': 
    #          return np.random.randint(one_br_low, one_br_low + high + 1)
    #         else:
    #          return np.random.randint(two_br_low, two_br_low + high + 1)

    #     map_data = [inverse_haversine(workplace, distance*math.sqrt(random.random()), random.random()*2*math.pi, unit=Unit.MILES) for _ in range(num_points)]
    #     map_data = pd.DataFrame(map_data, columns=['lat', 'long'])
    #     map_data['type'] = [random.choice(['studio', '1_br', '2_br']) for _ in range(map_data.shape[0])]


    #     map_data['rent'] = map_data['type'].apply(lambda x: rent_gen(x))

    #     return map_data

    def get_map_data():
        engine = create_engine('sqlite:///address_data_sql.db')
        # read in random apartment data plus real data

        return pd.read_sql('SELECT * FROM address_data_sql;', engine)



    def get_geocoords(address=address):
        workplace = urllib.parse.quote(address)
        try: url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{workplace}.json?access_token={mapbox_access_token}'
        except IndexError:
            st.write('Check your address again for typos. The address must be within the immediate DC/MD/VA area.')
            return
        session = requests.session()
        location = session.get(url)
        return location.json()['features'][0]['center']

    workplace = get_geocoords(address)[::-1]

    # PART 4 - Show graph of listings

    # There is a bug in plotly where if you set the marker style, the color defaults to gray.
    # https://github.com/plotly/plotly.py/issues/2485
    # https://github.com/plotly/plotly.js/issues/2813 ('Note that the array `marker.color` and `marker.size`', are only available for *circle* symbols.')

    results = get_map_data()
    results = results[(results.rent <= rental_range[1]) & (results.rent >= rental_range[0]) & (results.type.isin(apt_types))]

    if not len(results):
        st.write(''' 
        ## No listings met your search criteria
        Consider broadening your criteria.
        ''')
    else:

        def isochrone_layer(mode, minutes, workplace=workplace): # minutes = '10,20,30'
            profile = f'mapbox/{mode}'
            coordinates = str(workplace[1]) + ',' +  str(workplace[0])
            contours_minutes = f'contours_minutes={minutes}'
            r = requests.get(f'https://api.mapbox.com/isochrone/v1/{profile}/{coordinates}?{contours_minutes}&polygons=true&access_token={mapbox_access_token}').json()
            length = len(minutes.split(','))

            polygons = [Polygon(r['features'][i]['geometry']['coordinates'][0]) for i in range(length-1, -1, -1)] # create list in order of smallest to largest polygon
            return polygons

        # Get the isochrone data
        ten_thirty_layer = isochrone_layer(mode, '10,20,30')
        forty_layer = isochrone_layer(mode, '40')

        # There is a bug in plotly where if you set the marker style, the color defaults to gray.
        # https://github.com/plotly/plotly.py/issues/2485
        # https://github.com/plotly/plotly.js/issues/2813 ('Note that the array `marker.color` and `marker.size`', are only available for *circle* symbols.')

        # create list of polygons
        polys = isochrone_layer(mode, '10,20,30') + isochrone_layer(mode, '40')    

        def create_plotly_isochrones(polygons, colors, opacity=0.15): # enter list of polygons and func will output code for plotly
            assert len(polygons) == len(colors), 'check length of inputs'
            layers = [(polygons[i] - polygons[i-1]).__geo_interface__ for i in range(len(polygons) - 1, 0, -1)]
            layers += [polygons[0].__geo_interface__]

            layers = [{'source': layers[i], 'type': 'fill', 'color': colors[i], 'opacity': opacity} for i in range(len(layers))]

            return layers

                
        def which_polygon(point, polygons): # returns bool if point in polygon. Will loop through polys from smallest to largest.
            point = Point(point) # create point
            point_found = False
            for i in range(4):
                if polygons[i].contains(point): # check if polygon contains point
                    point_found = True
                    break
            if not point_found: return 4
            else: return i    
        
        results['polygon'] = results.apply(lambda x: which_polygon([x.long, x.lat], polys), axis=1)
        results['adjusted_rent'] = (results['rent'] + (results['polygon'] +1) * 10 * 2 * 20 /60 * 40).astype('int') # 10 minute increments


        results['commute time (minutes)'] = results.apply(lambda x: '<10' if x.polygon == 0 else '10-20' if x.polygon == 1 else '20-30' if x.polygon == 2 else '30-40' if x.polygon == 3 else '>40', axis=1)

# There is a bug in plotly where if you set the marker style, the color defaults to gray.
# https://github.com/plotly/plotly.py/issues/2485
# https://github.com/plotly/plotly.js/issues/2813 ('Note that the array `marker.color` and `marker.size`', are only available for *circle* symbols.')
# https://stackoverflow.com/questions/59628536/option-symbol-in-scattermapbox-is-not-working
# https://plotly.com/python/reference/scattermapbox/ Sets the marker symbol. Full list: https://www.mapbox.com/maki-icons/ Note that the array `marker.color` and `marker.size` are only available for "circle" symbols.

        results.rename(columns={'polygon':'zone'}, inplace=True)

        px.set_mapbox_access_token(mapbox_access_token)
        fig = px.scatter_mapbox(results, lat="lat", lon="long", hover_name="type", hover_data=["rent", "zone", "random_real"],
                                color="adjusted_rent", zoom=12, height=600)

        fig.update_layout(mapbox_style="light")
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

        fig.add_trace(go.Scattermapbox(
                lat=[workplace[0]],
                lon=[workplace[1]],
                marker=go.scattermapbox.Marker(
                size=25,
                color='red',          
                ),
                marker_symbol = 'star',
                hoverinfo = 'none',
                showlegend = False
                )  
            )

        fig.update_layout(
            mapbox = {
                'style': "light",
                'center': { 'lon': workplace[1], 'lat': workplace[0]},
                'zoom': 12, 'layers': create_plotly_isochrones(polys, ['blue', 'red', 'yellow', 'green'], 0.1) # enter colors from largest to smallest isochrone
            },
            margin = {'l':0, 'r':0, 'b':0, 't':0})

        st.plotly_chart(fig) 

       
        results = results.sort_values('adjusted_rent').groupby('commute time (minutes)').head(3)
        results.index = results.groupby('zone').cumcount() + 1
        results.drop('zone', axis=1, inplace=True)
        results = results.reset_index().rename(columns = {'index': 'rank', 'adjusted_rent': 'effective rent'})
        results.drop('rank', axis=1, inplace=True)

        # Reorder columns to put rents next to one another
        results = results.reindex(columns=['rent', 'effective rent', 'lat', 'long', 'random_real', 'type', 'commute time (minutes)'])

        opacity = 0.15
        color_conv = {'red': f'rgba(255,0,0,{opacity})', 'blue': f'rgba(0,0,255,{opacity})', 'green': f'rgba(0,128,0,{opacity})', 
                    'yellow': f'rgba(255,255,0,{opacity})', 'grey': f'rgb(240, 240, 240, {opacity})'}
        time_conv = {'green': '<10', 'yellow': '10-20', 'red': '20-30', 'blue': '30-40', 'grey': '>40'}

        s='''
            green, yellow, red, blue, grey
            '''
        li=s.split(',')
        li=[l.replace('\n','') for l in li]
        li=[l.replace(' ','') for l in li]

        # import pandas as pd
        # import plotly.graph_objects as go

        df=pd.DataFrame.from_dict({'colour': li})
        df['rgba'] = df.colour.map(color_conv)
        df['time'] = df.colour.map(time_conv)

        color_fig = go.Figure(data=[go.Table(
        header=dict(
            values=["Commute times (minutes)"],
            line_color='black', fill_color='white',
            align='center', font=dict(color='black', size=14)
        ),
        cells=dict(
            values=[df.time],
            line_color=['black'], fill_color=[df.rgba],
            align='center', font=dict(color='black', size=11)
        ))
        ])
        color_fig.update_layout(width=400, height=240, margin=dict(t=0, b=0, pad=0))
        st.plotly_chart(color_fig)

        st.write('''
                ## The three cheapest apartments for each commute length
                ''')
                

        # CSS to inject contained in a string
        hide_table_row_index = """
                    <style>
                    tbody th {display:none}
                    .blank {display:none}
                    </style>
                    """

        # Inject CSS with Markdown
        st.markdown(hide_table_row_index, unsafe_allow_html=True)

        st.table(results)

        st.write('''
        ## Future work
        The final version will use data scraped from a real estate listings site such as [apartments.com](https://www.apartments.com). You will see addresses in the table above instead of latitude and longitude.
        '''
        )




            