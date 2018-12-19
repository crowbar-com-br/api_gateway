import	json
from	conx	import connex

def receiveToken(request, body, keys, url, msSlug, slug):
	import	app
	import requests
	from falcon import HTTPUnauthorized
	from	ms				import microService

	microServices	= app.load() # Let's load the list of MS we have
	body			= json.loads(body)

	for ms in microServices: # Let's find if we have the requested
		if (ms['slug'] == msSlug):
			url			= microService.getURL(ms) # Let's get the best URL of the requested MS
			publicKey	= body['publicKey'] # Let's get the requester Public Key
			data		= connex.receiveRequest(request, body, keys) # Okay, let's decrypt our received request
			response	= connex.sendRequest(url, slug, keys, data['headers'], data['payload'], data['content']) # Let's encrypt and request the designed MS
			data		= connex.receiveResponse(keys, response) # Now decrypt the response received from the MS
			return data['content']['status']

	return None

def checkToken(token, keys, url):
	import app

	payload		= {
		"Authorization"	: token
	}

	response	= app.sendRequest(
		url,
		"/services/authentication/statusToken",
		keys,
		"",
		payload,
		{"":""},
		""
	)
	print(response.text)
	return		connex.receiveResponse(keys, response)

def hug_checkToken(token):
	import	requests

	if 'Bearer' in token:
		url = "http://localhost:8080/token_authenticated"

		headers = {
			'cache-control': "no-cache",
			'Authorization': token.replace('Bearer ', '')
		}

		response = requests.request("GET", url, headers=headers)
		if response.status_code == 200:
			return True
		else:
			return False
	else:
		return False
