/*display all sums of age by TVShow, ordered by sum (ascending)*/
SELECT name, SUM(age) FROM Person
       JOIN TVShowPerson ON TVShowPerson.person_id = Person.id,
       	    TVShow ON TVShow.id = TVShowPerson.tvshow_id
       GROUP BY name ORDER BY SUM(age) ASC;

/*display the youngest Person of each TVShow, ordered by age (ascending)*/
SELECT name, first_name, last_name, MIN(age) FROM Person
       JOIN TVShowPerson ON TVShowPerson.person_id = Person.id,
            TVShow ON TVShow.id = TVShowPerson.tvshow_id
       GROUP BY name ORDER BY MIN(age);
