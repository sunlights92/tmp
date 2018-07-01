import requests
import json

query = "cats+dogs"

#NB. add 'start=3' to the query string to move to later results
r = requests.get('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=' + query)

# JSON object
theJson = r.content
theObject = json.loads(theJson)

# Print it all out
for index,result in enumerate(theObject['responseData']['results']):
    print str(index+1) + ") " + result['titleNoFormatting']
    print result['url']
