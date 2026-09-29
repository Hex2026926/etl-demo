
SELECT * FROM titanic LIMIT 10;

SELECT COUNT(*) AS total_passengers FROM titanic;

SELECT Survived, COUNT(*) AS cnt,
       ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM titanic), 2) AS pct
FROM titanic GROUP BY Survived;

SELECT Sex, Survived, COUNT(*) AS cnt
FROM titanic GROUP BY Sex, Survived;

SELECT ROUND(AVG(Age), 2) AS avg_age, ROUND(AVG(Fare), 2) AS avg_fare
FROM titanic;