import requests

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'

start = input('Enter the start time (YYYY-MM-DD) >>>')
end  = input('Enter the end time (YYYY-MM-DD) >>>')
lat = input('Enter the latitude of the area you are interested in (XX.XX) >>>')
lon = input('Enter the longitude (XX.XX) >>>')
maxrad = input('Enter the Max radius (km) >>>')
minmag = input('Enter the Min magnitude >>>')


response = requests.get(url, headers={'Accept': 'application/json'},params={
    'format':'geojson',
    'starttime':start,
    'endtime': end,
    'latitude':lat,
    'longitude':lon,
    'maxradiuskm':maxrad,
    'minmagnitude':minmag
})

data = response.json()
data_len = len(data['features'])

for el in range(0,data_len):
    main = data['features'][el]["properties"]

    print(el+1,". Place: ",main["place"], "; Magnitude: ",main['mag'],sep="")

