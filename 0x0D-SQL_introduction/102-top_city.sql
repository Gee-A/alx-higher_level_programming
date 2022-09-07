-- display the top 3 cities temperature during July and August ordered by temperature
SELECT city, AVG(value) 'avg_temp' FROM temperature WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
