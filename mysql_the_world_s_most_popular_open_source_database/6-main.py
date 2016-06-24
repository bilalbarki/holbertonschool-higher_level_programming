import time
import BaseHTTPServer
import mysql.connector
import json

HOST_NAME = 'localhost' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 9898 # Maybe set this to 9000.


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "application/json")
        s.end_headers()
    def do_GET(s):
        json = ""
        path_splitted = s.path.strip('/').split('/')
        if len(path_splitted) == 1 and path_splitted[0] == "tvshows":
            json = s.tvshows()
            s.send_json(json)

        elif len(path_splitted) == 2 and path_splitted[0] == "tvshow":
            json = s.tvshow_id(path_splitted)
            s.send_json(json)
            
        elif len(path_splitted) == 3 and path_splitted[0] == "tvshow" and path_splitted[2]=="actors":
            json = s.actors(path_splitted)
            s.send_json(json)
            
        elif len(path_splitted) == 3 and path_splitted[0] == "tvshow" and path_splitted[2]=="seasons":
            json = s.seasons(path_splitted)
            s.send_json(json)
            
        elif len(path_splitted) == 5 and path_splitted[0] == "tvshow" and path_splitted[4]=="episodes":
            json = s.episodes(path_splitted)
            s.send_json(json)
           
        elif len(path_splitted) == 6 and path_splitted[0] == "tvshow" and path_splitted[4]=="episode":
            json = s.episode_number(path_splitted)
            s.send_json(json)
            

    def get_from_db(s, query):
        results = None
        try:
            db = mysql.connector.connect(
                host = "173.246.108.142",
                port = '3306',
                user = "student",
                password = "aLQQLXGQp2rJ4Wy5",
                database = "Project_169",
                charset = 'utf8',
                use_unicode= False,
            )
            if db.is_connected():
                cursor = db.cursor()
                cursor.execute(query)
                results = cursor.fetchall()

        except mysql.connector.Error as e:
            print(e)

        finally:
            db.close()
            return results

    def tvshows(self):
        query = "SELECT id, name, poster FROM TVShow ORDER BY name ASC"
        results = self.get_from_db(query)
        if results == None:
            return None
        nlist = []
        for (id, name, poster) in results:
            ndict = {}
            ndict['name'] = str(name)
            ndict['id'] = str(id)
            ndict['poster'] = str(poster)
            nlist.append(ndict)
        return json.dumps(nlist)

    def tvshow_id(self, path_splitted):
        query = "SELECT TVShow.id, TVShow.name, TVShow.poster, TVShow.overview, Network.name, GROUP_CONCAT(Genre.name) FROM TVShow JOIN Network ON TVShow.network_id = Network.id JOIN TVShowGenre ON TVShow.id = TVShowGenre.tvshow_id JOIN Genre ON TVShowGenre.genre_id = Genre.id WHERE TVShow.id = %s" % path_splitted[1]
        results = self.get_from_db(query)
        if results == None:
            return None
        print results
        nlist = []
        for (name, id, poster, overview, network, genres) in results:
            ndict = {}
            ndict['name'] = str(id)
            ndict['id'] = str(name)
            ndict['poster'] = str(poster)
            ndict['overview'] = str(overview)
            ndict['network'] = str(network)
            ndict['genres'] = str(genres)
            nlist.append(ndict)
        return json.dumps(nlist)

    def actors(self, path_splitted):
        query = "SELECT Actor.id, Actor.name FROM TVShowActor JOIN Actor ON TVShowActor.actor_id = Actor.id WHERE TVShowActor.tvshow_id = %s ORDER BY Actor.name ASC" % path_splitted[1]
        results = self.get_from_db(query)
        if results == None:
            return None
        nlist = []
        for (name,id) in results:
            ndict = {}
            ndict['name'] = str(id)
            ndict['id'] = str(name)
            nlist.append(ndict)
        return json.dumps(nlist)

    def seasons(self, path_splitted):
        query = "SELECT id, number FROM Season WHERE Season.tvshow_id = %s ORDER BY number ASC" % path_splitted[1]
        results = self.get_from_db(query)
        if results == None:
            return None
        nlist = []
        for (number,id) in results:
            ndict = {}
            ndict['number'] = str(id)
            ndict['id'] = str(number)
            nlist.append(ndict)
        return json.dumps(nlist)
    
    def episodes(self, path_splitted):
        query = "SELECT Episode.id, Episode.number, Episode.name FROM TVShow JOIN Season ON TVShow.id = Season.tvshow_id JOIN Episode ON Season.id = Episode.season_id WHERE TVShow.id = %s AND Season.id = %s ORDER BY Episode.number ASC""" % (path_splitted[1], path_splitted[3])
        results = self.get_from_db(query)
        if results == None:
             return None
        nlist = []
        for (id,number,name) in results:
            ndict = {}
            ndict['number'] = str(number)
            ndict['id'] = str(id)
            ndict['name'] = str(name)
            nlist.append(ndict)
        return json.dumps(nlist)

    def episode_number(self, path_splitted):
        query = "SELECT Episode.id, Episode.number, Episode.name, Episode.overview FROM TVShow JOIN Season ON TVShow.id = Season.tvshow_id JOIN Episode ON Season.id = Episode.season_id WHERE TVShow.id = %s AND Season.id = %s AND Episode.id = %s ORDER BY Episode.number ASC" % (path_splitted[1],path_splitted[3], path_splitted[5])
        results = self.get_from_db(query)
        if results == None:
             return None
        nlist = []
        for (overview,name,number,id) in results:
            ndict = {}
            ndict['number'] = str(number)
            ndict['id'] = str(id)
            ndict['name'] = str(name)
            ndict['overview'] = str(overview)
            nlist.append(ndict)
        return json.dumps(nlist)

    def send_json(s, json):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "application/json")
        s.end_headers()
        s.wfile.write(json)

    def query_not_found(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "application/json")
        s.end_headers()
        s.wfile.write('[{"query": "not found"}]')

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
