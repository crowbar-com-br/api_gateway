import	base64
import	hug
import	json
import	requests
from	authorization	import auth
from	conx			import connex
from	cryption		import cryptKey
from	models			import MicroService

api 				= hug.get(on_invalid=hug.redirect.not_found)
key					= cryptKey.Key()
token_authenticated	= hug.authentication.token(auth.hug_checkToken)

def save(data):
	file = open("data_file.json", "r+")
	file_open = file.read()
	if (is_json(file_open)):
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
def microServices(body):
	"""Return the list of avaiables MicroServices"""
	return load()

@api.get()
def test(request):
	return cryptKey.newKey()

@api.get(
	'/services/{slug}',
	version	=	1,
	examples=	'http://localhost:8000/services/api_gateway',
	requires=token_authenticated
)
def microService(slug):
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
def microService(name, description, slug, url):
	"""Create a new MicroService"""
	microService = MicroService(name, description, slug, [url])
	save(microService.__dict__)
	return microService.__dict__

@api.post(
	'/authentication',
	version=1
)
def getToken(body):
	"""Get a token"""
	if (is_json(body)):
		body 		= json.loads(body)
		username	= body['username']
		password	= body['password']
		return auth.getToken(username, password, key)
	else:
		return 403

@api.get(
	'/authentication',
	version=1
)
def checkToken(request):
	"""Check if the token is still valid"""
	return auth.checkToken(request)

def is_json(myjson):
	try:
		json_object = json.loads(myjson)
	except:
		return False
	return True
