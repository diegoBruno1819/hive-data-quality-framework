SELECT COUNT(*)
FROM (
    SELECT id, COUNT(*)
    FROM {table}
    GROUP BY id
    HAVING COUNT(*) > 1
) t;
