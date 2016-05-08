#! /usr/bin/python


import argparse
import logging
import psycopg2

# set the log output file, and log level
logging.basicConfig(filename="snippets.log", level = logging.DEBUG)
logging.debug("Connecting to PostgreSQL")
connection = psycopg2.connect(database="snippets")
logging.debug("Database connection established.")

def put(name, snippet):

    """Store a nippet with an associated name."""
    logging.info("Storing snippet {!r}: {!r}".format(name, snippet))
    cursor = connection.cursor()
    command = "insert into snippets values (%s, %s)"
    cursor.execute(command, (name, snippet))
    connection.commit()
    logging.debug("snipet stored successfully.")
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
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="Name of the snippet")
    put_parser.add_argument("snippet", help="Snippet text")

    arguments = parser.parse_args()
        # convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "put":
                name, snippet = put(**arguments)
                print("stored {!r} as {!r}".format(snippet, name))
    elif command == "get":
                snipet = get(**arguments)
                print("Retrieved snippet: {!r}".format(snippet))

if __name__ == "__main__":
    main()

