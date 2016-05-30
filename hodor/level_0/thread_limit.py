import urllib2, urllib
import multiprocessing.pool as npool
from multiprocessing import Lock

#configuration start
id_number=40
allowed_number_of_threads_at_one_time=20
votes=1024
#configuration end

def thread_it():
    urllib2.urlopen('http://173.246.108.142/level0.php', url_params)
    lock.acquire()
    try:
        global vote_counter
        print "Vote", vote_counter, "has been submitted!"
        vote_counter+=1
    finally:
        lock.release()

params = { 'id': id_number, 'holdthedoor': 'Submit' }
url_params = urllib.urlencode(params) # url encode the parameters
vote_counter=1
lock=Lock()
pool = npool.ThreadPool(allowed_number_of_threads_at_one_time) #max number of threads at a time
for i in range (votes):
    t = pool.apply_async(thread_it,args=())

print "Please standby..."
t.wait()
print "Done!"
