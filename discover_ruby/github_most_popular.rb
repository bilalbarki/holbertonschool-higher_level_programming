require 'httpclient'

def req(extheaders, query)
	client = HTTPClient.new
	client.get_content('https://api.github.com/search/repositories?', query, extheaders)
end

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token fa51959c07bf48159fbaa3c6800b12efb49f217e'
}

query=["q", "language:ruby"], ["sort", "stars"], ["order", "desc"]

puts req(extheaders, query)