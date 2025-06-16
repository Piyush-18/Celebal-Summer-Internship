SELECT hacker_id, name
FROM (
    SELECT s.hacker_id, s.challenge_id, h.name
    FROM Submissions s
    JOIN Challenges c ON s.challenge_id = c.challenge_id
    JOIN Difficulty d ON c.difficulty_level = d.difficulty_level
    JOIN Hackers h ON s.hacker_id = h.hacker_id
    WHERE s.score = d.score
) AS tb1
GROUP BY hacker_id, name
HAVING COUNT(challenge_id) > 1
ORDER BY COUNT(challenge_id) DESC, hacker_id;
