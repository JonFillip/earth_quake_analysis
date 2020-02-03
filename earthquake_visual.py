import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = "/Users/johnphillip/PycharmProjects/earth_quake_analysis/data" \
           "/eq_data_1_day_m1.json"

with open(filename) as file_object:
    eq_data = json.load(file_object)

eq_dicts = eq_data['features']

# Extracting Magnitudes
mags, longs, lats = [], [], []
for eq_dict in eq_dicts:
    try:
        mag = eq_dict['properties']['mag']
        long = eq_dict['geometry']['coordinates'][0]
        lat = eq_dict['geometry']['coordinates'][1]
    except ValueError:
        print("Value not found for this data key.")
    else:
        mags.append(mag)
        longs.append(long)
        lats.append(lat)

# Map the earthquakes.
data = [Scattergeo(lon=longs, lat=lats)]
my_layout = Layout(title='Global Earthquakes')

# Style the plot
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='eq_html_plots/global_earthquakes_visualization.html')
