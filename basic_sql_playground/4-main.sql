/*improves the database*/

INSERT INTO EyesColor(person_id, color) VALUES (
       (SELECT id FROM Person WHERE first_name = "Jon" AND last_name = "Snow"),
       "Brown"
);

INSERT INTO EyesColor(person_id, color) VALUES (
       (SELECT id FROM Person WHERE first_name = "Arya" AND last_name = "Stark"),
       "Green"
);

/*create a new table TVShow*/
CREATE TABLE TVShow (
       id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,       
       name char(128) NOT NULL
);

/*create a new table TVShowPerson*/
CREATE TABLE TVShowPerson (
       tvshow_id INTEGER NOT NULL,
       person_id INTEGER NOT NULL,
       FOREIGN KEY(tvshow_id) REFERENCES TVShow(id),
       FOREIGN KEY(person_id) REFERENCES Person(id)
);

INSERT INTO TVShow (name) VALUES
       ("Homeland"),
       ("The big bang theory"),
       ("Game of Thrones"),
       ("Breaking bad");

INSERT INTO TVShowPerson (tvshow_id, person_id) VALUES
       (
	(SELECT id FROM TVShow WHERE name = "Breaking bad"), 
	(SELECT id FROM Person WHERE first_name = "Walter Junior" AND last_name = "White")
       ),
       (
        (SELECT id FROM TVShow WHERE name = "Game of Thrones"),
        (SELECT id FROM Person WHERE first_name = "Jaime" AND last_name = "Lannister")
       ),
       (
        (SELECT id FROM TVShow WHERE name = "The big bang theory"),
        (SELECT id FROM Person WHERE first_name = "Sheldon" AND last_name = "Cooper")
       ),
       (
        (SELECT id FROM TVShow WHERE name = "Game of Thrones"),
        (SELECT id FROM Person WHERE first_name = "Tyrion" AND last_name = "Lannister")
       ),
       (
        (SELECT id FROM TVShow WHERE name = "Game of Thrones"),
        (SELECT id FROM Person WHERE first_name = "Jon" AND last_name = "Snow")
       ),
       (
        (SELECT id FROM TVShow WHERE name = "Game of Thrones"),
        (SELECT id FROM Person WHERE first_name = "Arya" AND last_name = "Stark")
       );

SELECT * FROM Person;
SELECT * FROM EyesColor;
SELECT * FROM TVShow;
SELECT * FROM TVShowPerson;
