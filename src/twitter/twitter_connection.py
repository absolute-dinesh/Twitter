import json

class Connection:
	def __init__(self,type_of_connection,path_to_key):
		self.type_of_connection = type_of_connection
		self.path_to_key = path_to_key

	def reading_keys(self):
		with open(self.path_to_key) as json_data:
			data = json.load(json_data)
		return data

	def showit(self):
		data = self.reading_keys()
		print(data)

	def api_call(self):
		pass

