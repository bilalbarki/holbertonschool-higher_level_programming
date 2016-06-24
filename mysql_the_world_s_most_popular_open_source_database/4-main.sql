\! echo "\nList of all TVShows by all Genres ordered by genre name (A-Z)? (if a genre has 0 TVShow, please display NULL)"
SELECT Genre.name as "Genre name", TVShow.name  as "TVShow name" FROM TVShow
       RIGHT JOIN TVShowGenre 
       	     on (TVShow.id = TVShowGenre.tvshow_id)
       RIGHT JOIN Genre 
       	     on (TVShowGenre.genre_id = Genre.id)
       ORDER BY Genre.name;

\! echo "\nName of the pilot (first episode of the first season) of each TVShow ordered by TVShow name (A-Z)?"
SELECT TVShow.name as "TVShow name", Episode.name as "Episode name" FROM TVShow
       JOIN Season 
       	    on (TVShow.id = Season.tvshow_id)
       JOIN Episode 
       	    on (Season.id = Episode.season_id)
       WHERE (Episode.number = 1 and Season.number = 1)
       ORDER BY TVShow.name;

\! echo "\nList of all Genres by all TVShows ordered by TVShow name (A-Z)? (if a genre has 0 TVShow, please display NULL as TVShow name)"
SELECT TVShow.name as "TVShow name", Genre.name as "Genre name" FROM TVShow
       RIGHT JOIN TVShowGenre 
       	     on (TVShow.id = TVShowGenre.tvshow_id)
       RIGHT JOIN Genre 
       	     on (TVShowGenre.genre_id = Genre.id)
       ORDER BY TVShow.name;
