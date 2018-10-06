import urllib, json
import requests
with krbContext(using_keytab=True, principal='...', keytab_file='...'):
	url1 = "http://maps.googleapis.com/maps/api/geocode/json?address=googleplex&sensor=false"
	url = "http://maps.googleapis.com/maps/api/geocode/json?"

	print url
	r = requests.get(url)

	print r.json()
	print type(r)