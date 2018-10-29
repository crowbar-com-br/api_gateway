# filename: main.py
"""A basic (single function) API written using hug"""
import hug

@hug.get('/')
def hello_wolrd():
	"""Says hello world"""
	return "Hello world!!"
