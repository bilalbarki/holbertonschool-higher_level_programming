import urllib2, json

def http_get(url, headers):
	req = urllib2.Request(url, None, headers)
	response = urllib2.urlopen(req)
	return response.read()
	
request_headers = { 'User-Agent': 'Holberton_School', 'Authorization': 'token fa51959c07bf48159fbaa3c6800b12efb49f217e' }
resp_dict = json.loads( http_get('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc', request_headers) )
for item in resp_dict['items']: print item['full_name'] 
