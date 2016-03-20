require 'httpclient'
require 'json'

def req(url, query, extheaders)
	client = HTTPClient.new
	client.get_content(url, query, extheaders)
end

extheaders = { 'User-Agent' => 'Holberton_School', 'Authorization' => 'token fa51959c07bf48159fbaa3c6800b12efb49f217e' }
gitHash=JSON.parse( req('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc', nil, extheaders) )
output=[]
threads=[]

gitHash['items'].each do |name|
	threads << Thread.new{ output << { 'full_name' => name['full_name'], 'location' => JSON.parse( req(name['owner']['url'], nil, extheaders) )['location']} }
end

threads.each { |t| t.join }
puts output.to_json
