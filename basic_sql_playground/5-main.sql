/*Uses INNER JOIN, COUNT, SUM*/

SELECT DISTINCT last_name FROM Person 
       JOIN TVShowPerson ON TVShowPerson.person_id = Person.id,
       	    TVShow ON TVShow.id = TVShowPerson.tvshow_id       
       WHERE name = "Game of Thrones" ORDER BY last_name ASC;

SELECT COUNT(age) FROM Person WHERE age > 30;

SELECT Person.id, first_name, last_name, age, color, name FROM Person
       JOIN TVShowPerson ON TVShowPerson.person_id = Person.id,
            TVShow ON TVShow.id = TVShowPerson.tvshow_id,
	    EyesColor ON EyesColor.person_id = Person.id;

/*Displays sum of age*/
SELECT SUM(age) FROM Person;
