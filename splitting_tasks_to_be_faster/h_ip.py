import threading, json, urllib

class IPThread(threading.Thread):
    def __init__(self, ip, callback):
        threading.Thread.__init__(self)
        self.__ip = ip
        self.__callback = callback

    def run(self):
        print "Search: %s" % self.__ip
        req = urllib.urlopen("https://api.ip2country.info/ip?%s" % self.__ip)
        p_json = json.loads(req.read())
        self.__callback(p_json['countryName'])
