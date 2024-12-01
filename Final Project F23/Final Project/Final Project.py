# Tariro Musarandega
#
# CS 140 Final Project: World Map
#
# Resources:
# Dr Lee
# PQRC
# Plotly Website
# Geopandas Website
# https://www.youtube.com/watch?v=aJmaw3QKMvk
# https://www.youtube.com/watch?v=Q0z1cPD_7yE
# https://www.youtube.com/watch?v=T_DbNmDTdpU

import plotly. express as px
import geopandas as gpd
import pandas as pd
import plotly.graph_objects as go

# Load GeoJSON file for countries and ask geopandas to read the file
countries = gpd.read_file("countries.geojson")

# Load CSV file for exports data and ask pandas to read the file
mainExports = pd.read_csv("exports-by-country-2023.csv")

# check for null data
# print(mainExports.isnull().sum())

# Merge the two data files using the iso a3 codes of countries
mergedData = countries.merge(mainExports, left_on=["ISO_A3"], right_on=["cca3"])

# check if the data merged well
# print(mergedData)

mergedData.set_index(["ISO_A3"], inplace=True)

# draw the choropleth map
fig = px.choropleth(
    mergedData,
    geojson=mergedData.geometry,
    locations=mergedData.index,
    # color the countries based on their export's classification
    color=mergedData["Export Class"],
    # choose an interesting presentation of the map
    projection="orthographic",
    # input the data that will be displayed by the hover feature
    hover_name="Country Name",
    hover_data=["Subregion", "Main Export 2020", "Total value of Main Export exported in 2020 ($USD Billion)"])

# update the map title and position
fig.update_layout(
    title_text="World Trade Map",
    title_x=0.5,
    title_y=0.95,
    margin={"r": 0, "t": 50, "l": 0, "b": 0})

# generate country name text as scatter points and position them at the center of countries' geometry
countryNames = go.Scattergeo(
    lon=mergedData.geometry.centroid.x,
    lat=mergedData.geometry.centroid.y,
    text=mergedData['Country Name'],
    mode='text',
    textfont=dict(size=8, color='black'),
    showlegend=False,
    hoverinfo="none")

# add the country names to the map
fig.add_trace(countryNames)

# generate fun looking features to add to the map
fig.update_geos(
    bgcolor='black',
    showland=True,
    landcolor='white',
    showcoastlines=True,
    coastlinecolor='gray',
    showocean=True,
    oceancolor="lightblue",)

# add the features to the map
fig.update_traces(marker=dict(line=dict(width=0.5, color='white')))

# Add lines connecting main trade partners using a for loop
for index, row in mergedData.iterrows():
    # specify the row that contains the main trade partner ISO A3 codes
    mainTradePartnerIso = row['Main Trade Partner']

    # use a conditional statement to choose cells that are not null to counter errors in the data
    if pd.notnull(mainTradePartnerIso):
        # locate the center of the main trade partner country in the merged data
        mainTradePartnerCoords = mergedData.loc[mainTradePartnerIso].geometry.centroid

        # Use trade volume to set line width
        # convert the trade volume to numerica values to counter error messages that occurred
        tradeVolume = pd.to_numeric(row["Volume of Trade ($USD Billions)"],  errors='coerce')

        # use conditional statement in case some data cells are null or have invalid values
        if not pd.isnull(tradeVolume):
            # use trade volume to determine line width and adjust by .01 for aesthetic reasons
            lineWidth = tradeVolume * 0.01

            # generate the lines that connect main trade partners of trade volume width
            line_trace = go.Scattergeo(
                lon=[row.geometry.centroid.x, mainTradePartnerCoords.x],
                lat=[row.geometry.centroid.y, mainTradePartnerCoords.y],
                mode='lines',
                line=dict(width=lineWidth, color='black'),
                showlegend=False,
                hoverinfo="text",
                text=f"Main Trade Partner ISO: {mainTradePartnerIso}<br>Trade Volume: {tradeVolume:.2f}B")
            fig.add_trace(line_trace)

# add lines of longitude and latitude to the map for a realistic look
fig.update_geos(lataxis_showgrid=True, lonaxis_showgrid=True)

# update the map's size and margins for the best presentation and adjust top to allow the map title to show
fig.update_layout(height=500, margin={"r": 0, "t": 75, "l": 0, "b": 0})


# Show the interactive plot
fig.show()


















