import	json
import	rsa

class Key:
	"""The class for the keys"""

	def __init__(self):
		self.public		= ""
		self.private	= ""
		self.newKeys()

	def newKeys(self):
		(self.public, self.private) = rsa.newkeys(2048)

	def isSet(self):
		if(self.public == ""):
			return False
		return True

def encryptData(data, key_pub):
	data = json.dumps(data).encode('utf8')
	return rsa.encrypt(data, key_pub)

def decryptData(data, key_pri):
	data = rsa.decrypt(data, key_pri)
	return data.decode('utf8')
