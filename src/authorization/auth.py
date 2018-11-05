class Authorization:
	"""The class for the authentication micro-service"""
	token	= ""

	def __init__(self, token):
		self.token	= token

def getToken(username, password):
	import	requests

	url = "http://localhost:8080/getToken"

	headers = {
		'cache-control': "no-cache"
	}

	payload = {
		'username':	username,
		'password':	password
	}

	response = requests.request("POST", url, headers=headers, data=payload)
	return response.text
