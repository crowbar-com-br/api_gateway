# filename: models.py

class MicroService(object):
	"""The class for the API Gateway responses"""
	name		= ""
	description	= ""
	slug		= ""
	urls		= []

	def __init__(self, name, description, slug, urls):
		self.name			= name
		self.description	= description
		self.slug			= slug
		self.urls			= urls
