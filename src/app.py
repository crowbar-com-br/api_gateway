import	hug
import	json
from	authorization	import auth
from	conx			import connex
from	cryption		import cryptKey
from	ms				import microService

api 				= hug.get(on_invalid=hug.redirect.not_found)
key					= cryptKey.Key()
token_authenticated	= hug.authentication.token(auth.hug_checkToken)

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

@api.get(
	'/services',
	version	=	1,
	requires=token_authenticated
)
def microServices():
	"""Return the list of avaiables MicroServices"""
	return load()

@api.get(
	'/services/{ms}/{slug}',
	version	=	1,
	examples=	'http://localhost:8000/services/api_gateway'
)
def getMSs(ms: "A String slug of the MS you're loking for", slug: "The slug of the option in the ms"):
	"""Return the requested Micro-Service"""
	slug	= "/" + slug
	return getMS(ms, slug)

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
	microServices	= load()
	for ms in microServices:
		if (ms['slug'] == msSlug):
			url	= microService.getURL(ms)
			return json.loads(requests.request("GET", url + slug).text)
	hug.redirect.not_found()

@api.get(
	'/create',
	version=1,
	examples='name=API&description=Description&slug=api_gateway&url=http://www.somethi.ng',
	requires=token_authenticated
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
		'publicKey'	: cryptKey.savePublic(key.public)
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
