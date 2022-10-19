SELECT date,sum(prod_price*prod_qty) as Ventes
FROM Transaction
WHERE date BETWEEN "2019-01-01" AND "2019-12-31"
GROUP BY date;
