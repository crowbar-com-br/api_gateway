class MicroService(object):
	"""The class for the Micro-Services"""
	name		= ""
	description	= ""
	slug		= ""
	urls		= []
	publicKey	= ""

	def __init__(self, name, description, slug, urls, publicKey):
		self.name			= name
		self.description	= description
		self.slug			= slug
		self.urls			= urls
		self.publicKey		= publicKey

def pingURL(url):
	import	json
	import	os
	import	requests
	import	time

	start		= time.time()
	response	= requests.request("GET", url + "/status")
	duration	= time.time() - start
	response	= json.loads(response.text)
	return ((response['CPU'] * response['Memory']) - duration)

def getURL(microService):
	urls		= microService.urls
	responses	= []
	if urls.__len__() == 1:
		return urls[0]
	else:
		for url in urls:
			responses.append(pingURL(url))
		lowest		= responses[0]
		lowestURL	= urls[0]
		for index, response in enumerate(responses):
			if not response == False:
				if response < lowest and response > 0:
					lowest		= response
					lowestURL	= urls[index]
		return lowestURL
