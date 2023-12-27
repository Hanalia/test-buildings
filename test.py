import pandas as pd
import json

# Path to your Excel and GeoJSON files
excel_file_path = 'result.xlsx'
geojson_file_path = '서울시아파트.json'
output_geojson_file_path = 'output_geojson_file.geojson'

# Load the Excel file
df = pd.read_excel(excel_file_path, dtype=str)

# Create a dictionary mapping BD_MGT_SN to names
bd_mgt_sn_to_name = dict(zip(df.iloc[:, 16], df.iloc[:, 15]))

print(bd_mgt_sn_to_name)

# Load the GeoJSON file
with open(geojson_file_path, 'r') as file:
    geojson_data = json.load(file)

# Filter and update GeoJSON features
filtered_features = []
for feature in geojson_data['features']:
    bd_mgt_sn = feature['properties'].get('BD_MGT_SN')
    if bd_mgt_sn in bd_mgt_sn_to_name:
        feature['properties']['NAME'] = bd_mgt_sn_to_name[bd_mgt_sn]
        filtered_features.append(feature)

# Update the GeoJSON data with filtered features
geojson_data['features'] = filtered_features

# Save the new GeoJSON file
with open(output_geojson_file_path, 'w') as file:
    json.dump(geojson_data, file)

print("GeoJSON file processed and saved as:", output_geojson_file_path)
