import csv
from datetime import datetime

from plotly import offline
from plotly.graph_objs import Layout

# Set the row limit to reduce implementation time
num_row = 10000

# Open csv file and examine structure data
filename = "data/earth_fires_7days.csv"
with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    # Extract the longitude, latitude, brightness, event_title and current_date
    longs, lats, dates, brightness, hover_text = [], [], [], [], []
    row_num = 0
    for row in reader:
        try:
            current_date = datetime.strptime(row[5], '%Y-%m-%d')
            lon = row[1]
            lat = row[0]
            burn = float(row[2])
            event_title = f"{current_date.strftime('%m/%d/%y')} - {burn}"

        except ValueError:
            print(f"Data not found for {current_date}.")

        else:
            dates.append(current_date)
            longs.append(lon)
            lats.append(lat)
            brightness.append(burn)
            hover_text.append(event_title)

    # Style and map the fire events
    data = [{
        'type': 'scattergeo',
        'lon': longs,
        'lat': lats,
        'text': hover_text,
        'marker': {
            'size': [bright / 30 for bright in brightness],
            'color': brightness,
            'colorscale': 'inferno',
            'reversescale': True,
            'colorbar': {'title': 'Brightness'}

        }
    }]
    # Set the plot layout
    my_layout = Layout(title='Global Fire Chart')
    fig = {'data': data, 'layout': my_layout}

# Plot the chart.
if __name__ == "__main__":
    offline.plot(fig, filename='eq_html_plots/fire_map.html')
