import urllib2, json, threading

def http_get(url, headers):
	req = urllib2.Request(url, None, headers)
	response = urllib2.urlopen(req)
	return response.read()

def thread_it(item):
	data.append( {'full_name': item['full_name'], 'location':json.loads( http_get(item['owner']['url'], request_headers) )['location']} )
	return;
	
request_headers = { 'User-Agent': 'Holberton_School', 'Authorization': 'token fa51959c07bf48159fbaa3c6800b12efb49f217e' }
resp_dict = json.loads( http_get('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc', request_headers) )
data = []
threads = []
for item in resp_dict['items']:
	t = threading.Thread(target=thread_it,args=(item,))
	threads.append(t)
	t.start()
t.join()
print json.dumps(data, sort_keys=True)
