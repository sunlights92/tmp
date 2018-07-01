#!/usr/bin/python3
import json
import urllib.request, urllib.parse
hits = []
def showsome(searchfor):
   query = urllib.parse.urlencode({'q': searchfor})
   url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
   search_response = urllib.request.urlopen(url)
   search_results = search_response.read().decode("utf8")
   results = json.loads(search_results)
   data = results['responseData']
   print('Total results: %s' % data['cursor']['estimatedResultCount'])
   print(data['results'])
   hits = data['results']
   print('Top %d hits:' % len(hits))
   print(hits)

for h in hits:
    print(' ',h['title'])
print(' ', h['url'])

showsome('jaguar')
