import urllib2, urllib
import multiprocessing.pool as npool
from multiprocessing import Lock

#configuration start
id_number=40
allowed_number_of_threads_at_one_time=25
votes=1024
#configuration end

def thread_it():
    post = urllib2.urlopen('http://173.246.108.142/level0.php', url_params)
    lock.acquire()
    try:
        global vote_counter
        if post.getcode() == 200:
            print "Vote", vote_counter, "has been submitted!"
            vote_counter+=1
        else:
            print "Vote", vote_counter, "failed with status", post.getcode()
    finally:
        lock.release()
    post.close()

params = { 'id': id_number, 'holdthedoor': 'Submit' }
url_params = urllib.urlencode(params) # url encode the parameters
vote_counter=1
lock=Lock()
pool = npool.ThreadPool(allowed_number_of_threads_at_one_time) #max number of threads at a time
print "Please standby..."

for i in range (votes):
    t = pool.apply_async(thread_it,args=())
pool.close()
pool.join()
print "Done!"
