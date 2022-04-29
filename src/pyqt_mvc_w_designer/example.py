import pkg_resources

def add_one(number):
	stream = pkg_resources.resource_stream(__name__, "res/test_data_file.txt")
	print(stream.read().decode())
	return number + 1

