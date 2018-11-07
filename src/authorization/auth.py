class Authorization:
	"""The class for the authentication micro-service"""
	token	= ""

	def __init__(self, token):
		self.token	= token

def getToken(username, password):
	import	json
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
	return json.loads(response.text)

def checkToken(request):
	import	requests

	authorization = request.get_header("Authorization")

	if 'Bearer' in authorization:
		url = "http://localhost:8080/token_authenticated"

		headers = {
			'cache-control': "no-cache",
			'Authorization': authorization.replace('Bearer ', '')
		}

		response = requests.request("GET", url, headers=headers)
		return response.status_code
	else:
		return 403

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
