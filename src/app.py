# filename: app.py
"""A basic (single function) API written using hug"""
import hug

@hug.get('/')
@hug.local()
def hello_wolrd():
	"""Says hello world"""
	return {
		'message': "Hello world!!!"
	}
