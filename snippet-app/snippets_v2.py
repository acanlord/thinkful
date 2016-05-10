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


def get(name, snippet):

    """Read a nippet with an associated name."""
    logging.info("Storing snippet {!r}: {!r}".format(name, snippet))
    cursor = connection.cursor()
    row = cursor.fetchone()
    while row is not None:
        print (row)
        row = cursor.fetchone()
    logging.debug("snipet pulled successfully.")
    return name, snippet



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

