SELECT DISTINCT a.company_name,
         a.highest_price,
         ts AS datetime,
         a.hour
FROM 
    (SELECT name AS company_name,
         SUBSTRING(ts,
         12,
         2) AS hour,
         max(high) AS highest_price
    FROM "19"
    GROUP BY  1, 2
    ORDER BY  1, 2 ) a, "19" b
WHERE a.company_name=b.name
        AND a.hour = SUBSTRING(b.ts, 12, 2)
        AND a.highest_price = b.high
ORDER BY  1, 4 ;