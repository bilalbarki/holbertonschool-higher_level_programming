require 'httpclient'
require 'json'

def req(url, query, extheaders)
	_client = HTTPClient.new
	_client.get_content(url, query, extheaders)
end

extheaders = { 'User-Agent' => 'Holberton_School', 'Authorization' => 'token fa51959c07bf48159fbaa3c6800b12efb49f217e' }
_gitHash=JSON.parse( req('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc', nil, extheaders) )
_output=[]

_gitHash['items'].each do |name|
	_output << {'full_name' => name['full_name'], 'location' => JSON.parse( req(name['owner']['url'], nil, extheaders) )['location']}
end

puts _output.to_json
