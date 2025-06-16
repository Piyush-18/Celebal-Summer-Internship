SELECT ROUND(lat_n, 4)
FROM (
    SELECT lat_n, PERCENT_RANK() OVER (ORDER BY lat_n) AS percentrank
    FROM station
) AS sub1
WHERE percentrank = 0.5;
