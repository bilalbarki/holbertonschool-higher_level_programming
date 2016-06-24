import mysql.connector

def connect():
    ''' Connect to MySQL database '''
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
            do_it(db)
           
    except mysql.connector.Error as e:
        print(e)
 
    finally:
        db.close()

def do_it(db):
    cursor = db.cursor()
    cursor.execute(shows_sql)
    shows = cursor.fetchall()
    for show in shows:
        print "%s:" % show[0]
        cursor.execute(seasons_sql + str(show[1]))
        seasons = cursor.fetchall()
        for season in seasons:
            print "\tSeason %s:" % str(season[1])
            episodes_sql = "SELECT Episode.name, Episode.number FROM Episode WHERE Episode.season_id = %s ORDER BY Episode.number" % str(season[0])
            cursor.execute(episodes_sql)
            episodes = cursor.fetchall()
            for episode in episodes:
                print "\t\t%s: %s" %(str(episode[1]), str(episode[0]))

shows_sql = "SELECT TVShow.name, TVShow.id FROM TVShow ORDER BY TVShow.name"
seasons_sql = "SELECT Season.id, Season.number FROM Season WHERE Season.tvshow_id="
connect()
