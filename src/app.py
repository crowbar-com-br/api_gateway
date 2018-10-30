import	hug
import	json
from	models	import MicroService

api = hug.get(on_invalid=hug.redirect.not_found)

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

@api.urls('/', version=1)
def microServices():
	"""Return the list of avaiables MicroServices"""
	return load()

@api.urls('/{slug}', version=1, examples='slug=api_gateway')
def microService(slug):
	"""Return the requested MicroService"""
	microServices = load()
	for microService in microServices:
		if (microService['slug'] == slug):
			return microService
	hug.redirect.not_found()

@api.urls(
	'/create',
	version=1,
	examples='name=API&description=Description&slug=api_gateway&url=http://www.somethi.ng'
)
def microService(name, description, slug, url):
	"""Create a new MicroService"""
	microService = MicroService(name, description, slug, [url])
	save(microService.__dict__)
	return microService.__dict__

def is_json(myjson):
	try:
		json_object = json.loads(myjson)
	except:
		print("FALSO")
		return False
	return True
