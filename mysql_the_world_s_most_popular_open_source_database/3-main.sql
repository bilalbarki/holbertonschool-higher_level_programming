\! echo "\nList of TVShows ordered by name (A-Z) with more than or equal 4 seasons?"
SELECT name FROM (SELECT TVShow.name, count(Season.tvshow_id) as nb_seasons FROM TVShow
       JOIN Season on 
       	    (TVShow.id = Season.tvshow_id)
       	    GROUP BY Season.tvshow_id
       	    ORDER BY name) as tvshow
       WHERE nb_seasons >= 4;

\! echo "\nList of TVShows ordered by name (A-Z) with the Genre 'Comedy'?"
SELECT TVShow.name FROM TVShow
       JOIN TVShowGenre 
       	    on (TVShow.id = TVShowGenre.tvshow_id)
       JOIN Genre 
       	    on (TVShowGenre.genre_id = Genre.id)
       WHERE Genre.name = "Comedy"
       ORDER BY TVShow.name;

\! echo "\n List of Actors ordered by name (A-Z) for the TVShow 'The Big Bang Theory'?"
SELECT Actor.name FROM TVShow
       JOIN TVShowActor 
       	    on (TVShow.id = TVShowActor.tvshow_id)
       JOIN Actor 
       	    on (TVShowActor.actor_id = Actor.id)
       WHERE TVShow.name = "The Big Bang Theory"
       ORDER BY Actor.name;

\! echo "\n Top 10 of actors by number of TVShows where they are? (without Actor name order => can be random)"
SELECT Actor.name, count(TVShow.id) as nb_tvshows FROM TVShow
       JOIN TVShowActor 
       	    on (TVShow.id = TVShowActor.tvshow_id)
       JOIN Actor 
       	    on (TVShowActor.actor_id = Actor.id)
       GROUP BY Actor.name
       ORDER BY nb_tvshows DESC        
       LIMIT 10;
