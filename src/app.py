import	hug
import	json
import	os
import	requests
from	authorization	import auth
from	conx			import connex
from	cryption		import cryptKey
from	ms				import microService

api 	= hug.get(on_invalid=hug.redirect.not_found)
keys 	= cryptKey.Key()

def save(data):
	file = open("./.cache/data_file.json", "r+")
	file_open = file.read()
	if (isJSON(file_open)):
		content = json.loads(file_open)
	else:
		content = []
	content.append(data)
	file.close()
	open("./.cache/data_file.json", "w").close()
	file = open("./.cache/data_file.json", "r+")
	file.write(json.dumps(content))
	file.close()

def load():
	if not os.path.exists('./.cache/data_file.json'):
		with open("./.cache/data_file.json", "w") as file:
			file.write("[]")
			file.close()
		return load()
	else:
		with open("./.cache/data_file.json", "r") as read_file:
			data = json.load(read_file)
		return data

@api.get(
	'/services',
	version=1
)
def microServices():
	return load()

@api.post(
	'/create',
	version=1,
	examples='name=API&description=Description&slug=api_gateway&url=http://www.somethi.ng'
)
def createMicroService(
	name,
	description,
	slug,
	url,
	response
):
	"""Create a new MicroService"""
	ms	= microService.MicroService(name, description, slug, [url])
	save(ms.__dict__)
	return ms.__dict__

def ms_get(msSlug, slug):
	microServices	= load() # Get a list of our MSs
	for ms in microServices:
		if (ms['slug'] == msSlug):
			url	= microService.getURL(ms) # Get the best URL of this MS
			return json.loads(requests.request("GET", url + slug).text) # Make a GET request to this MS
	hug.redirect.not_found() #Uho, we don't have this MS

def ms_post(msSlug, slug, body, request):
	microServices	= load() # Let's load the list of MS we have
	body			= json.loads(body)

	for ms in microServices: # Let's find if we have the requested
		if (ms['slug'] == msSlug):
			url			= microService.getURL(ms) # Let's get the best URL of the requested MS
			return json.loads(requests.request("POST", url + slug, body).text)
	hug.redirect.not_found() # Oho, we don't have the requested MS

@api.get(
	'/services/{ms}',
	version	=	1,
	examples=	'http://localhost:8000/services/api_gateway'
)
def getMS(ms: "A String slug of the MS you're loking for"):
	"""Return the requested Micro-Service"""
	return ms_get(ms, "")

@api.get(
	'/services/{ms}/{slug}',
	version	=	1,
	examples=	'http://localhost:8000/services/api_gateway'
)
def getMSs(ms: "A String slug of the MS you're loking for", slug: "The slug of the option in the ms"):
	"""Return the requested Micro-Service"""
	slug	= "/" + slug
	return ms_get(ms, slug)
# TODO: THIS IS RIDICULOUS, PLEASE, FIND A BETTER WAY!!
@api.get(
	'/services/{ms}/{slug}/{one}',
	version	=	1,
)
def getMSs_one(ms, slug, one):
	slug	= "/" + slug + "/" + one
	return ms_get(ms, slug)

@api.get(
	'/services/{ms}/{slug}/{one}/{two}',
	version	=	1
)
def getMSs_two(ms, slug, one, two):
	slug	= "/" + slug + "/" + one + "/" + two
	return ms_get(ms, slug)

@api.get(
	'/services/{ms}/{slug}/{one}/{two}/{three}',
	version	=	1
)
def getMSs_three(ms, slug, one, two, three):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three
	return ms_get(ms, slug)

@api.get(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}',
	version	=	1
)
def getMSs_four(ms, slug, one, two, three, four):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four
	return ms_get(ms, slug)

@api.get(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}/{five}',
	version	=	1
)
def getMSs_five(ms, slug, one, two, three, four, five):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four + "/" + five
	return ms_get(ms, slug)

@api.get(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}/{five}/{six}',
	version	=	1
)
def getMSs_six(ms, slug, one, two, three, four, five, six):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four + "/" + five + "/" + six
	return ms_get(ms, slug)

@api.get(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}/{five}/{six}/{seven}',
	version	=	1
)
def getMSs_seven(ms, slug, one, two, three, four, five, six, seven):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four + "/" + five + "/" + six + "/" + seven
	return ms_get(ms, slug)

@api.get(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}/{five}/{six}/{seven}/{eight}',
	version	=	1
)
def getMSs_eight(ms, slug, one, two, three, four, five, six, seven, eight):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four + "/" + five + "/" + six + "/" + seven + "/" + eight
	return ms_get(ms, slug)

@api.get(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}/{five}/{six}/{seven}/{eight}/{nine}',
	version	=	1
)
def getMSs_nine(ms, slug, one, two, three, four, five, six, seven, eight, nine):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four + "/" + five + "/" + six + "/" + seven + "/" + eight + "/" + nine
	return ms_get(ms, slug)

@api.get(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}/{five}/{six}/{seven}/{eight}/{nine}/{ten}',
	version	=	1
)
def getMSs_ten(ms, slug, one, two, three, four, five, six, seven, eight, nine, ten):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four + "/" + five + "/" + six + "/" + seven + "/" + eight + "/" + nine + "/" + ten
	return ms_get(ms, slug)

# def getMS(msSlug, slug):
# 	import requests
# 	microServices	= load() # Get a list of our MSs
# 	for ms in microServices:
# 		if (ms['slug'] == msSlug):
# 			url	= microService.getURL(ms) # Get the best URL of this MS
# 			return json.loads(requests.request("GET", url + slug).text) # Make a GET request to this MS
# 	hug.redirect.not_found() #Uho, we don't have this MS

@api.post(
	'/services/{ms}/{slug}',
	version	=	1,
	examples=	'http://localhost:8000/services/api_gateway'
)
def postMSs(ms: "A String slug of the MS you're loking for", slug: "The slug of the option in the ms", body, request):
	"""Return the requested Micro-Service"""
	slug	= "/" + slug
	return ms_post(ms, slug, body, request)

@api.post(
	'/services/{ms}/{slug}/{one}',
	version	=	1,
)
def postMSs_one(ms, slug, body, request, one):
	slug	= "/" + slug + "/" + one
	return ms_post(ms, slug, body, request)

@api.post(
	'/services/{ms}/{slug}/{one}/{two}',
	version	=	1
)
def postMSs_two(ms, slug, body, request, one, two):
	slug	= "/" + slug + "/" + one + "/" + two
	return ms_post(ms, slug, body, request)

@api.post(
	'/services/{ms}/{slug}/{one}/{two}/{three}',
	version	=	1
)
def postMSs_three(ms, slug, body, request, one, two, three):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three
	return ms_post(ms, slug, body, request)

@api.post(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}',
	version	=	1
)
def postMSs_four(ms, slug, body, request, one, two, three, four):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four
	return ms_post(ms, slug, body, request)

@api.post(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}/{five}',
	version	=	1
)
def postMSs_five(ms, slug, body, request, one, two, three, four, five):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four + "/" + five
	return ms_post(ms, slug, body, request)

@api.post(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}/{five}/{six}',
	version	=	1
)
def postMSs_six(ms, slug, body, request, one, two, three, four, five, six):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four + "/" + five + "/" + six
	return ms_post(ms, slug, body, request)

@api.post(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}/{five}/{six}/{seven}',
	version	=	1
)
def postMSs_seven(ms, slug, body, request, one, two, three, four, five, six, seven):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four + "/" + five + "/" + six + "/" + seven
	return ms_post(ms, slug, body, request)

@api.post(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}/{five}/{six}/{seven}/{eight}',
	version	=	1
)
def postMSs_eight(ms, slug, body, request, one, two, three, four, five, six, seven, eight):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four + "/" + five + "/" + six + "/" + seven + "/" + eight
	return ms_post(ms, slug, body, request)

@api.post(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}/{five}/{six}/{seven}/{eight}/{nine}',
	version	=	1
)
def postMSs_nine(ms, slug, body, request, one, two, three, four, five, six, seven, eight, nine):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four + "/" + five + "/" + six + "/" + seven + "/" + eight + "/" + nine
	return ms_post(ms, slug, body, request)

@api.post(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}/{five}/{six}/{seven}/{eight}/{nine}/{ten}',
	version	=	1
)
def postMSs_ten(ms, slug, body, request, one, two, three, four, five, six, seven, eight, nine, ten):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four + "/" + five + "/" + six + "/" + seven + "/" + eight + "/" + nine + "/" + ten
	return ms_post(ms, slug, body, request)

# def postMS(msSlug, slug, body, request): # Disabled for now
# 	import requests
#
# 	microServices	= load() # Let's load the list of MS we have
# 	body			= json.loads(body)
#
# 	for ms in microServices: # Let's find if we have the requested
# 		if (ms['slug'] == msSlug):
# 			url			= microService.getURL(ms) # Let's get the best URL of the requested MS
# 			publicKey	= body['publicKey'] # Let's get the requester Public Key
# 			data		= connex.receiveRequest(request, body, keys) # Okay, let's decrypt our received request
# 			response	= connex.sendRequest(url, slug, keys, data['headers'], data['payload'], data['content']) # Let's encrypt and request the designed MS
# 			data		= connex.receiveResponse(keys, response) # Now decrypt the response received from the MS
# 			return		  connex.sendResponse(keys, data['payload'], data['content'], publicKey) # And now, let's return a encrypted response to the requester
# 	hug.redirect.not_found() # Oho, we don't have the requested MS

@api.get(
	'/publicKey',
	version=1
)
def getPublicKey():
	"""Returns the public key of this Micro-Service"""
	return {
		'publicKey'	: cryptKey.savePublic(keys.public)
	}

@api.get(
	'/status',
	version=1
)
def getStatus():
	"""Returns the actual status of this MS server"""
	import psutil
	return {
		'CPU'	: psutil.cpu_percent(),
		'Memory': psutil.virtual_memory()[2]
	}

def isJSON(content: "A expected JSON"):
	"""Check if the param content can be a JSON"""
	try:
		object = json.loads(content)
	except:
		return False
	return True
