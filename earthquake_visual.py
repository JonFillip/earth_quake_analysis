import json

from plotly import offline
from plotly.graph_objs import Layout

# Explore the structure of the data.
filename = "/Users/johnphillip/PycharmProjects/earth_quake_analysis/data" \
           "/eq_data_30_day_m1.json"

with open(filename) as file_object:
    eq_data = json.load(file_object)

eq_dicts = eq_data['features']
title = eq_data['metadata']['title']

# Extracting Magnitudes
mags, longs, lats, hover_texts = [], [], [], []
for eq_dict in eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    longs.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': longs,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5 * mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    }
}]
my_layout = Layout(title=title)

# Style the plot
fig = {'data': data, 'layout': my_layout}
offline.plot(fig,
             filename='/Users/johnphillip/PycharmProjects'
                      '/earth_quake_analysis/eq_html_plots'
                      '/global_earthquakes_30days.html')
