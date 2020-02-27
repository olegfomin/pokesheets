# It calls the web-service and produces the CSV file that contains the fields
# as follows: ID,NAME,WEIGHT,TYPES
import sys
import requests

#The base URL where %s is the name of pockemon
BASE_URL = "https://pokeapi.co/api/v2/pokemon/%s/"

# The helper function that receives the pockemon name and adds the record into
# the stdout or into stderr if such a name does not exist
def pockemonIntoFile(pockemonName):
    theUrl = BASE_URL % pockemonName
    r = requests.get(url = theUrl)
    if r.text.find("Not Found") == 0: # Verifying whether the name exists
        sys.stderr.write("%s not found\n" % pockemonName)
        return
    dataAsJson = r.json()
    theId = dataAsJson["id"]
    name = pockemonName
    weight = dataAsJson["weight"]
    types = dataAsJson["types"]
    accumulator = ""
    i=0
    while i < len(types): # Traversing through the types and retrieve their names
        div = ""
        if i > 0: # No pipe charater for the very first element
            div = "|"
        accumulator=accumulator+div+types[i]["type"]["name"]
        i += 1

    sys.stdout.write("%d,%s,%d,%s\n" % (theId, name, weight, accumulator))


sys.stdout.write("ID,NAME,WEIGHT,TYPES\n") # Writing the CSV file header
i = 1
while i < len(sys.argv): # Traversing through the arguments except the first one
    pockemonIntoFile(sys.argv[i])
    i += 1
