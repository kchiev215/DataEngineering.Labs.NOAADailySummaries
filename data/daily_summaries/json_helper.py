import urllib.request
import json

offset = 1
file = 0

while file < 2:
    url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=FIPS:10003&startdate=2018-01-01&enddate=2018-01-31&limit=1000&' + 'offset=' + str(offset)
    headers = {'TOKEN': 'BwEQHKXofzVilsfljZDVTimCdklIiGLh'}
    req = urllib.request.Request(url, headers=headers)
    file_name = 'daily_summaries_FIPS10003_jan_2018_j' + str(file) + '.json'
    with urllib.request.urlopen(req) as f:
        data = json.load(f)
    with open(file_name, 'w') as w:
        json.dump(data, w)
    file += 1
    offset += 1000
