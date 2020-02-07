import json

filename = "/Users/johnphillip/PycharmProjects/earth_quake_analysis/data" \
           "/latest_eq_data_30_m1.json"
with open(filename) as f:
    new_file = json.load(f)
# Make eq_data_30_day_m1.json more readable

readable_file = '/Users/johnphillip/PycharmProjects/earth_quake_analysis/data' \
                '/ready_record.json'
with open(readable_file, 'w') as obj:
    json.dump(new_file, obj, indent=4)
