import datetime 
import plotly.graph_objs as go

print("okay")
latitudes = []
longitudes = []
#+CGPSINFO: 8132.330713,N,12388.243804,W,120323,211021.0,120.3,0.0,0.0
with open('gpsreturn2.txt', 'r') as textr:

    for line in textr:
        if line.startswith("+CGPSINFO"):
           # print(line)
            strip = line.replace("+CGPSINFO: ", "")
            gpsreturn = strip
            gpsfields = gpsreturn.split(",")
            ##convert into DDM format
            print(line)
            print(strip)
            try:
                latitude = float(gpsfields[0][:2]) + float(gpsfields[0][2:])/60
                if gpsfields[1] == 'S':
                    latitude = -latitude
                longitude = float(gpsfields[2][:3]) + float(gpsfields[2][3:])/60 
                if gpsfields[3] == 'W':
                    longitude = -longitude
            except:
                print("no data")

           # print("lat:",latitude)
           # print("long:", longitude)
            latitudes.append((latitude))
            longitudes.append((longitude))


            trace = go.Scattermapbox(
                lat=latitudes,
                lon=longitudes,
                mode='markers',
                marker=dict(
                    size=9,
                    color='blue',
                    opacity=0.7
                ),
            )

            # Create the layout for the plot
            layout = go.Layout(
                #mapbox_style="white-bg",
                mapbox_style="open-street-map",
                #mapbox_layers=[
                #    {
                #        "below": 'traces',
                #        "sourcetype": "raster",
                #        "sourceattribution": "United States Geological Survey",
                #        "source": [
                #            "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                #        ]
                #    }
                #])
            )


            gpstimef=gpsfields[4] + ',' + gpsfields[5]
        if line.startswith("+202"):
            # Parse the gpstime value as a time object
            try:
                gpstime = datetime.datetime.strptime(str(gpstimef), '%d%m%y,%H%M%S.%f')
            except:
                print("add error here")
            # Format the time object as a string in the same format as clocktime
            #gpstime_formatted = time_obj.strftime('%H:%M:%S')

         #   print("GPStime:",gpstime)
         #   print("Clocktime:",line)
            #print("GPSTime: ", gpstime)

# Create the figure object and add the trace and layout
fig = go.Figure(data=[trace], layout=layout)

# Show the plot
fig.show()


   #     if line.strip():
   #         with open('cleanreturn.txt','a') as texta:
   #             texta.write(line)
