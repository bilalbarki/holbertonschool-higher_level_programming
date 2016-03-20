require 'httpclient'
require 'json'

def req(url, extheaders, query)
	client = HTTPClient.new
	client.get_content(url, query, extheaders)
end

_extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token fa51959c07bf48159fbaa3c6800b12efb49f217e'
}
_query=["q", "language:ruby"], ["sort", "stars"], ["order", "desc"]
_url='https://api.github.com/search/repositories?'

_gitHash=JSON.parse(req(_url, _extheaders, _query))

puts _gitHash['items'].map{ |name| name['full_name'] }.join("\n")
