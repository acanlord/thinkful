import argparse
import logging

# set the log output file, and log level
logging.basicConfig(filename="snippets.log", level = logging.DEBUG)

def put(name, snippet):
	"""
	Store a nippet with an associated name.

	Returns the name and the snippet
	"""
	logging.error("FIXME: Unimplemented - put({!r},{!r})".format(name,snippet))
	return name, snippet

def get(name):
	"""Retrieve the snippet with a given name.

	IF there is no such snippet, return '404: Snippet Not Fount'.
	
	Returns the snippet.
	"""
	logging.error("FIXME: Unimplementd - get({!r})".format(name))
	return""


def main():
	"""Main function"""
	logging.info("Constructin parser")
	parser = argparse.ArgumentParser(description="Store and retrieve snippets of text")
	arguments = parser.parse_args()

if __name__ == "__main__":
	main()


