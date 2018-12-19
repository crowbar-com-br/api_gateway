import	hug
import	json
from	authorization	import auth
from	conx			import connex
from	cryption		import cryptKey
from	ms				import microService

api 				= hug.get(on_invalid=hug.redirect.not_found)
keys 				= cryptKey.Key()

def save(data):
	file = open("./cache/data_file.json", "r+")
	file_open = file.read()
	if (isJSON(file_open)):
		content = json.loads(file_open)
	else:
		content = []
	content.append(data)
	file.close()
	open("./cache/data_file.json", "w").close()
	file = open("./cache/data_file.json", "r+")
	file.write(json.dumps(content))
	file.close()

def load():
	with open("./cache/data_file.json", "r") as read_file:
		data = json.load(read_file)
	return data

@api.post(
	'/services',
	version	=	1
)
def microServices(request, body):
	"""Return the list of avaiables MicroServices"""
	if auth.receiveToken(request, body, keys, "http://localhost:8000", "authentication", "/statusToken"):
		return connex.sendResponse(keys, "", load(), json.loads(body)['publicKey'])

@api.get(
	'/services/{ms}/{slug}',
	version	=	1,
	examples=	'http://localhost:8000/services/api_gateway'
)
def getMSs(ms: "A String slug of the MS you're loking for", slug: "The slug of the option in the ms"):
	"""Return the requested Micro-Service"""
	slug	= "/" + slug
	return getMS(ms, slug)
# TODO: THIS IS RIDICULOUS, PLEASE, FIND A BETTER WAY!!
@api.get(
	'/services/{ms}/{slug}/{one}',
	version	=	1,
)
def getMSs_one(ms, slug, one):
	slug	= "/" + slug + "/" + one
	return getMS(ms, slug)

@api.get(
	'/services/{ms}/{slug}/{one}/{two}',
	version	=	1
)
def getMSs_two(ms, slug, one, two):
	slug	= "/" + slug + "/" + one + "/" + two
	return getMS(ms, slug)

@api.get(
	'/services/{ms}/{slug}/{one}/{two}/{three}',
	version	=	1
)
def getMSs_three(ms, slug, one, two, three):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three
	return getMS(ms, slug)

@api.get(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}',
	version	=	1
)
def getMSs_four(ms, slug, one, two, three, four):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four
	return getMS(ms, slug)

@api.get(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}/{five}',
	version	=	1
)
def getMSs_five(ms, slug, one, two, three, four, five):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four + "/" + five
	return getMS(ms, slug)

@api.get(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}/{five}/{six}',
	version	=	1
)
def getMSs_six(ms, slug, one, two, three, four, five, six):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four + "/" + five + "/" + six
	return getMS(ms, slug)

@api.get(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}/{five}/{six}/{seven}',
	version	=	1
)
def getMSs_seven(ms, slug, one, two, three, four, five, six, seven):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four + "/" + five + "/" + six + "/" + seven
	return getMS(ms, slug)

@api.get(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}/{five}/{six}/{seven}/{eight}',
	version	=	1
)
def getMSs_eight(ms, slug, one, two, three, four, five, six, seven, eight):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four + "/" + five + "/" + six + "/" + seven + "/" + eight
	return getMS(ms, slug)

@api.get(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}/{five}/{six}/{seven}/{eight}/{nine}',
	version	=	1
)
def getMSs_nine(ms, slug, one, two, three, four, five, six, seven, eight, nine):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four + "/" + five + "/" + six + "/" + seven + "/" + eight + "/" + nine
	return getMS(ms, slug)

@api.get(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}/{five}/{six}/{seven}/{eight}/{nine}/{ten}',
	version	=	1
)
def getMSs_ten(ms, slug, one, two, three, four, five, six, seven, eight, nine, ten):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four + "/" + five + "/" + six + "/" + seven + "/" + eight + "/" + nine + "/" + ten
	return getMS(ms, slug)

def getMS(msSlug, slug):
	import requests
	microServices	= load() # Get a list of our MSs
	for ms in microServices:
		if (ms['slug'] == msSlug):
			url	= microService.getURL(ms) # Get the best URL of this MS
			return json.loads(requests.request("GET", url + slug).text) # Make a GET request to this MS
	hug.redirect.not_found() #Uho, we don't have this MS

@api.post(
	'/services/{ms}/{slug}',
	version	=	1,
	examples=	'http://localhost:8000/services/api_gateway'
)
def postMSs(ms: "A String slug of the MS you're loking for", slug: "The slug of the option in the ms", body, request):
	"""Return the requested Micro-Service"""
	slug	= "/" + slug
	return postMS(ms, slug, body, request)

@api.post(
	'/services/{ms}/{slug}/{one}',
	version	=	1,
)
def postMSs_one(ms, slug, body, request, one):
	slug	= "/" + slug + "/" + one
	return postMS(ms, slug, body, request)

@api.post(
	'/services/{ms}/{slug}/{one}/{two}',
	version	=	1
)
def postMSs_two(ms, slug, body, request, one, two):
	slug	= "/" + slug + "/" + one + "/" + two
	return postMS(ms, slug, body, request)

@api.post(
	'/services/{ms}/{slug}/{one}/{two}/{three}',
	version	=	1
)
def postMSs_three(ms, slug, body, request, one, two, three):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three
	return postMS(ms, slug, body, request)

@api.post(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}',
	version	=	1
)
def postMSs_four(ms, slug, body, request, one, two, three, four):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four
	return postMS(ms, slug, body, request)

@api.post(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}/{five}',
	version	=	1
)
def postMSs_five(ms, slug, body, request, one, two, three, four, five):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four + "/" + five
	return postMS(ms, slug, body, request)

@api.post(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}/{five}/{six}',
	version	=	1
)
def postMSs_six(ms, slug, body, request, one, two, three, four, five, six):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four + "/" + five + "/" + six
	return postMS(ms, slug, body, request)

@api.post(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}/{five}/{six}/{seven}',
	version	=	1
)
def postMSs_seven(ms, slug, body, request, one, two, three, four, five, six, seven):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four + "/" + five + "/" + six + "/" + seven
	return postMS(ms, slug, body, request)

@api.post(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}/{five}/{six}/{seven}/{eight}',
	version	=	1
)
def postMSs_eight(ms, slug, body, request, one, two, three, four, five, six, seven, eight):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four + "/" + five + "/" + six + "/" + seven + "/" + eight
	return postMS(ms, slug, body, request)

@api.post(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}/{five}/{six}/{seven}/{eight}/{nine}',
	version	=	1
)
def postMSs_nine(ms, slug, body, request, one, two, three, four, five, six, seven, eight, nine):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four + "/" + five + "/" + six + "/" + seven + "/" + eight + "/" + nine
	return postMS(ms, slug, body, request)

@api.post(
	'/services/{ms}/{slug}/{one}/{two}/{three}/{four}/{five}/{six}/{seven}/{eight}/{nine}/{ten}',
	version	=	1
)
def postMSs_ten(ms, slug, body, request, one, two, three, four, five, six, seven, eight, nine, ten):
	slug	= "/" + slug + "/" + one + "/" + two + "/" + three + "/" + four + "/" + five + "/" + six + "/" + seven + "/" + eight + "/" + nine + "/" + ten
	return postMS(ms, slug, body, request)

def postMS(msSlug, slug, body, request):
	import requests

	microServices	= load() # Let's load the list of MS we have
	body			= json.loads(body)

	for ms in microServices: # Let's find if we have the requested
		if (ms['slug'] == msSlug):
			url			= microService.getURL(ms) # Let's get the best URL of the requested MS
			publicKey	= body['publicKey'] # Let's get the requester Public Key
			data		= connex.receiveRequest(request, body, keys) # Okay, let's decrypt our received request
			response	= connex.sendRequest(url, slug, keys, data['headers'], data['payload'], data['content']) # Let's encrypt and request the designed MS
			data		= connex.receiveResponse(keys, response) # Now decrypt the response received from the MS
			return		  connex.sendResponse(keys, data['payload'], data['content'], publicKey) # And now, let's return a encrypted response to the requester
	hug.redirect.not_found() # Oho, we don't have the requested MS

@api.get(
	'/create',
	version=1,
	examples='name=API&description=Description&slug=api_gateway&url=http://www.somethi.ng'
)
def creartemicroService(name, description, slug, url):
	"""Create a new MicroService"""
	microService = MicroService(name, description, slug, [url])
	save(microService.__dict__)
	return microService.__dict__

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
