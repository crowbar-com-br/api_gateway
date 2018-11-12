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
	file = open("data_file.json", "r+")
	file_open = file.read()
	if (isJSON(file_open)):
		content = json.loads(file_open)
	else:
		content = []
	content.append(data)
	file.close()
	open("data_file.json", "w").close()
	file = open("data_file.json", "r+")
	file.write(json.dumps(content))
	file.close()

def load():
	with open("data_file.json", "r") as read_file:
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
	'/services/{slug}',
	version	=	1,
	examples=	'http://localhost:8000/services/api_gateway',
	requires=token_authenticated
)
def createmicroService(slug: "A String slug of the MS you're loking for"):
	"""Return the requested MicroService"""
	microServices = load()
	for microService in microServices:
		if (microService['slug'] == slug):
			return microService
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

def isJSON(myjson: "A expected JSON"):
	"""Check if the param object can be a JSON"""
	try:
		json_object = json.loads(myjson)
	except:
		return False
	return True
