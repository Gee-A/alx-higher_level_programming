-- lists all cities contained in the database 'hbtn_0d_usa'
-- each record should display: cities.id - cities.name - states.name. sorted in asc by cities.id

SELECT cities.id, cities.name, states.name
FROM cities LEFT JOIN states 
ON states.id = cities.states_id
ORDER BY cities.id;
