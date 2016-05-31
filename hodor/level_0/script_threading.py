import urllib2, urllib, time, threading

params = { 'id': '40', 'holdthedoor': 'Submit' }
url_params = urllib.urlencode(params)

def thread_it(i):
    urllib2.urlopen('http://173.246.108.142/level0.php', url_params)

threads = []
print "Please standby..."

for i in range (1, 1025):
    t = threading.Thread(target=thread_it,args=(i,))
    threads.append(t)
    t.start()
    print "Vote", i, "has been submitted for processing!"
    time.sleep(0.3)

t.join()
print "Done!"
