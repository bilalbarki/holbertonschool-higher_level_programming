import urllib2

def http_get(url, headers):
	req = urllib2.Request(url, None, headers)
	response = urllib2.urlopen(req)
	return response.read()
	
request_headers = { 'User-Agent': 'Holberton_School', 'Authorization': 'token fa51959c07bf48159fbaa3c6800b12efb49f217e' }
print http_get('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc', request_headers)
