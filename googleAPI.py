import urllib2
import sys
import traceback
import json

from settings import API_KEY, GEOCODE_LOCATION

# code for api
def get_url_location(location):
	return "{},+Nepal".format(location)


# get api url for given location
def get_api_url(location, api_key):
	api_url = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}".format(location, api_key)
	return api_url


# getting longitude and latitude from the google map api
def get_long_lat(location):
	url_location = get_url_location(location)
	formatted_location = "{}, Nepal".format(location)
	geocode = GEOCODE_LOCATION.get(location, '')
	if geocode:
		return geocode
	print "getting the longitude and latitude of {} from google api......".format(formatted_location)
	try:
		api_url = get_api_url(url_location, API_KEY)
	except Exception, err:
		print traceback.format_exc()
    
	resp = urllib2.urlopen(api_url)
	resp_dict = json.loads(resp.read())

	results = resp_dict.get('results', '')

	if results:
		for result in results:
			formatted_address = result.get('formatted_address', '')
			if formatted_address == formatted_location:
				geometry = result.get('geometry', '')
				if geometry:
					loc = result.get('geometry').get('location')
					lat = loc.get('lat')
					lng = loc.get('lng')
					geocode = "{}, {}".format(round(lat, 6), round(lng, 6))
					GEOCODE_LOCATION[location] = geocode
					return geocode
	return 'Not found in google api'
