SELECT 
    team, 
    league, 
    SUM(MP) AS MP, 
    SUM(W) AS W, 
    SUM(L) AS L, 
    SUM(D) AS D,
    SUM(GF) AS GF, 
    SUM(GA) AS GA, 
    SUM(GD) AS GD, 
    SUM(P) AS P
FROM (
    SELECT 
        team, league, MP, W, L, D, GF, GA, GD, P 
    FROM 
        {{ ref('home_table') }}
    UNION ALL
    SELECT 
        team, league, MP, W, L, D, GF, GA, GD, P 
    FROM 
        {{ ref('away_table') }}
) 
AS 
    overall
GROUP BY 
    team, 
    league
ORDER BY
    league,
    P DESC
