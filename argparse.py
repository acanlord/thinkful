# Store an item using fully qualified names
python3 snippets.py --type "puet" --name "list" --snippet "A sequence of things - created using []"


# Store an item using abbreviations
python3 snippets.py -t "put" -n "list" -s "A sequence of things - created using []"

# Use positional rather than optional arguments
python3 snippets.py put list "A sequence of things - created using []"

