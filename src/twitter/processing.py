import twitter_connection as t


class Processing:
	con1 = t.Connection("show","../../values.json")
	print(con1.reading_keys())

