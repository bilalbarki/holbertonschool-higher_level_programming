require 'httpclient'

def req(url, query, extheaders)
	client = HTTPClient.new
	client.get_content(url, query, extheaders)
end

extheaders = { 'User-Agent' => 'Holberton_School', 'Authorization' => 'token fa51959c07bf48159fbaa3c6800b12efb49f217e' }
File.open('/tmp/40', 'w') do |file|
	file.write( req('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc', nil, extheaders) )
end
puts "The file was saved!"